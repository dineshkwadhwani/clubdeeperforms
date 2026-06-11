"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import Image from "next/image";

const FOUNDERS = [
  { name: "Harish Butle", nameMarathi: "हरीश बुटले", city: "Pune", photo: "/founders/harish_butle.png", role: "Chief Promoter" },
  { name: "D. K. Deshmukh", nameMarathi: "डी. के. देशमुख", city: "Latur", photo: "/founders/dk_deshmukh.png", role: "Founder Member" },
  { name: "Vinayak Gaikwad", nameMarathi: "विनायक गायकवाड", city: "Latur", photo: "/founders/vinayak_gaikwad.png", role: "Founder Member" },
  { name: "G. M. Mahajan", nameMarathi: "जी. एम. महाजन", city: "Bhusawal", photo: "/founders/gm_mahajan.png", role: "Founder Member" },
  { name: "G. S. Patil", nameMarathi: "जी. एस. पाटील", city: "Navapur / Nasik", photo: "/founders/gs_patil.png", role: "Founder Member" },
  { name: "Nityedra Oke", nameMarathi: "नित्येंद्र ओके", city: "Akola", photo: "/founders/nityedra_oke.png", role: "Founder Member" },
  { name: "Anand Nasery", nameMarathi: "अनंत नासेरी", city: "Nagpur", photo: "/founders/anant_naseri.png", role: "Founder Member" },
];

