# Architecture overview

Vision de alto nivel del framework y de como encajan las piezas.

## Contexto

El framework resuelve problemas de ruteo de vehiculos (VRP) para flotas con multiples viajeros, capacidades y ventanas horarias. Generaliza el TSP clasico del `reference/` a escenarios logisticos reales.

## Componentes

```text
+------------------+     HTTP/WS     +--------------------+     +-------------+
|   Dashboard      | <-------------> |    Engine (API)    | --> |  PostgreSQL |
|   Next.js 15     |                 |    FastAPI         |     |    (Prisma) |
+------------------+                 +---------+----------+     +-------------+
                                               |
                             +-----------------+----------------+
                             |                 |                |
                          +--v---+        +----v-----+      +---v----+
                          | ILP  |        | Metaheur |      | OR-Tools|
                          | PuLP |        | GA + ALNS|      |         |
                          +------+        +----------+      +---------+
```

## Responsabilidades

### Dashboard (`apps/dashboard`)

- UI de instancias, corridas y comparativas
- i18n (`next-intl`) y tema claro/oscuro (`next-themes`)
- Capa de datos via Prisma hacia PostgreSQL
- Llamadas al motor por REST (submit run) y WebSocket (progreso)

### Motor (`engine`)

- API FastAPI que expone los tres solvers
- Contratos Pydantic espejo de `packages/shared`
- Registro de metricas y eventos por corrida

### Paquete compartido (`packages/shared`)

- Tipos TypeScript que definen el contrato cliente-servidor
- Fuente de verdad: los schemas Pydantic del motor deben coincidir

## Motores de optimizacion

| Motor          | Uso recomendado                                   | Estado    |
| -------------- | ------------------------------------------------- | --------- |
| ILP (PuLP/CBC) | Instancias pequeñas, validacion de calidad        | Planeado  |
| Metaheuristico | Instancias medianas y grandes, flexibilidad       | Planeado  |
| OR-Tools       | Baseline industrial, VRPTW listo                  | Planeado  |

## Flujo de una corrida

1. Usuario selecciona instancia, motor y objetivo en el dashboard
2. Dashboard persiste un `Run` en estado `QUEUED` y llama a `/solve` del motor
3. Motor ejecuta el solver elegido, emite eventos de progreso por WebSocket
4. Al terminar, motor escribe `RouteResult` y marca `Run` como `COMPLETED`
5. Dashboard muestra las rutas en el mapa (MapLibre) y metricas

## Decisiones clave

- **Motor en Python**: reutiliza el trabajo de `reference/`, aprovecha PuLP y OR-Tools nativos
- **Dashboard en Next.js**: App Router con Server Components para datos persistidos
- **Sin IA**: los tres motores son deterministas o heuristicos clasicos, fuertemente defendibles para clientes que desconfian de modelos ML
- **Docker-first**: el host solo necesita Docker; evita conflictos de versiones
