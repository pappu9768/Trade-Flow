from schemas.userSchema import UserCreate 
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"])

def register_service(user:UserCreate,db:Session = Depends(get_db)):
    try:
        #check whether mail exist
        existing_user = db.query(User).filter(
            User.email == user.email
        ).first()
        
        if(existing_user):
            return{
                "success":False,
                "Message":"User already Exist"
            }
        #hash pssword
        hashed_passord = pwd_context.hash(user.password)
        
        new_user = User(
            First_Name=user.First_Name,
            Last_Name=user.Last_Name,
            email=user.email,
            password=hashed_passord,
            role="employee"
            
        )
        
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        return {
        "success": True,
        "message": "User registered successfully",
        "data": {
            "id": new_user.id,
            "first_name": new_user.First_Name,
            "last_name": new_user.Last_Name,
            "email": new_user.email,
            "role": new_user.role
            }
        }
    except Exception as e:
        return{
            "error":str(e)
        }
