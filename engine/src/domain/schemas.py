"""Pydantic schemas mirroring TypeScript shared contracts.

These MUST stay in sync with packages/shared/src/vrp.ts and engine.ts.
Any breaking change here requires the same change on the TS side.
"""

from typing import Literal

from pydantic import BaseModel, Field

SolverEngine = Literal["ilp", "metaheuristic", "ortools"]
OptimizationObjective = Literal["distance", "time", "fuel", "cost", "vehicles"]


class GeoPoint(BaseModel):
    lat: float
    lng: float


class TimeWindow(BaseModel):
    start_minutes: int = Field(alias="startMinutes")
    end_minutes: int = Field(alias="endMinutes")


class Depot(BaseModel):
    id: str
    name: str
    location: GeoPoint


class Customer(BaseModel):
    id: str
    name: str
    location: GeoPoint
    demand: float
    service_time_minutes: int | None = Field(default=None, alias="serviceTimeMinutes")
    time_window: TimeWindow | None = Field(default=None, alias="timeWindow")


class Vehicle(BaseModel):
    id: str
    capacity: float
    max_duration_minutes: int | None = Field(default=None, alias="maxDurationMinutes")
    fuel_consumption_per_km: float | None = Field(default=None, alias="fuelConsumptionPerKm")
    cost_per_km: float | None = Field(default=None, alias="costPerKm")
    start_depot_id: str = Field(alias="startDepotId")
    end_depot_id: str | None = Field(default=None, alias="endDepotId")


class VrpInstance(BaseModel):
    id: str
    name: str
    depots: list[Depot]
    customers: list[Customer]
    vehicles: list[Vehicle]
    distance_matrix_meters: list[list[float]] | None = Field(
        default=None, alias="distanceMatrixMeters"
    )
    duration_matrix_seconds: list[list[float]] | None = Field(
        default=None, alias="durationMatrixSeconds"
    )


class Route(BaseModel):
    vehicle_id: str = Field(alias="vehicleId")
    stops: list[str]
    total_distance_meters: float = Field(alias="totalDistanceMeters")
    total_duration_seconds: float = Field(alias="totalDurationSeconds")
    total_load: float = Field(alias="totalLoad")


class VrpSolution(BaseModel):
    instance_id: str = Field(alias="instanceId")
    engine: SolverEngine
    objective: OptimizationObjective
    objective_value: float = Field(alias="objectiveValue")
    routes: list[Route]
    unassigned_customer_ids: list[str] = Field(alias="unassignedCustomerIds")
    elapsed_seconds: float = Field(alias="elapsedSeconds")
    is_optimal: bool = Field(alias="isOptimal")


class SolveRequest(BaseModel):
    instance: VrpInstance
    engine: SolverEngine
    objective: OptimizationObjective
    time_limit_seconds: int | None = Field(default=None, alias="timeLimitSeconds")
    seed: int | None = None
    engine_params: dict | None = Field(default=None, alias="engineParams")


class EngineHealth(BaseModel):
    status: Literal["ok", "degraded"]
    version: str
    available_engines: list[SolverEngine] = Field(alias="availableEngines")
