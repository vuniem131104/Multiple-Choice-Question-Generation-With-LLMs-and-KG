from fastapi import APIRouter, Depends, HTTPException, status, Request
from auth.schemas import UserCreate, UserResponse, UserLogin, LoginResponse
from auth.database import Database
from auth.security import verify_password, get_password_hash

router = APIRouter(prefix="/api/auth", tags=["authentication"])


async def get_db(request: Request) -> Database:
    """Get database instance from app state."""
    return request.app.state.db


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(user: UserCreate, db: Database = Depends(get_db)):
    """Register a new user."""
    # Check if user already exists
    query = "SELECT user_id FROM users WHERE user_name = $1 OR email = $2"
    existing_user = await db.fetchrow(query, user.user_name, user.email)
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already registered"
        )
    
    # Hash password
    hashed_password = get_password_hash(user.password)
    
    # Insert user
    query = """
        INSERT INTO users (user_name, email, password, full_name)
        VALUES ($1, $2, $3, $4)
        RETURNING user_id, user_name, email, full_name, teaching_courses, created_at
    """
    new_user = await db.fetchrow(
        query,
        user.user_name,
        user.email,
        hashed_password,
        user.full_name
    )
    
    return UserResponse(**dict(new_user))


@router.post("/login", response_model=LoginResponse)
async def login(
    credentials: UserLogin,
    db: Database = Depends(get_db)
):
    """Login and return user info."""
    # Get user
    query = "SELECT * FROM users WHERE user_name = $1"
    user = await db.fetchrow(query, credentials.user_name)
    
    if not user or not verify_password(credentials.password, user['password']):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    
    # Return user info
    user_data = UserResponse(**dict(user))
    return LoginResponse(
        user=user_data,
        message="Login successful"
    )


@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: Database = Depends(get_db)):
    """Get user by ID."""
    query = "SELECT * FROM users WHERE user_id = $1"
    user = await db.fetchrow(query, user_id)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return UserResponse(**dict(user))


@router.get("/users", response_model=list[UserResponse])
async def list_users(db: Database = Depends(get_db)):
    """List all users."""
    query = "SELECT * FROM users ORDER BY created_at DESC"
    users = await db.fetch(query)
    
    return [UserResponse(**dict(user)) for user in users]
