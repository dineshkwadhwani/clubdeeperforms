"""
Club Deeper – Google Forms Creator
===================================
Creates 20 detailed planning questionnaires (English + Marathi) in Google Forms.
Each form is linked to a Google Sheet for response collection.
Run once; outputs form_urls.json for use in the Vercel web app.

Usage:
    python3 create_forms.py

Requirements:
    pip3 install -r requirements.txt
    Place your credentials.json in the same folder before running.
"""

import os
import json
import time
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# ── Auth scopes ──────────────────────────────────────────────────────────────
SCOPES = [
    "https://www.googleapis.com/auth/forms.body",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/spreadsheets",
]

CREDS_FILE  = os.path.join(os.path.dirname(__file__), "credentials.json")
TOKEN_FILE  = os.path.join(os.path.dirname(__file__), "token.json")
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "form_urls.json")
FOLDER_NAME = "Club Deeper Planning Forms"


def get_credentials():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w") as t:
            t.write(creds.to_json())
    return creds


def get_or_create_folder(drive_service, folder_name):
    q = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
    results = drive_service.files().list(q=q, fields="files(id,name)").execute()
    files = results.get("files", [])
    if files:
        return files[0]["id"]
    meta = {"name": folder_name, "mimeType": "application/vnd.google-apps.folder"}
    folder = drive_service.files().create(body=meta, fields="id").execute()
    return folder["id"]


def move_to_folder(drive_service, file_id, folder_id):
    f = drive_service.files().get(fileId=file_id, fields="parents").execute()
    prev = ",".join(f.get("parents", []))
    drive_service.files().update(
        fileId=file_id,
        addParents=folder_id,
        removeParents=prev,
        fields="id,parents"
    ).execute()


def create_linked_sheet(drive_service, sheets_service, form_id, title):
    """Create a Google Sheet and link it to the form for response collection."""
    sheet_meta = {"properties": {"title": f"{title} – Responses"}}
    sheet = sheets_service.spreadsheets().create(body=sheet_meta, fields="spreadsheetId").execute()
    sheet_id = sheet["spreadsheetId"]
    return sheet_id


def build_form_body(title, description, sections):
    """
    sections = list of {
        "title": str,
        "questions": list of {
            "text": str,          # English question
            "marathi": str,       # Marathi translation
            "type": "TEXT"|"PARAGRAPH"|"MULTIPLE_CHOICE"|"CHECKBOX",
            "options": [str]      # only for MULTIPLE_CHOICE / CHECKBOX
        }
    }
    Returns the form creation body + list of update requests.
    """
    form_body = {
        "info": {
            "title": title,
            "documentTitle": title,
        }
    }
    return form_body


def build_update_requests(sections):
    requests = []
    index = 0

    for sec in sections:
        # Section header
        requests.append({
            "createItem": {
                "item": {
                    "title": sec["title"],
                    "description": sec.get("description", ""),
                    "pageBreakItem": {}
                },
                "location": {"index": index}
            }
        })
        index += 1

        for q in sec["questions"]:
            combined_title = f"{q['text']}  |  {q['marathi']}"
            qtype = q.get("type", "PARAGRAPH")

            if qtype == "TEXT":
                question_item = {
                    "textQuestion": {"paragraph": False}
                }
            elif qtype == "PARAGRAPH":
                question_item = {
                    "textQuestion": {"paragraph": True}
                }
            elif qtype == "MULTIPLE_CHOICE":
                question_item = {
                    "choiceQuestion": {
                        "type": "RADIO",
                        "options": [{"value": o} for o in q.get("options", [])],
                        "shuffle": False
                    }
                }
            elif qtype == "CHECKBOX":
                question_item = {
                    "choiceQuestion": {
                        "type": "CHECKBOX",
                        "options": [{"value": o} for o in q.get("options", [])],
                        "shuffle": False
                    }
                }
            else:
                question_item = {"textQuestion": {"paragraph": True}}

            requests.append({
                "createItem": {
                    "item": {
                        "title": combined_title,
                        "questionItem": {
                            "question": {
                                "required": False,
                                **question_item
                            }
                        }
                    },
                    "location": {"index": index}
                }
            })
            index += 1

    return requests


def create_form(forms_service, drive_service, folder_id, title, description, sections):
    print(f"  Creating form: {title} ...")

    # Step 1: Create blank form
    form_body = {"info": {"title": title, "documentTitle": title}}
    form = forms_service.forms().create(body=form_body).execute()
    form_id = form["formId"]

    # Step 2: Add description via update
    desc_request = [{
        "updateFormInfo": {
            "info": {"description": description},
            "updateMask": "description"
        }
    }]
    forms_service.forms().batchUpdate(
        formId=form_id,
        body={"requests": desc_request}
    ).execute()

    # Step 3: Add all questions
    update_requests = build_update_requests(sections)
    if update_requests:
        # Send in batches of 30 to avoid API limits
        batch_size = 30
        for i in range(0, len(update_requests), batch_size):
            batch = update_requests[i:i+batch_size]
            forms_service.forms().batchUpdate(
                formId=form_id,
                body={"requests": batch}
            ).execute()
            time.sleep(0.5)

    # Step 4: Move to folder
    move_to_folder(drive_service, form_id, folder_id)

    form_url = f"https://docs.google.com/forms/d/{form_id}/viewform"
    edit_url = f"https://docs.google.com/forms/d/{form_id}/edit"
    print(f"    ✓ Done → {form_url}")
    return {"form_id": form_id, "view_url": form_url, "edit_url": edit_url}


# ══════════════════════════════════════════════════════════════════════════════
# ALL 20 QUESTIONNAIRES
# ══════════════════════════════════════════════════════════════════════════════

ALL_FORMS = []

# ── 1. CBSE / STATE SCHOOL ───────────────────────────────────────────────────
ALL_FORMS.append({
    "title": "Club Deeper – CBSE/State School (K12) Planning Questionnaire",
    "description": "Detailed planning questionnaire for the CBSE/State School project at Club Deeper Campus. Please answer all questions as thoroughly as possible.\n\nक्लब डीपर कॅम्पसमधील CBSE/राज्य शाळा प्रकल्पासाठी सविस्तर नियोजन प्रश्नावली.",
    "sections": [
        {
            "title": "Section 1: Vision & Identity | विभाग १: दृष्टी आणि ओळख",
            "questions": [
                {"text": "What is the proposed name of the school?", "marathi": "शाळेचे प्रस्तावित नाव काय आहे?", "type": "TEXT"},
                {"text": "What is the school's vision statement?", "marathi": "शाळेचे ध्येय वाक्य काय आहे?", "type": "PARAGRAPH"},
                {"text": "What affiliation is preferred – CBSE, State Board, or both?", "marathi": "कोणती संलग्नता अपेक्षित आहे – CBSE, राज्य मंडळ, किंवा दोन्ही?", "type": "MULTIPLE_CHOICE", "options": ["CBSE only", "State Board only", "Both CBSE and State Board", "To be decided"]},
                {"text": "What is the target student demographic – local rural, urban, NRI, or mixed?", "marathi": "लक्ष्यित विद्यार्थी वर्ग कोण आहे – स्थानिक ग्रामीण, शहरी, NRI, किंवा मिश्र?", "type": "MULTIPLE_CHOICE", "options": ["Local rural students", "Urban students", "NRI students", "Mixed / All of the above"]},
                {"text": "What pedagogy focus is intended? (STEM, Arts, Sports, Holistic, etc.)", "marathi": "शिक्षण पद्धतीचा केंद्रबिंदू काय असेल? (STEM, कला, क्रीडा, सर्वांगीण, इ.)", "type": "PARAGRAPH"},
                {"text": "What languages of instruction will be offered?", "marathi": "शिक्षणाचे माध्यम कोणते असेल?", "type": "CHECKBOX", "options": ["English", "Marathi", "Hindi", "Semi-English", "Bilingual (English + Marathi)"]},
                {"text": "What is the 5-year student strength target (year-wise)?", "marathi": "५ वर्षांचे विद्यार्थी संख्येचे लक्ष्य (वर्षनिहाय) काय आहे?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 2: Academic Structure | विभाग २: शैक्षणिक रचना",
            "questions": [
                {"text": "Which classes will be offered at launch?", "marathi": "सुरुवातीला कोणत्या इयत्ता सुरू होतील?", "type": "MULTIPLE_CHOICE", "options": ["Classes 1-12 from Day 1", "Classes 5-12 from Day 1", "Classes 1-8 first, then expand", "Classes 5-8 first, then expand"]},
                {"text": "How many sections per class? How many students per section?", "marathi": "प्रत्येक वर्गात किती तुकड्या? प्रत्येक तुकडीत किती विद्यार्थी?", "type": "TEXT"},
                {"text": "What streams will be offered at 11th–12th level?", "marathi": "११वी-१२वी साठी कोणते प्रवाह उपलब्ध असतील?", "type": "CHECKBOX", "options": ["Science (PCM)", "Science (PCB)", "Commerce", "Arts/Humanities", "Vocational", "All streams"]},
                {"text": "Will NEET/JEE/MHT-CET coaching be integrated with school timetable?", "marathi": "NEET/JEE/MHT-CET कोचिंग शाळेच्या वेळापत्रकात एकत्रित केले जाईल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, fully integrated", "Yes, as separate after-school program", "No, separate coaching center will handle it", "To be decided"]},
                {"text": "What is the academic calendar structure?", "marathi": "शैक्षणिक दिनदर्शिकेची रचना कशी असेल?", "type": "MULTIPLE_CHOICE", "options": ["Annual (one board exam)", "Semester system", "Trimester system", "Term-based (3 terms)"]},
                {"text": "Will school follow NEP 2020 framework from launch?", "marathi": "शाळा सुरुवातीपासून NEP 2020 अनुसरेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, from Day 1", "Transition in 2-3 years", "No, follow existing curriculum", "To be decided"]},
                {"text": "What optional/elective subjects will be offered at secondary level?", "marathi": "माध्यमिक स्तरावर कोणते वैकल्पिक विषय उपलब्ध असतील?", "type": "PARAGRAPH"},
                {"text": "Will there be provision for students with special educational needs?", "marathi": "विशेष शैक्षणिक गरजा असलेल्या विद्यार्थ्यांसाठी तरतूद असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, full inclusive education", "Yes, limited support", "No", "To be decided"]},
            ]
        },
        {
            "title": "Section 3: Infrastructure & Classrooms | विभाग ३: पायाभूत सुविधा आणि वर्गखोल्या",
            "questions": [
                {"text": "Total number of classrooms required at full capacity?", "marathi": "पूर्ण क्षमतेवर एकूण किती वर्गखोल्या लागतील?", "type": "TEXT"},
                {"text": "What is the preferred standard classroom size (in sq. ft.)?", "marathi": "मानक वर्गखोलीचा पसंतीचा आकार (चौ. फुटात) किती?", "type": "TEXT"},
                {"text": "Will all classrooms have smart boards / interactive displays from Day 1?", "marathi": "सर्व वर्गखोल्यांमध्ये पहिल्या दिवसापासून स्मार्ट बोर्ड असतील का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, all classrooms", "Phase 1: senior classes only", "Phase 2 onwards", "No"]},
                {"text": "Preferred ventilation type for classrooms?", "marathi": "वर्गखोल्यांसाठी पसंतीचे वायुवीजन?", "type": "MULTIPLE_CHOICE", "options": ["Natural cross-ventilation", "Ceiling fans only", "Air conditioning", "Hybrid (fans + AC for senior classes)"]},
                {"text": "How many science labs are needed? (Physics, Chemistry, Biology)", "marathi": "किती विज्ञान प्रयोगशाळा लागतील? (भौतिकशास्त्र, रसायनशास्त्र, जीवशास्त्र)", "type": "TEXT"},
                {"text": "How many computer labs are needed? How many seats per lab?", "marathi": "किती संगणक प्रयोगशाळा लागतील? प्रत्येकात किती जागा?", "type": "TEXT"},
                {"text": "Will there be a robotics/AI/coding lab?", "marathi": "रोबोटिक्स/AI/कोडिंग लॅब असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, from Day 1", "Phase 2 onwards", "No", "To be decided"]},
                {"text": "What sports facilities are required on the school plot?", "marathi": "शाळेच्या जागेवर कोणत्या क्रीडा सुविधा आवश्यक आहेत?", "type": "PARAGRAPH"},
                {"text": "Will there be an auditorium? Seating capacity?", "marathi": "सभागृह असेल का? बसण्याची क्षमता किती?", "type": "TEXT"},
            ]
        },
        {
            "title": "Section 4: Residential & Hostel | विभाग ४: निवासी सुविधा",
            "questions": [
                {"text": "What percentage of students will be residential vs. day scholars at launch?", "marathi": "सुरुवातीला किती टक्के विद्यार्थी निवासी विरुद्ध दिवस विद्यार्थी असतील?", "type": "TEXT"},
                {"text": "Preferred dormitory room type?", "marathi": "पसंतीचा वसतिगृह खोली प्रकार?", "type": "MULTIPLE_CHOICE", "options": ["2-bed rooms", "4-bed rooms", "6-bed rooms", "Mix of all types"]},
                {"text": "Will boys and girls hostels be in separate buildings?", "marathi": "मुला-मुलींचे वसतिगृह वेगळ्या इमारतींमध्ये असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, completely separate buildings", "Same building, separate floors", "Same building, separate wings", "To be decided"]},
                {"text": "What self-study/common facilities are needed in the hostel?", "marathi": "वसतिगृहात कोणत्या स्वयं-अध्ययन/सामान्य सुविधा आवश्यक आहेत?", "type": "CHECKBOX", "options": ["Self-study hall", "Common room with TV", "Indoor games room", "Wi-Fi throughout", "Laundry facility", "Canteen/tuck shop"]},
                {"text": "What is the warden arrangement? 24-hour coverage required?", "marathi": "पाळक व्यवस्था काय असेल? २४ तास उपस्थिती आवश्यक आहे का?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 5: Fees, Staffing & Operations | विभाग ५: शुल्क, कर्मचारी आणि संचालन",
            "questions": [
                {"text": "What is the target annual tuition fee range for Classes 5-10?", "marathi": "इयत्ता ५-१० साठी वार्षिक शिक्षण शुल्काचे लक्ष्य काय आहे?", "type": "TEXT"},
                {"text": "What is the target annual tuition fee range for Classes 11-12?", "marathi": "इयत्ता ११-१२ साठी वार्षिक शिक्षण शुल्काचे लक्ष्य काय आहे?", "type": "TEXT"},
                {"text": "What is the hostel fee per annum? What does it include?", "marathi": "वार्षिक वसतिगृह शुल्क किती? त्यात काय समाविष्ट आहे?", "type": "PARAGRAPH"},
                {"text": "What is the scholarship/concession policy?", "marathi": "शिष्यवृत्ती/सवलत धोरण काय आहे?", "type": "PARAGRAPH"},
                {"text": "What is the target teacher:student ratio?", "marathi": "शिक्षक:विद्यार्थी गुणोत्तर लक्ष्य काय आहे?", "type": "TEXT"},
                {"text": "How many resident teaching staff will need on-campus accommodation?", "marathi": "किती निवासी शिक्षण कर्मचाऱ्यांना कॅम्पसवर राहण्याची सोय लागेल?", "type": "TEXT"},
                {"text": "Will Deepa Coins be used for all student transactions on campus?", "marathi": "कॅम्पसवर सर्व विद्यार्थी व्यवहारांसाठी दीपा कॉईन्स वापरले जातील का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, exclusively", "Yes, with cash backup option", "No", "To be decided"]},
                {"text": "What is the target launch date / first academic session?", "marathi": "लक्ष्यित प्रारंभ तारीख / पहिले शैक्षणिक सत्र कोणते?", "type": "TEXT"},
                {"text": "Any other important requirements or comments for the school project?", "marathi": "शाळा प्रकल्पासाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा टिप्पण्या?", "type": "PARAGRAPH"},
            ]
        },
    ]
})

