# Microsserviço de Consulta de Futebol (Série A)

Microsserviço de automatização de pesquisa que, dado o nome de uma cidade do Brasil, retorna quais clubes de futebol da Série A do campeonato nacional mandam seus jogos nela e em qual estádio.

## Tecnologias e Arquitetura

Este projeto foi desenvolvido com uma arquitetura moderna de microsserviços, utilizando as seguintes tecnologias e conceitos:

- **Linguagem:** Python 3.10+
- **Framework API:** **FastAPI**
- **Padronização de Dados:** **Pydantic**
- **Cache:** **Redis** para armazenamento temporário de resultados de pesquisa.
- **Contêinerização:** **Docker**
- **Orquestração:** **Kubernetes (K8s)**
- **Design Patterns:** **Repository Pattern** para abstração da camada de dados.
- **Testes:** Testes unitários com **Pytest**.

## Pré-requisitos

Para rodar este projeto localmente, você precisa ter instalado:

- **Python 3.10+**
- **Docker**
- **Docker Compose** (opcional, para rodar Redis facilmente)
