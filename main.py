# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
# from pymongo import MongoClient




# conn = MongoClient("mongodb://localhost:27017/")
# db = conn["notes"] # database name
# collection = db["notes"] # collection name

# @app.get("/", response_class=HTMLResponse)
# async def read_item(request: Request):
#     docs = collection.find({})
#     newDocs = []
#     for doc in docs:
#         newDocs.append({
#             "id": doc["_id"],
#             "note": doc["note"]
#         })
#     return templates.TemplateResponse(
#         request=request, name="index.html", context={"notes": newDocs}
#     ) 