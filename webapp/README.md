# Club Deeper – Planning Portal (Web App)

Next.js 14 + Tailwind CSS web application for Club Deeper campus planning.

## Features
- Bilingual (English + Marathi) homepage with Sinhgad hill silhouette
- Date-based password authentication (no database needed)
- User dashboard with 20 project surveys (Google Forms embedded)
- Admin panel with project enable/disable configuration
- In-memory server-side config (resets on restart by design)

## Passwords
- **User**: `clubdeeper` + today's date in ddmmyyyy (e.g. `clubdeeper10062026`)
- **Admin**: `dinesh` + today's date in ddmmyyyy (e.g. `dinesh10062026`)

## Deploy on Vercel
1. Push this folder to GitHub
2. Connect repo to Vercel
3. Set root directory to `webapp/` (or deploy from root if you move files)
4. Deploy — no environment variables needed

## Local Development
```bash
npm install
npm run dev
```
Open http://localhost:3000
