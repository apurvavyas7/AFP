from fastapi import FastAPI,Request, UploadFile, File
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import os

app = FastAPI()
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


# add path to templates 
templates = Jinja2Templates(directory="./templates")

#Route - Root visit home page
@app.get("/")

# function on root directory
def home(request:Request):
    return templates.TemplateResponse(request,"home.html",{"courses": courses_list })

# file upload route
@app.get("/upload")
def upload_file(request:Request):
    return templates.TemplateResponse(request,"upload.html")

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    with open(file.filename, "wb") as f:
        content = await file.read()
        f.write(content)

    return {"message": "File uploaded successfully"}
    

@app.get("/contactus")
# function on contact us directory
def contact_us():
    return{"message":"Contact Us Page"}