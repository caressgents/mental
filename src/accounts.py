import os
import hashlib
from dotenv import load_dotenv
from src.db import add_user, get_user

load_dotenv()
salt = os.environ["SALT"]

def hash_password(password):
    return hashlib.sha256((password + salt).encode("utf-8")).hexdigest()

async def create_account(account_data):
    username = account_data["username"]
    password = hash_password(account_data["password"])

    success = await add_user(username, password)
    return success

async def authenticate(account_data):
    username = account_data["username"]
    password = hash_password(account_data["password"])

    user = await get_user(username)
    if user and user["password"] == password:
        return True
    return False
