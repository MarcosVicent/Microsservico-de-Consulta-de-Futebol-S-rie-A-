from fastapi import APIRouter, Depends, HTTPException, status
from app.services.futebol_service import FutebolService
from app.crud.clube_repository import ClubeRepository
from app.models.clube import Clube
from typing import List, Dict, Any

router = APIRouter()

clube_repo = ClubeRepository()

futebol_service = FutebolService(repository=clube_repo)

@router.get(
    "/clubes-serie-a/{cidade}",
    response_model=Dict[str, Any],
    summary="Obtém clubes da Série A por cidade",
    description="Retorna uma lista de clubes da Série A presentes na cidade informada, juntamente com seus estádios."
)
async def get_clubes_serie_a(cidade: str):
    """
    Endpoint para buscar clubes da Série A do Campeonato Brasileiro por cidade.

    - **cidade**: Nome da cidade para pesquisar.
    """
    if not cidade:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="O nome da cidade não pode estar vazio.")

    resultado = await futebol_service.obter_clubes_da_serie_a_por_cidade(cidade.title())

    if not resultado["clubes_serie_a"] and "mensagem" in resultado:
        return resultado
    elif not resultado["clubes_serie_a"]:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nenhum clube da Série A encontrado para a cidade de {cidade}.")
    
    return resultado
