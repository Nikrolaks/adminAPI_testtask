from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from typing import List

from .. import tables
from ..database import get_session
from ..models.users import UserCreate, UserUpdate


class UsersService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, user_id: int) -> tables.Users:
        user = self.session.query(tables.Users).filter_by(id=user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return user

    def get_list(self) -> List[tables.Users]:
        users = self.session.query(tables.Users).all()
        return users

    def get(self, user_id: int) -> tables.Users:
        return self._get(user_id)

    def create(self, user_data: UserCreate) -> tables.Users:
        user = tables.Users(**user_data.dict())
        self.session.add(user)
        self.session.commit()
        return user

    def update(self, user_id: int, user_data: UserUpdate) -> tables.Users:
        user = self._get(user_id)
        for field, value in user_data:
            setattr(user, field, value)
        self.session.commit()
        return user

    def delete(self, user_id: int) -> None:
        user = self._get(user_id)
        self.session.delete(user)
        self.session.commit()
