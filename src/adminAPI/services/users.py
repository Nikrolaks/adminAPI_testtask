from fastapi import Depends
from sqlalchemy.orm import Session

from typing import List

from .. import tables
from ..database import get_session

class UsersService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self) -> List[tables.Users]:
        users = self.session.query(tables.Users).all()
        return users