# ── 2. COACHING CENTER ───────────────────────────────────────────────────────
ALL_FORMS.append({
    "title": "Club Deeper – Coaching Center (NEET/JEE/CET) Planning Questionnaire",
    "description": "Detailed planning questionnaire for the Residential Coaching Center at Club Deeper Campus.\n\nक्लब डीपर कॅम्पसमधील निवासी कोचिंग सेंटरसाठी सविस्तर नियोजन प्रश्नावली.",
    "sections": [
        {
            "title": "Section 1: Vision & Target Exams | विभाग १: दृष्टी आणि लक्ष्य परीक्षा",
            "questions": [
                {"text": "Which competitive exams will the coaching center prepare students for?", "marathi": "कोचिंग सेंटर कोणत्या स्पर्धा परीक्षांसाठी विद्यार्थ्यांना तयार करेल?", "type": "CHECKBOX", "options": ["NEET (Medical)", "JEE Main", "JEE Advanced", "MHT-CET", "UPSC", "MPSC", "All of the above"]},
                {"text": "Will coaching be residential only or also open to day scholars?", "marathi": "कोचिंग केवळ निवासी असेल की दिवस विद्यार्थ्यांसाठीही खुले असेल?", "type": "MULTIPLE_CHOICE", "options": ["Residential only", "Day scholars only", "Both residential and day scholars", "To be decided"]},
                {"text": "Will this be integrated with the K12 school or a standalone center?", "marathi": "हे K12 शाळेशी एकत्रित असेल की स्वतंत्र केंद्र असेल?", "type": "MULTIPLE_CHOICE", "options": ["Fully integrated with school", "Separate standalone center", "Partially integrated", "To be decided"]},
                {"text": "What is the target student intake per year?", "marathi": "वर्षाला विद्यार्थी प्रवेशाचे लक्ष्य किती?", "type": "TEXT"},
                {"text": "What batch sizes are preferred for coaching?", "marathi": "कोचिंगसाठी पसंतीचे बॅच आकार किती?", "type": "MULTIPLE_CHOICE", "options": ["Small batches (20-25)", "Medium batches (30-40)", "Large batches (50+)", "Flexible based on subject"]},
            ]
        },
        {
            "title": "Section 2: Academic & Faculty | विभाग २: शैक्षणिक आणि शिक्षक वर्ग",
            "questions": [
                {"text": "What is the preferred teaching methodology for coaching?", "marathi": "कोचिंगसाठी पसंतीची शिक्षण पद्धती कोणती?", "type": "CHECKBOX", "options": ["Live classroom teaching", "Recorded video lectures", "Hybrid (live + recorded)", "One-on-one mentoring", "AI-based adaptive learning"]},
                {"text": "How many full-time faculty members are needed per stream (NEET/JEE/CET)?", "marathi": "प्रत्येक प्रवाहासाठी (NEET/JEE/CET) किती पूर्णवेळ शिक्षक लागतील?", "type": "TEXT"},
                {"text": "Will faculty be resident on campus?", "marathi": "शिक्षक कॅम्पसवर राहतील का?", "type": "MULTIPLE_CHOICE", "options": ["All faculty resident", "Some resident, some visiting", "All visiting faculty", "To be decided"]},
                {"text": "How many doubt-clearing sessions per week per subject?", "marathi": "प्रत्येक विषयासाठी आठवड्यात किती शंका-निरसन सत्रे?", "type": "TEXT"},
                {"text": "Will there be regular mock tests? How frequently?", "marathi": "नियमित सराव परीक्षा होतील का? किती वारंवार?", "type": "MULTIPLE_CHOICE", "options": ["Weekly", "Bi-weekly", "Monthly", "Before each major exam"]},
                {"text": "What study material will be provided – printed, digital, or both?", "marathi": "कोणते अभ्यास साहित्य दिले जाईल – मुद्रित, डिजिटल, किंवा दोन्ही?", "type": "MULTIPLE_CHOICE", "options": ["Printed only", "Digital only (tablets/e-books)", "Both printed and digital", "To be decided"]},
                {"text": "Will there be performance tracking and parent reporting system?", "marathi": "कामगिरी ट्रॅकिंग आणि पालक अहवाल प्रणाली असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, digital dashboard for parents", "Yes, monthly written reports", "Basic SMS/WhatsApp updates", "To be decided"]},
            ]
        },
        {
            "title": "Section 3: Infrastructure & Classrooms | विभाग ३: पायाभूत सुविधा",
            "questions": [
                {"text": "How many dedicated coaching classrooms are needed?", "marathi": "किती समर्पित कोचिंग वर्गखोल्या लागतील?", "type": "TEXT"},
                {"text": "What AV/technology setup is needed in each coaching classroom?", "marathi": "प्रत्येक कोचिंग वर्गखोलीत कोणती AV/तंत्रज्ञान व्यवस्था लागेल?", "type": "CHECKBOX", "options": ["Projector", "Smart board", "Recording setup (for video lectures)", "Good acoustics / soundproofing", "Individual student tablets", "High-speed Wi-Fi"]},
                {"text": "How many practice test halls are needed? Capacity each?", "marathi": "किती सराव परीक्षा हॉल लागतील? प्रत्येकाची क्षमता किती?", "type": "TEXT"},
                {"text": "Will there be a dedicated online test/CBT (Computer Based Test) lab?", "marathi": "समर्पित ऑनलाइन परीक्षा/CBT लॅब असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No", "Share with school computer lab", "To be decided"]},
                {"text": "What is the self-study hall requirement? Hours of operation?", "marathi": "स्वयं-अध्ययन हॉलची आवश्यकता काय आहे? कार्याचे तास किती?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 4: Residential & Welfare | विभाग ४: निवासी सुविधा आणि कल्याण",
            "questions": [
                {"text": "Will coaching students share hostel with school students or have separate hostel?", "marathi": "कोचिंग विद्यार्थी शाळेच्या विद्यार्थ्यांसोबत वसतिगृह सामायिक करतील का की स्वतंत्र असेल?", "type": "MULTIPLE_CHOICE", "options": ["Separate hostel block", "Shared with school students", "Separate floor in same building", "To be decided"]},
                {"text": "What stress management / mental health support will be provided?", "marathi": "तणाव व्यवस्थापन / मानसिक आरोग्य सहाय्य काय दिले जाईल?", "type": "PARAGRAPH"},
                {"text": "What is the daily schedule structure (wake up, study, meals, recreation)?", "marathi": "दैनंदिन वेळापत्रकाची रचना कशी असेल (उठणे, अभ्यास, जेवण, मनोरंजन)?", "type": "PARAGRAPH"},
                {"text": "Will mobile phones be allowed? What is the device policy?", "marathi": "मोबाइल फोनला परवानगी असेल का? उपकरण धोरण काय असेल?", "type": "MULTIPLE_CHOICE", "options": ["Phones allowed at all times", "Phones allowed only during recreation hours", "No personal phones, tablets provided", "Completely restricted"]},
                {"text": "What recreational facilities will be available for coaching students?", "marathi": "कोचिंग विद्यार्थ्यांसाठी कोणत्या मनोरंजन सुविधा उपलब्ध असतील?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 5: Fees & Administration | विभाग ५: शुल्क आणि प्रशासन",
            "questions": [
                {"text": "What is the target annual coaching fee (residential)?", "marathi": "वार्षिक कोचिंग शुल्काचे लक्ष्य (निवासी) किती?", "type": "TEXT"},
                {"text": "What is the target annual coaching fee (day scholar)?", "marathi": "वार्षिक कोचिंग शुल्काचे लक्ष्य (दिवस विद्यार्थी) किती?", "type": "TEXT"},
                {"text": "Will there be merit-based scholarships? Criteria?", "marathi": "गुणवत्तेवर आधारित शिष्यवृत्ती असेल का? निकष काय?", "type": "PARAGRAPH"},
                {"text": "What is the admission/selection process for coaching?", "marathi": "कोचिंगसाठी प्रवेश/निवड प्रक्रिया काय असेल?", "type": "PARAGRAPH"},
                {"text": "Any other important requirements or comments?", "marathi": "इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा टिप्पण्या?", "type": "PARAGRAPH"},
            ]
        },
    ]
})

# ── 3. LIBRARY ───────────────────────────────────────────────────────────────
ALL_FORMS.append({
    "title": "Club Deeper – Library Planning Questionnaire",
    "description": "Detailed planning questionnaire for the Campus Library at Club Deeper.\n\nक्लब डीपर कॅम्पस लायब्ररीसाठी सविस्तर नियोजन प्रश्नावली.",
    "sections": [
        {
            "title": "Section 1: Scope & Collections | विभाग १: व्याप्ती आणि संग्रह",
            "questions": [
                {"text": "Who will the library serve? (School students, coaching students, skill students, residents, public?)", "marathi": "लायब्ररी कोणाला सेवा देईल? (शाळा विद्यार्थी, कोचिंग विद्यार्थी, कौशल्य विद्यार्थी, रहिवासी, सार्वजनिक?)", "type": "CHECKBOX", "options": ["School students (5-12)", "Coaching students", "Skill campus students", "Residential families", "General public", "All of the above"]},
                {"text": "What is the target book collection at launch? At full capacity?", "marathi": "सुरुवातीला पुस्तक संग्रहाचे लक्ष्य किती? पूर्ण क्षमतेवर किती?", "type": "TEXT"},
                {"text": "What categories of books should be prioritized?", "marathi": "कोणत्या श्रेणीच्या पुस्तकांना प्राधान्य द्यावे?", "type": "CHECKBOX", "options": ["Academic textbooks", "Reference books", "Competitive exam books", "Fiction/Literature", "Marathi literature", "Children's books", "Research journals", "Newspapers & magazines"]},
                {"text": "Will there be a digital/e-library component?", "marathi": "डिजिटल/ई-लायब्ररी घटक असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, full e-library with digital terminals", "Yes, but only supplementary to physical", "No, physical books only", "To be decided"]},
                {"text": "Will the library subscribe to online databases (JSTOR, NCERT digital, etc.)?", "marathi": "लायब्ररी ऑनलाइन डेटाबेसची सदस्यता घेईल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No", "To be decided"]},
            ]
        },
        {
            "title": "Section 2: Infrastructure | विभाग २: पायाभूत सुविधा",
            "questions": [
                {"text": "What is the target seating capacity of the library?", "marathi": "लायब्ररीची लक्ष्यित बैठक क्षमता किती?", "type": "TEXT"},
                {"text": "Will there be a separate junior library for Classes 5-8?", "marathi": "इयत्ता ५-८ साठी स्वतंत्र कनिष्ठ लायब्ररी असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, separate room", "Yes, separate section within main library", "No, combined", "To be decided"]},
                {"text": "What spaces are needed inside the library?", "marathi": "लायब्ररीमध्ये कोणत्या जागा लागतील?", "type": "CHECKBOX", "options": ["Silent reading zone", "Group study rooms", "Librarian's desk & office", "Digital terminals area", "Newspaper/periodical section", "Audio-visual viewing area", "Story-telling corner for children", "Teacher resource room"]},
                {"text": "What book tracking system is preferred?", "marathi": "पुस्तक ट्रॅकिंग प्रणाली कोणती पसंत आहे?", "type": "MULTIPLE_CHOICE", "options": ["RFID-based", "Barcode-based", "Manual register", "Software-based (integrated with campus ERP)", "To be decided"]},
                {"text": "What are the operating hours of the library?", "marathi": "लायब्ररीचे कार्यालयीन तास कोणते असतील?", "type": "MULTIPLE_CHOICE", "options": ["School hours only (8am-5pm)", "Extended hours including evenings", "24/7 for residential students", "To be decided"]},
                {"text": "How many librarian/assistant staff are needed?", "marathi": "किती ग्रंथपाल/सहाय्यक कर्मचारी लागतील?", "type": "TEXT"},
            ]
        },
        {
            "title": "Section 3: Operations & Budget | विभाग ३: संचालन आणि बजेट",
            "questions": [
                {"text": "What is the estimated initial budget for books and setup?", "marathi": "पुस्तके आणि उभारणीसाठी अंदाजित प्रारंभिक बजेट किती?", "type": "TEXT"},
                {"text": "What is the annual budget for new book acquisitions?", "marathi": "नवीन पुस्तक खरेदीसाठी वार्षिक बजेट किती?", "type": "TEXT"},
                {"text": "Will library membership be included in school/hostel fees or charged separately?", "marathi": "लायब्ररी सदस्यत्व शाळा/वसतिगृह शुल्कात समाविष्ट असेल का की वेगळे आकारले जाईल?", "type": "MULTIPLE_CHOICE", "options": ["Included in school/hostel fees", "Separate nominal fee", "Free for all campus residents", "To be decided"]},
                {"text": "Will the library be open to the surrounding community or restricted to campus?", "marathi": "लायब्ररी आसपासच्या समुदायासाठी खुली असेल का की केवळ कॅम्पससाठी?", "type": "MULTIPLE_CHOICE", "options": ["Open to all", "Campus only", "Campus + paid community membership", "To be decided"]},
                {"text": "Any other important requirements or comments for the library?", "marathi": "लायब्ररीसाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा टिप्पण्या?", "type": "PARAGRAPH"},
            ]
        },
    ]
})

