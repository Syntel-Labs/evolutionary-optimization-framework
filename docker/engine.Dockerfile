# syntax=docker/dockerfile:1.7
# FastAPI engine (development target).
# Installs PuLP (with CBC), OR-Tools and the rest of the Python stack.
# The source tree is bind-mounted in docker compose for live reload.

FROM python:3.11-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        coinor-cbc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

FROM base AS dev
COPY engine/pyproject.toml ./
RUN pip install --upgrade pip && pip install -e ".[dev]" || true
COPY engine/ ./
RUN pip install -e ".[dev]"
EXPOSE 8000
CMD ["sh", "-c", "uvicorn src.api.app:app --host 0.0.0.0 --port ${ENGINE_PORT:-8000} --reload"]
