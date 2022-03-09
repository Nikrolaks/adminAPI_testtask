from fastapi import APIRouter, Depends

from typing import List

from ..models.users import User
from ..services.users import UsersService


router = APIRouter(
    prefix='/users'
)


@router.get('/', response_model=List[User])
def get_users(service: UsersService = Depends()):
    return service.get_list()
