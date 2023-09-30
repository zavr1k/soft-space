from dataclasses import asdict
from typing import Optional

from fastapi import APIRouter, Depends, status

from src import crud
from src.dependencies import get_async_session
from src.schemas.user import User, UserCreate
from src.settings import settings

router = APIRouter(prefix="/user", tags=["User"])


@router.get("/", response_model=list[User], status_code=status.HTTP_200_OK)
async def get_all(
    limit: int = 5,
    offset: Optional[int] = None,
    db=Depends(get_async_session)
) -> list[User]:
    limit = min(max(limit, 0), settings.FETCH_LIMIT)
    users = await crud.user.get_all(db, limit=limit, offset=offset)
    return [User(**asdict(user)) for user in users]


@router.get("/{id}", response_model=User, status_code=status.HTTP_200_OK)
async def get(id: int, db=Depends(get_async_session)):
    user = await crud.user.get(db, id)
    return User(**asdict(user))


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create(user: UserCreate, db=Depends(get_async_session)):
    new_user = await crud.user.create(db, user.model_dump())
    return User(**asdict(new_user))


@router.patch("/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
async def update(user_id: int, update_data: UserCreate, db=Depends(get_async_session)):
    updated_user = await crud.user.update(db, user_id, update_data.model_dump())
    return User(**asdict(updated_user))


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(user_id: int, db=Depends(get_async_session)):
    await crud.user.delete(db, user_id)
