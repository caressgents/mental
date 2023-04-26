import asyncio
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from src.accounts import create_account, authenticate
from src.ai_chat import generate_response
from src.db import init_db

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

async def start_app():
    await init_db()

@app.on_event("startup")
async def startup():
    asyncio.create_task(start_app())

@app.post("/create_account")
async def create_account_post(request: Request, account_data: dict):
    success = await create_account(account_data)
    return {"success": success}

@app.post("/authenticate")
async def authenticate_post(request: Request, account_data: dict):
    success = await authenticate(account_data)
    return {"success": success}

@app.post("/chat")
async def chat_post(request: Request, message: str):
    response = await generate_response(message)
    return {"response": response}

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