# ── 4. STUDY CENTER (UPSC/MPSC) ──────────────────────────────────────────────
ALL_FORMS.append({
    "title": "Club Deeper – Study Center (UPSC/MPSC) Planning Questionnaire",
    "description": "Detailed planning questionnaire for the UPSC/MPSC Study Center at Club Deeper Campus.\n\nक्लब डीपर कॅम्पसमधील UPSC/MPSC अभ्यास केंद्रासाठी सविस्तर नियोजन प्रश्नावली.",
    "sections": [
        {
            "title": "Section 1: Scope & Target Exams | विभाग १: व्याप्ती आणि लक्ष्य परीक्षा",
            "questions": [
                {"text": "Which exams will the study center focus on?", "marathi": "अभ्यास केंद्र कोणत्या परीक्षांवर लक्ष केंद्रित करेल?", "type": "CHECKBOX", "options": ["UPSC Civil Services", "MPSC State Services", "MPSC Group B/C", "Police Bharti", "Banking (IBPS/SBI)", "Staff Selection Commission (SSC)", "Defence (NDA/CDS)", "All competitive exams"]},
                {"text": "Will this center be residential, day-scholar, or both?", "marathi": "हे केंद्र निवासी, दिवस विद्यार्थी, किंवा दोन्ही असेल?", "type": "MULTIPLE_CHOICE", "options": ["Residential only", "Day scholars only", "Both", "To be decided"]},
                {"text": "What is the target student intake per batch?", "marathi": "प्रति बॅच विद्यार्थी प्रवेशाचे लक्ष्य किती?", "type": "TEXT"},
                {"text": "What is the primary target demographic for this center?", "marathi": "या केंद्रासाठी प्राथमिक लक्ष्य वर्ग कोण?", "type": "MULTIPLE_CHOICE", "options": ["Rural youth from Maharashtra", "Graduates from across India", "Economically weaker sections", "All aspirants regardless of background"]},
            ]
        },
        {
            "title": "Section 2: Academic Program | विभाग २: शैक्षणिक कार्यक्रम",
            "questions": [
                {"text": "What coaching programs will be offered (Foundation, Mains, Interview)?", "marathi": "कोणते कोचिंग कार्यक्रम उपलब्ध असतील (फाउंडेशन, मुख्य, मुलाखत)?", "type": "CHECKBOX", "options": ["Foundation/Prelims course", "Mains specific course", "Interview preparation", "Full integrated course (Prelims + Mains + Interview)", "Short-term crash courses"]},
                {"text": "Duration of each program?", "marathi": "प्रत्येक कार्यक्रमाचा कालावधी किती?", "type": "PARAGRAPH"},
                {"text": "Will there be dedicated Marathi medium batches for MPSC?", "marathi": "MPSC साठी समर्पित मराठी माध्यमाचे बॅच असतील का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No", "Both Marathi and English medium", "To be decided"]},
                {"text": "Guest lectures by IAS/IPS officers – planned?", "marathi": "IAS/IPS अधिकाऱ्यांकडून अतिथी व्याख्याने – नियोजित आहेत का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, regularly", "Yes, occasionally", "No", "To be decided"]},
                {"text": "Will answer writing practice be a structured part of the program?", "marathi": "उत्तरलेखन सराव कार्यक्रमाचा संरचित भाग असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, daily answer writing", "Yes, weekly", "No", "To be decided"]},
                {"text": "What current affairs resources will be provided?", "marathi": "कोणते चालू घडामोडी संसाधन उपलब्ध असतील?", "type": "CHECKBOX", "options": ["Daily newspaper reading sessions", "Curated current affairs notes", "Online current affairs platform", "Weekly current affairs tests", "Monthly magazines"]},
            ]
        },
        {
            "title": "Section 3: Infrastructure | विभाग ३: पायाभूत सुविधा",
            "questions": [
                {"text": "How many teaching/lecture rooms are needed?", "marathi": "किती शिक्षण/व्याख्यान कक्ष लागतील?", "type": "TEXT"},
                {"text": "What is the self-study room capacity needed?", "marathi": "स्वयं-अध्ययन कक्षाची आवश्यक क्षमता किती?", "type": "TEXT"},
                {"text": "Will the study center have its own dedicated library?", "marathi": "अभ्यास केंद्राची स्वतःची समर्पित लायब्ररी असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, separate library", "Shared with campus library", "Small reference room only", "To be decided"]},
                {"text": "24/7 study room access needed for residential students?", "marathi": "निवासी विद्यार्थ्यांसाठी २४/७ अभ्यास कक्ष प्रवेश आवश्यक आहे का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No, limited hours", "To be decided"]},
            ]
        },
        {
            "title": "Section 4: Fees & Social Impact | विभाग ४: शुल्क आणि सामाजिक प्रभाव",
            "questions": [
                {"text": "What is the target fee for residential UPSC/MPSC program (annual)?", "marathi": "निवासी UPSC/MPSC कार्यक्रमाचे लक्ष्यित शुल्क (वार्षिक) किती?", "type": "TEXT"},
                {"text": "Will subsidized/free seats be available for economically weaker students?", "marathi": "आर्थिकदृष्ट्या दुर्बल विद्यार्थ्यांसाठी अनुदानित/मुफ्त जागा उपलब्ध असतील का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, significant number of free seats", "Yes, partial subsidy", "No", "To be decided"]},
                {"text": "Will the center track and publish selection results?", "marathi": "केंद्र निवड निकाल मागोवा घेईल आणि प्रकाशित करेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No", "To be decided"]},
                {"text": "Any other important requirements or comments for the study center?", "marathi": "अभ्यास केंद्रासाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा टिप्पण्या?", "type": "PARAGRAPH"},
            ]
        },
    ]
})

# ── 5. SKILL CAMPUS ──────────────────────────────────────────────────────────
ALL_FORMS.append({
    "title": "Club Deeper – Skill Campus (25-30 Skill Units) Planning Questionnaire",
    "description": "Detailed planning questionnaire for the Skill Development Campus at Club Deeper.\n\nक्लब डीपर कौशल्य विकास कॅम्पससाठी सविस्तर नियोजन प्रश्नावली.",
    "sections": [
        {
            "title": "Section 1: Skill Units & Competencies | विभाग १: कौशल्य युनिट्स आणि क्षमता",
            "questions": [
                {"text": "List the 25-30 skill competencies planned. Which are highest priority for Phase 1?", "marathi": "नियोजित २५-३० कौशल्य क्षमता सांगा. टप्पा १ साठी कोणत्या सर्वोच्च प्राधान्याच्या आहेत?", "type": "PARAGRAPH"},
                {"text": "Which skill sectors will be covered?", "marathi": "कोणते कौशल्य क्षेत्र समाविष्ट केले जातील?", "type": "CHECKBOX", "options": ["Healthcare & Nursing", "IT & Software", "Construction & Plumbing", "Electrical & Electronics", "Agriculture & Horticulture", "Hospitality & Food Service", "Beauty & Wellness", "Retail & Logistics", "Automotive", "Handicrafts & Textiles", "Media & Entertainment", "Financial Services"]},
                {"text": "Will skill programs be aligned with National Skill Qualification Framework (NSQF)?", "marathi": "कौशल्य कार्यक्रम राष्ट्रीय कौशल्य पात्रता फ्रेमवर्क (NSQF) शी सुसंगत असतील का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, all programs NSQF aligned", "Some programs NSQF aligned", "No", "To be decided"]},
                {"text": "Will the campus seek Skill University affiliation?", "marathi": "कॅम्पस कौशल्य विद्यापीठ संलग्नता मिळवण्याचा प्रयत्न करेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, that is the long-term goal", "No", "Partner with existing skill university", "To be decided"]},
                {"text": "Will industry partnerships be established for each skill unit?", "marathi": "प्रत्येक कौशल्य युनिटसाठी उद्योग भागीदारी स्थापित केली जाईल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, mandatory for each unit", "Yes, for selected units", "No", "To be decided"]},
            ]
        },
        {
            "title": "Section 2: Student Profile & Admission | विभाग २: विद्यार्थी प्रोफाइल आणि प्रवेश",
            "questions": [
                {"text": "What is the minimum educational qualification for admission to skill programs?", "marathi": "कौशल्य कार्यक्रमांसाठी प्रवेशाची किमान शैक्षणिक पात्रता काय आहे?", "type": "MULTIPLE_CHOICE", "options": ["8th pass", "10th pass", "12th pass", "Varies by skill program", "No minimum qualification"]},
                {"text": "What is the target age range for skill students?", "marathi": "कौशल्य विद्यार्थ्यांसाठी लक्ष्यित वयोगट किती?", "type": "TEXT"},
                {"text": "Will the skill campus primarily serve rural youth?", "marathi": "कौशल्य कॅम्पस प्रामुख्याने ग्रामीण युवकांना सेवा देईल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, primarily rural focus", "Mix of rural and urban", "No specific preference", "To be decided"]},
                {"text": "Total capacity of skill campus students at full operation?", "marathi": "पूर्ण कार्यावर कौशल्य कॅम्पस विद्यार्थ्यांची एकूण क्षमता किती?", "type": "TEXT"},
                {"text": "Duration of each skill program (short course, 6-month, 1-year, 2-year)?", "marathi": "प्रत्येक कौशल्य कार्यक्रमाचा कालावधी (लघु कोर्स, ६ महिने, १ वर्ष, २ वर्षे)?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 3: Service Integration with Campus | विभाग ३: कॅम्पससह सेवा एकत्रीकरण",
            "questions": [
                {"text": "Which campus services will skill students provide as part of their training?", "marathi": "प्रशिक्षणाचा भाग म्हणून कौशल्य विद्यार्थी कोणत्या कॅम्पस सेवा पुरवतील?", "type": "CHECKBOX", "options": ["Canteen / food service", "Laundry", "Barber / beauty services", "Plumbing & electrical maintenance", "Gardening & horticulture", "IT support", "Healthcare assistance", "Construction & civil work", "Security", "All of the above"]},
                {"text": "Will skill students receive stipend for campus services rendered?", "marathi": "कॅम्पस सेवांसाठी कौशल्य विद्यार्थ्यांना भत्ता मिळेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, paid in Deepa Coins", "Yes, paid in cash", "No, it is part of training", "To be decided"]},
                {"text": "How will service quality from skill students be monitored?", "marathi": "कौशल्य विद्यार्थ्यांकडून सेवेची गुणवत्ता कशी तपासली जाईल?", "type": "PARAGRAPH"},
                {"text": "Will internships within the campus count toward certification?", "marathi": "कॅम्पसमधील इंटर्नशिप प्रमाणपत्रासाठी गणली जाईल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No", "To be decided"]},
            ]
        },
        {
            "title": "Section 4: Infrastructure & Placement | विभाग ४: पायाभूत सुविधा आणि नियुक्ती",
            "questions": [
                {"text": "How many training workshops/labs are needed for Phase 1?", "marathi": "टप्पा १ साठी किती प्रशिक्षण कार्यशाळा/लॅब लागतील?", "type": "TEXT"},
                {"text": "What equipment/tools list is needed for top 5 priority skill units?", "marathi": "शीर्ष ५ प्राधान्य कौशल्य युनिट्ससाठी उपकरणे/साधनांची यादी काय लागेल?", "type": "PARAGRAPH"},
                {"text": "Will there be a dedicated placement cell?", "marathi": "समर्पित नियुक्ती कक्ष असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No", "Shared with education division", "To be decided"]},
                {"text": "What is the target placement rate after skill program completion?", "marathi": "कौशल्य कार्यक्रम पूर्ण झाल्यानंतर लक्ष्यित नियुक्ती दर किती?", "type": "TEXT"},
                {"text": "Will there be entrepreneurship support for skill graduates?", "marathi": "कौशल्य पदवीधरांसाठी उद्योजकता सहाय्य असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, startup incubation", "Yes, micro-credit support", "No", "To be decided"]},
                {"text": "Any other important requirements or comments for the skill campus?", "marathi": "कौशल्य कॅम्पससाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा टिप्पण्या?", "type": "PARAGRAPH"},
            ]
        },
    ]
})

