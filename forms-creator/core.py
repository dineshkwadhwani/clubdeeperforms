"""
Club Deeper – Google Forms Creator v2
Shared core utilities used by all batch scripts.
"""

import os, json, time, sys
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = [
    "https://www.googleapis.com/auth/forms.body",
    "https://www.googleapis.com/auth/drive",
]

BASE_DIR    = os.path.dirname(os.path.abspath(__file__))
CREDS_FILE  = os.path.join(BASE_DIR, "credentials.json")
TOKEN_FILE  = os.path.join(BASE_DIR, "token.json")
URLS_FILE   = os.path.join(BASE_DIR, "form_urls.json")
FOLDER_NAME = "Club Deeper Planning Forms"

# ── Logging ──────────────────────────────────────────────────────────────────
def log(msg, level="INFO"):
    prefix = {"INFO": "  ✦", "OK": "  ✓", "ERR": "  ✗", "HEAD": "══"}
    print(f"{prefix.get(level,'  ')} {msg}", flush=True)

def banner(title):
    width = 62
    print("\n" + "═" * width, flush=True)
    print(f"  {title}", flush=True)
    print("═" * width, flush=True)

# ── Auth ─────────────────────────────────────────────────────────────────────
def get_credentials():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDS_FILE):
                print(f"\n✗  credentials.json not found at {CREDS_FILE}")
                print("   Download it from Google Cloud Console and place it here.\n")
                sys.exit(1)
            flow = InstalledAppFlow.from_client_secrets_file(CREDS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w") as t:
            t.write(creds.to_json())
    return creds

# ── Drive folder ─────────────────────────────────────────────────────────────
def get_or_create_folder(drive, name):
    q = f"name='{name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
    res = drive.files().list(q=q, fields="files(id,name)").execute()
    files = res.get("files", [])
    if files:
        return files[0]["id"]
    meta = {"name": name, "mimeType": "application/vnd.google-apps.folder"}
    f = drive.files().create(body=meta, fields="id").execute()
    return f["id"]

def move_to_folder(drive, file_id, folder_id):
    f = drive.files().get(fileId=file_id, fields="parents").execute()
    prev = ",".join(f.get("parents", []))
    drive.files().update(
        fileId=file_id,
        addParents=folder_id,
        removeParents=prev,
        fields="id,parents"
    ).execute()

# ── Form builder ─────────────────────────────────────────────────────────────
def build_requests(sections):
    """
    sections = list of dicts:
      { "title": str, "description": str (optional),
        "questions": [ { "en": str, "mr": str,
                         "type": "PARAGRAPH"|"TEXT"|"RADIO"|"CHECKBOX",
                         "options": [str] } ] }
    """
    requests = []
    idx = 0
    for sec in sections:
        requests.append({
            "createItem": {
                "item": {
                    "title": sec["title"],
                    "description": sec.get("description", ""),
                    "pageBreakItem": {}
                },
                "location": {"index": idx}
            }
        })
        idx += 1
        for q in sec["questions"]:
            title = f"{q['en']}  |  {q['mr']}"
            qtype = q.get("type", "PARAGRAPH")
            if qtype == "TEXT":
                qi = {"textQuestion": {"paragraph": False}}
            elif qtype == "PARAGRAPH":
                qi = {"textQuestion": {"paragraph": True}}
            elif qtype == "RADIO":
                qi = {"choiceQuestion": {"type": "RADIO",
                       "options": [{"value": o} for o in q.get("options", [])],
                       "shuffle": False}}
            elif qtype == "CHECKBOX":
                qi = {"choiceQuestion": {"type": "CHECKBOX",
                       "options": [{"value": o} for o in q.get("options", [])],
                       "shuffle": False}}
            else:
                qi = {"textQuestion": {"paragraph": True}}

            requests.append({
                "createItem": {
                    "item": {
                        "title": title,
                        "questionItem": {"question": {"required": False, **qi}}
                    },
                    "location": {"index": idx}
                }
            })
            idx += 1
    return requests

# ── Create one form ───────────────────────────────────────────────────────────
def create_form(forms, drive, folder_id, title, description, sections, delay=2.0):
    log(f"Creating: {title}")

    # 1. Create blank form
    form = forms.forms().create(body={"info": {"title": title, "documentTitle": title}}).execute()
    form_id = form["formId"]

    # 2. Set description
    forms.forms().batchUpdate(formId=form_id, body={"requests": [{
        "updateFormInfo": {"info": {"description": description}, "updateMask": "description"}
    }]}).execute()
    time.sleep(delay)

    # 3. Add questions in batches of 25
    all_reqs = build_requests(sections)
    total = len(all_reqs)
    batch_size = 25
    batches = [all_reqs[i:i+batch_size] for i in range(0, total, batch_size)]

    for bi, batch in enumerate(batches):
        log(f"  Batch {bi+1}/{len(batches)}  ({len(batch)} items)...")
        for attempt in range(3):
            try:
                forms.forms().batchUpdate(formId=form_id, body={"requests": batch}).execute()
                time.sleep(delay)
                break
            except HttpError as e:
                if e.resp.status == 429:
                    wait = 30 * (attempt + 1)
                    log(f"  Rate limited — waiting {wait}s...", "ERR")
                    time.sleep(wait)
                else:
                    raise

    # 4. Move to folder
    move_to_folder(drive, form_id, folder_id)
    time.sleep(1)

    view_url = f"https://docs.google.com/forms/d/{form_id}/viewform"
    edit_url = f"https://docs.google.com/forms/d/{form_id}/edit"
    log(f"  Done → {view_url}", "OK")
    return {"form_id": form_id, "view_url": view_url, "edit_url": edit_url}

# ── URL file merge ────────────────────────────────────────────────────────────
def load_urls():
    if os.path.exists(URLS_FILE):
        with open(URLS_FILE) as f:
            return {e["index"]: e for e in json.load(f)}
    return {}

def save_urls(url_map):
    entries = sorted(url_map.values(), key=lambda x: x["index"])
    with open(URLS_FILE, "w") as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)
    log(f"form_urls.json updated — {len(entries)} total entries", "OK")

