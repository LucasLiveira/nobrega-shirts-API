from pydantic import BaseModel, Field, EmailStr


class UsuarioModel(BaseModel):
    id: str = Field(...)
    nome: str = Field(...)
    email: EmailStr = Field(...)
    senha: str = Field(...)

    class Config:
        json_schema_extra = {
            "usuario": {
                "nome": "Nome Sobrenome",
                "emial": "nome@gmail.com",
                "senha": "SenHa123!"
            }
        }


class UsuarioAdmModel(BaseModel):
    nome: str = Field(...)
    cpf: str = Field(...)
    cnpj: str = Field(...)
    email: EmailStr = Field(...)
    senha: str = Field(...)

    class Config:
        json_schema_extra = {
            "usuario": {
                "nome": "Nome Sobrenome",
                "emial": "nome@gmail.com",
                "senha": "SenHa123!"
            }
        }


class UsuarioCriarModel(BaseModel):
    nome: str = Field(...)
    email: EmailStr = Field(...)
    senha: str = Field(...)

    class Config:
        json_schema_extra = {
            "usuario": {
                "nome": "Nome Sobrenome",
                "emial": "nome@gmail.com",
                "senha": "SenHa123!"
            }
        }


class UsuarioLoginModel(BaseModel):
    email: EmailStr = Field(...)
    senha: str = Field(...)

    class Config:
        json_schema_extra = {
            "usuario": {
                "emial": "nome@gmail.com",
                "senha": "SenHa123!"
            }
        }