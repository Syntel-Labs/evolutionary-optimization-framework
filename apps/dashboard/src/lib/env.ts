/**
 * Acceso centralizado a variables de entorno del dashboard.
 *
 * Regla del proyecto: ningun valor de configuracion vive hardcodeado
 * en el codigo. Cualquier consumidor debe leerlo desde este modulo.
 * Si una variable requerida falta, fallamos temprano.
 */

function requireEnv(name: string): string {
  const value = process.env[name];
  if (!value || value.length === 0) {
    throw new Error(`Variable de entorno requerida no definida: ${name}`);
  }
  return value;
}

function optionalEnv(name: string, fallback: string): string {
  return process.env[name] ?? fallback;
}

export const env = {
  engineUrl: optionalEnv("NEXT_PUBLIC_ENGINE_URL", "http://localhost:8000"),
  defaultLocale: optionalEnv("NEXT_PUBLIC_DEFAULT_LOCALE", "es"),
  nodeEnv: optionalEnv("NODE_ENV", "development"),
} as const;

export { requireEnv };
