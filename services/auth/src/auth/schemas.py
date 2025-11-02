from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from datetime import datetime


class UserBase(BaseModel):
    user_name: str = Field(..., min_length=3, max_length=100)
    email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    full_name: Optional[str] = None


class UserCreate(UserBase):
    password: str = Field(..., min_length=8)


class UserLogin(BaseModel):
    user_name: str
    password: str


class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)
    
    user_id: int
    teaching_courses: Optional[List[str]] = None
    created_at: datetime


class LoginResponse(BaseModel):
    user: UserResponse
    message: str
