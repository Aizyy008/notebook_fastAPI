import datetime
from pydantic import BaseModel


class Note(BaseModel):
    id: int
    title: str
    description: str
    important : bool 
    created_at: datetime.datetime
    updated_at: datetime.datetime