from fastapi import FastAPI
from db import database, notes
from models import Note, NoteIn, NoteDl, NoteUp
from typing import List, Optional

app = FastAPI()

# GET : คือการขอข้อมูลจาก Server โดยจะส่ง data ขอผ่าน URL
# POST : คือการขอสร้างข้อมูลใหม่บน Server
# DELETE : คือการขอลบข้อมูลบน Server
# PUT : คล้าย POST แต่จุดประสงค์ คือ การขออัปเดตข้อมูลทั้งหมดทุก field
# PATCH : คือการอัปเดตข้อมูลเฉพาะ field ที่เราส่งไป


@app.get("/")
def read_root():
    return {"Hello": "Programmers"}


# เชื่อมต่อ Database เมื่อเข้าเว็บ
@app.on_event("startup")
async def startup():
    await database.connect()


# ยกเลิกเชื่อมต่อ Database เมื่อออกจจากเว็บ
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# สร้างข้อมูล
@app.post("/notes/", response_model=Note)
async def create_note(note: NoteIn):
    '''Create Note'''
    query = notes.insert().values(text=note.text, completed=note.completed)
    last_record_id = await database.execute(query)
    return {**note.dict(), "id": last_record_id}


# อัปเดตข้อมูล
@app.put("/notes/")
async def update_note(note: NoteUp):
    '''Update Note'''
    print(note, flush=True)
    query = notes.update().values(completed=note.completed).where(notes.c.id == note.id)
    id = await database.execute(query)
    return id


# อัปเดตข้อมูล
@app.patch("/notes/")
async def patch_note(note: NoteUp):
    '''Patch Note'''
    print(note, flush=True)
    query = notes.update().values(completed=note.completed).where(notes.c.id == note.id)
    id = await database.execute(query)
    return id


# ลบข้อมูล
@app.delete("/notes/")
async def delete_note(note: NoteDl):
    '''Delete Note'''
    print(note, flush=True)
    query = notes.delete().where(notes.c.id == note.id)
    id = await database.execute(query)
    if not id:
        return f"Not found ID : {id}"
    return f"ID : {id} Deleted"


# แสดงข้อมูลรายการ
@app.get("/notes/", response_model=List[Note])
async def read_notes(showCompleted: Optional[bool] = False):
    '''Get Note'''
    query = notes.select()
    query = query.where(notes.c.completed == showCompleted)
    return await database.fetch_all(query)

# mrchoke test

@app.get("/mrchoke")
def mrchoke():
    return "I am MrChoke"

@app.get("/masolae")
def mrchoke():
    return "I am Masolae"