export default function HomePage() {
  const [showLogin, setShowLogin] = useState(false);
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const router = useRouter();

  async function handleLogin(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    setError("");
    const res = await fetch("/api/auth", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ password }),
    });
    const data = await res.json();
    setLoading(false);
    if (data.success) {
      if (data.role === "admin") router.push("/admin");
      else router.push("/dashboard");
    } else {
      setError("Incorrect password. Please try again.");
    }
  }

  return (
    <main className="min-h-screen" style={{ background: "var(--cream)" }}>

      {/* ── Top nav ── */}
      <nav className="fixed top-0 left-0 right-0 z-50 flex items-center justify-between px-8 py-4"
        style={{ background: "rgba(13,34,24,0.97)", backdropFilter: "blur(12px)", borderBottom: "1px solid rgba(200,137,42,0.2)" }}>
        <div className="flex items-center gap-3">
          <div className="w-9 h-9 rounded-full flex items-center justify-center text-lg"
            style={{ background: "rgba(200,137,42,0.15)", border: "1px solid rgba(200,137,42,0.4)" }}>
            🌿
          </div>
          <div>
            <div className="font-display font-bold text-white text-base leading-tight">Club Deeper</div>
            <div className="text-xs" style={{ color: "#E8A84A", fontFamily: "'Tiro Devanagari Marathi', serif" }}>क्लब डीपर</div>
          </div>
        </div>

        <div className="flex items-center gap-4">
          {/* Brochure download */}
          <a href="/ClubDeeper_Brochure.pdf" download="ClubDeeper_Brochure.pdf"
            className="flex items-center gap-2 px-4 py-2 text-sm transition-all duration-200 hover:opacity-80"
            style={{ color: "#E8A84A", border: "1px solid rgba(200,137,42,0.4)", fontFamily: "'Inter', sans-serif", letterSpacing: "0.03em" }}>
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
              <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/>
            </svg>
            Brochure
          </a>
          <button onClick={() => setShowLogin(true)}
            className="px-5 py-2 text-sm font-medium transition-all duration-200 hover:scale-105"
            style={{ background: "linear-gradient(135deg, #C8892A, #E8A84A)", color: "#fff", fontFamily: "'Inter', sans-serif", letterSpacing: "0.04em" }}>
            Login &nbsp;/&nbsp; <span style={{ fontFamily: "'Tiro Devanagari Marathi', serif" }}>प्रवेश</span>
          </button>
        </div>
      </nav>

      {/* ── Hero ── */}
      <section className="relative min-h-screen flex flex-col items-center justify-center pt-16 overflow-hidden"
        style={{ background: "#0A1A10" }}>

        {/* Hill silhouette */}
        <svg className="absolute bottom-0 left-0 right-0 w-full" viewBox="0 0 1440 340" preserveAspectRatio="none"
          style={{ height: "50vh" }}>
          <defs>
            <linearGradient id="h1" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="#1B3A2D" /><stop offset="100%" stopColor="#0D2218" />
            </linearGradient>
            <linearGradient id="h2" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="#142C1E" /><stop offset="100%" stopColor="#091510" />
            </linearGradient>
            <linearGradient id="h3" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="#243D30" /><stop offset="100%" stopColor="#1B3A2D" />
            </linearGradient>
          </defs>
          {/* Stars */}
          {[[180,55],[420,35],[690,50],[960,30],[1200,60],[1350,42],[320,78],[830,68],[100,90],[1050,85]].map(([cx,cy],i) => (
            <circle key={i} cx={cx} cy={cy} r={i%3===0?1.5:1} fill="white" opacity={0.25+((i*7)%3)*0.1} />
          ))}
          {/* Far hills */}
          <path d="M0,230 C130,180 220,148 350,165 C470,182 530,132 650,122 C770,112 830,152 950,142 C1070,132 1150,105 1270,122 C1380,138 1420,158 1440,155 L1440,340 L0,340 Z" fill="url(#h1)" opacity="0.85" />
          {/* Sinhgad fort silhouette — gold */}
          <path d="M588,162 L592,152 L596,145 L599,141 L602,137 L606,135 L610,137 L613,141 L616,136 L620,132 L624,134 L627,138 L630,143 L634,150 L638,162 Z" fill="#C8892A" opacity="0.55" />
          <rect x="591" y="143" width="3" height="9" fill="#C8892A" opacity="0.45" />
          <rect x="598" y="138" width="3" height="7" fill="#C8892A" opacity="0.45" />
          <rect x="605" y="136" width="3" height="9" fill="#C8892A" opacity="0.45" />
          <rect x="612" y="134" width="3" height="8" fill="#C8892A" opacity="0.45" />
          <rect x="619" y="137" width="3" height="8" fill="#C8892A" opacity="0.45" />
          {/* Mid hills */}
          <path d="M0,272 C90,245 175,215 295,222 C400,228 460,192 580,198 C700,204 780,178 900,183 C1020,188 1100,208 1210,202 C1320,196 1390,218 1440,222 L1440,340 L0,340 Z" fill="url(#h2)" />
          {/* Near hill */}
          <path d="M0,300 C110,278 210,262 355,268 C500,274 590,252 710,257 C830,262 940,246 1060,252 C1180,258 1320,274 1440,278 L1440,340 L0,340 Z" fill="url(#h3)" />
        </svg>

        {/* Hero content */}
        <div className="relative z-10 text-center px-6 pb-40 max-w-5xl mx-auto">
          <div className="inline-flex items-center gap-3 mb-10">
            <div style={{ width: "48px", height: "1px", background: "rgba(200,137,42,0.5)" }}></div>
            <span className="text-xs tracking-widest" style={{ color: "#C8892A", letterSpacing: "0.22em", fontFamily: "'Inter', sans-serif", textTransform: "uppercase" }}>
              Osade · Velhe · Pune · Est. 2026
            </span>
            <div style={{ width: "48px", height: "1px", background: "rgba(200,137,42,0.5)" }}></div>
          </div>

          {/* Bilingual title */}
          <div className="flex flex-col md:flex-row items-center justify-center gap-4 md:gap-12 mb-5">
            <h1 className="font-display font-bold text-white leading-none" style={{ fontSize: "clamp(2.8rem, 7vw, 5rem)" }}>
              Club Deeper
            </h1>
            <div style={{ width: "1px", height: "64px", background: "rgba(200,137,42,0.35)" }} className="hidden md:block" />
            <h1 className="font-bold text-white leading-none" style={{ fontSize: "clamp(2.2rem, 5.5vw, 4rem)", fontFamily: "'Tiro Devanagari Marathi', serif" }}>
              क्लब डीपर
            </h1>
          </div>

          <div className="flex justify-center mb-8">
            <div style={{ width: "90px", height: "2px", background: "linear-gradient(90deg, transparent, #C8892A, transparent)" }} />
          </div>

          {/* Bilingual tagline */}
          <div className="grid md:grid-cols-2 gap-6 md:gap-10 mb-12 max-w-4xl mx-auto">
            <p className="text-base md:text-lg font-light text-right"
              style={{ color: "rgba(247,243,236,0.78)", fontFamily: "'Playfair Display', serif", fontStyle: "italic", lineHeight: "1.85" }}>
              A path-breaking campus of education, skill, social purpose and community — rising from the hills of Sinhgad.
            </p>
            <div style={{ width: "1px", background: "rgba(200,137,42,0.2)" }} className="hidden md:block" />
            <p className="text-base text-left"
              style={{ color: "rgba(247,243,236,0.75)", fontFamily: "'Tiro Devanagari Marathi', serif", lineHeight: "2.1" }}>
              शिक्षण, कौशल्य, सामाजिक उद्देश आणि समुदायाचा एक अभूतपूर्व कॅम्पस — सिंहगडाच्या डोंगरांतून उदयास येत आहे.
            </p>
          </div>

          <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
            <button onClick={() => setShowLogin(true)}
              className="inline-flex items-center gap-2 px-8 py-3 text-sm font-medium transition-all duration-300 hover:scale-105"
              style={{ background: "linear-gradient(135deg, #C8892A, #E8A84A)", color: "#fff", letterSpacing: "0.06em", fontFamily: "'Inter', sans-serif" }}>
              Enter Planning Portal
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </button>
            <a href="/ClubDeeper_Brochure.pdf" download="ClubDeeper_Brochure.pdf"
              className="inline-flex items-center gap-2 px-8 py-3 text-sm font-medium transition-all duration-300 hover:scale-105"
              style={{ border: "1px solid rgba(200,137,42,0.5)", color: "#E8A84A", letterSpacing: "0.06em", fontFamily: "'Inter', sans-serif" }}>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
                <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/>
              </svg>
              Download Brochure
            </a>
          </div>
        </div>
      </section>

      {/* ── About section ── */}
      <section className="py-24 px-6" style={{ background: "var(--parchment)" }}>
        <div className="max-w-6xl mx-auto">
          <div className="flex items-center gap-4 mb-12">
            <div style={{ width: "3px", height: "36px", background: "#C8892A" }} />
            <div>
              <div className="font-display text-2xl font-semibold" style={{ color: "#1B3A2D" }}>The Vision</div>
              <div className="text-lg" style={{ fontFamily: "'Tiro Devanagari Marathi', serif", color: "#6B7565" }}>दृष्टी</div>
            </div>
          </div>

          <div className="grid md:grid-cols-2 gap-12 items-start">
            <p className="leading-relaxed" style={{ color: "#1A1A1A", fontFamily: "'Playfair Display', serif", fontSize: "1.05rem", lineHeight: "1.95" }}>
              Club Deeper is the vision of Shri. Harish Butle — a path-breaking educational institution spread over 50 pristine acres at Osade (Velhe), on the Panshet Road, in the embrace of Sinhgad Fort and the Khadakwasla backwaters. It brings together high-quality education, future-oriented skill development and meaningful social cause under one self-sustaining, nature-friendly, technologically advanced campus — designed for 3,000+ residential students, 200 families and an entire community.
            </p>
            <p className="leading-relaxed" style={{ color: "#1A1A1A", fontFamily: "'Tiro Devanagari Marathi', serif", fontSize: "1.05rem", lineHeight: "2.1" }}>
              क्लब डीपर हा श्री. हरीश बुटले यांचा दूरदर्शी संकल्प आहे — खडकवासला जलाशयाच्या काठावर, सिंहगड किल्ल्याच्या सावलीत, ओसाडे (वेल्हे) येथील ५० एकर हरित भूमीवर उभारलेला एक अभूतपूर्व शैक्षणिक कॅम्पस. उच्च दर्जाचे शिक्षण, कौशल्य विकास आणि सामाजिक उद्दिष्टे एकाच स्वावलंबी, निसर्गस्नेही कॅम्पसमध्ये एकत्र आणून ३,०००+ निवासी विद्यार्थी आणि २०० कुटुंबांना सेवा देण्याचे हे स्वप्न आहे.
            </p>
          </div>
        </div>
      </section>

      {/* ── Campus pillars ── */}
      <section className="py-20 px-6" style={{ background: "var(--cream)" }}>
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-14">
            <h2 className="font-display text-3xl font-semibold mb-1" style={{ color: "#1B3A2D" }}>Campus Pillars</h2>
            <p className="text-xl" style={{ fontFamily: "'Tiro Devanagari Marathi', serif", color: "#6B7565" }}>कॅम्पसचे स्तंभ</p>
            <div className="flex justify-center mt-4">
              <div style={{ width: "60px", height: "2px", background: "linear-gradient(90deg, transparent, #C8892A, transparent)" }} />
            </div>
          </div>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-5">
            {[
              { icon: "🎓", en: "Education Campus", mr: "शिक्षण कॅम्पस", desc: "CBSE School · Coaching · Library · Study Centre" },
              { icon: "🛠️", en: "Skill Campus", mr: "कौशल्य कॅम्पस", desc: "25–30 skill units · Software Development Park" },
              { icon: "🤝", en: "Social Projects", mr: "सामाजिक प्रकल्प", desc: "Hospital · Old Age Home · Rural Development" },
              { icon: "🏏", en: "Sport & Culture", mr: "क्रीडा व संस्कृती", desc: "Cricket · Indoor Sports · Gymnasium · Pool" },
            ].map((p) => (
              <div key={p.en} className="p-6 text-center transition-all duration-200 hover:-translate-y-1 hover:shadow-md"
                style={{ background: "var(--parchment)", border: "1px solid var(--parchment-dark)", borderTop: "3px solid #C8892A" }}>
                <div className="text-4xl mb-3">{p.icon}</div>
                <div className="font-display font-semibold text-sm mb-1" style={{ color: "#1B3A2D" }}>{p.en}</div>
                <div className="text-sm mb-3" style={{ fontFamily: "'Tiro Devanagari Marathi', serif", color: "#6B7565" }}>{p.mr}</div>
                <p className="text-xs leading-relaxed" style={{ color: "#6B7565" }}>{p.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ── Founder Members ── */}
      <section className="py-20 px-6" style={{ background: "#0D2218" }}>
        <div className="max-w-6xl mx-auto">

          {/* Section header */}
          <div className="text-center mb-14">
            <p className="text-xs tracking-widest uppercase mb-3" style={{ color: "#C8892A", letterSpacing: "0.2em", fontFamily: "'Inter', sans-serif" }}>
              Core Committee · मुख्य समिती
            </p>
            <h2 className="font-display text-3xl font-bold text-white mb-1">Founder Members</h2>
            <p className="text-xl" style={{ fontFamily: "'Tiro Devanagari Marathi', serif", color: "rgba(247,243,236,0.65)" }}>संस्थापक सदस्य</p>
            <div className="flex justify-center mt-5">
              <div style={{ width: "80px", height: "2px", background: "linear-gradient(90deg, transparent, #C8892A, transparent)" }} />
            </div>
          </div>

          {/* Founders grid */}
          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-7 gap-6 justify-items-center">
            {FOUNDERS.map((f, i) => (
              <div key={i} className="flex flex-col items-center text-center group">
                {/* Photo frame */}
                <div className="relative mb-4 transition-transform duration-300 group-hover:-translate-y-2"
                  style={{
                    width: "110px",
                    height: "110px",
                    borderRadius: "4px",
                    border: "2px solid rgba(200,137,42,0.35)",
                    padding: "3px",
                    background: "rgba(200,137,42,0.06)",
                    boxShadow: "0 4px 24px rgba(0,0,0,0.4)",
                  }}>
                  <div style={{ position: "relative", width: "100%", height: "100%", borderRadius: "2px", overflow: "hidden" }}>
                    <Image
                      src={f.photo}
                      alt={f.name}
                      fill
                      style={{ objectFit: "cover", objectPosition: "top" }}
                      sizes="110px"
                    />
                  </div>
                  {/* Gold corner accent */}
                  <div style={{ position: "absolute", top: "-2px", right: "-2px", width: "12px", height: "12px", borderTop: "2px solid #C8892A", borderRight: "2px solid #C8892A" }} />
                  <div style={{ position: "absolute", bottom: "-2px", left: "-2px", width: "12px", height: "12px", borderBottom: "2px solid #C8892A", borderLeft: "2px solid #C8892A" }} />
                </div>

                {/* Name */}
                <div className="font-display font-semibold text-white text-sm leading-tight mb-1">{f.name}</div>
                <div className="text-xs mb-1" style={{ fontFamily: "'Tiro Devanagari Marathi', serif", color: "rgba(247,243,236,0.6)" }}>{f.nameMarathi}</div>
                <div className="text-xs" style={{ color: "#C8892A", fontFamily: "'Inter', sans-serif" }}>{f.city}</div>
                {f.role === "Chief Promoter" && (
                  <div className="mt-1 px-2 py-0.5 text-xs"
                    style={{ background: "rgba(200,137,42,0.15)", color: "#E8A84A", border: "1px solid rgba(200,137,42,0.3)", fontFamily: "'Inter', sans-serif", fontSize: "0.6rem", letterSpacing: "0.05em" }}>
                    Chief Promoter
                  </div>
                )}
              </div>
            ))}
          </div>

          {/* Foundation note */}
          <div className="text-center mt-12">
            <div style={{ width: "60px", height: "1px", background: "rgba(200,137,42,0.3)", margin: "0 auto 16px" }} />
            <p className="text-sm" style={{ color: "rgba(247,243,236,0.4)", fontFamily: "'Inter', sans-serif" }}>
              DEEPER · Saad Manuskichi Foundation · Tumhi-Aamhi Palak
            </p>
          </div>
        </div>
      </section>

      {/* ── Brochure CTA banner ── */}
      <section className="py-14 px-6" style={{ background: "#1B3A2D", borderTop: "1px solid rgba(200,137,42,0.2)", borderBottom: "1px solid rgba(200,137,42,0.2)" }}>
        <div className="max-w-4xl mx-auto flex flex-col md:flex-row items-center justify-between gap-6">
          <div>
            <h3 className="font-display text-xl font-semibold text-white mb-1">Download the Club Deeper Brochure</h3>
            <p className="text-sm" style={{ fontFamily: "'Tiro Devanagari Marathi', serif", color: "rgba(247,243,236,0.6)" }}>
              क्लब डीपर माहितीपत्रक डाउनलोड करा
            </p>
            <p className="text-xs mt-1" style={{ color: "rgba(247,243,236,0.4)", fontFamily: "'Inter', sans-serif" }}>
              Version 1.0 · Akshayya Tritiya 19th April 2026 · 8 pages
            </p>
          </div>
          <a href="/ClubDeeper_Brochure.pdf" download="ClubDeeper_Brochure.pdf"
            className="flex-shrink-0 flex items-center gap-3 px-8 py-3 font-medium transition-all duration-300 hover:scale-105 hover:shadow-lg"
            style={{ background: "linear-gradient(135deg, #C8892A, #E8A84A)", color: "#fff", fontFamily: "'Inter', sans-serif", fontSize: "0.875rem", letterSpacing: "0.05em" }}>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
              <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/>
            </svg>
            Download PDF Brochure
          </a>
        </div>
      </section>

      {/* ── Footer ── */}
      <footer className="py-8 px-8" style={{ background: "#070F09", borderTop: "1px solid rgba(200,137,42,0.1)" }}>
        <div className="max-w-6xl mx-auto flex flex-col md:flex-row items-center justify-between gap-3">
          <div className="text-xs" style={{ color: "rgba(247,243,236,0.3)", fontFamily: "'Inter', sans-serif" }}>
            © 2026 Club Deeper LLP · 495, Narayan Peth, Balkrishna Apts., Pune 411 030
          </div>
          <div className="text-xs" style={{ color: "rgba(247,243,236,0.3)", fontFamily: "'Inter', sans-serif" }}>
            clubdeeper203@gmail.com · 777 000 6760 / 777 000 6860
          </div>
          <div className="text-xs" style={{ color: "rgba(247,243,236,0.2)", fontFamily: "'Inter', sans-serif" }}>
            Software by Eduval Pvt. Ltd.
          </div>
        </div>
      </footer>

      {/* ── Login Modal ── */}
      {showLogin && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4"
          style={{ background: "rgba(7,15,9,0.88)", backdropFilter: "blur(10px)" }}
          onClick={(e) => { if (e.target === e.currentTarget) { setShowLogin(false); setError(""); setPassword(""); } }}>
          <div className="w-full max-w-sm p-8 relative"
            style={{ background: "var(--parchment)", border: "1px solid rgba(200,137,42,0.3)", boxShadow: "0 40px 100px rgba(0,0,0,0.5)" }}>
            <button onClick={() => { setShowLogin(false); setError(""); setPassword(""); }}
              className="absolute top-4 right-4 text-lg opacity-40 hover:opacity-80 transition-opacity"
              style={{ color: "#1A1A1A" }}>✕</button>

            <div className="text-center mb-7">
              <div className="text-4xl mb-3">🌿</div>
              <h2 className="font-display text-xl font-semibold mb-1" style={{ color: "#1B3A2D" }}>Welcome</h2>
              <p style={{ fontFamily: "'Tiro Devanagari Marathi', serif", color: "#6B7565", fontSize: "1rem" }}>स्वागत आहे</p>
              <div className="flex justify-center mt-3">
                <div style={{ width: "40px", height: "1px", background: "#C8892A" }} />
              </div>
            </div>

            <form onSubmit={handleLogin}>
              <label className="block text-xs uppercase tracking-wider mb-2" style={{ color: "#6B7565", letterSpacing: "0.1em", fontFamily: "'Inter', sans-serif" }}>
                Access Password / पासवर्ड
              </label>
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Enter password"
                className="w-full px-4 py-3 text-sm outline-none mb-1"
                style={{
                  background: "white",
                  border: "1px solid var(--parchment-dark)",
                  borderBottom: error ? "2px solid #c0392b" : "2px solid #C8892A",
                  color: "#1A1A1A",
                  fontFamily: "'Inter', sans-serif",
                }}
                autoFocus
              />
              {error && <p className="text-xs mb-3" style={{ color: "#c0392b" }}>{error}</p>}
              {!error && <div className="mb-4" />}
              <button type="submit" disabled={loading}
                className="w-full py-3 text-sm font-medium tracking-wider transition-all duration-200 hover:opacity-90 disabled:opacity-50"
                style={{ background: "#1B3A2D", color: "white", letterSpacing: "0.08em", fontFamily: "'Inter', sans-serif" }}>
                {loading ? "Verifying..." : "Enter Portal →"}
              </button>
            </form>

            <p className="text-center text-xs mt-5" style={{ color: "#6B7565", opacity: 0.6, fontFamily: "'Inter', sans-serif" }}>
              Contact your coordinator for access
            </p>
          </div>
        </div>
      )}
    </main>
  );
}
