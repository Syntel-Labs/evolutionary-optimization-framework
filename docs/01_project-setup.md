# Project setup

Guia de puesta en marcha local en Windows + WSL2 usando Docker. El host no necesita Node, Python ni pnpm instalados: todo corre en contenedores.

## Requisitos

- Windows 11 con WSL2 (Ubuntu)
- Docker Desktop con integracion WSL2 activa
- Git

Verificar desde WSL:

```bash
docker --version
docker compose version
git --version
```

## Primer arranque

Desde la raiz del repo:

```bash
cp .env.example .env
docker compose up --build
```

Servicios disponibles:

- Dashboard: <http://localhost:3000>
- Motor: <http://localhost:8000>
- Health del motor: <http://localhost:8000/health>
- PostgreSQL: `localhost:5432` (usuario y credenciales en `.env`)

## Identidad del stack en docker

Todo lo visible desde el host se prefija con el valor de `COMPOSE_PROJECT_PREFIX` (default `evopfr`). Esto permite distinguir este stack de otros que tengas corriendo.

Ejemplo con prefijo default:

| Recurso     | Nombre host-visible |
| ----------- | ------------------- |
| Proyecto    | `evopfr`            |
| Contenedor  | `evopfr-web`        |
| Contenedor  | `evopfr-engine`     |
| Contenedor  | `evopfr-postgres`   |
| Red         | `evopfr-net`        |
| Volumen     | `evopfr-pgdata`     |

Los nombres internos de servicio (`web`, `engine`, `postgres`) no llevan prefijo: son hostnames DNS que usan `DATABASE_URL`, `NEXT_PUBLIC_ENGINE_URL` y la config CORS del motor.

Para correr varios stacks en paralelo, cambiar `COMPOSE_PROJECT_PREFIX` en `.env` (por ejemplo `evopfr-dev`, `evopfr-staging`) y asegurarse que los puertos expuestos no choquen (`WEB_PORT`, `ENGINE_PORT`, `POSTGRES_PORT`).

## Variables de entorno

Reglas del proyecto:

- Todo valor configurable vive en `.env` y esta documentado en `.env.example`
- Nunca hardcodear puertos, hosts, tiempos limite ni credenciales
- `.env` nunca se versiona, `.env.example` siempre

Archivos:

- `.env.example` raiz: variables compartidas entre servicios
- `apps/dashboard/.env.example`: variables del front
- `engine/.env.example`: variables del motor

Al agregar una variable nueva, actualizar el `.env.example` correspondiente en el mismo commit.

## Flujo de desarrollo

### Dashboard (Next.js)

Live reload automatico. Editar archivos en `apps/dashboard/src/**` y los cambios se reflejan sin reconstruir.

### Motor (FastAPI)

Live reload con `uvicorn --reload`. Editar archivos en `engine/src/**` y el servidor se recarga.

### Base de datos

```bash
# Generar cliente Prisma despues de cambiar schema.prisma
docker compose exec web pnpm db:generate

# Correr migraciones en desarrollo
docker compose exec web pnpm db:migrate:dev
```

## Comandos de verificacion

```bash
# Linter TypeScript
docker compose exec web pnpm lint

# Linter Python
docker compose exec engine ruff check .

# Tests del motor
docker compose exec engine pytest

# Typecheck TypeScript
docker compose exec web pnpm typecheck
```

## Troubleshooting WSL

- **Permisos en volumes**: si aparecen errores `EACCES` en archivos generados por contenedor, ejecutar desde WSL `sudo chown -R $USER:$USER .`
- **Puerto 3000/8000 ocupado**: cambiar `WEB_PORT` o `ENGINE_PORT` en `.env`
- **Docker Desktop no ve el repo**: asegurar que el proyecto esta dentro de `\\wsl$\Ubuntu\...` o en un path mapeado a WSL, no en `C:\`
- **Build lento de OR-Tools**: la primera vez tarda porque compila wheels; las siguientes usan cache

## Apagar el stack

```bash
docker compose down          # detiene contenedores
docker compose down -v       # tambien borra la data de postgres
```
