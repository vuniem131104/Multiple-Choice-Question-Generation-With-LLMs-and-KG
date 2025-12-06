from indexing.shared.settings.chunker import ChunkerSetting
from indexing.shared.utils import tokens_calculator
from base import BaseModel 
from base import BaseService
from logger import get_logger
from indexing.shared.utils import tokens_calculator

logger = get_logger(__name__)


class ChunkerInput(BaseModel):
    contents: str
    course_code: str

class ChunkerOutput(BaseModel):
    chunks: list[str]
    course_code: str


class ChunkerService(BaseService):
    chunker_setting: ChunkerSetting

    def process(self, inputs: ChunkerInput) -> ChunkerOutput:
        """ Processes the input to split contents into chunks based on headers and token limits.

        Args:
            inputs (ChunkerInput): Input data containing contents, file name, positions, and unit.

        Returns:
            ChunkerOutput: Output data containing processed chunks, file name, positions, and unit.
        """
        chunks = self._split_by_headers(inputs.contents)
        return ChunkerOutput(chunks=chunks, course_code=inputs.course_code)

    def _split_by_headers(self, content: str) -> list[str]:
        """Split content by markdown headers while respecting token limits.
        
        Args:
            content (str): The markdown content to split
            
        Returns:
            list[str]: List of text chunks
        """
        lines = content.split('\n')
        chunks = []
        current_chunk = []
        current_tokens = 0
        header_stack = []  # Stack to track hierarchy of headers
        first_line_processed = False
        
        for line_idx, line in enumerate(lines):
            # Check if line is a header (only first line with # or lines with ##, ###, etc.)
            is_header = False
            if line.startswith('#'):
                # First line: only treat as header if it's exactly # (level 1)
                if line_idx == 0 and not first_line_processed:
                    first_line_processed = True
                    if line.startswith('# ') and not line.startswith('##'):
                        is_header = True
                        header_level = 1
                # All other lines: treat as header if it's ## or higher (not single #)
                elif line.startswith('## '):
                    is_header = True
                    header_level = len(line) - len(line.lstrip('#'))
            
            if is_header:
                # Update header stack based on level
                # Keep headers up to the parent level
                header_stack = [h for h in header_stack if h[0] < header_level]
                header_stack.append((header_level, line))
                
                # Check if we should start a new chunk for major sections (## level)
                if header_level == 2:
                    # If current chunk has content and meets minimum token requirement
                    if current_chunk and current_tokens >= self.chunker_setting.min_token_per_chunk:
                        chunk_content = '\n'.join(current_chunk)
                        chunks.append(chunk_content)
                        current_chunk = []
                        current_tokens = 0
                    
                    # Start new chunk with full header hierarchy (excluding the current header)
                    # We'll add the current header after this
                    if current_chunk == []:  # Only add context if starting fresh
                        current_chunk = self._build_header_context(header_stack[:-1])
                        current_tokens = tokens_calculator('\n'.join(current_chunk))
                
                current_chunk.append(line)
                current_tokens = tokens_calculator('\n'.join(current_chunk))
                
            else:
                # Regular content line (including comment lines like #...)
                line_tokens = tokens_calculator(line)
                potential_tokens = current_tokens + line_tokens
                
                # Check if adding this line would exceed max tokens
                if potential_tokens > self.chunker_setting.max_token_per_chunk and current_chunk:
                    # Save current chunk if it meets minimum requirement
                    if current_tokens >= self.chunker_setting.min_token_per_chunk:
                        chunk_content = '\n'.join(current_chunk)
                        chunks.append(chunk_content)
                        
                        # Start new chunk with header context
                        current_chunk = self._build_header_context(header_stack)
                        current_tokens = tokens_calculator('\n'.join(current_chunk))
                    
                current_chunk.append(line)
                current_tokens = tokens_calculator('\n'.join(current_chunk))
        
        # Add the last chunk if it has content
        if current_chunk:
            chunk_content = '\n'.join(current_chunk)
            chunks.append(chunk_content)
        
        logger.info(f"Split content into {len(chunks)} chunks")
        return chunks
    
    def _build_header_context(self, header_stack: list[tuple[int, str]]) -> list[str]:
        """Build the header hierarchy context for a new chunk.
        
        Args:
            header_stack (list[tuple[int, str]]): Stack of (level, header_text) tuples
            
        Returns:
            list[str]: Lines representing the header hierarchy
        """
        context_lines = []
        for level, header in header_stack:
            context_lines.append(header)
        return context_lines
        


# if __name__ == "__main__":
#     # Example usage
#     import json 
#     service = ChunkerService(chunker_setting=ChunkerSetting(
#         max_token_per_chunk=1000,
#         min_token_per_chunk=500,
#     ))
#     with open("/home/lehoangvu/KLTN/services/generation/src/generation/shared/static_files/dsa2025/book.md", "r") as f:
#         content = f.read()
#     input_data = ChunkerInput(contents=content, course_code="dsa2025")

#     output_data = service.process(input_data)
#     chunks = output_data.chunks
#     with open(f"/home/lehoangvu/KLTN/chunks_{input_data.course_code}.json", "w", encoding='utf-8') as f:
#         json.dump(chunks, f, indent=4, ensure_ascii=False)