FROM python:3.12.1-slim as python-base

# Configurações de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Instalação de dependências de sistema
RUN apt-get update && apt-get install --no-install-recommends -y \
    curl build-essential

# Instalação do Poetry
RUN pip install poetry

# Definir o diretório de trabalho para a instalação das dependências
WORKDIR $PYSETUP_PATH

# Copiar arquivos Poetry antes de instalar dependências
COPY poetry.lock pyproject.toml ./

# Instalar dependências do projeto
RUN poetry install --no-dev

RUN apt-get update && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

# Definir o diretório de trabalho para o código da aplicação
WORKDIR /app

# Copiar o código-fonte da aplicação
COPY . /app/

# Expor a porta 8000 para o Django
EXPOSE 8000

# Comando para rodar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