# ── 6. SOFTWARE DEVELOPMENT PARK ─────────────────────────────────────────────
ALL_FORMS.append({
    "title": "Club Deeper – Software Development Park Planning Questionnaire",
    "description": "Detailed planning questionnaire for the Software Development Park at Club Deeper Campus.\n\nक्लब डीपर सॉफ्टवेअर डेव्हलपमेंट पार्कसाठी सविस्तर नियोजन प्रश्नावली.",
    "sections": [
        {
            "title": "Section 1: Vision & Model | विभाग १: दृष्टी आणि मॉडेल",
            "questions": [
                {"text": "What is the primary purpose of the Software Development Park?", "marathi": "सॉफ्टवेअर डेव्हलपमेंट पार्कचा प्राथमिक उद्देश काय आहे?", "type": "MULTIPLE_CHOICE", "options": ["Training center for software skills", "Incubator for student startups", "Commercial IT workspace (co-working)", "All three combined", "To be decided"]},
                {"text": "Will it serve as the development center for Club Deeper's own ERP (Eduval)?", "marathi": "हे क्लब डीपरच्या स्वतःच्या ERP (Eduval) साठी विकास केंद्र म्हणून काम करेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No", "Partially", "To be decided"]},
                {"text": "Will external companies be invited to set up offices/teams here?", "marathi": "बाह्य कंपन्यांना येथे कार्यालये/टीम स्थापन करण्यासाठी आमंत्रित केले जाईल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, primary revenue model", "Yes, secondary", "No", "To be decided"]},
                {"text": "What technology domains will be focused on?", "marathi": "कोणत्या तंत्रज्ञान क्षेत्रांवर लक्ष केंद्रित केले जाईल?", "type": "CHECKBOX", "options": ["Web/Mobile Development", "AI & Machine Learning", "EdTech", "HealthTech", "AgriTech", "Cybersecurity", "Data Analytics", "No specific focus"]},
            ]
        },
        {
            "title": "Section 2: Infrastructure | विभाग २: पायाभूत सुविधा",
            "questions": [
                {"text": "What is the total seating/workstation capacity planned?", "marathi": "एकूण बैठक/वर्कस्टेशन क्षमता किती नियोजित आहे?", "type": "TEXT"},
                {"text": "What internet bandwidth is required (minimum)?", "marathi": "किमान इंटरनेट बँडविड्थ किती लागेल?", "type": "MULTIPLE_CHOICE", "options": ["100 Mbps", "500 Mbps", "1 Gbps", "Above 1 Gbps", "To be decided"]},
                {"text": "Will there be a dedicated server room / data center?", "marathi": "समर्पित सर्व्हर रूम / डेटा सेंटर असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, full on-premise data center", "Yes, small server room", "Cloud-only, no on-premise", "To be decided"]},
                {"text": "What meeting/collaboration rooms are needed?", "marathi": "कोणते बैठक/सहयोग कक्ष लागतील?", "type": "PARAGRAPH"},
                {"text": "Power backup requirement (UPS/generator) for the tech park?", "marathi": "टेक पार्कसाठी वीज बॅकअप (UPS/जनरेटर) आवश्यकता किती?", "type": "PARAGRAPH"},
                {"text": "Will the park operate 24/7?", "marathi": "पार्क २४/७ कार्य करेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, 24/7", "Standard business hours only", "Extended hours (7am-11pm)", "To be decided"]},
            ]
        },
        {
            "title": "Section 3: Training & Talent | विभाग ३: प्रशिक्षण आणि प्रतिभा",
            "questions": [
                {"text": "Will coding/software skills be taught to skill campus students here?", "marathi": "येथे कौशल्य कॅम्पस विद्यार्थ्यांना कोडिंग/सॉफ्टवेअर कौशल्ये शिकवली जातील का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No", "To be decided"]},
                {"text": "What certifications will students earn?", "marathi": "विद्यार्थी कोणती प्रमाणपत्रे मिळवतील?", "type": "PARAGRAPH"},
                {"text": "Will there be a startup incubation program?", "marathi": "स्टार्टअप इनक्युबेशन कार्यक्रम असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No", "Future phase", "To be decided"]},
                {"text": "What is the revenue model for the Software Development Park?", "marathi": "सॉफ्टवेअर डेव्हलपमेंट पार्कचे महसूल मॉडेल काय आहे?", "type": "PARAGRAPH"},
                {"text": "Any other important requirements or comments?", "marathi": "इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा टिप्पण्या?", "type": "PARAGRAPH"},
            ]
        },
    ]
})

# ── 7. OLD AGE HOME ──────────────────────────────────────────────────────────
ALL_FORMS.append({
    "title": "Club Deeper – Old Age Home Planning Questionnaire",
    "description": "Detailed planning questionnaire for the Old Age Home at Club Deeper Campus.\n\nक्लब डीपर कॅम्पसमधील वृद्धाश्रमासाठी सविस्तर नियोजन प्रश्नावली.",
    "sections": [
        {
            "title": "Section 1: Vision & Resident Profile | विभाग १: दृष्टी आणि रहिवासी प्रोफाइल",
            "questions": [
                {"text": "What is the vision for the old age home – luxury retirement, affordable care, or social service?", "marathi": "वृद्धाश्रमाची दृष्टी काय आहे – लक्झरी सेवानिवृत्ती, परवडणारी काळजी, की सामाजिक सेवा?", "type": "MULTIPLE_CHOICE", "options": ["Luxury/premium retirement community", "Mid-segment comfortable retirement", "Affordable / subsidized for needy elderly", "Mix of paid and subsidized", "To be decided"]},
                {"text": "What is the target capacity of the old age home?", "marathi": "वृद्धाश्रमाची लक्ष्यित क्षमता किती?", "type": "TEXT"},
                {"text": "What age group will be admitted?", "marathi": "कोणता वयोगट प्रवेश घेऊ शकेल?", "type": "TEXT"},
                {"text": "Will couples be accommodated together?", "marathi": "जोडप्यांना एकत्र राहण्याची सोय असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, couple rooms available", "No, individual rooms only", "Both options available", "To be decided"]},
                {"text": "Will the home accept residents with dementia / Alzheimer's?", "marathi": "वृद्धाश्रम स्मृतिभ्रंश / अल्झायमर रुग्णांना स्वीकारेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, with specialized memory care unit", "No, only physically healthy residents", "To be decided"]},
                {"text": "Is this integrated with the Club Deeper residential family community or separate?", "marathi": "हे क्लब डीपर निवासी कुटुंब समुदायाशी एकत्रित आहे की वेगळे?", "type": "MULTIPLE_CHOICE", "options": ["Integrated – elderly in same community", "Separate dedicated old age home building", "Both – some integrated, some separate", "To be decided"]},
            ]
        },
        {
            "title": "Section 2: Care & Medical Services | विभाग २: सेवा आणि वैद्यकीय सुविधा",
            "questions": [
                {"text": "What level of medical care will be provided on-site?", "marathi": "ऑन-साइट किती स्तराची वैद्यकीय सेवा दिली जाईल?", "type": "MULTIPLE_CHOICE", "options": ["Basic first aid only", "Nurse on duty 24/7", "Doctor on duty daily", "Full nursing home level care", "To be decided"]},
                {"text": "Will there be tie-up with the Club Deeper Hospital for emergency care?", "marathi": "आपत्कालीन सेवेसाठी क्लब डीपर रुग्णालयाशी करार असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No, self-sufficient medical unit", "To be decided"]},
                {"text": "What specialized care units are planned?", "marathi": "कोणत्या विशेष सेवा युनिट्सचे नियोजन आहे?", "type": "CHECKBOX", "options": ["Physiotherapy room", "Memory care / dementia unit", "Palliative care unit", "Yoga & wellness room", "Occupational therapy", "None – basic care only"]},
                {"text": "What daily care services will be provided?", "marathi": "कोणत्या दैनंदिन सेवा दिल्या जातील?", "type": "CHECKBOX", "options": ["Meals (3 times/day)", "Housekeeping", "Laundry", "Medication management", "Physiotherapy", "Recreational activities", "Transportation for medical visits", "All of the above"]},
                {"text": "How many care staff per resident is planned?", "marathi": "प्रति रहिवासी किती सेवा कर्मचारी नियोजित आहेत?", "type": "TEXT"},
            ]
        },
        {
            "title": "Section 3: Living Spaces | विभाग ३: राहण्याची जागा",
            "questions": [
                {"text": "What room types will be offered?", "marathi": "कोणते खोली प्रकार उपलब्ध असतील?", "type": "CHECKBOX", "options": ["Single room (independent)", "Double/shared room", "Studio apartment", "1BHK apartment", "Couple suite"]},
                {"text": "Will rooms be accessible for wheelchairs?", "marathi": "खोल्या व्हीलचेअरसाठी सुलभ असतील का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, all rooms", "Yes, some rooms", "No", "To be decided"]},
                {"text": "What common areas are planned?", "marathi": "कोणते सामायिक क्षेत्र नियोजित आहेत?", "type": "CHECKBOX", "options": ["Dining hall", "Garden / walking path", "Temple / prayer room", "Common TV/recreation room", "Library corner", "Activity room (crafts/yoga)", "Outdoor sitting areas"]},
                {"text": "Will there be intergenerational programs connecting elderly with campus students?", "marathi": "वृद्ध आणि कॅम्पस विद्यार्थ्यांना जोडणारे आंतरपीढी कार्यक्रम असतील का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, structured programs", "Yes, informal interactions", "No", "To be decided"]},
            ]
        },
        {
            "title": "Section 4: Fees & Sustainability | विभाग ४: शुल्क आणि टिकाऊपणा",
            "questions": [
                {"text": "What is the target monthly fee per resident?", "marathi": "प्रति रहिवासी लक्ष्यित मासिक शुल्क किती?", "type": "TEXT"},
                {"text": "Will there be a one-time entry/corpus deposit?", "marathi": "एकवेळ प्रवेश/कॉर्पस ठेव असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No", "Optional", "To be decided"]},
                {"text": "Will subsidized seats be available for economically weaker elderly?", "marathi": "आर्थिकदृष्ट्या दुर्बल वृद्धांसाठी अनुदानित जागा उपलब्ध असतील का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No", "CSR funded seats", "To be decided"]},
                {"text": "Any other important requirements or comments for the old age home?", "marathi": "वृद्धाश्रमासाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा टिप्पण्या?", "type": "PARAGRAPH"},
            ]
        },
    ]
})

