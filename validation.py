from pydantic import BaseModel, EmailStr

class user(BaseModel):
    id:int
    name:str = "Apurva"
    sign_ts:str |  None = None
    isactive:bool 
    Email:EmailStr

objuser = user(id=123 ,name="Apurva", isactive=True, Email="apurva@example.com")
print(objuser)