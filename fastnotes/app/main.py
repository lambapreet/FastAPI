from  fastapi import FastAPI
from app.notes import services as note_services


app = FastAPI()


@app.post("/notes")
async def note_create(new_note: dict):
    note = await note_services.create_note(new_note["tittle"],new_note["cotent"])
    return note

@app.get("/notes/{note_id}")
async def get_note(note_id:int):
    note = await note_services.get_note(note_id)
    return note

@app.get("/notes")
async def get_note_all():
    notes = await note_services.get_all_notes()
    return notes

@app.put("/notes/{note_id}")
async def note_update(note_id:int, new_note:dict):
    new_tittle = new_note.get("tittle")
    new_cotent = new_cotent.get("cotent")
    note = await note_services.update_notes(note_id, new_tittle, new_cotent)
    return note

@app.patch("/notes/{note_id}")
async def note_patch(note_id:int,new_note:dict):
    new_tittle = new_note.get("tittle")
    new_cotent = new_cotent.get("cotent")
    note = await note_services.patch_notes(note_id, new_tittle, new_cotent)
    return note

@app.delete("/notes/{note_id}")
async def note_delete(note_id:int):
    respones = await note_services.delete_note(note_id)
    return respones