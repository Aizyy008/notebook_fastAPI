from models.note import Note

def note_dict(item) -> dict:
    return {
        "id": str(item.get("_id", "")),
        "title": item.get("title", ""),
        "description": item.get("description", ""),
        "important": item.get("important", False),
    }

def  Notes(items) -> list:
    return [note_dict(item) for item in items]