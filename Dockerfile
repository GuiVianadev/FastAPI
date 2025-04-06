FROM python:3.12-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o conteúdo da aplicação para dentro do container
COPY . .

# Garante que o script de inicialização está presente e tem permissão de execução
COPY entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

# Atualiza o pip e instala as dependências do projeto
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta usada pela aplicação
EXPOSE 8000

# Define o script de entrada do container
CMD ["./entrypoint.sh"]
