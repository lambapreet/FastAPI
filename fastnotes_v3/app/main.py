from  fastapi import FastAPI
from app.notes import services as note_services
from app.notes.schemas import NoteCreate, NoteUpdate, NotePatch, NoteResponse
from typing import List
from app.db.config import SessionDepends


app = FastAPI()


@app.post("/notes", response_model=NoteResponse)
async def note_create(session:SessionDepends ,new_note: NoteCreate):
    note = await note_services.create_note(session,new_note)
    return note

@app.get("/notes/{note_id}", response_model=NoteResponse)
async def get_note(session:SessionDepends,note_id:int):
    note = await note_services.get_note(session,note_id)
    return note

@app.get("/notes", response_model=List[NoteResponse])
async def get_note_all(session:SessionDepends):
    notes = await note_services.get_all_notes(session)
    return notes

@app.put("/notes/{note_id}",response_model=NoteResponse)
async def note_update(session:SessionDepends,note_id:int, new_note:NoteUpdate):
    note = await note_services.update_notes(session,note_id, new_note)
    return note

@app.patch("/notes/{note_id}",response_model=NoteResponse)
async def note_patch(session:SessionDepends,note_id:int,new_note:NotePatch):
    note = await note_services.patch_notes(session,note_id,new_note)
    return note

@app.delete("/notes/{note_id}")
async def note_delete(session:SessionDepends,note_id:int):
    respones = await note_services.delete_note(session,note_id)
    return respones