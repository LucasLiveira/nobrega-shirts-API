from models.PedidoModel import PedidosModel
from repositories.PedidoRepository import (
    criar_pedido
)


async def registrar_pedido(pedido: PedidosModel):
    novo_pedido = await criar_pedido(pedido)
    return {
        "mensagem": "Pedido realizado com sucesso!",
        "dados": novo_pedido,
        "status": 201
    }
