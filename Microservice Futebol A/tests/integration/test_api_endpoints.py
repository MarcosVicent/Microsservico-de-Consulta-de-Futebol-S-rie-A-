import pytest
from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch, AsyncMock
from app.models.clube import Clube

client = TestClient(app)

@patch('app.api.v1.endpoints.clube_repo', new_callable=AsyncMock)
@pytest.mark.asyncio
async def test_get_clubes_serie_a_sucesso(mock_clube_repo):
    cidade_teste = "São Paulo"
    mock_clube_repo.get_clubes_da_serie_a_por_cidade.return_value = [
        Clube(nome="Corinthians", estadio="Neo Química Arena", cidade=cidade_teste),
        Clube(nome="Palmeiras", estadio="Allianz Parque", cidade=cidade_teste)
    ]

    response = client.get(f"/api/v1/clubes-serie-a/{cidade_teste}")
    
    assert response.status_code == 200
    data = response.json()
    assert data["cidade"] == cidade_teste
    assert len(data["clubes_serie_a"]) == 2
    assert data["clubes_serie_a"][0]["nome_clube"] == "Corinthians"
    assert data["clubes_serie_a"][1]["estadio"] == "Allianz Parque"

@patch('app.api.v1.endpoints.clube_repo', new_callable=AsyncMock)
@pytest.mark.asyncio
async def test_get_clubes_serie_a_cidade_nao_encontrada(mock_clube_repo):
    cidade_teste = "CidadeInexistente"
    mock_clube_repo.get_clubes_da_serie_a_por_cidade.return_value = []

    response = client.get(f"/api/v1/clubes-serie-a/{cidade_teste}")
    
    assert response.status_code == 404
    assert "Nenhum clube da Série A encontrado" in response.json()["detail"]

@pytest.mark.asyncio
async def test_get_clubes_serie_a_cidade_vazia():
    response = client.get("/api/v1/clubes-serie-a/")
    
    assert response.status_code == 404