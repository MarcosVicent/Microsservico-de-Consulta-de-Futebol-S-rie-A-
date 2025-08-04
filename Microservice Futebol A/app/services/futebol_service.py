from typing import List, Dict, Any
from app.crud.clube_repository import ClubeRepository
from app.models.clube import Clube

class FutebolService:
    def __init__(self, repository: ClubeRepository):
        self.repository = repository

    async def obter_clubes_da_serie_a_por_cidade(self, cidade: str) -> Dict[str, Any]:
        """
        Obtém os clubes da Série A para uma cidade específica e formata a resposta.
        """
        clubes = await self.repository.get_clubes_da_serie_a_por_cidade(cidade)

        if not clubes:
            return {
                "cidade": cidade,
                "clubes_serie_a": [],
                "mensagem": f"Nenhum clube da Série A encontrado para {cidade} ou cidade não reconhecida."
            }
        
        clubes_formatados = []
        for clube in clubes:
            clubes_formatados.append({
                "nome_clube": clube.nome,
                "estadio": clube.estadio
            })

        return {
            "cidade": cidade,
            "clubes_serie_a": clubes_formatados
        }