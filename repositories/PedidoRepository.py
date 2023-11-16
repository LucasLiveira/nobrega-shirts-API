import motor.motor_asyncio

from decouple import config

from models.PedidoModel import PedidosModel


MONGODB_URL = config("MONGODB_URL")

cliente = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

database = cliente.nobregashirts

pedido_collection = database.get_collection("pedidos")


def pedido_helper(pedidos):
    return {
        "id": str(pedidos["_id"]),
        "item": pedidos["item"],
        "quantidade": pedidos["quantidade"],
        "cliente": pedidos["cliente"]
    }


async def criar_pedido(pedidos: PedidosModel) -> dict:

    pedido_criado = await pedido_collection.insert_one(pedidos.__dict__)

    novo_pedido = await pedido_collection.find_one({"_id": pedido_criado.inserted_id})

    return pedido_helper(novo_pedido)


