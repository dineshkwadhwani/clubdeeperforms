# Club Deeper – Claude Setup Instructions for New Mac

**For:** Claude AI Assistant  
**Purpose:** Setup and run Club Deeper Planning Platform on a new Mac machine  
**Project:** https://github.com/[your-repo] (clubdeeperforms)

---

## Quick Start Checklist

- [ ] User has cloned the repo to new Mac
- [ ] User has copied `credentials.json` from old machine to `forms-creator/` folder
- [ ] User has copied `token.json` from old machine to `forms-creator/` folder (if exists)
- [ ] User has copied `form_urls.json` from old machine to `webapp/` folder

---

## Part 1: Forms Creator Setup (Python)

### Step 1 – Verify Python & Install Dependencies
```bash
python3 --version  # Should be 3.9+
cd forms-creator
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 2 – Verify Credentials
- `credentials.json` must exist in `forms-creator/` folder
- This file was downloaded from Google Cloud Console (user's responsibility)
- If missing, ask user to provide it

### Step 3 – Test Forms Creator (Optional)
```bash
python3 create_forms.py
```
- This will open a browser for Google OAuth
- Will create/update Google Forms in "Club Deeper Planning Forms" folder
- Generates `form_urls.json` with all form URLs

### Step 4 – Copy form_urls.json to Webapp
```bash
cp form_urls.json ../webapp/
```

---

## Part 2: Webapp Setup (Next.js)

### Step 1 – Check Node.js
```bash
node --version  # Should be 18+
npm --version
```

### Step 2 – Install Dependencies
```bash
cd webapp
npm install
```

### Step 3 – Verify form_urls.json
- `webapp/form_urls.json` must exist (copied from forms-creator)
- If missing, generate it first from forms-creator

### Step 4 – Start Development Server
```bash
npm run dev
```
- Opens http://localhost:3000
- Hot reload enabled

### Step 5 – Test Authentication
- **User Login:** Username: `clubdeeper` + today's date in ddmmyyyy
  - Example: `clubdeeper22062026` (for 22 June 2026)
- **Admin Login:** Username: `dinesh` + today's date in ddmmyyyy
  - Example: `dinesh22062026` (for 22 June 2026)

---

## Project Structure

```
clubdeeperforms/
├── context.md                    ← Setup overview
├── credentials.json              ← REQUIRED (user's file, not in git)
├── README.md                     ← Project overview
├── forms-creator/
│   ├── batch1_education.py       ← Form templates
│   ├── batch2_skill.py
│   ├── batch3_social.py
│   ├── batch4_sports.py
│   ├── batch5_residential.py
│   ├── batch6_sustainability.py
│   ├── batch7_infrastructure.py
│   ├── core.py                   ← Core form creation logic
│   ├── create_forms.py           ← MAIN SCRIPT – run this
│   ├── update_projects.py        ← For updating existing forms
│   ├── requirements.txt          ← Python dependencies
│   ├── setup.sh                  ← Mac setup script
│   ├── credentials.json          ← REQUIRED (user's file)
│   ├── token.json                ← OPTIONAL (auto-generated after first run)
│   └── form_urls.json            ← GENERATED – copy to webapp
├── webapp/                       ← Next.js application
│   ├── package.json
│   ├── next.config.mjs
│   ├── tsconfig.json
│   ├── tailwind.config.js
│   ├── form_urls.json            ← REQUIRED (copy from forms-creator)
│   ├── app/
│   │   ├── layout.tsx            ← Root layout
│   │   ├── page.tsx              ← Homepage (bilingual)
│   │   ├── globals.css
│   │   ├── admin/
│   │   │   └── page.tsx          ← Admin panel
│   │   ├── dashboard/
│   │   │   └── page.tsx          ← User dashboard
│   │   └── api/
│   │       ├── auth/
│   │       │   └── route.ts      ← Date-based auth
│   │       └── config/
│   │           └── route.ts      ← Admin config
│   └── lib/
│       ├── auth.ts               ← Auth utilities
│       ├── projects.ts           ← Project data & utilities
│       └── store.ts              ← In-memory config store
```

---

## Critical Files (User Must Provide)

| File | Location | Purpose | From Old Mac |
|------|----------|---------|--------------|
| `credentials.json` | `forms-creator/` | Google API access | ✅ Required |
| `token.json` | `forms-creator/` | Google OAuth token | ✅ Optional (auto-gen) |
| `form_urls.json` | `webapp/` | Form URLs list | ✅ Required |

---

## Key Commands

### Forms Creator
```bash
cd forms-creator
source venv/bin/activate
python3 create_forms.py        # Create all 20 forms
python3 update_projects.py     # Update specific form
```

### Webapp
```bash
cd webapp
npm install                    # Install dependencies
npm run dev                    # Start dev server (localhost:3000)
npm run build                  # Build for production
npm start                      # Start production build
npm run lint                   # Run ESLint
```

---

## Authentication Details

### Date-Based Passwords
All passwords are date-based and reset daily. Format: `ddmmyyyy`

**Example for 22 June 2026:**
- User: `clubdeeper22062026`
- Admin: `dinesh22062026`

**Example for 10 December 2026:**
- User: `clubdeeper10122026`
- Admin: `dinesh10122026`

### How It Works
- No database required
- Passwords validated server-side in `app/api/auth/route.ts`
- Admin config stored in-memory (resets on server restart)

---

## Features to Test

1. **Homepage**
   - [ ] Loads bilingual content (English + Marathi)
   - [ ] Shows Sinhgad hill silhouette
   - [ ] Links to login pages

2. **User Dashboard**
   - [ ] Login with `clubdeeper` + today's date
   - [ ] See all 20 projects
   - [ ] Google Forms embedded in each project card
   - [ ] Forms load correctly

3. **Admin Panel**
   - [ ] Login with `dinesh` + today's date
   - [ ] See all projects with enable/disable toggle
   - [ ] Changes reflected immediately in dashboard
   - [ ] Config resets on page refresh (if server restarted)

---

## Troubleshooting

### Python Issues
```bash
# Venv not activated?
source forms-creator/venv/bin/activate

# Missing packages?
pip install -r forms-creator/requirements.txt

# Google API error?
- Check credentials.json exists in forms-creator/
- Ensure Google Forms API is enabled in Google Cloud Console
```

### Node.js Issues
```bash
# Port 3000 in use?
npm run dev -- -p 3001

# Missing form_urls.json?
- Generate it: python3 forms-creator/create_forms.py
- Copy it: cp forms-creator/form_urls.json webapp/

# Module not found?
rm -rf node_modules package-lock.json
npm install
```

### Authentication Issues
- Passwords are date-based (ddmmyyyy format)
- Example for today: Check current date, append to username
- Admin config resets on server restart (expected behavior)

---

## Deployment (Vercel)

When ready to deploy:

```bash
# Push to GitHub
git add .
git commit -m "Setup for new Mac"
git push

# On Vercel:
1. Connect GitHub repo
2. Set root directory to "webapp/"
3. Deploy (no env vars needed)
```

---

## Environment Info

- **macOS** (new machine)
- **Python:** 3.9+ required
- **Node.js:** 18+ required
- **VS Code:** Latest version

---

## Support Notes for Claude

1. **Read this file first** if setup issues occur
2. **Check critical files** exist before running scripts
3. **Verify dates** in authentication (passwords change daily)
4. **Check port conflicts** if `localhost:3000` doesn't work
5. **See context.md** for overall project overview

---

**Last Updated:** 22 June 2026  
**Maintainer:** Dinesh Wadhwani
