import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    API_KEY_FUTEBOL: str = os.getenv("API_KEY_FUTEBOL", "sua_chave_padrao_se_nao_encontrar")

    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", 6379))
    REDIS_DB: int = int(os.getenv("REDIS_DB", 0))
    CACHE_TTL_SECONDS: int = int(os.getenv("CACHE_TTL_SECONDS", 3600))

    PROJECT_NAME: str = "Microsserviço de Futebol - Série A"
    VERSION: str = "0.1.0"

settings = Settings()