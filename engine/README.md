# Engine

Motor de optimizacion VRP expuesto via FastAPI. Implementa tres solvers conmutables: ILP (PuLP/CBC), metaheuristico (GA memetico + ALNS) y OR-Tools.

## Estructura

```bash
engine/
├── pyproject.toml        # dependencias y metadata
├── ruff.toml             # configuracion del linter
├── .env.example          # variables propias del motor
├── src/
│   ├── api/              # FastAPI app y routers
│   ├── config/           # settings (pydantic-settings)
│   ├── domain/           # schemas (espejo de packages/shared)
│   └── engines/
│       ├── ilp/          # solver ILP (PuLP/CBC)
│       ├── metaheuristic/# GA memetico + ALNS
│       └── ortools/      # solver OR-Tools
└── tests/
```

## Desarrollo local (sin docker)

```bash
cd engine
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
uvicorn src.api.app:app --reload --port ${ENGINE_PORT:-8000}
```

## Tests y linter

```bash
ruff check .
pytest
```
