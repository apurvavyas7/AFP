from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates

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
                }
                ]

# add path to templates 
templates = Jinja2Templates(directory="./templates")

#Route - Root visit home page
@app.get("/")

# function on root directory
def home(request:Request):
    return templates.TemplateResponse(request,"home.html",{"courses": courses_list })

@app.get("/contactus")

# function on contact us directory
def contact_us():
    return{"message":"Contact Us Page"}