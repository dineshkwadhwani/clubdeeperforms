"use client";
import { useRouter } from "next/navigation";
import Link from "next/link";

const SRD_PDF = "/specs/ClubDeeper_SoftwareRequirements_v1.0.pdf";

const EPIC_SUMMARY = [
  { group: "Campus-Wide Platform", color: "#C8892A", bg: "#FFF8E1", icon: "🏗️", count: 15, mvp: 9,
    epics: ["Deeper Coins Digital Wallet","Unified RFID Identity","CCTV Surveillance Dashboard","Access Control (Zone Management)","Digital PA & Bell System","Campus Visitor Management","Canteen Meal Management","Notification Engine (Push/SMS/WhatsApp)","Admin Super Dashboard","Asset & Facility Maintenance","Energy & Utility Smart Metering","Cross-Campus BI Analytics","Biogas & Waste Operations","Farm & Agriculture Inventory","Animal Husbandry Log"] },
  { group: "Education Campus", color: "#1565C0", bg: "#E3F2FD", icon: "🏫", count: 24, mvp: 15,
    epics: ["Student Admissions & Enrollment","Student Profile & Academic Records","Timetable Management","Facial Recognition Attendance","Fee Collection & Deeper Coins","Exam & Assessment Management","Result Publishing & Report Cards","Parent Mobile App","Library RFID Management","Hostel Room Allocation","Discipline & Incident Register","Staff HR & Payroll","Leave Management","Transport GPS Tracking","Coaching Batch Management","CBT Mock Test Platform (NEET/JEE)","AI Performance Analytics","LMS Content Delivery","e-Library Digital Portal","Study Center Batch Management","Smart Board Content Management","Alumni & Placement Tracking","Parent-Teacher Communication","CBSE/NSQF Compliance Reports"] },
  { group: "Skill Campus", color: "#00695C", bg: "#E0F2F1", icon: "🛠️", count: 14, mvp: 7,
    epics: ["Skill Enrollment & Unit Assignment","NSQF Assessment & Certification","Campus Service Assignment (Self-Sufficiency Engine)","Deeper Coins Earnings Wallet","Live Service Quality Rating","Internship Placement Portal","Skill Hostel Management","Workshop Equipment Inventory","Government Scheme Enrollment (PMKVY)","Startup Incubation Tracker","Software Dev Park Workspace Booking","Placement Cell Job Board","Industry Certification Scheduling","Skill Impact Dashboard"] },
  { group: "Social Projects", color: "#B71C1C", bg: "#FFEBEE", icon: "🏥", count: 18, mvp: 10,
    epics: ["Hospital OPD Registration","Inpatient Ward & Bed Management","Electronic Medical Records (EMR)","Pharmacy Inventory & Dispensing","Doctor Appointment Scheduling","Medical Billing (Deeper Coins)","Diagnostic Lab Management","Nurse Call & Smart Sensor Monitoring","OAH Resident Registration & Care Plans","Medication & Caregiver Task Management","OAH Family Visit Booking","Care Center Registration & Therapy Scheduling","Therapy Progress Notes & IEP","Care Center Parent App (CCTV)","Wearable Fall Detection","Nursing Internship Roster","Rural Health Camp Management","Cross-Facility Wellbeing Dashboard"] },
  { group: "Sport & Cultural", color: "#1B5E20", bg: "#E8F5E9", icon: "🏏", count: 12, mvp: 7,
    epics: ["Sports Facility Booking (Courts, Pool, Gym)","Gym Membership Management","Pool Session & Coaching Schedule","Deeper Coins Sports Payments","Fitness Tracker & Workout Log","Sport Coaching Programme Enrollment","Indoor Games Court Booking","Tournament & Event Registration","Groundsman Maintenance Schedule","Sports Performance Tracking","Cultural Events Calendar","LED Scoreboard Integration"] },
  { group: "Residential Community", color: "#4A148C", bg: "#F3E5F5", icon: "🏘️", count: 13, mvp: 8,
    epics: ["Plot Sales CRM (Leads, Booking, Payments)","Plot Ownership Registry & Legal Docs","Visitor Management — QR Entry","Maintenance Request Portal","Monthly Maintenance Billing","Community Announcement App","Clubhouse Membership Management","Clubhouse Facility Booking (Spa, Pool, Dining)","Clubhouse F&B (Deeper Coins)","RWA Meeting & Voting","Security CCTV & Incident Log","Construction Approval Workflow","Intergenerational Event Calendar"] },
];

