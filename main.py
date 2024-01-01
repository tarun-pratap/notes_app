# from typing import Union
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
# from fastapi import FastAPI,Request
# from pymongo import MongoClient

# app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")
# templates = Jinja2Templates(directory="templates")
# conn=MongoClient("mongodb+srv://tarun3135:KhD6gpkuABrT1fdY@mongoyoutube.tn1bhqh.mongodb.net")

# @app.get("/", response_class=HTMLResponse)
# async def read_item(request: Request):
#     docs=conn.notes.notes.find_one({})
#     print(docs)
#     return templates.TemplateResponse("index.html", {"request": request})

from typing import Union
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from pymongo import MongoClient


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Connect to MongoDB
conn = MongoClient("mongodb+srv://tarun3135:KhD6gpkuABrT1fdY@mongoyoutube.tn1bhqh.mongodb.net")

