
from app.database import db

async def get_user_by_email(email: str):
    return await db.users.find_one({"email": email})

async def create_user(user: dict):
    await db.users.insert_one(user)
