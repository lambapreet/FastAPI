from app.db.config import async_session
from app.notes.models import Note
from sqlalchemy import select
from fastapi import HTTPException
from app.notes.schemas import NoteCreate, NoteUpdate, NotePatch, NoteResponse
from sqlalchemy.ext.asyncio import AsyncSession


async def create_note(session:AsyncSession,new_note: NoteCreate):
        note = Note(tittle=new_note.tittle,cotent=new_note.cotent)
        session.add(note)
        await session.commit()
        await session.refresh(note)
        return note
    
async def get_note(session:AsyncSession,note_id:int):
        note = await session.get(Note, note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        return note
    
async def get_all_notes(session:AsyncSession,):
        stmt = select(Note)
        notes = await session.scalars(stmt)
        return notes.all()
    
async def update_notes(session:AsyncSession,note_id:int, new_note:NoteUpdate):
        note = await session.get(Note, note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        
        # 🚨 Typo here
        note.tittle = new_note.tittle   # should be title (if your model uses title)
        note.cotent = new_note.cotent   # should be content (spelling issue)

        await session.commit()
        await session.refresh(note)
        return note

    
async def patch_notes(session:AsyncSession,note_id:int, new_note: NotePatch):
        note = await session.get(Note, note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        
        if new_note.tittle is not None:
            note.tittle = new_note.tittle
        if new_note.cotent is not None:
            note.cotent = new_note.cotent
        
        await session.commit()
        await session.refresh(note)
        return note
    
async def delete_note(session:AsyncSession,note_id:int):
        note = await session.get(Note, note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        await session.delete(note)
        await session.commit()
        return {"msg":"deleted"}