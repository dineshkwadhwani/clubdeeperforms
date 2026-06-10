# Club Deeper – Planning Platform

A two-part system for planning all 20 projects at Club Deeper Campus:

1. **forms-creator/** — Python script that creates 20 Google Forms (questionnaires) automatically via the Google Forms API
2. **webapp/** — Next.js web app (Vercel) that lists all projects and links to their Google Forms

---

## Folder Structure

```
clubdeeper/
├── forms-creator/
│   ├── create_forms.py      ← Run once to create all 20 Google Forms
│   ├── requirements.txt     ← Python dependencies
│   ├── setup.sh             ← One-time setup script (Mac)
│   ├── credentials.json     ← YOUR FILE – download from Google Cloud Console (not in git)
│   └── form_urls.json       ← Generated after running create_forms.py (copy to webapp)
└── webapp/                  ← Vercel web app (coming next)
```

---

## Step 1 – Run the Forms Creator

### Prerequisites
- Python 3.9+
- `credentials.json` downloaded from Google Cloud Console (see setup guide)

### One-time Setup
```bash
cd forms-creator
chmod +x setup.sh
./setup.sh
```

### Place your credentials file
Copy your downloaded `credentials.json` into the `forms-creator/` folder.

### Create all 20 Google Forms
```bash
python3 create_forms.py
```

- A browser window will open asking you to sign in to Google — sign in with the same Gmail account you used in Google Cloud Console
- The script will create all 20 forms in a Google Drive folder called **"Club Deeper Planning Forms"**
- A `form_urls.json` file will be generated with all form URLs

### First-time Google Auth
When you run the script for the first time, a browser window will open asking you to authorize the app. Click **"Continue"** (you may see a warning that the app is not verified — click "Advanced" then "Go to ClubDeeper Forms Builder (unsafe)" — this is safe as it's your own app).

---

## Step 2 – Web App (Coming Next)
The `webapp/` folder will contain a Next.js application that:
- Lists all 20 Club Deeper projects beautifully
- Links each project to its Google Form
- Shows response analytics from Google Sheets
- Deployed on Vercel

---

## Projects Covered (20 Forms)

| # | Project |
|---|---------|
| 1 | CBSE/State School (K12) |
| 2 | Coaching Center (NEET/JEE/CET) |
| 3 | Library |
| 4 | Study Center (UPSC/MPSC) |
| 5 | Skill Campus (25-30 Units) |
| 6 | Software Development Park |
| 7 | Old Age Home |
| 8 | Care Center |
| 9 | Hospital |
| 10 | Rural Development Center |
| 11 | Training Center |
| 12 | Cricket & Football Ground |
| 13 | Indoor Games Facility |
| 14 | Gymnasium & Swimming Pool |
| 15 | Residential Bungalow Complex |
| 16 | Clubhouse |
| 17 | Agriculture & Horticulture |
| 18 | Animal Husbandry |
| 19 | Campus Canteen & Food Services |
| 20 | Internal Roads & Campus Infrastructure |

---

## Important Notes
- `credentials.json` and `token.json` are in `.gitignore` — never commit them to GitHub
- All forms are in **English + Marathi** (bilingual)
- Each form is automatically linked to a Google Sheet for response collection
- `form_urls.json` contains both the public form URL and the edit URL for each form
