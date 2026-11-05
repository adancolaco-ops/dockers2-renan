
# Calculadora API com Docker

## Sobre o projeto

Este projeto consiste em uma API de calculadora desenvolvida
com Python e Flask, utilizando PostgreSQL para armazenar
o histórico das operações matemáticas.

A aplicação utiliza Docker e Docker Compose para executar
a API e o banco de dados em containers separados.

## Tecnologias utilizadas

- Python
- Flask
- PostgreSQL
- Docker
- Docker Compose

## Operações disponíveis

- Soma
- Subtração
- Multiplicação
- Divisão
- Potência

## Arquitetura do projeto

O projeto utiliza arquitetura em camadas:

- Controller: recebe as requisições HTTP.
- Service: executa os cálculos e valida os dados.
- Repository: realiza a comunicação com o banco de dados.
- Model: representa os dados dos cálculos.

## Estrutura de pastas

```text
calculadora-camadas/
├── api/
│   ├── app/
│   │   ├── controllers/
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── services/
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── exceptions.py
│   │   └── main.py
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
└── README.md
```

## Como executar

Com o Docker Desktop aberto, execute na pasta principal:

```bash
docker compose up --build
```

## Endereço da API

http://localhost:8000

## Verificação de funcionamento

http://localhost:8000/health

## Banco de dados

- Banco: calculadora
- Usuário: calc
- Porta interna: 5432

## Histórico

Os cálculos realizados são armazenados no PostgreSQL.
