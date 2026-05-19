# =========================
# Builder Stage
# =========================
FROM python:3.14-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalar Poetry
RUN pip install poetry

# Copiar archivos dependencias
COPY pyproject.toml poetry.lock ./

# Desactivar virtualenvs Poetry
RUN poetry config virtualenvs.create false

# Instalar dependencias
RUN poetry install --no-interaction --no-root

# =========================
# Runtime Stage
# =========================
FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# IMPORTANTE 😄🔥
ENV PYTHONPATH=/app/src

WORKDIR /app

# Copiar librerías instaladas desde builder
COPY --from=builder /usr/local/lib/python3.14 /usr/local/lib/python3.14

# Copiar binarios instalados (uvicorn, etc)
COPY --from=builder /usr/local/bin /usr/local/bin

# Copiar código proyecto
COPY . .

# Exponer puerto FastAPI
EXPOSE 8000

# Ejecutar aplicación
CMD ["uvicorn", "proyecto_final.api.main:app", "--host", "0.0.0.0", "--port", "8000"]