from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from typing import List

from ..models.users import User
from .. import tables
from ..database import get_session


router = APIRouter(
    prefix='/users'
)


@router.get('/', response_model=List[User])
def get_users(session: Session = Depends(get_session)):
    users = (
        session.query(tables.Users).all()
    )
    return users