const ROADMAP = [
  { q: "Q3 2026", label: "Foundation", color: "#C8892A", items: ["Deeper Coins Engine", "RFID Identity", "Notification Hub", "Access Control", "Admin Dashboard"] },
  { q: "Q4 2026", label: "School Core I", color: "#1565C0", items: ["Admissions", "Timetable", "Facial Attendance", "Visitor Management"] },
  { q: "Q1 2027", label: "School Core II", color: "#1565C0", items: ["Fees & Billing", "Exams & Results", "Parent Mobile App", "Library RFID", "Staff Payroll"] },
  { q: "Q2 2027", label: "Residential", color: "#4A148C", items: ["Plot Sales CRM", "Ownership Registry", "Residential Gate", "Maintenance Billing"] },
  { q: "Q3 2027", label: "Skill Campus", color: "#00695C", items: ["Skill Enrollment", "NSQF Assessment", "Service Assignment", "Deeper Coins Earnings", "Canteen Management"] },
  { q: "Q4 2027", label: "Sports & Coaching", color: "#1B5E20", items: ["Sports Booking", "Gym Membership", "Pool Sessions", "CBT Mock Tests", "Clubhouse"] },
  { q: "Q1 2028", label: "Hospital MVP", color: "#B71C1C", items: ["OPD Registration", "EMR", "Pharmacy", "Medical Billing", "Ward Management"] },
  { q: "Q2 2028", label: "Social Care", color: "#B71C1C", items: ["Nurse Call Sensors", "OAH Care Plans", "Care Center App", "Parent CCTV Access"] },
  { q: "Q3–Q4 2028", label: "Analytics & Phase 2", color: "#37474F", items: ["BI Dashboard", "AI Analytics", "LMS", "Government Schemes", "Asset Management"] },
  { q: "Q1 2029", label: "School Launch Prep", color: "#1565C0", items: ["Transport GPS", "Leave Management", "Load Testing", "Staff Training", "Go-Live ✓"] },
  { q: "2029–2030", label: "Phase 3 & Sustainability", color: "#37474F", items: ["Startup Incubation", "Farm Inventory", "Rural Health", "Impact Dashboard", "Full 84-Epic Completion"] },
];

