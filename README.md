# Evolutionary Optimization Framework

Framework modular de optimizacion para problemas de ruteo de vehiculos (VRP) con multiples motores conmutables: programacion lineal entera (ILP), metaheuristicas hibridas (GA memetico + ALNS) y un solver industrial de referencia (OR-Tools). Diseñado para escenarios logisticos reales: varios viajeros, flota heterogenea, capacidad, ventanas horarias y funcion objetivo configurable (distancia, tiempo, combustible, costo).

## Problema objetivo

Ruteo de vehiculos (VRP y variantes) como generalizacion del TSP:

- Multiples vehiculos con uno o varios depositos
- Capacidades por vehiculo (CVRP)
- Ventanas horarias por cliente (VRPTW)
- Funcion objetivo parametrizable: minimizar distancia, tiempo, combustible, costo o numero de vehiculos
- Sin dependencia de IA ni modelos entrenados: algoritmos deterministas y heuristicos clasicos

## Motores de optimizacion

| Motor           | Tipo                       | Uso recomendado                                      |
| --------------- | -------------------------- | ---------------------------------------------------- |
| ILP (PuLP/CBC)  | Exacto                     | Instancias pequeñas, validacion de calidad           |
| Metaheuristico  | GA memetico + ALNS         | Instancias medianas y grandes, calidad industrial    |
| OR-Tools        | Solver industrial Google   | Baseline robusto, VRPTW y restricciones complejas    |

## Arquitectura

- **Motor**: Python (FastAPI) sirviendo los tres solvers
- **Dashboard**: TypeScript + Next.js (App Router) con shadcn/ui + Tailwind
- **Base de datos**: PostgreSQL + Prisma
- **Mapas**: MapLibre GL (open-source)
- **i18n**: next-intl (español / ingles)
- **Tema**: next-themes (oscuro / claro)
- **Orquestacion**: Docker Compose

## Estructura del repositorio

```bash
.
├── apps/
│   └── dashboard/           # Next.js (TypeScript)
├── engine/                  # Motor Python (FastAPI + solvers)
│   ├── ilp/                 # Solver ILP (PuLP/CBC)
│   ├── metaheuristic/       # GA memetico + ALNS
│   └── ortools/             # Solver OR-Tools
├── packages/
│   └── shared/              # Tipos y contratos compartidos TS
├── docker/                  # Dockerfiles y compose
├── docs/                    # Documentacion tecnica
└── README.md
```

## Licencia

Copyright (c) 2026 Syntel Labs. All rights reserved. Uso comercial prohibido sin autorizacion expresa. Ver `LICENSE`.
