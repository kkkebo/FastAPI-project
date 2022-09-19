import fastapi
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database.db_setup import async_get_db, get_db
from api.utils.courses import get_user_courses
from pydantic_schemas.course import Course
from pydantic_schemas.user import UserCreate, User
from api.utils.users import get_user, get_users, get_user_by_email, create_user

router = fastapi.APIRouter()


@router.get("/users", response_model=list[User])
async def read_users(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.post("/users", response_model=User, status_code=201)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400, detail="Email is already registered"
        )
    return create_user(db=db, user=user)


@router.get("/user/{user_id}", response_model=User)
async def read_user(user_id: int, db: AsyncSession = Depends(async_get_db)):
    db_user = await get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# sync
# @router.get('/user/{user_id}', response_model=User)
# async def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = get_user(db=db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return get_user(db=db, user_id=user_id)


@router.get("/users/{user_id}/courses", response_model=list[Course])
async def read_user_courses(user_id: int, db: Session = Depends(get_db)):
    courses = get_user_courses(user_id=user_id, db=db)
    return courses
