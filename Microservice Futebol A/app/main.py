from fastapi import FastAPI
from app.api.v1 import endpoints
from app.core.config import settings
import uvicorn

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Microsserviço de automatização de pesquisa sobre clubes da Série A do Campeonato Brasileiro por cidade.",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(endpoints.router, prefix="/api/v1", tags=["Futebol"])

@app.get("/", include_in_schema=False)
async def read_root():
    return {"message": "Bem-vindo ao Microsserviço de Futebol. Acesse /docs para a documentação da API."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)