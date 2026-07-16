"use client";
import { useRouter } from "next/navigation";
import Link from "next/link";

const SPECS = [
  {
    group: "Education Campus",
    icon: "🏫",
    color: "#1565C0",
    lightColor: "#E3F2FD",
    projects: ["CBSE/State School (K12)", "Coaching Center (NEET/JEE/CET)", "Library", "Study Center (UPSC/MPSC)"],
    pdfFile: "EducationCampus_Specification_v2.0.pdf",
    xlsxFile: "EducationCampus_CostSheet_v2.0.xlsx",
    description: "Comprehensive specification covering all 4 education projects on the 5-acre academic zone.",
  },
  {
    group: "Skill Campus",
    icon: "🛠️",
    color: "#00695C",
    lightColor: "#E0F2F1",
    projects: ["Skill Campus (25–30 Skill Units)", "Software Development Park"],
    pdfFile: "SkillCampus_Specification_v2.0.pdf",
    xlsxFile: "SkillCampus_CostSheet_v2.0.xlsx",
    description: "Skill training workshops, live campus service model, and the internal IT development park.",
  },
  {
    group: "Social Projects",
    icon: "🏥",
    color: "#B71C1C",
    lightColor: "#FFEBEE",
    projects: ["Old Age Home", "Care Center", "Hospital"],
    pdfFile: "SocialProjects_Specification_v2.0.pdf",
    xlsxFile: "SocialProjects_CostSheet_v2.0.xlsx",
    description: "Healthcare and social welfare facilities serving campus residents and surrounding rural communities.",
  },
  {
    group: "Sport & Cultural Center",
    icon: "🏏",
    color: "#1B5E20",
    lightColor: "#E8F5E9",
    projects: ["Cricket & Football Ground", "Indoor Games Facility", "Gymnasium & Swimming Pool"],
    pdfFile: "SportCultural_Specification_v2.0.pdf",
    xlsxFile: "SportCultural_CostSheet_v2.0.xlsx",
    description: "Outdoor cricket and football grounds, 30,000 sq ft indoor sports hall, and gym with semi-Olympic pool.",
  },
  {
    group: "Residential Community",
    icon: "🏘️",
    color: "#4A148C",
    lightColor: "#F3E5F5",
    projects: ["Residential Bungalow Complex (200–250 plots)", "Clubhouse"],
    pdfFile: "ResidentialCommunity_Specification_v2.0.pdf",
    xlsxFile: "ResidentialCommunity_CostSheet_v2.0.xlsx",
    description: "Gated bungalow township and premium members-only clubhouse with spa and fine dining.",
  },
];

