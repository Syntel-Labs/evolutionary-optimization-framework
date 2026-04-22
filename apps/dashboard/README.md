# Dashboard

Aplicacion Next.js 15 (App Router) con TypeScript strict, Tailwind, `next-intl` y `next-themes`.

## Estructura

```bash
apps/dashboard/
├── messages/            # traducciones es/en
├── prisma/              # schema.prisma (compartido via DATABASE_URL)
├── src/
│   ├── app/
│   │   ├── [locale]/    # rutas traducidas
│   │   └── globals.css
│   ├── components/
│   ├── i18n/            # configuracion de next-intl
│   ├── lib/             # utilidades (env, etc.)
│   └── middleware.ts    # middleware de i18n
├── .env.example
└── package.json
```

## Desarrollo (via docker compose, recomendado)

Desde la raiz del repo:

```bash
docker compose up web
```

Con live reload automatico. Editar en `src/**` y recargar el navegador.

## Desarrollo (sin docker, opcional)

```bash
pnpm install
cp .env.example .env.local
pnpm dev
```

## Scripts

| Script                 | Proposito                           |
| ---------------------- | ----------------------------------- |
| `pnpm dev`             | Servidor de desarrollo              |
| `pnpm build`           | Build de produccion                 |
| `pnpm start`           | Servir el build                     |
| `pnpm lint`            | Correr ESLint                       |
| `pnpm lint:fix`        | Autofix de ESLint                   |
| `pnpm typecheck`       | TypeScript sin emitir               |
| `pnpm db:generate`     | Generar cliente Prisma              |
| `pnpm db:migrate:dev`  | Migracion de desarrollo             |
| `pnpm db:migrate`      | Migracion en prod (deploy)          |

## Variables de entorno

Todas documentadas en `.env.example`. Ningun valor vive hardcodeado en codigo: el acceso centralizado pasa por `src/lib/env.ts`.
