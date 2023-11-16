from fastapi import APIRouter, Body

from models.ShirtsModel import ShirtsModel
from repositories.ShirtsRepository import cadastrar_camisa

router = APIRouter()


@router.post("/", response_description="Rota para cadastrar camisa.")
async def rota_cadastrar_camisa(camisas: ShirtsModel = Body(...)):
    resultado = await cadastrar_camisa(camisas)

    return resultado