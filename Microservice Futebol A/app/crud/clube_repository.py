import httpx
from typing import List, Dict, Any, Optional
import redis
import json
from app.models.clube import Clube
from app.core.config import settings

class ClubeRepository:
    def __init__(self):
        self.redis_client = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
            decode_responses=True
        )
        self.cache_ttl = settings.CACHE_TTL_SECONDS
        self.api_key = settings.API_KEY_FUTEBOL

        self.mock_data = {
            "São Paulo": [
                {"nome": "Corinthians", "estadio": "Neo Química Arena", "cidade": "São Paulo"},
                {"nome": "Palmeiras", "estadio": "Allianz Parque", "cidade": "São Paulo"},
                {"nome": "São Paulo FC", "estadio": "MorumBIS", "cidade": "São Paulo"}
            ],
            "Rio de Janeiro": [
                {"nome": "Flamengo", "estadio": "Maracanã", "cidade": "Rio de Janeiro"},
                {"nome": "Fluminense", "estadio": "Maracanã", "cidade": "Rio de Janeiro"},
                {"nome": "Vasco da Gama", "estadio": "São Januário", "cidade": "Rio de Janeiro"},
                {"nome": "Botafogo", "estadio": "Estádio Nilton Santos", "cidade": "Rio de Janeiro"}
            ],
            "Belo Horizonte": [
                {"nome": "Atlético-MG", "estadio": "Arena MRV", "cidade": "Belo Horizonte"},
                {"nome": "Cruzeiro", "estadio": "Mineirão", "cidade": "Belo Horizonte"}
            ],
            "Porto Alegre": [
                {"nome": "Grêmio", "estadio": "Arena do Grêmio", "cidade": "Porto Alegre"},
                {"nome": "Internacional", "estadio": "Estádio Beira-Rio", "cidade": "Porto Alegre"}
            ],
        }

    async def get_clubes_da_serie_a_por_cidade(self, cidade: str) -> List[Clube]:
        cache_key = f"clubes_serie_a_{cidade.lower().replace(' ', '_')}"
        
        cached_data = self.redis_client.get(cache_key)
        if cached_data:
            print(f"Dados para {cidade} recuperados do Redis Cache.")
            return [Clube(**clube_dict) for clube_dict in json.loads(cached_data)]

        print(f"Dados para {cidade} não encontrados no cache, buscando da fonte original.")
        
        clubes_data = self.mock_data.get(cidade, [])

        clubes = [Clube(**clube_data) for clube_data in clubes_data]

        if clubes:
            self.redis_client.setex(cache_key, self.cache_ttl, json.dumps([c.dict() for c in clubes]))
            print(f"Dados para {cidade} salvos no Redis Cache.")
        
        return clubes