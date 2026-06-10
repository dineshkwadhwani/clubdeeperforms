"use client";
import { useState, useEffect, useCallback } from "react";
import { useRouter } from "next/navigation";
import { PROJECTS, CATEGORIES, Project } from "@/lib/projects";

export default function DashboardPage() {
  const router = useRouter();
  const [selectedProject, setSelectedProject] = useState<Project | null>(null);
  const [showForm, setShowForm] = useState(false);
  // overrides: null = use p.active default, true/false = admin override
  const [overrides, setOverrides] = useState<Record<number, boolean | null>>({});
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [loading, setLoading] = useState(true);

  const fetchOverrides = useCallback(async () => {
    try {
      const res = await fetch("/api/config");
      if (res.ok) {
        const data = await res.json();
        setOverrides(data);
      }
    } catch {
      // If fetch fails, just use p.active defaults — no harm done
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => { fetchOverrides(); }, [fetchOverrides]);

  // Final active state: admin override if set, otherwise p.active from projects.ts
  function isActive(p: Project): boolean {
    const override = overrides[p.index];
    if (override !== null && override !== undefined) return override;
    return p.active;
  }

  async function handleLogout() {
    await fetch("/api/auth", { method: "DELETE" });
    router.push("/");
  }

  function selectProject(p: Project) {
    setSelectedProject(p);
    setShowForm(false);
  }

  const activeCount = PROJECTS.filter(isActive).length;

  if (loading) return (
    <div className="min-h-screen flex items-center justify-center" style={{ background: "#0D2218" }}>
      <div className="text-center">
        <div className="text-4xl mb-4">🌿</div>
        <p className="font-display text-white text-lg">Loading...</p>
      </div>
    </div>
  );

  return (
    <div className="flex h-screen overflow-hidden" style={{ background: "var(--cream)" }}>

      {/* ── Sidebar ── */}
      <aside
        className={`flex flex-col flex-shrink-0 transition-all duration-300 ${sidebarOpen ? "w-72" : "w-16"}`}
        style={{ background: "#0D2218", borderRight: "1px solid rgba(200,137,42,0.25)", overflowY: "auto" }}>

        {/* Header */}
        <div className="flex items-center justify-between px-4 py-4 flex-shrink-0"
          style={{ borderBottom: "1px solid rgba(200,137,42,0.2)", minHeight: "68px" }}>
          {sidebarOpen && (
            <div className="flex items-center gap-3 overflow-hidden">
              <span className="text-2xl flex-shrink-0">🌿</span>
              <div className="overflow-hidden">
                <div className="font-display font-bold text-white text-base truncate">Club Deeper</div>
                <div className="text-xs truncate" style={{ fontFamily: "'Tiro Devanagari Marathi', serif", color: "#E8A84A" }}>क्लब डीपर</div>
              </div>
            </div>
          )}
          {!sidebarOpen && <span className="text-xl mx-auto">🌿</span>}
          <button onClick={() => setSidebarOpen(!sidebarOpen)}
            className="flex-shrink-0 w-7 h-7 flex items-center justify-center rounded transition-colors hover:bg-white/10 text-white/60 hover:text-white ml-2">
            {sidebarOpen ? "◂" : "▸"}
          </button>
        </div>

        {/* Project list */}
        <div className="flex-1 py-4 overflow-y-auto">
          {CATEGORIES.map((cat) => {
            const catProjects = PROJECTS.filter((p) => p.category === cat);
            return (
              <div key={cat} className="mb-5">
                {sidebarOpen && (
                  <div className="px-4 mb-2">
                    <span style={{ color: "#E8A84A", fontSize: "0.7rem", fontWeight: 700, letterSpacing: "0.14em", textTransform: "uppercase", fontFamily: "'Inter', sans-serif" }}>
                      {cat}
                    </span>
                  </div>
                )}
                {catProjects.map((p) => {
                  const active = isActive(p);
                  const isSelected = selectedProject?.index === p.index;
                  return (
                    <button key={p.index}
                      onClick={() => active ? selectProject(p) : undefined}
                      disabled={!active}
                      title={!active ? "Not yet enabled by administrator" : p.title}
                      style={{
                        display: "flex",
                        alignItems: "center",
                        gap: "12px",
                        width: "100%",
                        textAlign: "left",
                        padding: sidebarOpen ? "10px 16px" : "10px",
                        justifyContent: sidebarOpen ? "flex-start" : "center",
                        borderLeft: isSelected ? "3px solid #E8A84A" : "3px solid transparent",
                        background: isSelected ? "rgba(200,137,42,0.18)" : "transparent",
                        cursor: active ? "pointer" : "not-allowed",
                        opacity: active ? 1 : 0.4,
                        transition: "all 0.15s ease",
                      }}
                      onMouseEnter={(e) => {
                        if (active && !isSelected) {
                          (e.currentTarget as HTMLElement).style.background = "rgba(255,255,255,0.07)";
                          (e.currentTarget as HTMLElement).style.borderLeftColor = "rgba(200,137,42,0.5)";
                        }
                      }}
                      onMouseLeave={(e) => {
                        if (!isSelected) {
                          (e.currentTarget as HTMLElement).style.background = "transparent";
                          (e.currentTarget as HTMLElement).style.borderLeftColor = "transparent";
                        }
                      }}>
                      <span className="text-xl flex-shrink-0">{p.icon}</span>
                      {sidebarOpen && (
                        <div className="min-w-0 flex-1">
                          <div style={{
                            fontFamily: "'Inter', sans-serif",
                            fontSize: "0.875rem",
                            fontWeight: isSelected ? 600 : 500,
                            color: isSelected ? "#F5C842" : active ? "#F0EDE8" : "#6A8A78",
                            lineHeight: "1.3",
                            whiteSpace: "nowrap",
                            overflow: "hidden",
                            textOverflow: "ellipsis",
                          }}>
                            {p.title}
                          </div>
                          {!active && (
                            <div style={{ fontSize: "0.65rem", color: "#4A6A58", fontFamily: "'Inter', sans-serif", marginTop: "1px" }}>
                              Not yet enabled
                            </div>
                          )}
                        </div>
                      )}
                    </button>
                  );
                })}
              </div>
            );
          })}
        </div>

        {/* Footer */}
        <div className="flex-shrink-0 px-4 py-3" style={{ borderTop: "1px solid rgba(200,137,42,0.15)" }}>
          {sidebarOpen ? (
            <button onClick={handleLogout}
              className="w-full text-center py-2 text-sm transition-all hover:opacity-80"
              style={{ color: "#6A8A78", fontFamily: "'Inter', sans-serif" }}>
              Sign Out ↩
            </button>
          ) : (
            <button onClick={handleLogout} title="Sign Out"
              className="w-full flex justify-center py-2 text-lg opacity-40 hover:opacity-70 transition-opacity">↩</button>
          )}
        </div>
      </aside>

      {/* ── Main content ── */}
      <main className="flex-1 flex flex-col overflow-hidden">

        {/* Top bar */}
        <div className="flex items-center justify-between px-8 py-4 flex-shrink-0"
          style={{ background: "white", borderBottom: "1px solid var(--parchment-dark)", minHeight: "68px" }}>
          <div>
            <h1 className="font-display text-xl font-semibold" style={{ color: "var(--forest)" }}>
              {selectedProject ? selectedProject.title : "Planning Dashboard"}
            </h1>
            {selectedProject && (
              <p className="text-sm" style={{ fontFamily: "'Tiro Devanagari Marathi', serif", color: "var(--stone)" }}>
                {selectedProject.titleMarathi}
              </p>
            )}
          </div>
          <span className="category-pill">{selectedProject?.category ?? "Club Deeper"}</span>
        </div>

        {/* Content */}
        <div className="flex-1 overflow-auto">
          {!selectedProject ? (
            <div className="h-full flex flex-col items-center justify-center px-8 text-center">
              <div className="text-6xl mb-6">🌿</div>
              <h2 className="font-display text-2xl font-semibold mb-2" style={{ color: "var(--forest)" }}>
                Welcome to the Planning Portal
              </h2>
              <p className="text-xl mb-3" style={{ fontFamily: "'Tiro Devanagari Marathi', serif", color: "var(--stone)" }}>
                नियोजन पोर्टलमध्ये आपले स्वागत आहे
              </p>
              <div style={{ width: "40px", height: "2px", background: "var(--saffron)", margin: "0 auto 16px" }} />
              <p className="text-sm max-w-md" style={{ color: "var(--stone)" }}>
                Select an enabled project from the left to begin its planning survey. Greyed-out projects will be unlocked by your administrator.
              </p>
              <p className="text-sm max-w-md mt-3" style={{ fontFamily: "'Tiro Devanagari Marathi', serif", color: "var(--stone)", opacity: 0.8 }}>
                नियोजन सर्वेक्षण सुरू करण्यासाठी डाव्या बाजूने सक्रिय प्रकल्प निवडा.
              </p>
              <div className="flex gap-6 mt-10">
                {[["20", "Total Projects"], [String(activeCount), "Active Surveys"], ["50", "Acres"]].map(([n, l]) => (
                  <div key={l} className="text-center p-5" style={{ background: "var(--parchment)", border: "1px solid var(--parchment-dark)", minWidth: "100px" }}>
                    <div className="font-display text-3xl font-bold" style={{ color: l === "Active Surveys" ? "var(--saffron)" : "var(--forest)" }}>{n}</div>
                    <div className="text-xs mt-1" style={{ color: "var(--stone)" }}>{l}</div>
                  </div>
                ))}
              </div>
            </div>
          ) : !showForm ? (
            <div className="p-8 max-w-3xl">
              <div className="flex items-start gap-5 mb-8">
                <div className="text-6xl flex-shrink-0">{selectedProject.icon}</div>
                <div>
                  <span className="category-pill mb-3 inline-block">{selectedProject.category}</span>
                  <h2 className="font-display text-3xl font-semibold mb-1" style={{ color: "var(--forest)" }}>{selectedProject.title}</h2>
                  <p className="text-xl" style={{ fontFamily: "'Tiro Devanagari Marathi', serif", color: "var(--stone)" }}>{selectedProject.titleMarathi}</p>
                </div>
              </div>
              <div style={{ width: "50px", height: "2px", background: "var(--saffron)", marginBottom: "28px" }} />
              <div className="grid md:grid-cols-2 gap-6 mb-10">
                <div className="p-5" style={{ background: "var(--parchment)", borderLeft: "3px solid var(--saffron)" }}>
                  <p className="text-sm leading-relaxed" style={{ fontFamily: "'Playfair Display', serif", color: "var(--charcoal)", lineHeight: "1.9" }}>{selectedProject.description}</p>
                </div>
                <div className="p-5" style={{ background: "var(--parchment)", borderLeft: "3px solid rgba(200,137,42,0.4)" }}>
                  <p className="text-sm leading-relaxed" style={{ fontFamily: "'Tiro Devanagari Marathi', serif", color: "var(--charcoal)", lineHeight: "2.1" }}>{selectedProject.descriptionMarathi}</p>
                </div>
              </div>
              <div className="p-6" style={{ background: "white", border: "1px solid var(--parchment-dark)", borderTop: "3px solid var(--forest)" }}>
                <div className="flex flex-col md:flex-row md:items-center justify-between gap-5">
                  <div>
                    <h3 className="font-display text-lg font-semibold mb-1" style={{ color: "var(--forest)" }}>Planning Questionnaire</h3>
                    <p className="text-sm" style={{ fontFamily: "'Tiro Devanagari Marathi', serif", color: "var(--stone)" }}>नियोजन प्रश्नावली</p>
                    <p className="text-xs mt-2 max-w-sm" style={{ color: "var(--stone)" }}>Fill in the detailed planning survey. Responses are saved to Google Sheets automatically.</p>
                  </div>
                  <button onClick={() => setShowForm(true)}
                    className="flex-shrink-0 flex items-center gap-2 px-7 py-3 font-medium transition-all duration-200 hover:scale-105"
                    style={{ background: "var(--forest)", color: "white", fontFamily: "'Inter', sans-serif", fontSize: "0.875rem", letterSpacing: "0.05em", whiteSpace: "nowrap" }}>
                    Take Survey
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                  </button>
                </div>
              </div>
              <div className="mt-4 flex items-center gap-3">
                <div style={{ width: "20px", height: "1px", background: "var(--saffron)" }} />
                <a href={selectedProject.view_url} target="_blank" rel="noopener noreferrer"
                  className="text-xs hover:underline" style={{ color: "var(--saffron)" }}>Open form in new tab ↗</a>
              </div>
            </div>
          ) : (
            <div className="h-full flex flex-col">
              <div className="flex items-center justify-between px-6 py-3 flex-shrink-0"
                style={{ background: "var(--parchment)", borderBottom: "1px solid var(--parchment-dark)" }}>
                <div className="flex items-center gap-3">
                  <button onClick={() => setShowForm(false)} className="text-sm hover:opacity-70" style={{ color: "var(--stone)" }}>← Back</button>
                  <div style={{ width: "1px", height: "14px", background: "var(--parchment-dark)" }} />
                  <span className="text-sm font-medium" style={{ color: "var(--forest)" }}>{selectedProject.title}</span>
                </div>
                <a href={selectedProject.view_url} target="_blank" rel="noopener noreferrer"
                  className="text-xs hover:underline" style={{ color: "var(--saffron)" }}>Open in new tab ↗</a>
              </div>
              <div className="flex-1">
                <iframe src={selectedProject.view_url} className="form-iframe" title={selectedProject.title} />
              </div>
            </div>
          )}
        </div>
      </main>
    </div>
  );
}
