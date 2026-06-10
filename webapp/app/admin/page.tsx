"use client";
import { useState, useEffect, useCallback } from "react";
import { useRouter } from "next/navigation";
import { PROJECTS, CATEGORIES } from "@/lib/projects";

type AdminView = "config" | "analysis";

export default function AdminPage() {
  const router = useRouter();
  const [view, setView] = useState<AdminView>("config");
  // null = use p.active default, true/false = explicit admin override
  const [overrides, setOverrides] = useState<Record<number, boolean | null>>({});
  const [saving, setSaving] = useState(false);
  const [saved, setSaved] = useState(false);
  const [loading, setLoading] = useState(true);

  const fetchOverrides = useCallback(async () => {
    const res = await fetch("/api/config");
    if (res.status === 401) { router.push("/"); return; }
    const data = await res.json();
    setOverrides(data);
    setLoading(false);
  }, [router]);

  useEffect(() => { fetchOverrides(); }, [fetchOverrides]);

  async function handleLogout() {
    await fetch("/api/auth", { method: "DELETE" });
    router.push("/");
  }

  // Effective value: override if set, otherwise p.active
  function isActive(index: number): boolean {
    const p = PROJECTS.find((p) => p.index === index)!;
    const ov = overrides[index];
    if (ov !== null && ov !== undefined) return ov;
    return p.active;
  }

  function toggleProject(index: number) {
    const current = isActive(index);
    setOverrides((prev) => ({ ...prev, [index]: !current }));
    setSaved(false);
  }

  function enableAll() {
    const all: Record<number, boolean> = {};
    PROJECTS.forEach((p) => { all[p.index] = true; });
    setOverrides(all);
    setSaved(false);
  }

  function disableAll() {
    const none: Record<number, boolean> = {};
    PROJECTS.forEach((p) => { none[p.index] = false; });
    setOverrides(none);
    setSaved(false);
  }

  async function resetToDefaults() {
    await fetch("/api/config", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ __reset: true }),
    });
    // Re-fetch to get clean null state
    const res = await fetch("/api/config");
    setOverrides(await res.json());
    setSaved(false);
  }

  async function saveConfig() {
    setSaving(true);
    // Only save explicit overrides — build full config from effective values
    const fullConfig: Record<number, boolean> = {};
    PROJECTS.forEach((p) => { fullConfig[p.index] = isActive(p.index); });
    await fetch("/api/config", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(fullConfig),
    });
    setSaving(false);
    setSaved(true);
    setTimeout(() => setSaved(false), 2500);
  }

  const activeCount = PROJECTS.filter((p) => isActive(p.index)).length;

  if (loading) return (
    <div className="min-h-screen flex items-center justify-center" style={{ background: "#0D2218" }}>
      <div className="text-center">
        <div className="text-4xl mb-4">⚙️</div>
        <p className="font-display text-white text-lg">Loading Admin...</p>
      </div>
    </div>
  );

  return (
    <div className="flex h-screen overflow-hidden" style={{ background: "var(--cream)" }}>

      {/* Sidebar */}
      <aside className="w-60 flex flex-col flex-shrink-0"
        style={{ background: "#0D2218", borderRight: "1px solid rgba(200,137,42,0.25)" }}>
        <div className="px-5 py-5" style={{ borderBottom: "1px solid rgba(200,137,42,0.2)" }}>
          <div className="flex items-center gap-3 mb-1">
            <span className="text-2xl">⚙️</span>
            <div>
              <div className="font-display text-white font-bold text-base">Admin Panel</div>
              <div className="text-xs" style={{ color: "#E8A84A", fontFamily: "'Tiro Devanagari Marathi', serif" }}>प्रशासक</div>
            </div>
          </div>
        </div>

        <nav className="flex-1 py-5 px-3">
          {(["config", "analysis"] as AdminView[]).map((v) => (
            <button key={v} onClick={() => setView(v)}
              className="w-full text-left px-4 py-3 mb-1 flex items-center gap-3 transition-all duration-150"
              style={{
                borderLeft: view === v ? "3px solid #E8A84A" : "3px solid transparent",
                background: view === v ? "rgba(200,137,42,0.18)" : "transparent",
              }}
              onMouseEnter={(e) => { if (view !== v) (e.currentTarget as HTMLElement).style.background = "rgba(255,255,255,0.07)"; }}
              onMouseLeave={(e) => { if (view !== v) (e.currentTarget as HTMLElement).style.background = "transparent"; }}>
              <span className="text-xl">{v === "config" ? "🎛️" : "📊"}</span>
              <span style={{ fontFamily: "'Inter', sans-serif", fontSize: "0.9rem", fontWeight: view === v ? 600 : 500, color: view === v ? "#F5C842" : "#D0CCC4" }}>
                {v === "config" ? "Configuration" : "Analysis"}
              </span>
            </button>
          ))}
          <div className="mt-8 px-3">
            <div style={{ height: "1px", background: "rgba(200,137,42,0.15)", marginBottom: "16px" }} />
            <a href="/dashboard" className="block text-sm px-1 py-1 hover:opacity-80 transition-opacity"
              style={{ color: "#6A8A78", fontFamily: "'Inter', sans-serif" }}>← User Dashboard</a>
          </div>
        </nav>

        <div className="px-5 py-4" style={{ borderTop: "1px solid rgba(200,137,42,0.15)" }}>
          <button onClick={handleLogout} className="w-full text-center py-2 text-sm hover:opacity-80 transition-opacity"
            style={{ color: "#6A8A78", fontFamily: "'Inter', sans-serif" }}>Sign Out ↩</button>
        </div>
      </aside>

      {/* Main */}
      <main className="flex-1 flex flex-col overflow-hidden">
        <div className="flex items-center justify-between px-8 py-4 flex-shrink-0"
          style={{ background: "white", borderBottom: "1px solid var(--parchment-dark)", minHeight: "68px" }}>
          <div>
            <h1 className="font-display text-xl font-semibold" style={{ color: "var(--forest)" }}>
              {view === "config" ? "Survey Configuration" : "Response Analysis"}
            </h1>
            <p className="text-xs mt-0.5" style={{ color: "var(--stone)" }}>
              {view === "config"
                ? `${activeCount} of 20 surveys active · Edit projects.ts + redeploy for permanent changes`
                : "Analytics dashboard"}
            </p>
          </div>
          {view === "config" && (
            <div className="flex items-center gap-2">
              <button onClick={resetToDefaults} className="text-xs px-3 py-2 hover:opacity-80 transition-opacity"
                style={{ border: "1px solid var(--parchment-dark)", color: "var(--stone)", fontFamily: "'Inter', sans-serif" }}>
                Reset to Defaults
              </button>
              <button onClick={disableAll} className="text-xs px-3 py-2 hover:opacity-80 transition-opacity"
                style={{ border: "1px solid var(--parchment-dark)", color: "var(--stone)", fontFamily: "'Inter', sans-serif" }}>
                Disable All
              </button>
              <button onClick={enableAll} className="text-xs px-3 py-2 hover:opacity-80 transition-opacity"
                style={{ border: "1px solid var(--saffron)", color: "var(--saffron)", fontFamily: "'Inter', sans-serif" }}>
                Enable All
              </button>
              <button onClick={saveConfig} disabled={saving}
                className="text-xs px-5 py-2 font-medium hover:opacity-90 disabled:opacity-50 transition-opacity"
                style={{ background: saved ? "#2A5A45" : "var(--forest)", color: "white", fontFamily: "'Inter', sans-serif" }}>
                {saving ? "Saving..." : saved ? "✓ Saved" : "Apply Changes"}
              </button>
            </div>
          )}
        </div>

        <div className="flex-1 overflow-auto p-8">
          {view === "config" && (
            <div>
              <div className="grid md:grid-cols-2 gap-4 mb-8 max-w-3xl">
                <div className="p-4" style={{ background: "rgba(200,137,42,0.06)", border: "1px solid rgba(200,137,42,0.2)" }}>
                  <p className="text-xs font-semibold mb-1" style={{ color: "var(--saffron)" }}>Permanent (code)</p>
                  <p className="text-xs" style={{ color: "var(--stone)" }}>
                    Edit <code className="px-1 py-0.5 text-xs" style={{ background: "var(--parchment-dark)" }}>active: true/false</code> in <code className="px-1 py-0.5 text-xs" style={{ background: "var(--parchment-dark)" }}>lib/projects.ts</code>, commit and redeploy.
                  </p>
                </div>
                <div className="p-4" style={{ background: "rgba(107,117,101,0.06)", border: "1px solid var(--parchment-dark)" }}>
                  <p className="text-xs font-semibold mb-1" style={{ color: "var(--stone)" }}>Session (runtime)</p>
                  <p className="text-xs" style={{ color: "var(--stone)" }}>
                    Toggle here and click Apply Changes. Overrides reset on server restart.
                  </p>
                </div>
              </div>

              {CATEGORIES.map((cat) => {
                const catProjects = PROJECTS.filter((p) => p.category === cat);
                return (
                  <div key={cat} className="mb-8">
                    <div className="flex items-center gap-3 mb-3">
                      <div style={{ width: "3px", height: "22px", background: "var(--saffron)" }} />
                      <h2 className="font-display text-base font-semibold" style={{ color: "var(--forest)" }}>{cat}</h2>
                    </div>
                    <div className="grid gap-2">
                      {catProjects.map((p) => {
                        const active = isActive(p.index);
                        const ov = overrides[p.index];
                        const isOverridden = ov !== null && ov !== undefined && ov !== p.active;
                        return (
                          <div key={p.index} className="flex items-center justify-between p-4"
                            style={{
                              background: active ? "white" : "var(--parchment)",
                              border: `1px solid ${active ? "rgba(200,137,42,0.25)" : "var(--parchment-dark)"}`,
                              borderLeft: `4px solid ${active ? "var(--saffron)" : "#C5D0C0"}`,
                              transition: "all 0.15s ease",
                            }}>
                            <div className="flex items-center gap-4">
                              <span className="text-2xl">{p.icon}</span>
                              <div>
                                <div className="flex items-center gap-2 flex-wrap">
                                  <span className="text-sm font-medium" style={{ color: active ? "var(--charcoal)" : "var(--stone)", fontFamily: "'Inter', sans-serif" }}>
                                    {p.title}
                                  </span>
                                  {isOverridden && (
                                    <span className="text-xs px-2 py-0.5"
                                      style={{ background: "rgba(200,137,42,0.12)", color: "var(--saffron)", border: "1px solid rgba(200,137,42,0.3)", fontFamily: "'Inter', sans-serif", fontSize: "0.6rem" }}>
                                      session override
                                    </span>
                                  )}
                                </div>
                                <div className="text-xs mt-0.5" style={{ fontFamily: "'Tiro Devanagari Marathi', serif", color: "var(--stone)", opacity: 0.75 }}>{p.titleMarathi}</div>
                                <div className="text-xs mt-0.5" style={{ color: "var(--stone)", opacity: 0.55, fontFamily: "'Inter', sans-serif" }}>
                                  Default in code: <span style={{ color: p.active ? "#2A7A4A" : "#999" }}>{p.active ? "active" : "inactive"}</span>
                                </div>
                              </div>
                            </div>
                            <div className="flex items-center gap-4 flex-shrink-0">
                              <span className="text-xs font-medium" style={{ color: active ? "var(--saffron)" : "var(--stone)", fontFamily: "'Inter', sans-serif", minWidth: "50px", textAlign: "right" }}>
                                {active ? "Active" : "Inactive"}
                              </span>
                              <button onClick={() => toggleProject(p.index)}
                                style={{
                                  position: "relative", width: "44px", height: "24px", borderRadius: "12px",
                                  background: active ? "var(--forest)" : "#B5C5B0", flexShrink: 0,
                                  transition: "background 0.2s ease",
                                }}>
                                <span style={{
                                  position: "absolute", top: "2px", width: "20px", height: "20px",
                                  borderRadius: "50%", background: "white",
                                  left: active ? "calc(100% - 22px)" : "2px",
                                  boxShadow: "0 1px 4px rgba(0,0,0,0.25)",
                                  transition: "left 0.2s ease",
                                }} />
                              </button>
                            </div>
                          </div>
                        );
                      })}
                    </div>
                  </div>
                );
              })}
            </div>
          )}

          {view === "analysis" && (
            <div className="flex flex-col items-center justify-center py-24 text-center">
              <div className="text-6xl mb-6">📊</div>
              <h2 className="font-display text-3xl font-semibold mb-2" style={{ color: "var(--forest)" }}>Coming Soon</h2>
              <p className="text-xl mb-4" style={{ fontFamily: "'Tiro Devanagari Marathi', serif", color: "var(--stone)" }}>लवकरच येत आहे</p>
              <div style={{ width: "40px", height: "2px", background: "var(--saffron)", margin: "0 auto 20px" }} />
              <p className="text-sm max-w-lg" style={{ color: "var(--stone)", lineHeight: "1.8" }}>
                The analysis dashboard will aggregate survey responses across all 20 Google Sheets, display completion rates per project, and generate summary reports for the core committee.
              </p>
            </div>
          )}
        </div>
      </main>
    </div>
  );
}
