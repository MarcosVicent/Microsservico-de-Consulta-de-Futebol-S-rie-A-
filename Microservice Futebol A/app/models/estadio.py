from pydantic import BaseModel, Field

class Estadio(BaseModel):
    nome: str = Field(..., description="Nome do estádio.")
    capacidade: int = Field(None, description="Capacidade de público do estádio.")