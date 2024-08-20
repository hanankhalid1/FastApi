from fastapi import FastAPI # type: ignore
import uvicorn # type: ignore
from pydantic import BaseModel

app = FastAPI()

class StudentList(BaseModel):
    studentId : int
    studentName : str
    studentAge : int
    studentGrade : str

students : StudentList = [
    {
        "studentId" : 1,
        "studentName" : "John",
        "studentAge" : 20,
        "studentGrade" : "A"
    },
    {
        "studentId" : 2,
        "studentName" : "Doe",
        "studentAge" : 21,
        "studentGrade" : "B"
    }
]

# Reltrive all students
@app.get("/students")
def get_students():
    return students
#retrieving single student
@app.get("/student/{studentId}")
def get_student(studentId:int):
    for student in students:
        if student["studentId"] == studentId:
            return student
    return {"message":"Student not found"}

# adding Student
@app.post("/addStudent")
def add_student(student:StudentList):
    students.append(student)
    return {"message": "Student added successfully"}

# deleting student
@app.delete("/deleteStudent/{studentId}")
def delete_student(studentId:int):
    for student in students:
        if student["studentId"] == studentId:
         students.remove(student)
        return {"message" : "Student is delted succesfully"}
    return {"message" : "Student not found"}

#updating student
@app.put("/updateStudent/{studentId}")
def update_student(studentId: int, student: StudentList):
    for existing_student in students:
        if existing_student["studentId"] == studentId:
            existing_student.update(student.dict())
            return {"message": "Student updated successfully"}
    return {"message": "Student not found"}



















def start():
    uvicorn.run("students.main:app",host="127.0.0.1" , port=8080 , reload=True)