export default function SoftwareRequirementsPage() {
  const router = useRouter();

  async function handleLogout() {
    await fetch("/api/auth", { method: "DELETE" });
    router.push("/");
  }

  const totalEpics = EPIC_SUMMARY.reduce((s, g) => s + g.count, 0);
  const totalMVP   = EPIC_SUMMARY.reduce((s, g) => s + g.mvp, 0);

  return (
    <div className="flex h-screen overflow-hidden" style={{ background: "var(--cream)" }}>

      {/* ── Sidebar ── */}
      <aside className="flex flex-col flex-shrink-0 w-72"
        style={{ background: "#0D2218", borderRight: "1px solid rgba(200,137,42,0.25)", overflowY: "auto" }}>

        {/* Header */}
        <div className="flex items-center gap-3 px-4 py-4 flex-shrink-0"
          style={{ borderBottom: "1px solid rgba(200,137,42,0.2)", minHeight: "68px" }}>
          <span className="text-2xl flex-shrink-0">🌿</span>
          <div>
            <div className="font-display font-bold text-white text-base">Club Deeper</div>
            <div className="text-xs" style={{ fontFamily: "'Tiro Devanagari Marathi', serif", color: "#E8A84A" }}>क्लब डीपर</div>
          </div>
        </div>

        {/* Nav */}
        <div className="flex-1 py-4 overflow-y-auto">

          {/* Specifications */}
          <Link href="/specifications" style={{ display:"flex", alignItems:"center", gap:"12px", padding:"10px 16px", borderLeft:"3px solid transparent", textDecoration:"none", transition:"all 0.15s" }}
            onMouseEnter={e => { (e.currentTarget as HTMLElement).style.background="rgba(255,255,255,0.07)"; (e.currentTarget as HTMLElement).style.borderLeftColor="rgba(200,137,42,0.5)"; }}
            onMouseLeave={e => { (e.currentTarget as HTMLElement).style.background="transparent"; (e.currentTarget as HTMLElement).style.borderLeftColor="transparent"; }}>
            <span className="text-xl flex-shrink-0">📋</span>
            <span style={{ fontFamily:"'Inter',sans-serif", fontSize:"0.875rem", fontWeight:600, color:"#E8A84A" }}>Specifications</span>
          </Link>

          {/* Software Requirements — active */}
          <div style={{ display:"flex", alignItems:"center", gap:"12px", padding:"10px 16px", borderLeft:"3px solid #E8A84A", background:"rgba(200,137,42,0.18)" }}>
            <span className="text-xl flex-shrink-0">💻</span>
            <span style={{ fontFamily:"'Inter',sans-serif", fontSize:"0.875rem", fontWeight:600, color:"#F5C842" }}>Software Requirements</span>
          </div>

          {/* Dashboard */}
          <Link href="/dashboard" style={{ display:"flex", alignItems:"center", gap:"12px", padding:"10px 16px", borderLeft:"3px solid transparent", textDecoration:"none", transition:"all 0.15s" }}
            onMouseEnter={e => { (e.currentTarget as HTMLElement).style.background="rgba(255,255,255,0.07)"; (e.currentTarget as HTMLElement).style.borderLeftColor="rgba(200,137,42,0.5)"; }}
            onMouseLeave={e => { (e.currentTarget as HTMLElement).style.background="transparent"; (e.currentTarget as HTMLElement).style.borderLeftColor="transparent"; }}>
            <span className="text-xl flex-shrink-0">📊</span>
            <span style={{ fontFamily:"'Inter',sans-serif", fontSize:"0.875rem", fontWeight:500, color:"#F0EDE8" }}>Planning Dashboard</span>
          </Link>

          <div style={{ margin:"12px 16px 6px", height:"1px", background:"rgba(200,137,42,0.15)" }} />

          {/* Jump-to anchors */}
          <div className="px-4 mb-2">
            <span style={{ color:"#E8A84A", fontSize:"0.7rem", fontWeight:700, letterSpacing:"0.14em", textTransform:"uppercase", fontFamily:"'Inter',sans-serif" }}>Jump to</span>
          </div>
          {[["#overview","📊 Overview & Vision"],["#epics","📋 All 84 Epics"],["#roadmap","🗓️ Delivery Roadmap"],["#document","📄 Full Document"]].map(([href,label])=>(
            <a key={href} href={href} style={{ display:"flex", alignItems:"center", gap:"10px", padding:"7px 16px", borderLeft:"3px solid transparent", textDecoration:"none", transition:"all 0.15s" }}
              onMouseEnter={e => { (e.currentTarget as HTMLElement).style.background="rgba(255,255,255,0.07)"; (e.currentTarget as HTMLElement).style.borderLeftColor="rgba(200,137,42,0.5)"; }}
              onMouseLeave={e => { (e.currentTarget as HTMLElement).style.background="transparent"; (e.currentTarget as HTMLElement).style.borderLeftColor="transparent"; }}>
              <span style={{ fontFamily:"'Inter',sans-serif", fontSize:"0.8rem", color:"#A0BEA8" }}>{label}</span>
            </a>
          ))}
        </div>

        {/* Footer */}
        <div className="flex-shrink-0 px-4 py-3" style={{ borderTop:"1px solid rgba(200,137,42,0.15)" }}>
          <button onClick={handleLogout} className="w-full text-center py-2 text-sm transition-all hover:opacity-80"
            style={{ color:"#6A8A78", fontFamily:"'Inter',sans-serif" }}>Sign Out ↩</button>
        </div>
      </aside>

      {/* ── Main ── */}
      <main className="flex-1 flex flex-col overflow-hidden">

        {/* Top bar */}
        <div className="flex items-center justify-between px-8 py-4 flex-shrink-0"
          style={{ background:"white", borderBottom:"1px solid var(--parchment-dark)", minHeight:"68px" }}>
          <div>
            <h1 className="font-display text-xl font-semibold" style={{ color:"var(--forest)" }}>Software Requirements & Digital Roadmap</h1>
            <p className="text-sm" style={{ fontFamily:"'Tiro Devanagari Marathi',serif", color:"var(--stone)" }}>सॉफ्टवेअर आवश्यकता दस्तऐवज</p>
          </div>
          <span className="category-pill">84 Epics · 4-Year Roadmap · v1.0</span>
        </div>

        {/* Content */}
        <div className="flex-1 overflow-auto">
          <div className="max-w-5xl mx-auto px-8 py-8">

            {/* ── OVERVIEW ── */}
            <div id="overview" />

            {/* Stats row */}
            <div className="grid grid-cols-4 gap-4 mb-8">
              {[
                { n: String(totalEpics), label: "Total Epics", color: "var(--forest)" },
                { n: String(totalMVP),   label: "MVP Epics (Day 1)", color: "var(--saffron)" },
                { n: "8",  label: "Engineers", color: "var(--forest)" },
                { n: "4",  label: "Year Roadmap", color: "var(--forest)" },
              ].map(s => (
                <div key={s.label} className="text-center p-5"
                  style={{ background:"var(--parchment)", border:"1px solid var(--parchment-dark)" }}>
                  <div className="font-display text-3xl font-bold" style={{ color: s.color }}>{s.n}</div>
                  <div className="text-xs mt-1" style={{ color:"var(--stone)" }}>{s.label}</div>
                </div>
              ))}
            </div>

            {/* Download PDF banner */}
            <div id="document" className="mb-8 flex items-center justify-between p-6"
              style={{ background:"white", borderLeft:"4px solid var(--forest)", border:"1px solid var(--parchment-dark)", borderLeftWidth:"4px", borderLeftColor:"var(--forest)" }}>
              <div>
                <h2 className="font-display text-lg font-semibold mb-1" style={{ color:"var(--forest)" }}>
                  Software Requirements Document v1.0
                </h2>
                <p className="text-sm" style={{ color:"var(--stone)" }}>
                  Board-level presentation · 84 Epics · Delivery roadmap · Investment summary · July 2026
                </p>
              </div>
              <a href={SRD_PDF} target="_blank" rel="noopener noreferrer"
                style={{ display:"inline-flex", alignItems:"center", gap:"8px", padding:"12px 24px", background:"var(--forest)", color:"white", fontFamily:"'Inter',sans-serif", fontSize:"0.875rem", fontWeight:600, letterSpacing:"0.03em", textDecoration:"none", flexShrink:0, transition:"opacity 0.15s" }}
                onMouseEnter={e => (e.currentTarget as HTMLElement).style.opacity="0.85"}
                onMouseLeave={e => (e.currentTarget as HTMLElement).style.opacity="1"}>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
                  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                  <polyline points="14 2 14 8 20 8"/>
                  <line x1="12" y1="18" x2="12" y2="12"/>
                  <line x1="9" y1="15" x2="15" y2="15"/>
                </svg>
                Open Full PDF
              </a>
            </div>

            {/* Vision blurb */}
            <div className="mb-10 p-5" style={{ background:"var(--parchment)", borderLeft:"3px solid var(--saffron)" }}>
              <p className="text-sm leading-relaxed" style={{ color:"var(--stone)", lineHeight:"1.9" }}>
                The Club Deeper ERP is built around four principles: <strong style={{ color:"var(--forest)" }}>Deeper Coins First</strong> (every campus transaction is cashless), <strong style={{ color:"var(--forest)" }}>One Identity One Card</strong> (single RFID card for attendance, access, library, meals), <strong style={{ color:"var(--forest)" }}>Mobile by Default</strong> (families and residents on mobile; operations on desktop), and the <strong style={{ color:"var(--forest)" }}>Self-Sufficiency Loop</strong> — skill students deliver campus services, earn Deeper Coins, and log NSQF certification hours simultaneously.
              </p>
            </div>

            {/* ── EPICS ── */}
            <div id="epics" />
            <h2 className="font-display text-2xl font-semibold mb-2" style={{ color:"var(--forest)" }}>All 84 Epics — by Group</h2>
            <div style={{ width:"40px", height:"2px", background:"var(--saffron)", marginBottom:"24px" }} />

            <div className="grid gap-5 mb-12">
              {EPIC_SUMMARY.map(g => (
                <div key={g.group} style={{ border:"1px solid var(--parchment-dark)", borderTop:`4px solid ${g.color}`, background:"white", overflow:"hidden" }}>
                  {/* Header */}
                  <div className="flex items-center justify-between px-5 py-4" style={{ background: g.bg }}>
                    <div className="flex items-center gap-3">
                      <span style={{ fontSize:"1.75rem" }}>{g.icon}</span>
                      <div>
                        <div className="font-display font-semibold" style={{ color: g.color, fontSize:"1.05rem" }}>{g.group}</div>
                        <div className="text-xs mt-0.5" style={{ color:"var(--stone)" }}>
                          {g.count} epics total &nbsp;·&nbsp;
                          <span style={{ color: g.color, fontWeight:600 }}>{g.mvp} MVP</span>
                          &nbsp;·&nbsp; {g.count - g.mvp} Phase 2/3
                        </div>
                      </div>
                    </div>
                    {/* MVP badge */}
                    <span style={{ padding:"4px 12px", background: g.color, color:"white", fontSize:"0.72rem", fontWeight:700, fontFamily:"'Inter',sans-serif", letterSpacing:"0.08em" }}>
                      {g.mvp} MVP
                    </span>
                  </div>
                  {/* Epic list */}
                  <div className="px-5 py-4">
                    <div className="flex flex-wrap gap-2">
                      {g.epics.map((epic, i) => (
                        <span key={epic} style={{
                          display:"inline-block", padding:"3px 10px",
                          fontSize:"0.72rem", fontFamily:"'Inter',sans-serif", fontWeight:500,
                          background: i < g.mvp ? g.bg : "var(--parchment)",
                          color: i < g.mvp ? g.color : "var(--stone)",
                          border: `1px solid ${i < g.mvp ? g.color : "var(--parchment-dark)"}`,
                          borderRadius:"2px",
                        }}>
                          {i < g.mvp && <span style={{ marginRight:"4px", fontSize:"0.65rem" }}>★</span>}
                          {epic}
                        </span>
                      ))}
                    </div>
                    <p className="text-xs mt-3" style={{ color:"var(--stone)" }}>
                      <span style={{ color: g.color }}>★ filled = MVP</span> &nbsp;· outlined = Phase 2 or 3
                    </p>
                  </div>
                </div>
              ))}
            </div>

            {/* ── ROADMAP ── */}
            <div id="roadmap" />
            <h2 className="font-display text-2xl font-semibold mb-2" style={{ color:"var(--forest)" }}>Delivery Roadmap — 8-Person Team</h2>
            <div style={{ width:"40px", height:"2px", background:"var(--saffron)", marginBottom:"24px" }} />

            <div className="mb-12">
              {ROADMAP.map((q, i) => (
                <div key={q.q} className="flex gap-0 mb-0">
                  {/* Timeline spine */}
                  <div className="flex flex-col items-center" style={{ width:"48px", flexShrink:0 }}>
                    <div style={{ width:"14px", height:"14px", borderRadius:"50%", background: q.color, border:"2px solid white", boxShadow:`0 0 0 2px ${q.color}`, marginTop:"18px", flexShrink:0 }} />
                    {i < ROADMAP.length - 1 && <div style={{ width:"2px", flex:1, background:"var(--parchment-dark)", minHeight:"20px" }} />}
                  </div>
                  {/* Card */}
                  <div className="flex-1 mb-4 ml-2">
                    <div className="flex items-center gap-3 mb-2" style={{ paddingTop:"12px" }}>
                      <span style={{ fontFamily:"'Inter',sans-serif", fontSize:"0.75rem", fontWeight:700, color: q.color, letterSpacing:"0.06em" }}>{q.q}</span>
                      <span style={{ fontFamily:"'Playfair Display',serif", fontSize:"0.95rem", fontWeight:600, color:"var(--forest)" }}>{q.label}</span>
                    </div>
                    <div className="flex flex-wrap gap-2 pb-3" style={{ borderBottom: i < ROADMAP.length-1 ? "none" : "none" }}>
                      {q.items.map(item => (
                        <span key={item} style={{
                          display:"inline-block", padding:"3px 10px",
                          fontSize:"0.72rem", fontFamily:"'Inter',sans-serif", fontWeight:500,
                          background:"white", color: q.color,
                          border:`1px solid ${q.color}`,
                          borderRadius:"2px",
                        }}>{item}</span>
                      ))}
                    </div>
                  </div>
                </div>
              ))}
            </div>

            {/* Key dates callout */}
            <div className="grid grid-cols-3 gap-4 mb-10">
              {[
                { date:"Dec 2027", label:"Bungalow Plot Delivery", color:"#4A148C", note:"Plot CRM, Visitor Mgmt, Gate Security live" },
                { date:"Mid 2028", label:"Hospital Opens", color:"#B71C1C", note:"Full OPD, EMR, Pharmacy, Billing live" },
                { date:"Apr 2029", label:"School Launch", color:"#1B5E20", note:"All 15 Education MVP epics live + load tested" },
              ].map(d => (
                <div key={d.date} className="p-4 text-center" style={{ background:"white", border:`2px solid ${d.color}`, borderTop:`5px solid ${d.color}` }}>
                  <div className="font-display text-xl font-bold mb-1" style={{ color: d.color }}>{d.date}</div>
                  <div className="text-sm font-semibold mb-2" style={{ color:"var(--forest)" }}>{d.label}</div>
                  <div className="text-xs" style={{ color:"var(--stone)" }}>{d.note}</div>
                </div>
              ))}
            </div>

            {/* Investment row */}
            <div className="p-6 mb-10" style={{ background:"var(--forest)", color:"white" }}>
              <h3 className="font-display text-lg font-semibold mb-4" style={{ color:"#E8A84A" }}>Investment Summary</h3>
              <div className="grid grid-cols-4 gap-4">
                {[
                  { phase:"Phase 0 — Consulting",    period:"Jun–Jul 2026",      amount:"₹2,00,000",    note:"2 people · Surveys & planning" },
                  { phase:"Phase 1 — Requirements",  period:"Aug–Sep 2026",      amount:"₹3,60,000",    note:"2 people · Requirements & architecture" },
                  { phase:"Phase 2 — Build I",       period:"Oct 2026–Mar 2027", amount:"₹86,40,000",   note:"8 people · Platform, School, Admissions" },
                  { phase:"Phase 3 — Build II",      period:"Apr 2027–Sep 2027", amount:"₹86,40,000",   note:"8 people · Residential, Skill, Sports" },
                  { phase:"Phase 4 — Build III",     period:"Oct 2027–Mar 2028", amount:"₹86,40,000",   note:"8 people · Hospital, OAH, Analytics" },
                  { phase:"Phase 5 — Stabilisation", period:"Apr 2028–Jul 2028", amount:"₹43,20,000",   note:"6 people · Testing, UAT, Go-live" },
                  { phase:"3rd Party Testing",       period:"One-time",          amount:"₹18,00,000",   note:"Pen testing, performance, security audit" },
                ].map(p => (
                  <div key={p.phase} style={{ borderLeft:"2px solid rgba(200,137,42,0.4)", paddingLeft:"12px", marginBottom:"12px" }}>
                    <div style={{ fontSize:"0.65rem", color:"#90CAF9", fontFamily:"'Inter',sans-serif", letterSpacing:"0.06em", textTransform:"uppercase", marginBottom:"4px" }}>{p.phase}</div>
                    <div style={{ fontSize:"1rem", fontWeight:700, color:"#E8A84A", fontFamily:"'Playfair Display',serif" }}>{p.amount}</div>
                    <div style={{ fontSize:"0.65rem", color:"rgba(255,255,255,0.6)", marginTop:"3px" }}>{p.period}</div>
                    <div style={{ fontSize:"0.65rem", color:"rgba(255,255,255,0.5)", marginTop:"2px" }}>{p.note}</div>
                  </div>
                ))}
              </div>
              <div className="mt-4 pt-4" style={{ borderTop:"1px solid rgba(200,137,42,0.3)" }}>
                <span style={{ fontSize:"0.875rem", color:"rgba(255,255,255,0.7)" }}>Total development (excl. GST): </span>
                <span style={{ fontSize:"1.2rem", fontWeight:700, color:"#E8A84A", fontFamily:"'Playfair Display',serif" }}>₹3,26,00,000 + GST</span>
                <span style={{ fontSize:"0.8rem", color:"rgba(255,255,255,0.5)", marginLeft:"12px" }}>+ ₹36,00,000/year maintenance from Jul 2028 (3 people at cost) · excl. cloud infra & hardware</span>
              </div>
            </div>

            {/* Footer */}
            <div className="text-center pb-6" style={{ borderTop:"1px solid var(--parchment-dark)", paddingTop:"24px" }}>
              <p className="text-xs" style={{ color:"var(--stone)" }}>
                Prepared by Eduval Pvt. Ltd. · Ref: EDU-SRD-001 · v1.0 · July 2026 · Board Presentation
              </p>
              <a href={SRD_PDF} target="_blank" rel="noopener noreferrer"
                className="text-xs hover:underline mt-1 inline-block" style={{ color:"var(--saffron)" }}>
                Download full PDF ↗
              </a>
            </div>

          </div>
        </div>
      </main>
    </div>
  );
}
