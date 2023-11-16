from fastapi import APIRouter, Body, HTTPException

from models.PedidoModel import PedidosModel
from services.PedidoService import (
   registrar_pedido
)

router = APIRouter()


@router.post("/", response_description="Rota para realização dos pedidos.")
async def rota_criar_pedido(pedido: PedidosModel = Body(...)):
        resultado = await registrar_pedido(pedido)

        if not resultado['status'] == 201:
            raise HTTPException(status_code=resultado['status'], detail=resultado['mensagem'])

        return resultado
