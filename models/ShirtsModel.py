from pydantic import BaseModel, Field


class ShirtsModel(BaseModel):
    tamanho: str = Field(...)
    cor: str = Field(...)
    marca: str = Field(...)
    modelo: str = Field(...)

    class Config:
        json_schema_extra = {
            "camisas": {
                "tamanho": "P, M, G...",
                "cor": "branco, preto, azul, vermelho...",
                "marca": "boss, rutra, nike, adidas...",
                "modelo": "camiseta, regata, camisa..."
            }
        }