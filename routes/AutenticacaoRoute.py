from fastapi import APIRouter, Body, HTTPException

from models.UsuarioModel import UsuarioLoginModel
from services.AuthService import login_serice

router = APIRouter()


@router.post('/login')
async def login(usuario: UsuarioLoginModel = Body(...)):
    resultado = await login_serice(usuario)

    if not resultado['status'] == 200:
        raise HTTPException(status_code=resultado['status'], detail=resultado['mensagem'],)

    return resultado