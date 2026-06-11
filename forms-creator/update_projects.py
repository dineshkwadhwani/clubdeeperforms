"""
Club Deeper – update_projects.py
Reads form_urls.json and patches lib/projects.ts with the new form URLs and active flags.

Run:  python3 update_projects.py
"""

import os, json, re, sys

BASE_DIR    = os.path.dirname(os.path.abspath(__file__))
URLS_FILE   = os.path.join(BASE_DIR, "form_urls.json")

# ── Auto-locate projects.ts ───────────────────────────────────────
def find_projects_ts():
    # Try common locations relative to this script
    candidates = [
        os.path.join(BASE_DIR, "..", "webapp", "lib", "projects.ts"),
        os.path.join(BASE_DIR, "webapp", "lib", "projects.ts"),
        os.path.join(BASE_DIR, "..", "lib", "projects.ts"),
    ]
    for c in candidates:
        if os.path.exists(c):
            return os.path.normpath(c)
    return None

def log(msg, level="INFO"):
    prefix = {"INFO": "  ✦", "OK": "  ✓", "ERR": "  ✗"}
    print(f"{prefix.get(level,'  ')} {msg}", flush=True)

# ─────────────────────────────────────────────────────────────────
def main():
    print("\n" + "═" * 62)
    print("  Club Deeper – update_projects.py")
    print("═" * 62)

    # 1. Load form_urls.json
    if not os.path.exists(URLS_FILE):
        log(f"form_urls.json not found at: {URLS_FILE}", "ERR")
        log("Run at least one batch script first to generate it.", "ERR")
        sys.exit(1)

    with open(URLS_FILE) as f:
        entries = json.load(f)

    log(f"Loaded {len(entries)} entries from form_urls.json")

    # 2. Find projects.ts
    ts_path = find_projects_ts()
    if not ts_path:
        log("Could not auto-locate webapp/lib/projects.ts", "ERR")
        log("Please enter the full path to projects.ts:", "ERR")
        ts_path = input("  Path: ").strip()
        if not os.path.exists(ts_path):
            log("File not found. Aborting.", "ERR")
            sys.exit(1)

    log(f"Found projects.ts at: {ts_path}")

    # 3. Read current projects.ts
    with open(ts_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 4. Build lookup dict from JSON: index → entry
    url_map = {e["index"]: e for e in entries}

    # 5. For each entry, patch form_id, view_url, edit_url, active in the TS block
    updated_count = 0
    missing = []

    for entry in entries:
        idx   = entry["index"]
        fid   = entry["form_id"]
        vurl  = entry["view_url"]
        eurl  = entry["edit_url"]
        activ = "true" if entry.get("active", False) else "false"

        # Find the block for this index using a pattern anchor
        # We match the index line and then replace the 4 fields below it
        # Strategy: replace each field line within the block for this index

        block_pattern = (
            r'(index:\s*' + str(idx) + r'.*?'
            r'form_id:\s*")[^"]*(".*?)'
            r'(view_url:\s*")[^"]*(".*?)'
            r'(edit_url:\s*")[^"]*(".*?)'
            r'(active:\s*)(?:true|false)'
        )

        replacement = (
            r'\g<1>' + fid   + r'\g<2>'
            r'\g<3>' + vurl  + r'\g<4>'
            r'\g<5>' + eurl  + r'\g<6>'
            r'\g<7>' + activ
        )

        new_content, n = re.subn(block_pattern, replacement, content, flags=re.DOTALL)

        if n > 0:
            content = new_content
            updated_count += 1
            log(f"[{idx:02d}] Updated  active={activ}  form_id={fid[:12]}...", "OK")
        else:
            missing.append(idx)
            log(f"[{idx:02d}] WARNING — could not patch (check projects.ts structure)", "ERR")

    # 6. Write back
    backup_path = ts_path + ".bak"
    with open(backup_path, "w", encoding="utf-8") as f:
        with open(ts_path, "r", encoding="utf-8") as orig:
            f.write(orig.read())

    with open(ts_path, "w", encoding="utf-8") as f:
        f.write(content)

    print()
    print("═" * 62)
    log(f"Updated {updated_count} of {len(entries)} projects in projects.ts", "OK")
    log(f"Backup saved to: {backup_path}", "OK")

    if missing:
        log(f"Could NOT patch indexes: {missing}", "ERR")
        log("Check the projects.ts structure for those indexes manually.", "ERR")

    print()
    log("Next steps:")
    log("  1. Open projects.ts and verify the updated URLs look correct")
    log("  2. Run:  npm run build  (inside webapp/ folder)")
    log("  3. Commit and push to GitHub → Vercel will auto-redeploy")
    print()

if __name__ == "__main__":
    main()
