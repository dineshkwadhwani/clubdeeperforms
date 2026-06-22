# Club Deeper – Planning Platform – Setup Context

**Last Updated:** 22 June 2026  
**Project Location:** `/Users/Dinesh.Wadhwani/Library/CloudStorage/OneDrive-NICELtd/Documents/Documents/Personal/TS/Git/clubdeeperforms`

---

## Project Overview

A two-part system for planning all 20 projects at Club Deeper Campus:

1. **forms-creator/** — Python script that creates 20 Google Forms automatically via Google Forms API
2. **webapp/** — Next.js web app (Vercel) that lists projects and links to Google Forms

---

## Key Files & Credentials

### Critical Files (Not in Git)
- `credentials.json` — Required for Google Forms API access (download from Google Cloud Console)
- `token.json` — Auto-generated after first auth with Google
- `form_urls.json` — Generated after running `create_forms.py` (copy to webapp)

### Important Directories
- `/forms-creator/` — Python automation scripts
- `/webapp/` — Next.js application (Vercel deployable)
- `/webapp/lib/` — Core utilities (auth.ts, projects.ts, store.ts)
- `/webapp/app/` — Next.js pages and API routes

---

## Setup for New Mac Machine

### 1. Prerequisites
- Python 3.9+
- Node.js 18+ (for webapp)
- Git
- Google Cloud account with Forms API enabled

### 2. Forms Creator Setup
```bash
cd forms-creator
chmod +x setup.sh
./setup.sh
```

### 3. Place Credentials
Copy your `credentials.json` from Google Cloud Console into `forms-creator/` folder.

### 4. Generate Google Forms
```bash
python3 create_forms.py
```
- Browser will open for Google sign-in
- Forms created in Google Drive folder: **"Club Deeper Planning Forms"**
- `form_urls.json` will be generated

### 5. Copy form_urls.json to Webapp
```bash
cp form_urls.json ../webapp/
```

### 6. Webapp Setup
```bash
cd webapp
npm install
npm run dev
```
Open http://localhost:3000

---

## Authentication

### User Login
- **Username:** `clubdeeper`
- **Password:** `clubdeeper` + today's date in ddmmyyyy format
  - Example: `clubdeeper10062026` (for 10 June 2026)

### Admin Login
- **Username:** `dinesh`
- **Password:** `dinesh` + today's date in ddmmyyyy format
  - Example: `dinesh10062026` (for 10 June 2026)

---

## Deployment

### Vercel Deployment
1. Push to GitHub
2. Connect repo to Vercel
3. Set root directory to `webapp/`
4. Deploy (no environment variables needed)

### Local Development
```bash
npm install
npm run dev
```

---

## Important Notes

- **No database** — Uses date-based password authentication, in-memory config
- **Admin config resets** on server restart (by design)
- **Bilingual support** — English + Marathi homepage
- **Google Forms API** — Requires valid credentials.json for forms-creator to work
- **form_urls.json** — Must be copied to webapp after forms are created

---

## Tech Stack

- **Forms Creator:** Python 3.9+
- **Web App:** Next.js 14, TypeScript, Tailwind CSS
- **Deployment:** Vercel
- **APIs:** Google Forms API, date-based auth
