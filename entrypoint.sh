#!/bin/sh

# Executa as migrações do banco de dados
alembic upgrade head

# Inicia a aplicação FastAPI com Uvicorn
uvicorn fast_zero.app:app --host 0.0.0.0 --port 8000
