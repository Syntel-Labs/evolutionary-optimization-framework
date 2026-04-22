# syntax=docker/dockerfile:1.7
# Next.js 15 dashboard (development target).
# Uses pnpm with corepack for deterministic installs inside the container,
# so the host does not need Node or pnpm locally.

FROM node:20-alpine AS base
RUN corepack enable && corepack prepare pnpm@9.12.0 --activate
WORKDIR /app

FROM base AS deps
# Copy workspace manifests first for better layer caching
COPY pnpm-workspace.yaml package.json ./
COPY apps/dashboard/package.json apps/dashboard/
COPY packages/shared/package.json packages/shared/
RUN pnpm install --frozen-lockfile=false

FROM base AS dev
COPY --from=deps /app/node_modules ./node_modules
COPY --from=deps /app/apps/dashboard/node_modules ./apps/dashboard/node_modules
COPY . .
WORKDIR /app/apps/dashboard
EXPOSE 3000
CMD ["pnpm", "dev"]
