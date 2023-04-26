import aiosqlite
import os

async def init_db():
    async with aiosqlite.connect("mental_health_chatbot.db") as db:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
            """
        )
        await db.commit()

async def add_user(username: str, password: str) -> bool:
    try:
        async with aiosqlite.connect("mental_health_chatbot.db") as db:
            await db.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password),
            )
            await db.commit()
            return True
    except Exception:
        return False

async def get_user(username: str) -> dict:
    async with aiosqlite.connect("mental_health_chatbot.db") as db:
        cursor = await db.execute(
            "SELECT id, username, password FROM users WHERE username = ?", (username,)
        )
        user = await cursor.fetchone()
        if user:
            return {"id": user[0], "username": user[1], "password": user[2]}
        return None
