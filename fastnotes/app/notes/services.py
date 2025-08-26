from app.db.config import async_session
from app.notes.models import Note
from sqlalchemy import select
from fastapi import HTTPException


async def create_note(tittle:str, cotent:str):
    async with async_session() as session:
        note = Note(tittle=tittle,cotent=cotent)
        session.add(note)
        await session.commit()
        await session.refresh(note)
        return note
    
async def get_note(note_id:int):
    async with async_session() as session:
        note = await session.get(Note, note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        return note
    
async def get_all_notes():
    async with async_session() as session:
        stmt = select(Note)
        notes = await session.scalars(stmt)
        return notes.all()
    
async def update_notes(note_id:int, new_tittle:str, new_cotent:str):
    async with async_session() as session:
        note = await session.get(Note, note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        note.tittle = new_tittle
        note.cotent = new_cotent
        await session.commit()
        await session.refresh(note)
        return note
    
async def patch_notes(note_id:int, new_tittle:str | None=None, new_cotent:str | None=None):
    async with async_session() as session:
        note = await session.get(Note, note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        
        if new_tittle is not None:
            note.tittle = new_tittle
        if new_cotent is not None:
            note.cotent = new_cotent
        
        await session.commit()
        await session.refresh(note)
        return note
    
async def delete_note(note_id:int):
    async with async_session() as session:
        note = await session.get(Note, note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        await session.delete(note)
        await session.commit()
        return {"msg":"deleted"}