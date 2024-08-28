from sqlmodel import Field, SQLModel
from typing import Optional

class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    completed: bool = False
class UpdateTodo(SQLModel):
   title : str | None
   description : str | None    
   completed : bool | None