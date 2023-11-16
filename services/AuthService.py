from models.UsuarioModel import UsuarioLoginModel
from repositories.UsuarioRepository import buscar_usuario_por_email
from utils.AuthUtil import verificar_senha


async def login_serice(usuario: UsuarioLoginModel):
    usuario_encontrado = await buscar_usuario_por_email(usuario.email)

    if not usuario:
        return {
            "mensagem": "E-mail ou senha incorretos.",
            "dados": "",
            "status": 401
        }
    else:
        if verificar_senha(usuario.senha, usuario_encontrado["senha"]):
            return {
                "mensagem": "Login realizado com sucesso!",
                "dados": usuario_encontrado,
                "status": 200
            }
        else:
            return {
                "mensagem": "E-mail ou senha incorretos.",
                "dados": "",
                "status": 401
            }