def upsert_form(url_map, index, title, active, form_id, view_url, edit_url):
    url_map[index] = {
        "index": index,
        "title": title,
        "form_id": form_id,
        "view_url": view_url,
        "edit_url": edit_url,
        "active": active,
    }

# ── Batch runner ─────────────────────────────────────────────────────────────
def run_batch(batch_name, form_definitions):
    """
    form_definitions = list of:
      { "index": int, "title": str, "active": bool,
        "description": str, "sections": [...] }
    """
    banner(f"Club Deeper Forms v2  —  Batch: {batch_name.upper()}")
    log(f"Forms to create: {len(form_definitions)}")
    log(f"Delay between API calls: 2 seconds (safe mode)")

    if not os.path.exists(CREDS_FILE):
        log("credentials.json not found — aborting.", "ERR")
        sys.exit(1)

    log("Authenticating with Google...")
    creds = get_credentials()
    forms_svc = build("forms", "v1", credentials=creds)
    drive_svc = build("drive", "v3", credentials=creds)

    log(f"Getting/creating Drive folder: '{FOLDER_NAME}'...")
    folder_id = get_or_create_folder(drive_svc, FOLDER_NAME)
    log(f"Folder ID: {folder_id}", "OK")

    url_map = load_urls()
    results = []

    for i, fd in enumerate(form_definitions):
        banner(f"[{i+1}/{len(form_definitions)}]  {fd['title']}")
        try:
            info = create_form(
                forms_svc, drive_svc, folder_id,
                fd["title"], fd["description"], fd["sections"]
            )
            upsert_form(url_map, fd["index"], fd["title"], fd["active"],
                        info["form_id"], info["view_url"], info["edit_url"])
            save_urls(url_map)
            results.append({"index": fd["index"], "title": fd["title"], "status": "OK"})
        except Exception as e:
            log(f"FAILED: {e}", "ERR")
            results.append({"index": fd["index"], "title": fd["title"], "status": f"FAILED: {e}"})
        time.sleep(3)

    banner("BATCH COMPLETE")
    for r in results:
        status = "✓" if r["status"] == "OK" else "✗"
        print(f"  {status}  [{r['index']:02d}] {r['title']}")
    print()
    ok = sum(1 for r in results if r["status"] == "OK")
    log(f"{ok}/{len(results)} forms created successfully.")
    log(f"form_urls.json has been updated in: {URLS_FILE}")
    print()
