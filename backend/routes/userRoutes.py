from fastapi import APIRouter
from controllers.user_controllers import register_user,login_user
from schemas.userSchema import UserCreate
user_router = APIRouter(prefix='/users',tags=['users'])

@user_router.post("/register")
def register_a_new_user(user:UserCreate):
    return register_user(user)

@user_router.post("/login")
def login_existing_user():
    return login_user()