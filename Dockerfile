FROM python:3.13-slim

# Instala make e dependências básicas
RUN apt-get update && apt-get install -y make gcc && rm -rf /var/lib/apt/lists/*

# Cria um usuário não-root
RUN adduser --disabled-password --gecos '' devuser

# Diretório de trabalho dentro do container
WORKDIR /home/devuser/app

COPY requirements.txt .
COPY pyproject.toml .

RUN pip install --no-cache-dir -r requirements.txt && pip install -e .

COPY . .

CMD ["pytest"]
