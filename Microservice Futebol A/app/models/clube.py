from pydantic import BaseModel, Field

class Clube(BaseModel):
    nome: str = Field(..., description="Nome do clube.")
    estadio: str = Field(..., description="Nome do estádio onde o clube manda suas partidas.")
    cidade: str = Field(..., description="Cidade do clube.")