from schemas.userSchema import UserLogin
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db
from models.user import User
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"])

def login_service(login_user:UserLogin,db:Session=Depends(get_db)):
    try:
        email = db.query(User).filter(
            user.email == User.email
        ).fisrt()

        if not email:
             return {
            "Message":"Invalid email or email not exist",
             "success":False

        }

        check_password = passlib.verify(user.password,User.password)
        if check_password:
            return {
                "Message":"Invalid password",
                "success":False
            }
        return {
        "Message":"Login Successfull",
        "success":True
    }
    except Exception as e:
        return {
            "Error":str(e)
        }
