from pydantic import BaseModel,EmailStr,Field

class UserCreate(BaseModel):
    First_Name: str
    Last_Name: str
    email: EmailStr
    password: str = Field(min_length=8,max_length=72)
    role: str
    
class UserResponse(BaseModel):
    First_Name: str
    Last_Name: str
    email: EmailStr
    
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8,max_length=72)