# ── 8. CARE CENTER ───────────────────────────────────────────────────────────
ALL_FORMS.append({
    "title": "Club Deeper – Care Center Planning Questionnaire",
    "description": "Detailed planning questionnaire for the Care Center (toddlers, special needs, day care) at Club Deeper.\n\nक्लब डीपर केअर सेंटर (लहान मुले, विशेष गरजा, डे केअर) साठी सविस्तर नियोजन प्रश्नावली.",
    "sections": [
        {
            "title": "Section 1: Scope & Beneficiaries | विभाग १: व्याप्ती आणि लाभार्थी",
            "questions": [
                {"text": "Who will the care center serve?", "marathi": "केअर सेंटर कोणाला सेवा देईल?", "type": "CHECKBOX", "options": ["Toddlers (0-3 years)", "Pre-school children (3-5 years)", "Children with special needs", "Elderly (day care)", "Physically differently-abled individuals", "All of the above"]},
                {"text": "What is the target capacity for each beneficiary group?", "marathi": "प्रत्येक लाभार्थी गटासाठी लक्ष्यित क्षमता किती?", "type": "PARAGRAPH"},
                {"text": "Will this primarily serve families residing on campus?", "marathi": "हे प्रामुख्याने कॅम्पसवर राहणाऱ्या कुटुंबांना सेवा देईल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, campus families only", "Open to surrounding community too", "Both with priority to campus families", "To be decided"]},
                {"text": "Will it operate as a day care, residential care, or both?", "marathi": "हे डे केअर, निवासी काळजी, किंवा दोन्ही म्हणून कार्य करेल का?", "type": "MULTIPLE_CHOICE", "options": ["Day care only", "Residential care only", "Both", "To be decided"]},
            ]
        },
        {
            "title": "Section 2: Specialized Services | विभाग २: विशेष सेवा",
            "questions": [
                {"text": "What special needs categories will be catered to?", "marathi": "कोणत्या विशेष गरजा श्रेणी पूर्ण केल्या जातील?", "type": "CHECKBOX", "options": ["Autism Spectrum Disorder (ASD)", "Down Syndrome", "Cerebral Palsy", "Visual impairment", "Hearing impairment", "Learning disabilities", "Multiple disabilities", "All categories"]},
                {"text": "What therapies will be offered?", "marathi": "कोणत्या उपचारपद्धती उपलब्ध असतील?", "type": "CHECKBOX", "options": ["Speech therapy", "Occupational therapy", "Physiotherapy", "Behavioral therapy (ABA)", "Music therapy", "Art therapy", "None – basic care only"]},
                {"text": "Will there be a trained special educator on staff?", "marathi": "कर्मचारी वर्गात प्रशिक्षित विशेष शिक्षक असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, full-time", "Yes, part-time/visiting", "No", "To be decided"]},
                {"text": "What early childhood education program will be followed for toddlers?", "marathi": "लहान मुलांसाठी कोणता बालशिक्षण कार्यक्रम अनुसरला जाईल?", "type": "PARAGRAPH"},
                {"text": "Parent counseling and involvement – how will it be structured?", "marathi": "पालक समुपदेशन आणि सहभाग – ते कसे संरचित असेल?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 3: Infrastructure | विभाग ३: पायाभूत सुविधा",
            "questions": [
                {"text": "What spaces are needed in the care center?", "marathi": "केअर सेंटरमध्ये कोणत्या जागा लागतील?", "type": "CHECKBOX", "options": ["Play area (indoor)", "Play area (outdoor/sensory garden)", "Therapy rooms", "Sleeping/nap rooms", "Dining area", "Parent meeting room", "Medical/first aid room", "Staff room"]},
                {"text": "What safety features are non-negotiable?", "marathi": "कोणती सुरक्षा वैशिष्ट्ये अनिवार्य आहेत?", "type": "CHECKBOX", "options": ["CCTV in all rooms (accessible to parents)", "Padded flooring", "No sharp corners", "Secure entry/exit", "Allergy-safe environment", "24/7 staff coverage"]},
                {"text": "Caregiver to child ratio planned?", "marathi": "नियोजित काळजीवाहक ते मूल गुणोत्तर किती?", "type": "TEXT"},
            ]
        },
        {
            "title": "Section 4: Fees & Social Impact | विभाग ४: शुल्क आणि सामाजिक प्रभाव",
            "questions": [
                {"text": "What is the target monthly fee for day care services?", "marathi": "डे केअर सेवांसाठी लक्ष्यित मासिक शुल्क किती?", "type": "TEXT"},
                {"text": "Will services be subsidized for skill campus students' children?", "marathi": "कौशल्य कॅम्पस विद्यार्थ्यांच्या मुलांसाठी सेवा अनुदानित असतील का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No", "To be decided"]},
                {"text": "Any other important requirements or comments for the care center?", "marathi": "केअर सेंटरसाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा टिप्पण्या?", "type": "PARAGRAPH"},
            ]
        },
    ]
})

# ── 9. HOSPITAL ──────────────────────────────────────────────────────────────
ALL_FORMS.append({
    "title": "Club Deeper – Hospital Planning Questionnaire",
    "description": "Detailed planning questionnaire for the Hospital at Club Deeper Campus.\n\nक्लब डीपर कॅम्पसमधील रुग्णालयासाठी सविस्तर नियोजन प्रश्नावली.",
    "sections": [
        {
            "title": "Section 1: Vision & Scope | विभाग १: दृष्टी आणि व्याप्ती",
            "questions": [
                {"text": "What type of hospital is planned?", "marathi": "कोणत्या प्रकारचे रुग्णालय नियोजित आहे?", "type": "MULTIPLE_CHOICE", "options": ["Primary health center / clinic only", "Small hospital (20-50 beds)", "Medium hospital (50-100 beds)", "Full multi-specialty hospital (100+ beds)", "To be decided"]},
                {"text": "Who will the hospital primarily serve?", "marathi": "रुग्णालय प्रामुख्याने कोणाला सेवा देईल?", "type": "CHECKBOX", "options": ["Campus students", "Campus staff & families", "Residential bungalow community", "Old age home residents", "Surrounding rural villages", "General public"]},
                {"text": "What specialties will be offered?", "marathi": "कोणत्या विशेषता उपलब्ध असतील?", "type": "CHECKBOX", "options": ["General Medicine", "Pediatrics", "Orthopedics", "Gynecology & Obstetrics", "Cardiology", "Ophthalmology", "Dentistry", "Psychiatry & Mental Health", "Ayurveda/Naturopathy", "Emergency & Trauma"]},
                {"text": "Will it be a teaching hospital linked to the skill campus (nursing, paramedical)?", "marathi": "हे कौशल्य कॅम्पसशी (नर्सिंग, पॅरामेडिकल) जोडलेले शिक्षण रुग्णालय असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No", "Future phase", "To be decided"]},
                {"text": "Will there be a focus on rural health outreach programs?", "marathi": "ग्रामीण आरोग्य विस्तार कार्यक्रमांवर लक्ष केंद्रित असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, mobile health camps regularly", "Yes, periodic camps", "No", "To be decided"]},
            ]
        },
        {
            "title": "Section 2: Infrastructure & Departments | विभाग २: पायाभूत सुविधा आणि विभाग",
            "questions": [
                {"text": "How many inpatient beds are planned at launch?", "marathi": "सुरुवातीला किती आंतररुग्ण बेड नियोजित आहेत?", "type": "TEXT"},
                {"text": "What diagnostic facilities will be on-site?", "marathi": "ऑन-साइट कोणत्या निदान सुविधा असतील?", "type": "CHECKBOX", "options": ["Pathology lab", "Radiology (X-ray)", "Ultrasound", "CT Scan", "MRI", "ECG/Echo", "Pharmacy", "Blood bank"]},
                {"text": "Will there be an ICU / emergency ward?", "marathi": "ICU / आपत्कालीन वार्ड असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, full ICU", "Yes, basic emergency unit", "No", "To be decided"]},
                {"text": "How many operation theaters are needed?", "marathi": "किती शस्त्रक्रिया कक्ष लागतील?", "type": "TEXT"},
                {"text": "What is the OPD (outpatient) capacity needed per day?", "marathi": "दिवसाला किती OPD (बाह्यरुग्ण) क्षमता लागेल?", "type": "TEXT"},
                {"text": "Power backup requirement for hospital (critical for life support)?", "marathi": "रुग्णालयासाठी वीज बॅकअप आवश्यकता (जीवन समर्थनासाठी अत्यंत महत्त्वाचे)?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 3: Staffing & Fees | विभाग ३: कर्मचारी आणि शुल्क",
            "questions": [
                {"text": "How many full-time doctors are needed at launch?", "marathi": "सुरुवातीला किती पूर्णवेळ डॉक्टर लागतील?", "type": "TEXT"},
                {"text": "Will doctors be resident on campus?", "marathi": "डॉक्टर कॅम्पसवर राहतील का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, all resident", "Some resident, some visiting", "All visiting/OPD basis", "To be decided"]},
                {"text": "Will services be free for campus students and staff?", "marathi": "कॅम्पस विद्यार्थी आणि कर्मचाऱ्यांसाठी सेवा मुफ्त असतील का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, fully free", "Yes, heavily subsidized", "Only OPD free, procedures charged", "No, charged to all", "To be decided"]},
                {"text": "Will Deepa Coins be accepted for medical payments?", "marathi": "वैद्यकीय देयकांसाठी दीपा कॉईन्स स्वीकारले जातील का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No", "To be decided"]},
                {"text": "Will medical insurance be accepted? Which providers?", "marathi": "वैद्यकीय विमा स्वीकारला जाईल का? कोणते प्रदाते?", "type": "PARAGRAPH"},
                {"text": "Any other important requirements or comments for the hospital?", "marathi": "रुग्णालयासाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा टिप्पण्या?", "type": "PARAGRAPH"},
            ]
        },
    ]
})

# ── 10. RURAL DEVELOPMENT CENTER ─────────────────────────────────────────────
ALL_FORMS.append({
    "title": "Club Deeper – Rural Development Center Planning Questionnaire",
    "description": "Detailed planning questionnaire for the Rural Development Center at Club Deeper Campus.\n\nक्लब डीपर ग्रामीण विकास केंद्रासाठी सविस्तर नियोजन प्रश्नावली.",
    "sections": [
        {
            "title": "Section 1: Vision & Programs | विभाग १: दृष्टी आणि कार्यक्रम",
            "questions": [
                {"text": "What is the primary focus of the rural development center?", "marathi": "ग्रामीण विकास केंद्राचा प्राथमिक केंद्रबिंदू काय आहे?", "type": "CHECKBOX", "options": ["Farmer education & agri skills", "Women empowerment programs", "Village sanitation & water projects", "Digital literacy for rural youth", "Micro-enterprise development", "Health & nutrition awareness", "Panchayat/governance training", "All of the above"]},
                {"text": "Which villages/districts in the catchment area will be served?", "marathi": "सेवा क्षेत्रातील कोणती गावे/जिल्हे सेवा घेतील?", "type": "PARAGRAPH"},
                {"text": "Will the center work with government schemes (MGNREGA, PM Kisan, etc.)?", "marathi": "केंद्र सरकारी योजनांसह (MGNREGA, PM किसान, इ.) काम करेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, actively linked to government schemes", "Yes, help villagers access schemes", "No, independent programs only", "To be decided"]},
                {"text": "How many villages does the center aim to cover in Phase 1?", "marathi": "टप्पा १ मध्ये केंद्र किती गावे कव्हर करण्याचे लक्ष्य ठेवते?", "type": "TEXT"},
                {"text": "Will village immersion programs be included for campus students?", "marathi": "कॅम्पस विद्यार्थ्यांसाठी गाव विसर्जन कार्यक्रम समाविष्ट असतील का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, mandatory for all students", "Yes, optional", "No", "To be decided"]},
            ]
        },
        {
            "title": "Section 2: Operations & Outreach | विभाग २: संचालन आणि विस्तार",
            "questions": [
                {"text": "Will there be mobile outreach units to reach remote villages?", "marathi": "दुर्गम गावांपर्यंत पोहोचण्यासाठी मोबाइल विस्तार युनिट्स असतील का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No", "Future phase", "To be decided"]},
                {"text": "Will community radio / local media be used for outreach?", "marathi": "विस्तारासाठी सामुदायिक रेडिओ / स्थानिक माध्यमे वापरली जातील का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No", "To be decided"]},
                {"text": "What partnerships (NGO, government, corporate CSR) are planned?", "marathi": "कोणत्या भागीदारी (NGO, सरकार, कॉर्पोरेट CSR) नियोजित आहेत?", "type": "PARAGRAPH"},
                {"text": "How will impact be measured? (Metrics)", "marathi": "प्रभाव कसा मोजला जाईल? (मेट्रिक्स)", "type": "PARAGRAPH"},
                {"text": "What is the funding model – grants, CSR, campus cross-subsidy, or fee-based?", "marathi": "निधी मॉडेल काय आहे – अनुदान, CSR, कॅम्पस क्रॉस-सबसिडी, किंवा शुल्क-आधारित?", "type": "PARAGRAPH"},
                {"text": "Any other important requirements or comments for the rural development center?", "marathi": "ग्रामीण विकास केंद्रासाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा टिप्पण्या?", "type": "PARAGRAPH"},
            ]
        },
    ]
})

