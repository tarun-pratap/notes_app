# from fastapi import APIRouter
# from models.note import Note
# from config.db import conn
# from typing import Union
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from fastapi import FastAPI, Request
# from schemas.note import noteEntity,notesEntity
# note=APIRouter()
# templates = Jinja2Templates(directory="templates")
# @note.get("/", response_class=HTMLResponse)
# async def read_item(request: Request):
#         docs = conn.notes.notes.find({})
#         newDocs=[]
#         for doc in docs:
#                 newDocs.append({
#                         "id": str(doc["_id"]),
#                         "title":doc["title"],
#                         "desc":doc["desc"],
#                         "important":doc["important"]
#                 })
#         return templates.TemplateResponse("index.html", {"request": request, "newDocs":newDocs})
    
# @note.post("/")
# # async def create_item(request:Request):
# #         form=await request.form()
# #         formDict=dict(form)
# #         formDict['important']=True if formDict['important']=="on" else False
# #         note=conn.notes.notes.insert_one(formDict)
# #         return {"success":True}
# async def create_item(request: Request):
#     form = await request.form()
#     formDict = dict(form)
    
#     # Use get method to safely retrieve the value of 'important'
#     # If 'important' is not in formDict, default to False
#     is_important = formDict.get('important', False)
    
#     # Convert the value to a boolean
#     formDict['important'] = True if is_important == "on" else False

#     # Assuming conn is defined elsewhere in your code
#     note = conn.notes.notes.insert_one(formDict)
#     return {"success": True}
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request,HTTPException
from fastapi.responses import PlainTextResponse

from config.db import conn

note = APIRouter()
templates = Jinja2Templates(directory="templates")

# @note.get("/", response_class=HTMLResponse)
# async def read_item(request: Request):
#     # Retrieve all notes from the database
#     docs = conn.notes.notes.find({})
    
#     # Convert ObjectId to string and create a list of notes
#     new_docs = [
#         {
#             "id": str(doc["_id"]),
#             "title": doc["title"],
#             "desc": doc["desc"],
#             "important": doc["important"]
#         }
#         for doc in docs
#     ]
    
#     return templates.TemplateResponse("index.html", {"request": request, "newDocs": new_docs})
# @note.get("/retrieve_note")
# async def retrieve_note(request: Request, title: str):
#     # Retrieve the note based on the entered title
#     note = conn.notes.notes.find_one({"title": title})

#     # Check if the note exists
#     if note:
#         # Return the note details in JSON format
#         return {"id": str(note["_id"]),
#                  "title": note["title"], 
#                  "desc": note["desc"], "important": note["important"]}
#     else:
#         # If the note doesn't exist, raise a 404 error
#         raise HTTPException(status_code=404, detail="Note not found")
@note.get("/retrieve_note")
async def retrieve_note(request: Request, title: str):
    # Retrieve the note based on the entered title
    note = conn.notes.notes.find_one({"title": title})

    # Check if the note exists
    if note:
        # Format the note details as plain text with headings
        note_details_text = f"ID: {str(note['_id'])}\n" \
                            f"Title: {note['title']}\n" \
                            f"Description: {note['desc']}\n" \
                            f"Important: {note['important']}"

        # Return the formatted note details as plain text
        return PlainTextResponse(content=note_details_text, media_type="text/plain")
    else:
        # If the note doesn't exist, raise a 404 error
        raise HTTPException(status_code=404, detail="Note not found")
@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    form_dict = dict(form)
    
    # Use get method to safely retrieve the value of 'important'
    # If 'important' is not in form_dict, default to False
    is_important = form_dict.get('important', False)
    
    # Convert the value to a boolean
    form_dict['important'] = True if is_important == "on" else False

    # Assuming conn is defined elsewhere in your code
    # Insert the new note into the database
    note = conn.notes.notes.insert_one(form_dict)

    # Retrieve all notes from the database again
    # docs = conn.notes.notes.find({})
    
    # # Convert ObjectId to string and create a list of notes
    # new_docs = [
    #     {
    #         "id": str(doc["_id"]),
    #         "title": doc["title"],
    #         "desc": doc["desc"],
    #         "important": doc["important"]
    #     }
    #     for doc in docs
    # ]

    # Pass the updated list of notes to the template
    return templates.TemplateResponse("index.html", {"request": request, "success": True})
