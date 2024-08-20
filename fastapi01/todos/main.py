from fastapi import FastAPI # type: ignore
import uvicorn # type: ignore

app = FastAPI()

# dynamic path or path variable

@app.get("/gettodos/{userName}/{rollNo}")
def get_todos(userName  , rollNo ):
    print("Get todos called" , userName , rollNo)
    return userName + rollNo
#  Query param

@app.get("/getSingleTodo")
def get_single_todo(userName , rollNo):
    print("Get single todo called" , userName , rollNo)
    return userName + rollNo



@app.post("/addTodo")
def add_todo():
    print("Add todo called")

    return "addTodo is being called!!!"

@app.get("/")
def home():
    return "Welcome to the todos app"

def start():
    uvicorn.run("todos.main:app",host="127.0.0.1" , port=8080 , reload=True)