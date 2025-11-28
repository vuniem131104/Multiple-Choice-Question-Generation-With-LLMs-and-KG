from fastapi import APIRouter, UploadFile, File, Form, Request, HTTPException, Query
from fastapi.responses import JSONResponse, StreamingResponse
from logger import get_logger
from storage.minio import MinioInput
import tempfile
import os
from typing import List, Optional

logger = get_logger(__name__)
upload_router = APIRouter(tags=["upload"])


@upload_router.post("/upload")
async def upload_file(
    request: Request,
    file: UploadFile = File(...),
    course_code: str = Form(...),
    week_number: Optional[int] = None
):
    """
    Upload a lecture file to MinIO storage.
    Files are saved in bucket: {course_code}
    Path: /tuan-{week_number}/{file_name}
    """
    try:
        minio_service = request.app.state.minio_service
        
        # Ensure bucket exists
        bucket_name = course_code.lower()
        if not minio_service.bucket_exists(bucket_name):
            minio_service.create_bucket(bucket_name)
            logger.info(f"Created bucket: {bucket_name}")
        
        # Create object name with week prefix
        object_name = f"tuan-{week_number}/{file.filename}" if week_number is not None else file.filename
        
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            content = await file.read()
            temp_file.write(content)
            temp_file_path = temp_file.name
        
        try:
            # Upload to MinIO
            minio_service.upload_file(
                MinioInput(
                    bucket_name=bucket_name,
                    object_name=object_name,
                    file_path=temp_file_path,
                    content_type=file.content_type or "application/octet-stream"
                )
            )
            
            logger.info(f"Successfully uploaded {file.filename} to {bucket_name}/{object_name}")
            
            return JSONResponse(
                status_code=200,
                content={
                    "message": "File uploaded successfully",
                    "bucket": bucket_name,
                    "path": object_name,
                    "file_name": file.filename,
                    "course_code": course_code,
                    "week_number": week_number
                }
            )
        
        finally:
            # Clean up temporary file
            if os.path.exists(temp_file_path):
                os.unlink(temp_file_path)
    
    except Exception as e:
        logger.error(f"Error uploading file: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to upload file: {str(e)}")


@upload_router.get("/lectures")
async def list_lectures(
    request: Request,
    course_code: str = Query(..., description="Course code to fetch lectures for"),
):
    """
    List all lecture files from MinIO for a given course code.
    Returns lectures organized by week.
    Only returns PDF files.
    """
    try:
        minio_service = request.app.state.minio_service
        
        courses_data = []
        
        course_code = course_code.lower()
        bucket_name = course_code
        
        # Check if bucket exists
        if not minio_service.bucket_exists(bucket_name):
            logger.warning(f"Bucket {bucket_name} does not exist")
            return JSONResponse(
                status_code=200,
                content={"courses": []}
            )
        
        # List all files in the bucket
        try:
            files = minio_service.list_files(bucket_name, prefix="", recursive=True)
            
            # Filter only PDF files and organize by week
            weeks_data = {}
            for file_path in files:
                # Only include PDF files
                if not file_path.lower().endswith('.pdf'):
                    continue
                
                # Extract week number from path (e.g., "tuan-1/file.pdf")
                parts = file_path.split('/')
                if len(parts) >= 2 and parts[0].startswith('tuan-'):
                    week_str = parts[0].split('-')[1]
                    try:
                        week_number = int(week_str)
                        file_name = parts[-1]
                        
                        if week_number not in weeks_data:
                            weeks_data[week_number] = []
                        
                        weeks_data[week_number].append({
                            "file_name": file_name,
                            "file_path": file_path,
                            "bucket": bucket_name
                        })
                    except ValueError:
                        continue
            
            # Convert to sorted list
            weeks_list = [
                {
                    "week_number": week_num,
                    "files": files
                }
                for week_num, files in sorted(weeks_data.items())
            ]
            
            courses_data.append({
                "course_code": course_code,
                "bucket_name": bucket_name,
                "weeks": weeks_list
            })
            
        except Exception as e:
            logger.error(f"Error listing files for {bucket_name}: {str(e)}")
            return JSONResponse(
                status_code=200,
                content={"courses": []}
            )
        
        return JSONResponse(
            status_code=200,
            content={"courses": courses_data}
        )
    
    except Exception as e:
        logger.error(f"Error listing lectures: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to list lectures: {str(e)}")


@upload_router.get("/lectures/download")
async def download_lecture(
    request: Request,
    bucket: str = Query(..., description="Bucket name (course code)"),
    file_path: str = Query(..., description="File path in bucket"),
):
    """
    Download a lecture file from MinIO.
    Returns the file as a streaming response.
    """
    try:
        minio_service = request.app.state.minio_service
        
        # Check if bucket exists
        if not minio_service.bucket_exists(bucket):
            raise HTTPException(status_code=404, detail=f"Bucket {bucket} not found")
        
        # Get the file from MinIO
        try:
            response = minio_service._client.get_object(bucket, file_path)
            
            # Extract filename
            file_name = file_path.split('/')[-1]
            
            # Return as streaming response
            return StreamingResponse(
                response.stream(32*1024),
                media_type="application/pdf",
                headers={
                    "Content-Disposition": f'inline; filename="{file_name}"'
                }
            )
        except Exception as e:
            logger.error(f"Error downloading file {file_path} from {bucket}: {str(e)}")
            raise HTTPException(status_code=404, detail=f"File not found: {str(e)}")
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in download endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to download file: {str(e)}")
