import { NextRequest, NextResponse } from "next/server";
import { getAllOverrides, setAllOverrides, clearAllOverrides } from "@/lib/store";
import { cookies } from "next/headers";

// GET returns null for unset projects — client falls back to p.active
export async function GET() {
  return NextResponse.json(getAllOverrides());
}

// POST saves explicit admin overrides (admin only)
export async function POST(req: NextRequest) {
  const cookieStore = await cookies();
  const role = cookieStore.get("cd_role")?.value;
  if (role !== "admin") {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }
  const body = await req.json();
  // Special action: reset clears all overrides
  if (body.__reset === true) {
    clearAllOverrides();
    return NextResponse.json({ success: true, action: "reset" });
  }
  setAllOverrides(body);
  return NextResponse.json({ success: true });
}
