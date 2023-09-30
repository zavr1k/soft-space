from typing import Optional, Sequence

import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.user import User


class CRUDUser:
    async def create(self, db: AsyncSession, data: dict) -> User:
        stmt = sa.insert(User).values(**data).returning(User)
        result = await db.execute(stmt)
        await db.commit()
        return result.scalar_one()

    async def get(self, db: AsyncSession, user_id: int) -> User:
        query = sa.select(User).filter_by(id=user_id)
        result = await db.execute(query)
        return result.scalar_one()

    async def get_all(
        self,
        db: AsyncSession,
        limit: int = 5,
        offset: Optional[int] = None
    ) -> Sequence[User]:
        query = sa.select(User).limit(limit)

        if offset is not None:
            query = query.offset(offset)

        result = await db.execute(query)
        return result.scalars().all()

    async def update(
        self,
        db: AsyncSession,
        user_id: int,
        data: Optional[dict] = None,
    ) -> User:
        query = sa.update(User).filter_by(id=user_id).returning(User)
        if data:
            query = query.values(**data)
        result = await db.execute(query)
        await db.commit()
        return result.scalar_one()

    async def delete(self, db: AsyncSession, user_id: int) -> None:
        query = sa.delete(User).filter_by(id=user_id)
        await db.execute(query)
        await db.commit()


user = CRUDUser()
