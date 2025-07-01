from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from models.note import Note
from config.db import get_collection
from schemas.note import Notes, note_dict
from fastapi.templating import Jinja2Templates
from bson import ObjectId

note_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@note_router.get("/add-note/", response_class=HTMLResponse)
async def add_note_form(request: Request):
    return templates.TemplateResponse("add_note.html", {"request": request})

@note_router.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@note_router.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

@note_router.get("/notes")
async def get_notes(request: Request):
    newNotes = Notes(get_collection().find())
    return templates.TemplateResponse("index.html", {"request": request, "notes": newNotes})


@note_router.post("/add-note/", response_class=HTMLResponse)
async def add_note(
    request: Request,
    title: str = Form(...),
    description: str = Form(""),
    important: bool = Form(False)
):
    note = {"title": title, "description": description, "important": important}
    get_collection().insert_one(note)
    return templates.TemplateResponse("add_note.html", {"request": request, "success": True})

@note_router.get("/update-note/{note_id}", response_class=HTMLResponse)
async def update_note_form(request: Request, note_id: str):
    note = get_collection().find_one({"_id": ObjectId(note_id)})
    if not note:
        return HTMLResponse("Note not found", status_code=404)
    note["id"] = str(note["_id"])
    return templates.TemplateResponse("update_note.html", {"request": request, "note": note})

@note_router.post("/delete-note/{note_id}")
async def delete_note(request: Request, note_id: str):
    get_collection().delete_one({"_id": ObjectId(note_id)})
    # Redirect to notes page after deletion
    return RedirectResponse(url="/notes", status_code=303)