import { defineRouting } from "next-intl/routing";

export const SUPPORTED_LOCALES = ["es", "en"] as const;

export type SupportedLocale = (typeof SUPPORTED_LOCALES)[number];

export const routing = defineRouting({
  locales: SUPPORTED_LOCALES,
  defaultLocale:
    (process.env.NEXT_PUBLIC_DEFAULT_LOCALE as SupportedLocale | undefined) ??
    "es",
  localePrefix: "as-needed",
});
