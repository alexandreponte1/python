# Use a imagem oficial do Python como base
FROM python:3.12-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo de requisitos (se houver) ou crie um no próximo passo
COPY requirements.txt .

# Instale as dependências (Flask)
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da aplicação para o contêiner
COPY ./app /app

# Exponha a porta 5000 para acesso externo
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
