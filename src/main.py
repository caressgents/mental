import asyncio
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from src.accounts import create_account, authenticate
from src.ai_chat import generate_response
from src.db import init_db
from pydantic import BaseModel

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class ChatMessage(BaseModel):
    message: str

async def start_app():
    await init_db()

@app.on_event("startup")
async def startup():
    await start_app()

@app.post("/create_account")
async def create_account_post(request: Request, account_data: dict):
    success = await create_account(account_data)
    return {"success": success}

@app.post("/authenticate")
async def authenticate_post(request: Request, account_data: dict):
    success = await authenticate(account_data)
    return {"success": success}

@app.post("/chat")
async def chat_post(chat_message: ChatMessage):
    response = await generate_response(chat_message.message)
    return {"response": response}

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
