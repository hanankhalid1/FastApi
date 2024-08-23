from http.client import HTTPException
from fastapi import FastAPI  
import uvicorn 
from .config.db import create_tables , engine
from sqlmodel import Session  , select 
from .models.todos import Todo , UpdateTodo
from dotenv import load_dotenv


app = FastAPI()

@app.get("/getTodos")
def getTodos():
    with Session(engine) as session:
        statement = select(Todo)
        results = session.exec(statement)
        data = results.all()
        print(data)
        return data

@app.post("/addTodo")
def addTodo(todo : Todo):
    with Session(engine) as session:
        session.add(todo)
        session.commit()
        session.refresh(todo)
        print("Todo added succesfully")
        return todo

@app.put("/updateTodo/{id}")
def update_todo(id: int, todo: UpdateTodo):
    with Session(engine) as session:
        todo_db = session.get(Todo, id)  # Use the 'id' from the URL
        if not todo_db:
            raise HTTPException(status_code=404, detail="Todo not found")

        todo_data = todo.model_dump(exclude_unset=True)  # Corrected typo

        for key, value in todo_data.items():
            setattr(todo_db, key, value)

        session.commit()
        session.refresh(todo_db)
        return {"message": "Todo updated successfully"}
       
    
@app.delete("/deleteTodo/{id}")
def delete_todo(id: int):
    with Session(engine) as session:
        todo = session.get(Todo, id)
        if not todo:
            return None
        session.delete(todo)
        session.commit()
        return {"message": "Todo deleted successfully"}






def start():
    create_tables()
    uvicorn.run("todos.main:app",host="127.0.0.1" , port=8080 , reload=True)