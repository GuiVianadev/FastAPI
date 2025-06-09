# ✅ FastAPI Task API

Este é um projeto de API REST para gerenciamento de tarefas, desenvolvido com **FastAPI**, utilizando autenticação JWT, validação de dados com **Pydantic**, testes com **Pytest**, deploy com **Docker** e CI/CD via **GitHub Actions**.

---

## 🚀 Tecnologias Utilizadas

- **FastAPI** – Framework assíncrono para construção de APIs modernas e rápidas
- **Pydantic** – Validação de dados e criação de schemas
- **JWT (JSON Web Tokens)** – Autenticação e autorização segura
- **Pytest** – Testes automatizados
- **Docker** – Containerização da aplicação
- **GitHub Actions** – Integração contínua

---
```
## 📁 Estrutura do Projeto

fast_zero/
├── routers/ # Rotas da API (auth, users, todos)
├── app.py # Instância da aplicação FastAPI
├── database.py # Conexão com o banco de dados
├── models.py # Definição dos modelos SQLAlchemy
├── schemas.py # Schemas com Pydantic
├── security.py # Lógica de autenticação (JWT)
├── settings.py # Configurações de ambiente
migrations/ # Migrações de banco de dados
tests/ # Testes com pytest
.github/workflows/ci.yml # Workflow de CI (GitHub Actions)
Dockerfile # Dockerização do projeto
compose.yaml # Compose para ambiente com banco
.env # Variáveis de ambiente
---
```

## ⚙️ Como Executar

### 1. Clonar o projeto

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
2. Configurar variáveis de ambiente
Crie um arquivo .env com as configurações necessárias, por exemplo:

env
Copy
Edit
SECRET_KEY=chave_secreta_segura
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./database.db
3. Executar com Docker
bash
Copy
Edit
docker compose up --build
Acesse em: http://localhost:8000/docs

📚 Documentação
Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

🔐 Autenticação
A API utiliza autenticação baseada em JWT. Após o login, use o token recebido nas requisições:

http
Copy
Edit
Authorization: Bearer <seu_token>
✏️ Funcionalidades
✅ Registro e login de usuários

✅ Criação, listagem, edição e remoção de tarefas

✅ Validação de dados com Pydantic

✅ Testes automatizados para todas as rotas

✅ Proteção de rotas com JWT

✅ CI com GitHub Actions

✅ Containerização com Docker

🧪 Rodar os testes
bash
Copy
Edit
pytest
A cobertura de testes será gerada em htmlcov/ se configurada com pytest-cov.

🔄 CI com GitHub Actions
O workflow .github/workflows/ci.yml roda os testes automaticamente a cada push/pull request:

yaml
Copy
Edit
name: CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      - name: Run tests
        run: |
          pytest
🐳 Docker
Dockerfile
Contém a definição da imagem da aplicação com base em Python:

dockerfile
Copy
Edit
FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "fast_zero.app:app", "--host", "0.0.0.0", "--port", "8000"]
docker-compose.yml
Define os serviços (ex: app e banco de dados):

yaml
Copy
Edit
version: '3.9'
services:
  app:
    build: .
    ports:
      - "8000:8000"
    env_file:
      - .env
    volumes:
      - .:/app
📄 Licença
Distribuído sob a licença MIT. Veja LICENSE para mais detalhes.
