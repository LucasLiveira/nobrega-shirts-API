from fastapi import APIRouter, Body

from models.UsuarioModel import UsuarioAdmModel
from repositories.UsuarioAdmRepository import criar_usuarioadm

router = APIRouter()


@router.post("/", response_description="Rota para cadastrar camisa.")
async def rota_cadastrar_usuarioadm(camisas: UsuarioAdmModel = Body(...)):
    resultado = await criar_usuarioadm(camisas)

    return resultado