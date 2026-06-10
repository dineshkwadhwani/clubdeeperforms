import { NextRequest, NextResponse } from "next/server";

export function middleware(req: NextRequest) {
  const role = req.cookies.get("cd_role")?.value;
  const path = req.nextUrl.pathname;

  if (path.startsWith("/dashboard")) {
    if (!role) return NextResponse.redirect(new URL("/", req.url));
  }
  if (path.startsWith("/admin")) {
    if (role !== "admin") return NextResponse.redirect(new URL("/", req.url));
  }
  return NextResponse.next();
}

export const config = {
  matcher: ["/dashboard/:path*", "/admin/:path*"],
};
