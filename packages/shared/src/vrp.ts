/**
 * Contratos de dominio VRP compartidos entre dashboard y motor.
 *
 * Estos tipos son la fuente de verdad del contrato cliente-servidor.
 * El motor FastAPI expone Pydantic models equivalentes; cualquier
 * cambio aqui requiere espejo en engine/src/domain/schemas.py.
 */

export type SolverEngine = "ilp" | "metaheuristic" | "ortools";

export type OptimizationObjective =
  | "distance"
  | "time"
  | "fuel"
  | "cost"
  | "vehicles";

export interface GeoPoint {
  lat: number;
  lng: number;
}

export interface Depot {
  id: string;
  name: string;
  location: GeoPoint;
}

export interface Customer {
  id: string;
  name: string;
  location: GeoPoint;
  demand: number;
  serviceTimeMinutes?: number;
  timeWindow?: { startMinutes: number; endMinutes: number };
}

export interface Vehicle {
  id: string;
  capacity: number;
  maxDurationMinutes?: number;
  fuelConsumptionPerKm?: number;
  costPerKm?: number;
  startDepotId: string;
  endDepotId?: string;
}

export interface VrpInstance {
  id: string;
  name: string;
  depots: Depot[];
  customers: Customer[];
  vehicles: Vehicle[];
  distanceMatrixMeters?: number[][];
  durationMatrixSeconds?: number[][];
}

export interface Route {
  vehicleId: string;
  stops: string[];
  totalDistanceMeters: number;
  totalDurationSeconds: number;
  totalLoad: number;
}

export interface VrpSolution {
  instanceId: string;
  engine: SolverEngine;
  objective: OptimizationObjective;
  objectiveValue: number;
  routes: Route[];
  unassignedCustomerIds: string[];
  elapsedSeconds: number;
  isOptimal: boolean;
}