# ── 11. TRAINING CENTER ──────────────────────────────────────────────────────
ALL_FORMS.append({
    "title": "Club Deeper – Training Center Planning Questionnaire",
    "description": "Detailed planning questionnaire for the General Training Center at Club Deeper Campus.\n\nक्लब डीपर सामान्य प्रशिक्षण केंद्रासाठी सविस्तर नियोजन प्रश्नावली.",
    "sections": [
        {
            "title": "Section 1: Purpose & Audience | विभाग १: उद्देश आणि लक्ष्य वर्ग",
            "questions": [
                {"text": "What is the primary purpose of the training center?", "marathi": "प्रशिक्षण केंद्राचा प्राथमिक उद्देश काय आहे?", "type": "CHECKBOX", "options": ["Corporate training & workshops", "Teacher training (for campus staff)", "Leadership & management programs", "Entrepreneurship programs", "Government/municipal staff training", "NGO capacity building", "All of the above"]},
                {"text": "Who are the primary clients for the training center?", "marathi": "प्रशिक्षण केंद्रासाठी प्राथमिक ग्राहक कोण आहेत?", "type": "PARAGRAPH"},
                {"text": "Will the training center also host conferences and seminars?", "marathi": "प्रशिक्षण केंद्र परिषदा आणि चर्चासत्रे देखील आयोजित करेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, major revenue stream", "Yes, occasionally", "No", "To be decided"]},
                {"text": "What is the revenue model?", "marathi": "महसूल मॉडेल काय आहे?", "type": "MULTIPLE_CHOICE", "options": ["Fee-based (corporate clients pay)", "Government funded", "Hybrid model", "Non-profit / subsidized", "To be decided"]},
            ]
        },
        {
            "title": "Section 2: Infrastructure | विभाग २: पायाभूत सुविधा",
            "questions": [
                {"text": "How many training halls/rooms are needed? Capacity each?", "marathi": "किती प्रशिक्षण हॉल/खोल्या लागतील? प्रत्येकाची क्षमता किती?", "type": "TEXT"},
                {"text": "What is the main conference/seminar hall capacity needed?", "marathi": "मुख्य परिषद/चर्चासत्र हॉल क्षमता किती लागेल?", "type": "TEXT"},
                {"text": "What AV and technology setup is needed in training rooms?", "marathi": "प्रशिक्षण खोल्यांमध्ये कोणती AV आणि तंत्रज्ञान व्यवस्था लागेल?", "type": "PARAGRAPH"},
                {"text": "Will there be residential/accommodation for outstation training participants?", "marathi": "बाहेरगावाहून येणाऱ्या प्रशिक्षण सहभागींसाठी निवासाची व्यवस्था असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, dedicated guest rooms", "Shared with campus hostel", "No, participants arrange own stay", "To be decided"]},
                {"text": "Will the training center be shared with the Software Development Park?", "marathi": "प्रशिक्षण केंद्र सॉफ्टवेअर डेव्हलपमेंट पार्कशी सामायिक असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, shared facility", "No, separate building", "To be decided"]},
                {"text": "Any other important requirements or comments for the training center?", "marathi": "प्रशिक्षण केंद्रासाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा टिप्पण्या?", "type": "PARAGRAPH"},
            ]
        },
    ]
})

# ── 12. CRICKET & FOOTBALL GROUND ────────────────────────────────────────────
ALL_FORMS.append({
    "title": "Club Deeper – Cricket & Football Ground Planning Questionnaire",
    "description": "Detailed planning questionnaire for Cricket and Football facilities at Club Deeper Campus.\n\nक्लब डीपर क्रिकेट आणि फुटबॉल मैदानासाठी सविस्तर नियोजन प्रश्नावली.",
    "sections": [
        {
            "title": "Section 1: Scope & Standards | विभाग १: व्याप्ती आणि मानके",
            "questions": [
                {"text": "What standard of cricket ground is planned?", "marathi": "क्रिकेट मैदानाचे कोणते मानक नियोजित आहे?", "type": "MULTIPLE_CHOICE", "options": ["Full international-standard ground", "District/State level ground", "Practice ground with multiple pitches", "Basic recreational ground", "To be decided"]},
                {"text": "How many cricket practice pitches (nets) are planned?", "marathi": "किती क्रिकेट सराव खेळपट्ट्या (नेट्स) नियोजित आहेत?", "type": "TEXT"},
                {"text": "What pitch surface type is preferred?", "marathi": "खेळपट्टीचा कोणता पृष्ठभाग प्रकार पसंत आहे?", "type": "MULTIPLE_CHOICE", "options": ["Natural turf", "Synthetic/artificial turf", "Both – turf main + synthetic practice", "To be decided"]},
                {"text": "Will the football ground be FIFA standard or recreational?", "marathi": "फुटबॉल मैदान FIFA मानकाचे असेल की मनोरंजनाचे?", "type": "MULTIPLE_CHOICE", "options": ["FIFA standard (105m x 68m)", "Standard school/college level", "Recreational/informal", "To be decided"]},
                {"text": "Will lights/floodlights be installed for evening play?", "marathi": "संध्याकाळच्या खेळासाठी दिवे/फ्लडलाईट्स लावले जातील का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, full floodlights", "Yes, basic lighting", "No", "To be decided"]},
            ]
        },
        {
            "title": "Section 2: Facilities & Operations | विभाग २: सुविधा आणि संचालन",
            "questions": [
                {"text": "What player facilities are needed?", "marathi": "खेळाडूंसाठी कोणत्या सुविधा लागतील?", "type": "CHECKBOX", "options": ["Changing rooms (separate M/F)", "Showers", "Scoreboard (electronic)", "Spectator stands/seating", "Commentators box", "Equipment storage room", "Groundsman facility", "First aid room"]},
                {"text": "Will there be a coaching academy for cricket/football?", "marathi": "क्रिकेट/फुटबॉलसाठी कोचिंग अकादमी असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, full-time academy", "Yes, part-time/weekend", "No", "To be decided"]},
                {"text": "Will external teams be allowed to use the ground (revenue opportunity)?", "marathi": "बाह्य संघांना मैदान वापरण्याची परवानगी असेल का (महसूल संधी)?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No", "Yes, with priority to campus teams", "To be decided"]},
                {"text": "Will tournaments be hosted? What level?", "marathi": "स्पर्धा आयोजित केल्या जातील का? कोणत्या स्तराच्या?", "type": "PARAGRAPH"},
                {"text": "What is the expected annual maintenance budget for the grounds?", "marathi": "मैदानांसाठी अपेक्षित वार्षिक देखभाल बजेट किती?", "type": "TEXT"},
                {"text": "Any other important requirements or comments for sports grounds?", "marathi": "क्रीडा मैदानांसाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा टिप्पण्या?", "type": "PARAGRAPH"},
            ]
        },
    ]
})

# ── 13. INDOOR GAMES FACILITY ────────────────────────────────────────────────
ALL_FORMS.append({
    "title": "Club Deeper – Indoor Games Facility Planning Questionnaire",
    "description": "Detailed planning questionnaire for the Indoor Games Facility at Club Deeper Campus.\n\nक्लब डीपर इनडोअर गेम्स सुविधेसाठी सविस्तर नियोजन प्रश्नावली.",
    "sections": [
        {
            "title": "Section 1: Games & Sports | विभाग १: खेळ आणि क्रीडा",
            "questions": [
                {"text": "Which indoor sports/games will be accommodated?", "marathi": "कोणते इनडोअर क्रीडा/खेळ सामावले जातील?", "type": "CHECKBOX", "options": ["Badminton", "Table Tennis", "Squash", "Basketball (indoor)", "Volleyball (indoor)", "Carrom", "Chess", "Billiards/Snooker", "Boxing/Martial Arts", "Gymnastics", "Wrestling", "All of the above"]},
                {"text": "How many badminton courts are needed?", "marathi": "किती बॅडमिंटन कोर्ट लागतील?", "type": "TEXT"},
                {"text": "How many table tennis tables are needed?", "marathi": "किती टेबल टेनिस टेबल लागतील?", "type": "TEXT"},
                {"text": "Will the facility be used for competitive tournaments or recreational only?", "marathi": "सुविधा स्पर्धात्मक स्पर्धांसाठी वापरली जाईल की केवळ मनोरंजनासाठी?", "type": "MULTIPLE_CHOICE", "options": ["Both competitive and recreational", "Competitive primarily", "Recreational only", "To be decided"]},
                {"text": "Will the indoor hall be multi-purpose (events, exams, ceremonies also)?", "marathi": "इनडोअर हॉल बहुउद्देशीय (कार्यक्रम, परीक्षा, समारंभ) असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, fully multi-purpose", "Yes, but primarily for sports", "No, sports only", "To be decided"]},
            ]
        },
        {
            "title": "Section 2: Infrastructure | विभाग २: पायाभूत सुविधा",
            "questions": [
                {"text": "What is the total area needed for the indoor sports facility?", "marathi": "इनडोअर क्रीडा सुविधेसाठी एकूण क्षेत्रफळ किती लागेल?", "type": "TEXT"},
                {"text": "What flooring is required for which sport?", "marathi": "कोणत्या खेळासाठी कोणता फ्लोअरिंग आवश्यक आहे?", "type": "PARAGRAPH"},
                {"text": "Will spectator seating be provided?", "marathi": "प्रेक्षक बैठक उपलब्ध असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, permanent seating", "Yes, retractable/foldable", "No seating needed", "To be decided"]},
                {"text": "What ventilation/climate control is needed?", "marathi": "कोणते वायुवीजन/हवामान नियंत्रण लागेल?", "type": "MULTIPLE_CHOICE", "options": ["Natural ventilation only", "Fans + natural ventilation", "Full air conditioning", "Evaporative cooling", "To be decided"]},
                {"text": "Will there be a sports store / equipment room?", "marathi": "क्रीडा भांडार / उपकरण कक्ष असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No", "To be decided"]},
                {"text": "Any other important requirements or comments?", "marathi": "इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा टिप्पण्या?", "type": "PARAGRAPH"},
            ]
        },
    ]
})

# ── 14. GYMNASIUM & SWIMMING POOL ────────────────────────────────────────────
ALL_FORMS.append({
    "title": "Club Deeper – Gymnasium & Swimming Pool Planning Questionnaire",
    "description": "Detailed planning questionnaire for the Gymnasium and Swimming Pool at Club Deeper Campus.\n\nक्लब डीपर जिम्नॅशियम आणि जलतरण तलावासाठी सविस्तर नियोजन प्रश्नावली.",
    "sections": [
        {
            "title": "Section 1: Swimming Pool | विभाग १: जलतरण तलाव",
            "questions": [
                {"text": "What size swimming pool is planned?", "marathi": "कोणत्या आकाराचा जलतरण तलाव नियोजित आहे?", "type": "MULTIPLE_CHOICE", "options": ["Olympic size (50m)", "Semi-Olympic (25m)", "Recreational pool (15-20m)", "Both a competition pool and a learner pool", "To be decided"]},
                {"text": "Will there be a separate shallow pool for beginners/children?", "marathi": "नवशिक्यांसाठी/मुलांसाठी स्वतंत्र उथळ तलाव असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No", "To be decided"]},
                {"text": "Indoor or outdoor pool?", "marathi": "इनडोअर किंवा आउटडोअर तलाव?", "type": "MULTIPLE_CHOICE", "options": ["Indoor (covered)", "Outdoor (open)", "Both", "To be decided"]},
                {"text": "Will there be a swimming coaching program?", "marathi": "जलतरण कोचिंग कार्यक्रम असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, structured program for all ages", "Yes, for school students only", "No", "To be decided"]},
                {"text": "Who will have access to the pool?", "marathi": "तलावात कोणाला प्रवेश असेल?", "type": "CHECKBOX", "options": ["School students", "Coaching center students", "Skill campus students", "Residential families / bungalow owners", "General public (paid)", "All"]},
                {"text": "What safety and hygiene systems are required?", "marathi": "कोणती सुरक्षा आणि स्वच्छता प्रणाली आवश्यक आहे?", "type": "CHECKBOX", "options": ["Lifeguard 24/7 when pool is open", "Automated chlorination", "Water quality monitoring system", "CCTV", "Anti-slip flooring", "Pool cover"]},
            ]
        },
        {
            "title": "Section 2: Gymnasium | विभाग २: जिम्नॅशियम",
            "questions": [
                {"text": "Who will the gymnasium serve?", "marathi": "जिम्नॅशियम कोणाला सेवा देईल?", "type": "CHECKBOX", "options": ["Students (all)", "Campus staff", "Residential families", "General public (paid membership)", "All of the above"]},
                {"text": "What is the target capacity (simultaneous users)?", "marathi": "एकाच वेळी वापरकर्त्यांची लक्ष्यित क्षमता किती?", "type": "TEXT"},
                {"text": "What equipment categories are planned?", "marathi": "कोणत्या उपकरण श्रेणी नियोजित आहेत?", "type": "CHECKBOX", "options": ["Cardio machines (treadmill, cycle, elliptical)", "Free weights (dumbbells, barbells)", "Weight training machines", "Functional training area", "Stretching/yoga area", "CrossFit/functional fitness zone"]},
                {"text": "Will there be a certified personal trainer/fitness instructor on staff?", "marathi": "कर्मचारी वर्गात प्रमाणित वैयक्तिक प्रशिक्षक/फिटनेस प्रशिक्षक असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, full-time", "Yes, part-time", "No", "To be decided"]},
                {"text": "Will yoga/meditation sessions be conducted in or near the gymnasium?", "marathi": "जिम्नॅशियममध्ये किंवा जवळ योग/ध्यान सत्रे आयोजित केली जातील का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, daily sessions", "Yes, weekly", "No, separate yoga hall", "To be decided"]},
                {"text": "What is the membership/access fee structure planned?", "marathi": "नियोजित सदस्यत्व/प्रवेश शुल्क रचना काय आहे?", "type": "PARAGRAPH"},
                {"text": "Any other important requirements or comments for gym and pool?", "marathi": "जिम आणि तलावासाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा टिप्पण्या?", "type": "PARAGRAPH"},
            ]
        },
    ]
})

