from fastapi import FastAPI,Depends
from database import engine,get_db,Base
from sqlalchemy import text
from sqlalchemy.orm import Session
from models.user import User
from schemas.userSchema import UserCreate,UserLogin
from passlib.context import CryptContext

from routes.userRoutes import user_router
pwd_context = CryptContext(schemes=["bcrypt"])
app = FastAPI( title="Trade-Flow")
Base.metadata.create_all(bind=engine)


@app.get("/")
def test():
    return {
        "message":"Server is running"
    }

@app.get("/testdb")
def test_database():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            return {
                "success":True,
                "message":"Connected",
                "result":result.scalar()
            }
            
    except Exception as e:
        return {
            "success":False,
            "error":str(e)
        }
        
# @app.post("/register")
# def registration(user:UserCreate,db:Session = Depends(get_db)):
    # try:
        existing_user = db.query(User).filter(
            User.email == user.email
        ).first()
        
        if(existing_user):
            return{
                "success":False,
                "Message":"User already Exist"
            }
        
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
    # except Exception as e:
        return{
            "error":str(e)
        }

@app.post("/login")
def login(user:UserLogin,db: Session = Depends(get_db)):
    try:
        email_should_exist = db.query(User).filter(
            User.email == user.email
        ).first()

        if not email_should_exist:
            return {
                "message":"Email is invalid or email not exist",
                "success":False
            }
        
        check_password = pwd_context.verify(user.password,email_should_exist.password)
        if not check_password:
            return{
                 "message":"Password is invalid",
                "success":False,
            }
            
    except Exception as e:
        return{
            "error":str(e)
        }