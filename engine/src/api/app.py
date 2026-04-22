"""FastAPI application entrypoint.

Exposes the HTTP contract consumed by the dashboard. Currently only
health is implemented; VRP solve endpoints land in separate feature
branches.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config.settings import settings
from src.domain.schemas import EngineHealth

ENGINE_VERSION = "0.1.0"

app = FastAPI(
    title="Evolutionary Optimization Framework - Engine",
    version=ENGINE_VERSION,
    description="VRP optimization engine: ILP, metaheuristic and OR-Tools",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get("/health", response_model=EngineHealth)
def health() -> EngineHealth:
    """Liveness / readiness probe used by docker and the dashboard."""
    return EngineHealth(
        status="ok",
        version=ENGINE_VERSION,
        availableEngines=["ilp", "metaheuristic", "ortools"],
    )
