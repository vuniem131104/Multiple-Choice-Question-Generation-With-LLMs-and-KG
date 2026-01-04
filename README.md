# AI-Powered Multiple Choice Question (MCQ) Generation Platform

An intelligent educational platform for automated Multiple Choice Question (MCQ) generation using Retrieval-Augmented Generation (RAG) and Knowledge Graph technologies. The system leverages course materials to generate contextually relevant, high-quality MCQs for assessment and practice. Built with support for multiple AI models through LiteLLM and Neo4j knowledge graph for enhanced question generation.

## Architecture

This is a microservices-based application with the following components:

### Services

- **Auth Service** (`port 3001`): User authentication and authorization
- **Generation Service** (`port 3005`): MCQ generation using LLM models with RAG
- **RAG Service** (`port 3011`): Retrieval-Augmented Generation for context extraction
- **Indexing Service** (`port 3006`): Document processing and knowledge graph indexing
- **Frontend** (`port 3000`): React-based web interface for MCQ management

### Infrastructure

- **LiteLLM** (`port 9510`): Unified interface for multiple LLM providers (Gemini, Azure OpenAI, AWS Claude)
- **Neo4j** (`port 17474/17687`): Graph database for knowledge representation
- **PostgreSQL** (`port 15432`): Relational database for user and course data
- **MinIO** (`port 9000/9001`): Object storage for documents and media
- **Ollama** (`port 11434`): Local LLM hosting

## Project Structure

```
KLTN/
├── services/               # Microservices
│   ├── auth/              # Authentication service
│   ├── generation/        # MCQ generation service
│   ├── indexing/          # Document indexing service
│   └── rag/               # RAG context retrieval service
├── frontend/              # React frontend application
├── libs/                  # Shared libraries
│   ├── base/             # Base utilities
│   ├── graph_db/         # Neo4j integration
│   ├── lite_llm/         # LiteLLM wrapper
│   ├── logger/           # Logging utilities
│   ├── postgres_db/      # PostgreSQL integration
│   └── storage/          # MinIO storage utilities
├── docker/               # Dockerfiles for services
├── database/             # Database initialization scripts
├── outputs/              # Analysis outputs and results
├── archive/              # Research and evaluation scripts
├── config.yaml           # LiteLLM configuration
└── docker-compose.yml    # Docker orchestration
```

## Getting Started

### Prerequisites

- Docker & Docker Compose
- Python 3.13+
- Node.js 18+ (for frontend development)
- UV package manager (for Python dependencies)

### Installation & Running

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd KLTN
   ```

2. **Start all services with Docker Compose**
   ```bash
   docker-compose up -d
   ```

3. **Access the application**
   - Frontend: http://localhost:3000
   - Neo4j Browser: http://localhost:17474
   - MinIO Console: http://localhost:9001
   - LiteLLM API: http://localhost:9510

### Development Setup

#### Backend Services

```bash
# Install UV package manager
pip install uv

# Install dependencies
uv sync

# Run a specific service (example: RAG service)
cd services/rag
uv run python -m src.main
```

#### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Supported Courses

The platform currently supports the following courses:
- **int3405**: Introduction to Artificial Intelligence
- **dsa2025**: Data Structures and Algorithms 2025
- **rl2025**: Reinforcement Learning 2025

## Features

### MCQ Generation
- **Automated MCQ Creation**: Generate multiple choice questions from course materials
- **Context-Aware Questions**: Leverage RAG to create questions based on specific topics and difficulty levels
- **Knowledge Graph Enhanced**: Use graph relationships to generate questions testing concept connections
- **Quality Control**: Validate questions for clarity, difficulty, and educational value
- **Customizable**: Control question difficulty, topic focus, and distractor quality

### Knowledge Graph Integration
- Automated extraction of concepts, relationships, and entities from course materials
- Graph-based retrieval for contextually relevant question generation
- Entity similarity analysis for creating meaningful distractors
- Knowledge graph effectiveness evaluation for question quality

### Multi-Model Support
- Gemini 2.5 Flash
- Azure OpenAI (GPT-4, GPT-4o-mini)
- AWS Claude
- Local models via Ollama

### RAG Pipeline for MCQ Context
- Document chunking and embedding for course materials
- Semantic search to identify relevant content for questions
- Context extraction for question and answer generation
- Knowledge graph enhanced retrieval for topic selection

### User Management
- Role-based access control (Teachers/Students)
- Course enrollment and management
- Authentication with JWT tokens

## Technologies

### Backend
- **Python 3.13** with UV package manager
- **FastAPI** for REST APIs
- **Neo4j** for knowledge graph storage
- **PostgreSQL** for relational data
- **LiteLLM** for unified LLM interface

### Frontend
- **React 18** with TypeScript
- **Vite** for build tooling
- **TailwindCSS** for styling
- **React Query** for data fetching
- **Zustand** for state management

### Infrastructure
- **Docker & Docker Compose** for containerization
- **MinIO** for object storage
- **Nginx** for serving frontend

## Evaluation & Analysis

The `archive/` directory contains research and evaluation scripts for MCQ quality assessment:
- `analyze_kg_effectiveness.py`: Knowledge graph impact on question quality
- `kg_evaluation.py`: Quantitative KG metrics for MCQ generation
- `entities_similarity.ipynb`: Entity similarity computation for distractor creation
- `qa_topic_comparison.py`: MCQ topic coverage analysis
- `baseline.ipynb`: Comparison with baseline MCQ generation methods

MCQ generation results are stored in `outputs/` organized by model and course.

## API Documentation

Once services are running, API documentation is available at:
- Auth Service: http://localhost:3001/docs
- Generation Service: http://localhost:3005/docs
- RAG Service: http://localhost:3011/docs
- Indexing Service: http://localhost:3006/docs
