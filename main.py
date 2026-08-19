from fastapi import FastAPI

app = FastAPI()

#Route - Root
@app.get("/")

# function on root directory
def home():
    return{"message":"Good Morning"}