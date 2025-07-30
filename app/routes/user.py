
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from app.schemas import UserCreate
from app.auth import create_token
from app.models import create_user_dict
from app.crud import get_user_by_email, create_user
import re

router = APIRouter()

@router.post("/register")
async def register(user: UserCreate):
    if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d.*\d)[A-Za-z\d]{6,}$", user.password):
        raise HTTPException(status_code=400, detail={"mensaje": "Contraseña no válida"})

    if await get_user_by_email(user.email):
        raise HTTPException(status_code=400, detail={"mensaje": "El correo ya registrado"})

    token = create_token(user.email)
    user_dict = create_user_dict(user, token)
    await create_user(user_dict)
    user_dict.pop("_id", None)
    
    response = jsonable_encoder(user_dict)
    return response
