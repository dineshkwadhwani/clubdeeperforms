import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Club Deeper – Campus Planning Platform",
  description: "Planning platform for Club Deeper campus – a visionary educational and residential community near Sinhgad Fort, Pune.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
      </head>
      <body>{children}</body>
    </html>
  );
}
