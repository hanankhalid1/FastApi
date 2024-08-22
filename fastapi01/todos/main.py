from fastapi import FastAPI 
import uvicorn 
from sqlmodel import Field, SQLModel,Session , create_engine  , select 



app = FastAPI()

connection_string = 'postgresql://postgres.rcunvoreahgsktsjwata:Hananplus1434*@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres'

connection = create_engine(connection_string)

class Students(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    rollNo: str

SQLModel.metadata.create_all(connection)

@app.get("/getStudents")
def get_students():
     with Session(connection) as session:
         statement = select(Students)
         result = session.exec(statement)
         data = result.all()
         print(data)
         return data
     
@app.get("/getSingleStudent")
def get_single_student():
    with Session(connection) as session:
        statement = select(Students).where(
        Students.id == 1)
        result = session.exec(statement)
        print(result)
        return result.all()
    
@app.post("/addStudents")
def add_students():
    student1 = Students(id = 3 , name = "Umer" , rollNo = "42")
    student2 = Students(id = 4 , name = "Haroon" , rollNo = "12")
    
    session  = Session(connection)
    session.add(student1)
    session.add(student2)
    session.commit()
    return "Data added successfuly"

@app.post("/postStudents")
def post_students(id : int , name : str , rollNo : str):
    student = Students(id = id , name = name , rollNo = rollNo)
    session = Session(connection)
    session.add(student)
    session.commit()
    return "Data added successfully by query param"

@app.put("/updateStudents")
def update_students( id : int , name : str):
    with Session(connection) as session:
        statement = select(Students).where(Students.id ==id )
        result = session.exec(statement)
        updatedStudent = result.one()
        updatedStudent.name = name
        session.add(updatedStudent)
        session.commit()
        print(updatedStudent)
        return "Data updated successfully"
    
@app.delete("/deleteStudents")
def delete_students(id : int):
    with Session(connection) as session:
        statement = select(Students).where(Students.id == id)
        result = session.exec(statement)
        student = result.one()
        session.delete(student)
        session.commit()
        return "Data deleted successfully"

    

# dynamic path or path variable

# @app.get("/gettodos/{userName}/{rollNo}")
# def get_todos(userName  , rollNo ):
#     print("Get todos called" , userName , rollNo)
#     return userName + rollNo
# #  Query param

# @app.get("/getSingleTodo")
# def get_single_todo(userName , rollNo):
#     print("Get single todo called" , userName , rollNo)
#     return userName + rollNo



# @app.post("/addTodo")
# def add_todo():
#     print("Add todo called")

#     return "addTodo is being called!!!"

# @app.get("/")
# def home():
#     return "Welcome to the todos app"

def start():
    uvicorn.run("todos.main:app",host="127.0.0.1" , port=8080 , reload=True)