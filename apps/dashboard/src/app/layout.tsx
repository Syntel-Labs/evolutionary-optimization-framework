import type { ReactNode } from "react";
import "./globals.css";

export const metadata = {
  title: "Evolutionary Optimization Framework",
  description: "Fleet routing optimization with pluggable engines",
};

type RootLayoutProps = {
  children: ReactNode;
};

export default function RootLayout({ children }: RootLayoutProps) {
  return children;
}
