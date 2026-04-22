import type {
  OptimizationObjective,
  SolverEngine,
  VrpInstance,
  VrpSolution,
} from "./vrp";

/**
 * Contratos HTTP/WebSocket del motor de optimizacion.
 */

export interface SolveRequest {
  instance: VrpInstance;
  engine: SolverEngine;
  objective: OptimizationObjective;
  timeLimitSeconds?: number;
  seed?: number;
  engineParams?: Record<string, unknown>;
}

export interface SolveResponse {
  runId: string;
  status: "queued" | "running" | "completed" | "failed";
  solution?: VrpSolution;
  error?: string;
}

export interface RunProgressEvent {
  runId: string;
  type: "progress" | "improvement" | "log" | "done" | "error";
  elapsedSeconds: number;
  iteration?: number;
  currentObjective?: number;
  message?: string;
}

export interface EngineHealth {
  status: "ok" | "degraded";
  version: string;
  availableEngines: SolverEngine[];
}