export default function SpecificationsPage() {
  const router = useRouter();

  async function handleLogout() {
    await fetch("/api/auth", { method: "DELETE" });
    router.push("/");
  }

  return (
    <div className="flex h-screen overflow-hidden" style={{ background: "var(--cream)" }}>

      {/* ── Sidebar ── */}
      <aside
        className="flex flex-col flex-shrink-0 w-72"
        style={{ background: "#0D2218", borderRight: "1px solid rgba(200,137,42,0.25)", overflowY: "auto" }}>

        {/* Header */}
        <div className="flex items-center gap-3 px-4 py-4 flex-shrink-0"
          style={{ borderBottom: "1px solid rgba(200,137,42,0.2)", minHeight: "68px" }}>
          <span className="text-2xl flex-shrink-0">🌿</span>
          <div className="overflow-hidden">
            <div className="font-display font-bold text-white text-base truncate">Club Deeper</div>
            <div className="text-xs truncate" style={{ fontFamily: "'Tiro Devanagari Marathi', serif", color: "#E8A84A" }}>क्लब डीपर</div>
          </div>
        </div>

        {/* Navigation */}
        <div className="flex-1 py-4 overflow-y-auto">

          {/* Specifications — active/current page */}
          <div style={{
            display: "flex", alignItems: "center", gap: "12px",
            padding: "10px 16px",
            borderLeft: "3px solid #E8A84A",
            background: "rgba(200,137,42,0.18)",
          }}>
            <span className="text-xl flex-shrink-0">📋</span>
            <span style={{ fontFamily: "'Inter', sans-serif", fontSize: "0.875rem", fontWeight: 600, color: "#F5C842" }}>
              Specifications
            </span>
          </div>

          {/* Dashboard link */}
          <Link href="/dashboard" style={{
            display: "flex", alignItems: "center", gap: "12px",
            padding: "10px 16px",
            borderLeft: "3px solid transparent",
            textDecoration: "none",
            transition: "all 0.15s ease",
          }}
            onMouseEnter={(e) => {
              (e.currentTarget as HTMLElement).style.background = "rgba(255,255,255,0.07)";
              (e.currentTarget as HTMLElement).style.borderLeftColor = "rgba(200,137,42,0.5)";
            }}
            onMouseLeave={(e) => {
              (e.currentTarget as HTMLElement).style.background = "transparent";
              (e.currentTarget as HTMLElement).style.borderLeftColor = "transparent";
            }}>
            <span className="text-xl flex-shrink-0">📊</span>
            <span style={{ fontFamily: "'Inter', sans-serif", fontSize: "0.875rem", fontWeight: 500, color: "#F0EDE8" }}>
              Planning Dashboard
            </span>
          </Link>

          <div style={{ margin: "12px 16px 6px", height: "1px", background: "rgba(200,137,42,0.15)" }} />

          {/* Jump-to anchors */}
          <div className="px-4 mb-2">
            <span style={{ color: "#E8A84A", fontSize: "0.7rem", fontWeight: 700, letterSpacing: "0.14em", textTransform: "uppercase", fontFamily: "'Inter', sans-serif" }}>
              Jump to
            </span>
          </div>
          {SPECS.map((s) => (
            <a key={s.group} href={`#${s.group.replace(/[\s&]+/g, "-")}`}
              style={{
                display: "flex", alignItems: "center", gap: "12px",
                padding: "8px 16px",
                borderLeft: "3px solid transparent",
                textDecoration: "none",
                transition: "all 0.15s ease",
              }}
              onMouseEnter={(e) => {
                (e.currentTarget as HTMLElement).style.background = "rgba(255,255,255,0.07)";
                (e.currentTarget as HTMLElement).style.borderLeftColor = "rgba(200,137,42,0.5)";
              }}
              onMouseLeave={(e) => {
                (e.currentTarget as HTMLElement).style.background = "transparent";
                (e.currentTarget as HTMLElement).style.borderLeftColor = "transparent";
              }}>
              <span className="flex-shrink-0" style={{ fontSize: "1rem" }}>{s.icon}</span>
              <span style={{ fontFamily: "'Inter', sans-serif", fontSize: "0.8rem", color: "#A0BEA8", whiteSpace: "nowrap", overflow: "hidden", textOverflow: "ellipsis" }}>
                {s.group}
              </span>
            </a>
          ))}
        </div>

        {/* Footer */}
        <div className="flex-shrink-0 px-4 py-3" style={{ borderTop: "1px solid rgba(200,137,42,0.15)" }}>
          <button onClick={handleLogout}
            className="w-full text-center py-2 text-sm transition-all hover:opacity-80"
            style={{ color: "#6A8A78", fontFamily: "'Inter', sans-serif" }}>
            Sign Out ↩
          </button>
        </div>
      </aside>

      {/* ── Main content ── */}
      <main className="flex-1 flex flex-col overflow-hidden">

        {/* Top bar */}
        <div className="flex items-center justify-between px-8 py-4 flex-shrink-0"
          style={{ background: "white", borderBottom: "1px solid var(--parchment-dark)", minHeight: "68px" }}>
          <div>
            <h1 className="font-display text-xl font-semibold" style={{ color: "var(--forest)" }}>
              Project Specifications
            </h1>
            <p className="text-sm" style={{ fontFamily: "'Tiro Devanagari Marathi', serif", color: "var(--stone)" }}>
              प्रकल्प तपशील दस्तऐवज
            </p>
          </div>
          <span className="category-pill">Eduval Pvt. Ltd. · July 2026</span>
        </div>

        {/* Content */}
        <div className="flex-1 overflow-auto">
          <div className="max-w-5xl mx-auto px-8 py-8">

            {/* Intro */}
            <div className="mb-8 p-6" style={{
              background: "white",
              borderLeft: "4px solid var(--saffron)",
              border: "1px solid var(--parchment-dark)",
              borderLeftWidth: "4px",
              borderLeftColor: "var(--saffron)",
            }}>
              <p className="text-sm leading-relaxed" style={{ color: "var(--stone)", fontFamily: "'Inter', sans-serif", lineHeight: "1.8" }}>
                These Functional Specification Documents have been prepared by{" "}
                <strong style={{ color: "var(--forest)" }}>Eduval Pvt. Ltd.</strong> based on the planning surveys
                completed by the Club Deeper Core Committee (July 2026). Each document is the primary design brief
                for the appointed Civil Engineer, Architect (Omkar Yanbhar),
                and Project Manager. The Excel cost sheets provide itemised civil and fit-out cost estimates based
                on Pune/Maharashtra market rates.
              </p>
            </div>

            {/* Spec cards */}
            <div className="grid gap-6">
              {SPECS.map((s) => (
                <div key={s.group}
                  id={s.group.replace(/[\s&]+/g, "-")}
                  style={{
                    background: "white",
                    border: "1px solid var(--parchment-dark)",
                    borderTop: `4px solid ${s.color}`,
                    overflow: "hidden",
                  }}>

                  {/* Card header */}
                  <div className="flex items-start gap-4 p-6" style={{ background: s.lightColor }}>
                    <span style={{ fontSize: "2.5rem", lineHeight: 1, flexShrink: 0 }}>{s.icon}</span>
                    <div className="flex-1 min-w-0">
                      <h2 className="font-display font-semibold text-xl mb-1" style={{ color: s.color }}>
                        {s.group}
                      </h2>
                      <p className="text-sm mb-3" style={{ color: "var(--stone)" }}>{s.description}</p>
                      <div className="flex flex-wrap gap-2">
                        {s.projects.map((proj) => (
                          <span key={proj} style={{
                            display: "inline-block",
                            padding: "2px 10px",
                            fontSize: "0.72rem",
                            fontFamily: "'Inter', sans-serif",
                            fontWeight: 500,
                            background: "white",
                            color: s.color,
                            border: `1px solid ${s.color}`,
                            borderRadius: "2px",
                          }}>
                            {proj}
                          </span>
                        ))}
                      </div>
                    </div>
                  </div>

                  {/* Download links */}
                  <div className="flex flex-wrap items-center gap-4 px-6 py-4"
                    style={{ borderTop: `1px solid ${s.lightColor}` }}>

                    {/* PDF — opens in new tab */}
                    <a
                      href={`/specs/${s.pdfFile}`}
                      target="_blank"
                      rel="noopener noreferrer"
                      style={{
                        display: "inline-flex", alignItems: "center", gap: "8px",
                        padding: "10px 20px",
                        background: s.color, color: "white",
                        fontFamily: "'Inter', sans-serif", fontSize: "0.875rem",
                        fontWeight: 600, letterSpacing: "0.03em",
                        textDecoration: "none", transition: "opacity 0.15s",
                      }}
                      onMouseEnter={(e) => (e.currentTarget as HTMLElement).style.opacity = "0.85"}
                      onMouseLeave={(e) => (e.currentTarget as HTMLElement).style.opacity = "1"}
                    >
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                        <polyline points="14 2 14 8 20 8"/>
                        <line x1="12" y1="18" x2="12" y2="12"/>
                        <line x1="9" y1="15" x2="15" y2="15"/>
                      </svg>
                      View Specification PDF
                    </a>

                    {/* Excel — downloads */}
                    <a
                      href={`/specs/${s.xlsxFile}`}
                      download={s.xlsxFile}
                      style={{
                        display: "inline-flex", alignItems: "center", gap: "8px",
                        padding: "10px 20px",
                        background: "transparent", color: s.color,
                        border: `2px solid ${s.color}`,
                        fontFamily: "'Inter', sans-serif", fontSize: "0.875rem",
                        fontWeight: 600, letterSpacing: "0.03em",
                        textDecoration: "none", transition: "all 0.15s",
                      }}
                      onMouseEnter={(e) => {
                        (e.currentTarget as HTMLElement).style.background = s.color;
                        (e.currentTarget as HTMLElement).style.color = "white";
                      }}
                      onMouseLeave={(e) => {
                        (e.currentTarget as HTMLElement).style.background = "transparent";
                        (e.currentTarget as HTMLElement).style.color = s.color;
                      }}
                    >
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
                        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                        <polyline points="7 10 12 15 17 10"/>
                        <line x1="12" y1="15" x2="12" y2="3"/>
                      </svg>
                      Download Cost Sheet (.xlsx)
                    </a>

                    <span style={{ marginLeft: "auto", fontSize: "0.75rem", color: "var(--stone)", fontFamily: "'Inter', sans-serif" }}>
                      v2.0 · July 2026
                    </span>
                  </div>
                </div>
              ))}
            </div>

            {/* Footer note */}
            <div className="mt-10 pt-6 text-center" style={{ borderTop: "1px solid var(--parchment-dark)" }}>
              <p className="text-xs" style={{ color: "var(--stone)", fontFamily: "'Inter', sans-serif" }}>
                Prepared by Eduval Pvt. Ltd. · Engagement Ref: EDU-CD-2025-001 · All costs are indicative and subject to detailed design by the appointed civil engineer and architect.
              </p>
            </div>

          </div>
        </div>
      </main>
    </div>
  );
}
