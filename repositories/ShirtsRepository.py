import motor.motor_asyncio
from bson import ObjectId

from decouple import config

from models.ShirtsModel import ShirtsModel

MONGODB_URL = config("MONGODB_URL")

cliente = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

database = cliente.nobregashirts

camisa_collection = database.get_collection("camisas")


def camisa_helper(camisas):
    return {
        "id": str(camisas["_id"]),
        "tamanho": camisas["tamanho"],
        "cor": camisas["cor"],
        "marca": camisas["marca"],
        "modelo": camisas["modelo"]
    }


async def cadastrar_camisa(camisas: ShirtsModel) -> dict:
    camisa_cadastrada = await camisa_collection.insert_one(camisas.__dict__)

    nova_camisa = await camisa_collection.find_one({"_id": camisa_cadastrada.inserted_id})

    return camisa_helper(nova_camisa)


async def listar_camisa():
    return camisa_collection.find()


async def atualizar_camisa(id: str, dados_camisas: dict):
    camisa = await camisa_collection.find_one({"_id": ObjectId(id)})

    if camisa:
        camisa_atualizada = await camisa_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": dados_camisas}
        )

        return camisa_helper(camisa_atualizada)


async def deletar_camisa(id: str):
    camisa = await camisa_collection.find_one({"_id": ObjectId(id)})

    if camisa:
        await camisa_collection.delete_one({"_id": ObjectId(id)})