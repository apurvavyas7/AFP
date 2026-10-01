from fastapi import FastAPI,Request, UploadFile, File, HTTPException, Depends
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import os
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

app = FastAPI()

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
outh2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Make List with Dictionary

courses_list = [
                {
                    "id": 1, 
                    "course": "MCA", 
                    "semester": 4, 
                    "subjects": "Python,FastAPI,Research Methodology,Linux"
                },
                {
                    "id": 2, 
                    "course": "BscIT-Hons", 
                    "semester": 8, 
                    "subjects": "C,C++,Java,Networking,Database"
                },
                {
                    "id": 3, 
                    "course": "BscIT-CS", 
                    "semester": 6, 
                    "subjects": "Linux,Server,VirtualMachine,Python"
                },
                {
                    "id": 4, 
                    "course": "BscIT-DS", 
                    "semester": 6, 
                    "subjects": "Python,Data Science,Machine Learning,Deep Learning"
                },
                ]


# Add path to templates 
templates = Jinja2Templates(directory="./templates")

# Load environment variables 
load_dotenv()  

# Route - Root visit home page
@app.get("/")

# Function on root directory
def home(request:Request):
    return templates.TemplateResponse(request,"home.html",{"courses": courses_list })

# File upload route
@app.get("/upload")
def upload_file(request:Request):
    return templates.TemplateResponse(request,"upload.html")

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    with open(file.filename, "wb") as f:
        content = await file.read()
        f.write(content)

    return {"message": "File uploaded successfully"}

# Load environment variables
@app.get("/getENV")
def get_env(request:Request):
    envSettings = {"db_url": os.getenv("DATABASE_URL"),
                   "appName": os.getenv("APP_NAME"),
                   "debugStatus": os.getenv("DEBUG"),
                   "secretKey": os.getenv("SECRET_KEY")}
    return templates.TemplateResponse(request,"environment.html",{"envSettings": envSettings})

# Login
@app.post("/login")
def login(username: str, password: str):
    if username == "admin" and password == "123":
       token = jwt.decode({"sub": username}, SECRET_KEY, algorithm=ALGORITHM)
       return {"access_token": token}

    raise HTTPException(status_code=401, detail="Invalid username or password")

# protected API
@app.get("/protected")
def profile(token: str = Depends(outh2_scheme)):
    try:
       data=jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
       return {"message": f"Welcome {data['sub']}! This is a protected route."}
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Function on contact us directory
@app.get("/contactus")
def contact_us():
    return{"message":"Contact Us Page"}