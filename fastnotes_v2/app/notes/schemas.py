from pydantic import BaseModel

class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    pass

class NoteUpdate(NoteBase):
    pass

class NotePatch(BaseModel):   # for partial update
    title: str | None = None
    content: str | None = None

class NoteResponse(NoteBase):
    id: int

    class Config:
        from_attributes = True
