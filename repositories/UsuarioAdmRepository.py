import motor.motor_asyncio
from bson import ObjectId

from decouple import config

from models.UsuarioModel import UsuarioAdmModel

MONGODB_URL = config("MONGODB_URL")

cliente = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

database = cliente.nobregashirts

usuario_collection = database.get_collection("usuarioadm")


def usuarioadm_helper(usuarioadm):
    return {
        "id": str(usuarioadm["_id"]),
        "nome": usuarioadm["nome"],
        "cpf": usuarioadm["cpf"],
        "cnpj": usuarioadm["cnpj"],
        "emial": usuarioadm["email"],
        "senha": usuarioadm["senha"]
    }


async def criar_usuarioadm(usuarioadm: UsuarioAdmModel) -> dict:

    usuarioadm_criado = await usuario_collection.insert_one(usuarioadm.__dict__)

    novo_usuarioadm = await usuario_collection.find_one({"_id": usuarioadm_criado.inserted_id})

    return usuarioadm_helper(novo_usuarioadm)


async def listar_usuarioadm():
    return usuario_collection.find()


async def buscar_usuarioadm_por_email(emial: str) -> dict:
    usuarioadm = await usuario_collection.find_one({"email": emial})

    if usuarioadm:
        return usuarioadm_helper(usuarioadm)


async def atualizar_usuarioadm(id: str, dados_usuarioadm: dict):
    usuarioadm = await usuario_collection.find_one({"_id": ObjectId(id)})

    if usuarioadm:
        usuarioadm_atualizado = await usuario_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": dados_usuarioadm}
        )

        return usuarioadm_helper(usuarioadm_atualizado)


async def deletar_usuarioadm(id: str):
    usuarioadm = await usuario_collection.find_one({"_id": ObjectId(id)})

    if usuarioadm:
        await usuario_collection.delete_one({"_id": ObjectId(id)})