# ── 15. RESIDENTIAL BUNGALOW COMPLEX ─────────────────────────────────────────
ALL_FORMS.append({
    "title": "Club Deeper – Residential Bungalow Complex Planning Questionnaire",
    "description": "Detailed planning questionnaire for the Residential Bungalow Complex at Club Deeper.\n\nक्लब डीपर निवासी बंगला संकुलासाठी सविस्तर नियोजन प्रश्नावली.",
    "sections": [
        {
            "title": "Section 1: Product & Pricing | विभाग १: उत्पादन आणि किंमत",
            "questions": [
                {"text": "What is the target number of bungalow plots in Phase 1?", "marathi": "टप्पा १ मध्ये बंगला भूखंडांची लक्ष्यित संख्या किती?", "type": "TEXT"},
                {"text": "What is the standard plot size (sq. ft.)?", "marathi": "मानक भूखंड आकार (चौ. फुट) किती?", "type": "TEXT"},
                {"text": "What is the target price per plot (Phase 1)?", "marathi": "टप्पा १ साठी प्रति भूखंड लक्ष्यित किंमत किती?", "type": "TEXT"},
                {"text": "What is included in the plot price?", "marathi": "भूखंडाच्या किंमतीत काय समाविष्ट आहे?", "type": "CHECKBOX", "options": ["Road access", "Water connection", "Electricity connection", "Sewer line", "Boundary wall (plot)", "Free FSI / building permission", "Clubhouse membership", "All of the above"]},
                {"text": "Will buyers be able to construct their own bungalow or use a standard design?", "marathi": "खरेदीदार स्वतःचा बंगला बांधू शकतात का किंवा मानक डिझाइन वापरावे लागेल?", "type": "MULTIPLE_CHOICE", "options": ["Own design with architect approval", "Only standard designs from Club Deeper", "Choice of pre-approved designs", "To be decided"]},
                {"text": "Who is the target buyer profile?", "marathi": "लक्ष्यित खरेदीदार प्रोफाइल कोण आहे?", "type": "CHECKBOX", "options": ["DEEPER Foundation members", "Education community professionals", "NRI buyers", "HNI investors", "Retired professionals", "Anyone interested"]},
            ]
        },
        {
            "title": "Section 2: Community & Amenities | विभाग २: समुदाय आणि सुविधा",
            "questions": [
                {"text": "What community facilities will be exclusive to bungalow residents?", "marathi": "बंगला रहिवाशांसाठी कोणत्या समुदाय सुविधा विशेष असतील?", "type": "CHECKBOX", "options": ["Dedicated clubhouse", "Swimming pool access", "Gymnasium access", "Children's play area", "Community garden", "Security (gated)", "All campus amenities"]},
                {"text": "Will there be a residents' association / RWA?", "marathi": "रहिवासी संघटना / RWA असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No", "To be decided"]},
                {"text": "What is the annual maintenance charge (AMC) structure?", "marathi": "वार्षिक देखभाल शुल्क (AMC) रचना काय आहे?", "type": "TEXT"},
                {"text": "Will domestic help (via skill campus students) be available for bungalow residents?", "marathi": "बंगला रहिवाशांसाठी (कौशल्य कॅम्पस विद्यार्थ्यांमार्फत) घरगुती मदत उपलब्ध असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No", "To be decided"]},
                {"text": "What security arrangements are planned for the bungalow complex?", "marathi": "बंगला संकुलासाठी कोणती सुरक्षा व्यवस्था नियोजित आहे?", "type": "PARAGRAPH"},
                {"text": "Any other important requirements or comments for the bungalow complex?", "marathi": "बंगला संकुलासाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा टिप्पण्या?", "type": "PARAGRAPH"},
            ]
        },
    ]
})

# ── 16. CLUBHOUSE ────────────────────────────────────────────────────────────
ALL_FORMS.append({
    "title": "Club Deeper – Clubhouse Planning Questionnaire",
    "description": "Detailed planning questionnaire for the Clubhouse at Club Deeper Campus.\n\nक्लब डीपर क्लबहाऊससाठी सविस्तर नियोजन प्रश्नावली.",
    "sections": [
        {
            "title": "Section 1: Concept & Membership | विभाग १: संकल्पना आणि सदस्यत्व",
            "questions": [
                {"text": "What is the overall concept for the clubhouse?", "marathi": "क्लबहाऊसची एकूण संकल्पना काय आहे?", "type": "MULTIPLE_CHOICE", "options": ["Premium social club for bungalow residents only", "Multi-access club for all campus community", "Revenue-generating commercial club open to public", "Mix of exclusive and open access", "To be decided"]},
                {"text": "What membership categories are planned?", "marathi": "कोणत्या सदस्यत्व श्रेण्या नियोजित आहेत?", "type": "PARAGRAPH"},
                {"text": "What is the target number of club members?", "marathi": "क्लब सदस्यांची लक्ष्यित संख्या किती?", "type": "TEXT"},
                {"text": "What is the membership fee structure (one-time + annual)?", "marathi": "सदस्यत्व शुल्क रचना काय आहे (एकवेळ + वार्षिक)?", "type": "TEXT"},
                {"text": "Will Deepa Coins be the primary payment inside the clubhouse?", "marathi": "क्लबहाऊसमध्ये दीपा कॉईन्स प्राथमिक देयक असतील का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No", "Optional", "To be decided"]},
            ]
        },
        {
            "title": "Section 2: Facilities & Spaces | विभाग २: सुविधा आणि जागा",
            "questions": [
                {"text": "What F&B (food and beverage) facilities are planned in the clubhouse?", "marathi": "क्लबहाऊसमध्ये कोणत्या F&B (अन्न आणि पेय) सुविधा नियोजित आहेत?", "type": "CHECKBOX", "options": ["Fine dining restaurant", "Casual café/lounge", "Bar (with/without liquor license)", "Outdoor terrace dining", "Private dining rooms", "Banquet hall"]},
                {"text": "What recreational spaces are planned?", "marathi": "कोणते मनोरंजन स्थळ नियोजित आहेत?", "type": "CHECKBOX", "options": ["Lounge/reading room", "Indoor games (cards, chess, billiards)", "Kids play area", "Spa & wellness zone", "Rooftop/outdoor deck", "Screening room/mini theatre"]},
                {"text": "Will the clubhouse be available for private event bookings?", "marathi": "क्लबहाऊस खाजगी कार्यक्रम बुकिंगसाठी उपलब्ध असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No", "Members only", "To be decided"]},
                {"text": "What is the banquet/event hall capacity?", "marathi": "मेजवानी/कार्यक्रम हॉलची क्षमता किती?", "type": "TEXT"},
                {"text": "Any other important requirements or comments for the clubhouse?", "marathi": "क्लबहाऊससाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा टिप्पण्या?", "type": "PARAGRAPH"},
            ]
        },
    ]
})

# ── 17. AGRICULTURE & HORTICULTURE ───────────────────────────────────────────
ALL_FORMS.append({
    "title": "Club Deeper – Agriculture & Horticulture Planning Questionnaire",
    "description": "Detailed planning questionnaire for Agriculture and Horticulture at Club Deeper Campus.\n\nक्लब डीपर शेती आणि फलोत्पादनासाठी सविस्तर नियोजन प्रश्नावली.",
    "sections": [
        {
            "title": "Section 1: Scope & Purpose | विभाग १: व्याप्ती आणि उद्देश",
            "questions": [
                {"text": "What is the primary purpose of agriculture at Club Deeper?", "marathi": "क्लब डीपरमध्ये शेतीचा प्राथमिक उद्देश काय आहे?", "type": "CHECKBOX", "options": ["Campus food production (self-sufficiency)", "Agricultural training for skill students", "Rural development demonstration farm", "Commercial farming (revenue)", "Organic farm for restaurant/canteen supply", "All of the above"]},
                {"text": "How many acres will be allocated for agriculture?", "marathi": "शेतीसाठी किती एकर जमीन दिली जाईल?", "type": "TEXT"},
                {"text": "What crops/produce are planned?", "marathi": "कोणत्या पिकांची/उत्पादनांची योजना आहे?", "type": "PARAGRAPH"},
                {"text": "Will the farm be organic certified?", "marathi": "शेत सेंद्रिय प्रमाणित असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, full organic certification", "Yes, organic practices but not certified", "No", "To be decided"]},
                {"text": "What horticulture components are planned?", "marathi": "कोणते फलोत्पादन घटक नियोजित आहेत?", "type": "CHECKBOX", "options": ["Fruit orchard", "Vegetable garden", "Flower garden (for campus use)", "Nursery/plant propagation", "Medicinal herb garden", "Landscaping plants", "All of the above"]},
            ]
        },
        {
            "title": "Section 2: Training & Technology | विभाग २: प्रशिक्षण आणि तंत्रज्ञान",
            "questions": [
                {"text": "Will this be a training farm for skill/rural development students?", "marathi": "हे कौशल्य/ग्रामीण विकास विद्यार्थ्यांसाठी प्रशिक्षण शेत असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No", "Dual purpose", "To be decided"]},
                {"text": "What modern farming technologies will be demonstrated?", "marathi": "कोणत्या आधुनिक शेती तंत्रज्ञानाचे प्रात्यक्षिक केले जाईल?", "type": "CHECKBOX", "options": ["Drip irrigation", "Hydroponics", "Vermicomposting", "Solar-powered water pumps", "Poly house / greenhouse", "Precision farming / IoT sensors", "None – traditional methods only"]},
                {"text": "Water source for irrigation?", "marathi": "सिंचनासाठी पाण्याचा स्रोत काय?", "type": "MULTIPLE_CHOICE", "options": ["Borewell", "Rainwater harvesting", "Lift irrigation from Khadakwasla backwaters", "Mix of sources", "To be decided"]},
                {"text": "Will there be a composting facility for campus organic waste?", "marathi": "कॅम्पसच्या सेंद्रिय कचऱ्यासाठी कंपोस्टिंग सुविधा असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No", "To be decided"]},
                {"text": "Any other important requirements or comments for agriculture?", "marathi": "शेतीसाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा टिप्पण्या?", "type": "PARAGRAPH"},
            ]
        },
    ]
})

# ── 18. ANIMAL HUSBANDRY ─────────────────────────────────────────────────────
ALL_FORMS.append({
    "title": "Club Deeper – Animal Husbandry Planning Questionnaire",
    "description": "Detailed planning questionnaire for Animal Husbandry at Club Deeper Campus.\n\nक्लब डीपर पशुपालनासाठी सविस्तर नियोजन प्रश्नावली.",
    "sections": [
        {
            "title": "Section 1: Scope & Animals | विभाग १: व्याप्ती आणि प्राणी",
            "questions": [
                {"text": "What is the primary purpose of animal husbandry at Club Deeper?", "marathi": "क्लब डीपरमध्ये पशुपालनाचा प्राथमिक उद्देश काय आहे?", "type": "CHECKBOX", "options": ["Dairy (milk supply for campus)", "Training for skill students", "Rural development demonstration", "Commercial production", "Education for school students", "All of the above"]},
                {"text": "Which animals are planned to be kept?", "marathi": "कोणते प्राणी ठेवण्याचे नियोजित आहे?", "type": "CHECKBOX", "options": ["Cows / Buffalo (dairy)", "Goats", "Poultry (chickens, eggs)", "Pigs", "Fish (aquaculture)", "Bees (honey production)", "None – not planned"]},
                {"text": "How many cattle/dairy animals are planned?", "marathi": "किती गुरे/दुग्ध जनावरे नियोजित आहेत?", "type": "TEXT"},
                {"text": "What is the expected milk production target per day?", "marathi": "दिवसाला अपेक्षित दूध उत्पादन लक्ष्य किती?", "type": "TEXT"},
                {"text": "Will the dairy primarily supply the campus canteen/hospital?", "marathi": "दुग्धव्यवसाय प्रामुख्याने कॅम्पस कॅन्टीन/रुग्णालयाला पुरवठा करेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No, sold commercially", "Both campus use and commercial sale", "To be decided"]},
            ]
        },
        {
            "title": "Section 2: Infrastructure & Operations | विभाग २: पायाभूत सुविधा आणि संचालन",
            "questions": [
                {"text": "What infrastructure is needed for the animal husbandry unit?", "marathi": "पशुपालन युनिटसाठी कोणती पायाभूत सुविधा लागेल?", "type": "CHECKBOX", "options": ["Cattle shed", "Milking facility", "Feed storage", "Veterinary room", "Biogas plant (from animal waste)", "Fodder cultivation area", "Poultry shed"]},
                {"text": "Will there be a biogas plant to utilize animal waste?", "marathi": "प्राण्यांचा कचरा वापरण्यासाठी बायोगॅस प्लांट असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No", "To be decided"]},
                {"text": "What veterinary support is planned?", "marathi": "कोणता पशुवैद्यकीय आधार नियोजित आहे?", "type": "MULTIPLE_CHOICE", "options": ["Full-time vet on campus", "Part-time/visiting vet", "Tie-up with nearby veterinary college", "To be decided"]},
                {"text": "Will skill students from the agricultural program manage this unit?", "marathi": "कृषी कार्यक्रमातील कौशल्य विद्यार्थी हे युनिट व्यवस्थापित करतील का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No, dedicated paid staff", "Mix of students and staff", "To be decided"]},
                {"text": "Any other important requirements or comments for animal husbandry?", "marathi": "पशुपालनासाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा टिप्पण्या?", "type": "PARAGRAPH"},
            ]
        },
    ]
})

