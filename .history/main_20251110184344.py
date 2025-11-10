from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional

from db import(
    init_db,
    create_note_db,
    get_note_db,
    get_note_db,
    list_notes_db,
    update_note_db,
    delete_note_db,
)

from schemas import NoteCreate, NoteUpdate, NoteOut

app = FastAPI(title="Personal Knowledge API")

@app.on_event("startup") #create the schemas while the app is running
def on_startup():
    init_db()
    
def row_to_note_out(row) -> NoteOut:
    return NoteOut(
        id = row[0],
        title= row[1],
        content=row[2],
        source_url=row[3],
        category=row[4],
        is_favorite=bool(row[5]),
        created_at=row[6],
        updated_at=row[7],
    )
    
@app.post("/notes", response_model=NoteOut)
def create_note(note: NoteCreate):
    note_id = create_note_db(
        title=note.title,
        content=note.content,
        source_url=str(note.source_urşl) if note.source_url else None,
        category=note.category,
        is_favorite=note.is_favorite,
    )
    row = get_note_db(note_id)
    return row_to_note_out(row)

@app.get("/notes", response_model=List[NoteOut])
def list_notes(
    
    category: Optional[str] = None,
    search: Optional[str] = None,
    is_favorite: Optional[bool] = Query(default=None),
):
    rows = list_notes_db(category=category, search=search, is_favorite=is_favorite)
    return [row_to_note_out(r) for r in rows]


@app.get("/notes/{note_id: int}", response_model=NoteOut)
def get_note(note_id: int):
   
    row = get_note_db(note_id)
    if not row:
        raise HTTPExceptiom(status_code=404, detail="Note not found")
    return row_to_note_out(row)
    

@app.put("/notes/{note_id}", response_model=NoteOut)
def update_note(note_id: int, note: NoteUpdate):
    
    row = get_note_db(note_id)
    if not row:
        raise HTTPException(status_code=404, detail="Notenot found")
    
    update_note_db(
        note_id=note_id,
        title=note.title,
        content=note.content,
        source_url=str(note.source_url) if note.source_url else None,
        category=note.category,
        is_favorite=note.is_favorite,
    )
    updated_row = get_note_db(note_id)
    return row_to_note_out(updated_row)

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    row =get_note_db(note_id)
    if not row:
        raise HTTPException(status_code=404, detail="Note not found")
    delete_note_db(note_id)
    return {"detail": "Note deleted"}
