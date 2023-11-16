from fastapi import FastAPI

from routes.ShirtsRoute import router as ShirtsRoute
from routes.UsuarioRoute import router as UsuarioRoute
from routes.UsuarioAdmRoute import router as UsuarioAdmRoute
from routes.AutenticacaoRoute import router as AutenticacaoRoute
from routes.PedidoRoute import router as PedidoRoute

app = FastAPI()

app.include_router(PedidoRoute, tags=["Pedidos"], prefix="/api/pedidos")

app.include_router(AutenticacaoRoute, tags=["Autenticação"], prefix="/api/auth")

app.include_router(ShirtsRoute, tags=["Camisa"], prefix="/api/camisa")

app.include_router(UsuarioAdmRoute, tags=["UsuárioADM"], prefix="/api/usuarioadm")

app.include_router(UsuarioRoute, tags=["Usuário"], prefix="/api/usuario")


@app.get("/api/health", tags=["Health"])
async def health():
    return {
        "status": "OK!"
    }