# ── 19. CANTEEN / FOOD SERVICES ──────────────────────────────────────────────
ALL_FORMS.append({
    "title": "Club Deeper – Campus Canteen & Food Services Planning Questionnaire",
    "description": "Detailed planning questionnaire for Campus-wide Canteen and Food Services at Club Deeper.\n\nक्लब डीपर कॅम्पस कॅन्टीन आणि अन्न सेवांसाठी सविस्तर नियोजन प्रश्नावली.",
    "sections": [
        {
            "title": "Section 1: Scope & Operations | विभाग १: व्याप्ती आणि संचालन",
            "questions": [
                {"text": "How many canteen/dining facilities are needed across the campus?", "marathi": "कॅम्पसभरात किती कॅन्टीन/जेवण सुविधा लागतील?", "type": "TEXT"},
                {"text": "Who will manage the canteen operations?", "marathi": "कॅन्टीन संचालन कोण व्यवस्थापित करेल?", "type": "MULTIPLE_CHOICE", "options": ["In-house (campus managed)", "Outsourced caterer", "Skill campus students (training)", "Mix of skill students + professional", "To be decided"]},
                {"text": "What meals will be served?", "marathi": "कोणते जेवण दिले जाईल?", "type": "CHECKBOX", "options": ["Breakfast", "Mid-morning snack", "Lunch", "Evening snack/tea", "Dinner", "All meals (full board)"]},
                {"text": "What is the total seating capacity needed across all canteens?", "marathi": "सर्व कॅन्टीनमध्ये एकूण बैठक क्षमता किती लागेल?", "type": "TEXT"},
                {"text": "Will there be a central kitchen supplying all canteens?", "marathi": "सर्व कॅन्टीनना पुरवठा करणारे मध्यवर्ती स्वयंपाकघर असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, one central kitchen", "Separate kitchens for each canteen", "Central kitchen + satellite serveries", "To be decided"]},
                {"text": "What is the dietary policy for the campus canteen?", "marathi": "कॅम्पस कॅन्टीनसाठी आहार धोरण काय आहे?", "type": "CHECKBOX", "options": ["Vegetarian only", "Vegan options available", "Jain options available", "Non-vegetarian available", "Allergy-labeled food", "No specific policy"]},
            ]
        },
        {
            "title": "Section 2: Technology & Finance | विभाग २: तंत्रज्ञान आणि वित्त",
            "questions": [
                {"text": "Will all canteen payments be cashless via Deepa Coins?", "marathi": "सर्व कॅन्टीन देयक दीपा कॉईन्सद्वारे कॅशलेस असतील का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, Deepa Coins only", "Yes, with cash backup", "No, cash accepted", "To be decided"]},
                {"text": "Will meal plans be offered (monthly/quarterly prepaid)?", "marathi": "जेवण योजना उपलब्ध असतील का (मासिक/त्रैमासिक प्रीपेड)?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No, pay per meal", "Both options", "To be decided"]},
                {"text": "What FSSAI/food safety compliance is planned?", "marathi": "कोणती FSSAI/अन्न सुरक्षा अनुपालन नियोजित आहे?", "type": "PARAGRAPH"},
                {"text": "What is the target food cost per meal per student?", "marathi": "प्रति विद्यार्थी प्रति जेवण लक्ष्यित अन्न खर्च किती?", "type": "TEXT"},
                {"text": "Will there be a tuck shop/snack kiosk separate from the main canteen?", "marathi": "मुख्य कॅन्टीनपेक्षा वेगळे टक शॉप/स्नॅक कियोस्क असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No", "To be decided"]},
                {"text": "Any other important requirements or comments for food services?", "marathi": "अन्न सेवांसाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा टिप्पण्या?", "type": "PARAGRAPH"},
            ]
        },
    ]
})

# ── 20. INTERNAL ROADS & INFRASTRUCTURE ──────────────────────────────────────
ALL_FORMS.append({
    "title": "Club Deeper – Internal Roads & Campus Infrastructure Planning Questionnaire",
    "description": "Detailed planning questionnaire for Internal Roads and Campus-wide Infrastructure at Club Deeper.\n\nक्लब डीपर अंतर्गत रस्ते आणि कॅम्पस पायाभूत सुविधांसाठी सविस्तर नियोजन प्रश्नावली.",
    "sections": [
        {
            "title": "Section 1: Roads & Connectivity | विभाग १: रस्ते आणि जोडणी",
            "questions": [
                {"text": "What is the total internal road network length planned (km)?", "marathi": "नियोजित एकूण अंतर्गत रस्ते नेटवर्क लांबी (किमी) किती?", "type": "TEXT"},
                {"text": "What road surface type is preferred?", "marathi": "कोणता रस्ता पृष्ठभाग प्रकार पसंत आहे?", "type": "MULTIPLE_CHOICE", "options": ["Concrete roads throughout", "Asphalt/bitumen roads", "Paver blocks for pedestrian areas + concrete for vehicles", "Mix based on usage", "To be decided"]},
                {"text": "Will there be separate pedestrian pathways?", "marathi": "स्वतंत्र पादचारी मार्ग असतील का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, throughout campus", "Yes, in key areas only", "No, shared with vehicles", "To be decided"]},
                {"text": "Will there be dedicated cycling tracks?", "marathi": "समर्पित सायकल ट्रॅक असतील का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No", "To be decided"]},
                {"text": "How many entry/exit gates are planned for the campus?", "marathi": "कॅम्पससाठी किती प्रवेश/निर्गमन दरवाजे नियोजित आहेत?", "type": "TEXT"},
                {"text": "What is the internal transport plan (electric vehicles, cycle, walk)?", "marathi": "अंतर्गत वाहतूक योजना काय आहे (इलेक्ट्रिक वाहने, सायकल, चालणे)?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 2: Utilities | विभाग २: उपयुक्तता सेवा",
            "questions": [
                {"text": "What is the total water storage capacity needed for the campus (KL)?", "marathi": "कॅम्पससाठी एकूण पाण्याचा साठवण क्षमता किती लागेल (KL)?", "type": "TEXT"},
                {"text": "What is the primary water source for the campus?", "marathi": "कॅम्पससाठी प्राथमिक पाण्याचा स्रोत काय?", "type": "MULTIPLE_CHOICE", "options": ["Borewell", "Lift irrigation from Khadakwasla backwaters", "Municipal supply", "Rainwater harvesting + borewell", "To be decided"]},
                {"text": "What is the total connected load (KVA) estimated for the campus?", "marathi": "कॅम्पससाठी अंदाजित एकूण जोडलेला भार (KVA) किती?", "type": "TEXT"},
                {"text": "What % of power from solar is targeted?", "marathi": "सौर ऊर्जेपासून किती % ऊर्जा लक्ष्यित आहे?", "type": "MULTIPLE_CHOICE", "options": ["0% (grid only)", "10-25%", "25-50%", "50-75%", "100% solar goal", "To be decided"]},
                {"text": "What is the generator/DG backup capacity needed?", "marathi": "जनरेटर/DG बॅकअप क्षमता किती लागेल?", "type": "TEXT"},
                {"text": "What is the sewage treatment capacity needed (KLD)?", "marathi": "सांडपाणी प्रक्रिया क्षमता किती लागेल (KLD)?", "type": "TEXT"},
            ]
        },
        {
            "title": "Section 3: Digital & Safety Infrastructure | विभाग ३: डिजिटल आणि सुरक्षा पायाभूत सुविधा",
            "questions": [
                {"text": "What campus-wide Wi-Fi coverage is planned?", "marathi": "कॅम्पसभरात Wi-Fi कव्हरेज काय नियोजित आहे?", "type": "MULTIPLE_CHOICE", "options": ["Full coverage everywhere", "Academic buildings only", "Academic + residential only", "Key zones only", "To be decided"]},
                {"text": "How many CCTV cameras are planned campus-wide?", "marathi": "कॅम्पसभरात किती CCTV कॅमेरे नियोजित आहेत?", "type": "TEXT"},
                {"text": "Will there be a central security control room?", "marathi": "मध्यवर्ती सुरक्षा नियंत्रण कक्ष असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes", "No", "To be decided"]},
                {"text": "What waste management systems are planned campus-wide?", "marathi": "कॅम्पसभरात कोणत्या कचरा व्यवस्थापन प्रणाली नियोजित आहेत?", "type": "CHECKBOX", "options": ["Wet/dry waste segregation", "Organic composting", "Biogas from organic waste", "Plastic recycling", "Zero waste goal", "Outsourced to municipal body"]},
                {"text": "Will there be a campus-wide PA / announcement system?", "marathi": "कॅम्पसभरात PA / घोषणा प्रणाली असेल का?", "type": "MULTIPLE_CHOICE", "options": ["Yes, integrated digital PA", "Yes, basic zoned PA", "No", "To be decided"]},
                {"text": "What is the planned total capital expenditure for Phase 1 infrastructure?", "marathi": "टप्पा १ पायाभूत सुविधांसाठी नियोजित एकूण भांडवली खर्च किती?", "type": "TEXT"},
                {"text": "Any other important requirements or comments for campus infrastructure?", "marathi": "कॅम्पस पायाभूत सुविधांसाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा टिप्पण्या?", "type": "PARAGRAPH"},
            ]
        },
    ]
})


# ══════════════════════════════════════════════════════════════════════════════
# MAIN — create all forms
# ══════════════════════════════════════════════════════════════════════════════

def main():
    print("=" * 60)
    print("  Club Deeper – Google Forms Creator")
    print("  Creating 20 planning questionnaires...")
    print("=" * 60)

    if not os.path.exists(CREDS_FILE):
        print(f"\n❌  ERROR: credentials.json not found at {CREDS_FILE}")
        print("   Please download it from Google Cloud Console and place")
        print("   it in the same folder as this script.\n")
        return

    print("\n🔐  Authenticating with Google...")
    creds = get_credentials()

    forms_service   = build("forms",  "v1",     credentials=creds)
    drive_service   = build("drive",  "v3",     credentials=creds)
    sheets_service  = build("sheets", "v4",     credentials=creds)

    print(f"\n📁  Getting or creating Drive folder: '{FOLDER_NAME}'...")
    folder_id = get_or_create_folder(drive_service, FOLDER_NAME)
    print(f"    Folder ID: {folder_id}")

    results = []
    total = len(ALL_FORMS)

    for i, form_def in enumerate(ALL_FORMS):
        print(f"\n[{i+1}/{total}]", end=" ")
        try:
            info = create_form(
                forms_service,
                drive_service,
                folder_id,
                form_def["title"],
                form_def["description"],
                form_def["sections"]
            )
            results.append({
                "index":    i + 1,
                "title":    form_def["title"],
                "form_id":  info["form_id"],
                "view_url": info["view_url"],
                "edit_url": info["edit_url"],
            })
            time.sleep(1)  # Rate limiting
        except Exception as e:
            print(f"    ❌ FAILED: {e}")
            results.append({
                "index":  i + 1,
                "title":  form_def["title"],
                "error":  str(e),
            })

    # Save output
    with open(OUTPUT_FILE, "w") as f:
        json.dump(results, f, indent=2)

    print("\n" + "=" * 60)
    print(f"✅  Done! {sum(1 for r in results if 'form_id' in r)}/{total} forms created.")
    print(f"📄  Form URLs saved to: {OUTPUT_FILE}")
    print(f"📁  All forms are in your Google Drive folder: '{FOLDER_NAME}'")
    print("=" * 60)
    print("\nNext step: use form_urls.json to build the Vercel web app.")


if __name__ == "__main__":
    main()
