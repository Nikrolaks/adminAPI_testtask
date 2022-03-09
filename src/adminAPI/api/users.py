from fastapi import APIRouter, Depends, Response, status

from typing import List

from ..models.users import User, UserCreate, UserUpdate
from ..services.users import UsersService


router = APIRouter(
    prefix='/users'
)


@router.get('/', response_model=List[User])
def get_users(service: UsersService = Depends()):
    return service.get_list()

@router.get('/{user_id}', response_model=User)
def get_user(user_id: int, service: UsersService = Depends()):
    return service.get(user_id)

@router.post('/', response_model=User)
def create_user(user_data: UserCreate,
                service: UsersService = Depends()):
    return service.create(user_data)


@router.put('/{user_id}', response_model=User)
def update_user(user_id: int, user_data: UserUpdate, service: UsersService = Depends()):
    return service.update(user_id, user_data)


@router.delete('/{user_id}')
def delete_user(user_id: int, service: UsersService = Depends()):
    service.delete(user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
