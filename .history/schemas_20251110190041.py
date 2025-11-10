# schemas.py
from pydantic import BaseModel, HttpUrl
from typing import Optional

class NoteBase(BaseModel):
    title: str
    content: Optional[str] = None
    source_url: Optional[HttpUrl] = None
    category: Optional[str] = None
    is_favorite: bool = False

class NoteCreate(NoteBase):
    pass

class NoteUpdate(NoteBase):
    pass

class NoteOut(NoteBase):
    id: int
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True
