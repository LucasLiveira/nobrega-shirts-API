from pydantic import BaseModel, Field


class PedidosModel(BaseModel):
    item: str = Field(...)
    quantidade: str = Field(...)
    cliente: str = Field(...)

    class Config:
        json_schema_extra = {
            "usuario": {
                "item": "camisa",
                "quantidade": "2",
                "cliente": "Lucas"
            }
        }
