import { NextRequest, NextResponse } from "next/server";
import { checkUserPassword, checkAdminPassword } from "@/lib/auth";

export async function POST(req: NextRequest) {
  const { password } = await req.json();
  if (checkAdminPassword(password)) {
    const res = NextResponse.json({ success: true, role: "admin" });
    res.cookies.set("cd_role", "admin", { httpOnly: true, sameSite: "lax", maxAge: 86400 });
    return res;
  }
  if (checkUserPassword(password)) {
    const res = NextResponse.json({ success: true, role: "user" });
    res.cookies.set("cd_role", "user", { httpOnly: true, sameSite: "lax", maxAge: 86400 });
    return res;
  }
  return NextResponse.json({ success: false, message: "Invalid password" }, { status: 401 });
}

export async function DELETE() {
  const res = NextResponse.json({ success: true });
  res.cookies.delete("cd_role");
  return res;
}
