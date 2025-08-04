import pytest
from unittest.mock import AsyncMock, patch
from app.services.futebol_service import FutebolService
from app.crud.clube_repository import ClubeRepository
from app.models.clube import Clube

@pytest.fixture
def mock_clube_repository():
    return AsyncMock(spec=ClubeRepository)

@pytest.fixture
def futebol_service(mock_clube_repository):
    return FutebolService(repository=mock_clube_repository)

@pytest.mark.asyncio
async def test_obter_clubes_da_serie_a_por_cidade_encontrada(futebol_service, mock_clube_repository):
    mock_clubes_data = [
        Clube(nome="Corinthians", estadio="Neo Química Arena", cidade="São Paulo"),
        Clube(nome="Palmeiras", estadio="Allianz Parque", cidade="São Paulo")
    ]
    mock_clube_repository.get_clubes_da_serie_a_por_cidade.return_value = mock_clubes_data

    cidade_teste = "São Paulo"
    resultado = await futebol_service.obter_clubes_da_serie_a_por_cidade(cidade_teste)

    mock_clube_repository.get_clubes_da_serie_a_por_cidade.assert_called_once_with(cidade_teste)
    
    assert resultado["cidade"] == cidade_teste
    assert len(resultado["clubes_serie_a"]) == 2
    assert resultado["clubes_serie_a"][0]["nome_clube"] == "Corinthians"
    assert resultado["clubes_serie_a"][0]["estadio"] == "Neo Química Arena"

@pytest.mark.asyncio
async def test_obter_clubes_da_serie_a_por_cidade_nao_encontrada(futebol_service, mock_clube_repository):
    mock_clube_repository.get_clubes_da_serie_a_por_cidade.return_value = []

    cidade_teste = "Cidade Inexistente"
    resultado = await futebol_service.obter_clubes_da_serie_a_por_cidade(cidade_teste)

    mock_clube_repository.get_clubes_da_serie_a_por_cidade.assert_called_once_with(cidade_teste)
    
    assert resultado["cidade"] == cidade_teste
    assert not resultado["clubes_serie_a"]
    assert "mensagem" in resultado
    assert "nenhum clube da Série A encontrado" in resultado["mensagem"].lower()