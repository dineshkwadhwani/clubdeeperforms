"""
Club Deeper – Batch 3: SOCIAL PROJECTS
Projects: Old Age Home, Care Center, Hospital,
          Rural Development Center, Training Center

Run:  python3 batch3_social.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import run_batch

OLD_AGE_HOME = {
    "index": 7,
    "title": "Club Deeper – Old Age Home Planning Questionnaire",
    "active": False,
    "description": (
        "Comprehensive planning questionnaire for the Old Age Home at Club Deeper Campus.\n\n"
        "क्लब डीपर वृद्धाश्रमासाठी सर्वसमावेशक नियोजन प्रश्नावली."
    ),
    "sections": [
        {
            "title": "Section 1: Vision, Model & Resident Profile  |  विभाग १: दृष्टी, मॉडेल आणि रहिवासी प्रोफाइल",
            "questions": [
                {"en": "What is the vision and positioning of the Old Age Home?", "mr": "वृद्धाश्रमाची दृष्टी आणि पोझिशनिंग काय आहे?", "type": "RADIO", "options": ["Luxury/premium retirement community", "Mid-segment comfortable living", "Affordable / social service focused", "Mix of paid premium + subsidised social", "To be decided"]},
                {"en": "What is the target capacity?", "mr": "लक्ष्यित क्षमता किती?", "type": "TEXT"},
                {"en": "What age group will be admitted (60+, 65+, 70+)?", "mr": "कोणता वयोगट प्रवेश घेऊ शकेल (६०+, ६५+, ७०+)?", "type": "TEXT"},
                {"en": "Will couples be accommodated together? Couple suite option?", "mr": "जोडप्यांना एकत्र राहण्याची सोय असेल का? कपल सुइट पर्याय?", "type": "RADIO", "options": ["Yes, couple rooms/suites available", "No, individual rooms only", "Both options available", "To be decided"]},
                {"en": "Will the home accept residents with dementia / Alzheimer's — special memory care unit?", "mr": "वृद्धाश्रम स्मृतिभ्रंश / अल्झायमर रुग्णांना स्वीकारेल का — विशेष मेमरी केअर युनिट?", "type": "RADIO", "options": ["Yes, dedicated memory care unit", "Yes, limited cases with mild dementia", "No, only independent seniors", "To be decided"]},
                {"en": "Will the home accept bedridden / highly dependent residents?", "mr": "वृद्धाश्रम अंथरुणावर खिळलेल्या / अत्यंत अवलंबी रहिवाशांना स्वीकारेल का?", "type": "RADIO", "options": ["Yes, with palliative care unit", "Limited — mild dependency only", "No", "To be decided"]},
                {"en": "Is this integrated with the Club Deeper residential community or a separate, dedicated building?", "mr": "हे क्लब डीपर निवासी समुदायाशी एकत्रित आहे की स्वतंत्र, समर्पित इमारत आहे?", "type": "RADIO", "options": ["Integrated — elderly in same gated community", "Separate dedicated building on campus", "Both — some in community, some in dedicated block", "To be decided"]},
            ]
        },
        {
            "title": "Section 2: Care Services & Medical  |  विभाग २: सेवा आणि वैद्यकीय",
            "questions": [
                {"en": "What level of medical care will be provided on-site?", "mr": "ऑन-साइट किती स्तराची वैद्यकीय सेवा दिली जाईल?", "type": "RADIO", "options": ["Basic first aid and medication management only", "Nurse on duty 24/7", "Doctor visiting daily + nurse 24/7", "Full nursing home level care", "Hospital-level ICU and emergency", "To be decided"]},
                {"en": "Which specialised care units are planned?", "mr": "कोणते विशेष सेवा युनिट्स नियोजित आहेत?", "type": "CHECKBOX", "options": ["Physiotherapy room", "Occupational therapy", "Speech therapy", "Memory care / dementia unit", "Palliative / end-of-life care unit", "Yoga & wellness room", "Eye and dental screening facility", "None — basic care only"]},
                {"en": "Daily care services that will be provided?", "mr": "प्रतिदिन कोणत्या सेवा दिल्या जातील?", "type": "CHECKBOX", "options": ["3 meals/day + snacks (dietary-appropriate)", "Housekeeping and room cleaning", "Laundry services", "Medication administration and tracking", "Physiotherapy sessions", "Recreational and social activities", "Transportation for medical visits", "Emergency call system in each room/bathroom"]},
                {"en": "Caregiver-to-resident ratio planned (general wing / memory care wing)?", "mr": "नियोजित काळजीवाहक-ते-रहिवासी गुणोत्तर (सामान्य विंग / मेमरी केअर विंग)?", "type": "TEXT"},
                {"en": "Emergency call system in rooms and bathrooms — what type?", "mr": "खोल्या आणि स्नानगृहांमध्ये आपत्कालीन कॉल प्रणाली — कोणत्या प्रकारची?", "type": "RADIO", "options": ["Wired pull-cord system", "Wireless wearable panic button", "Smart sensor-based monitoring", "To be decided"]},
                {"en": "Medical tie-up with Club Deeper Hospital for referrals and emergencies?", "mr": "रेफरल आणि आपत्कालीन परिस्थितीसाठी क्लब डीपर रुग्णालयाशी वैद्यकीय करार?", "type": "RADIO", "options": ["Yes, formal SLA with hospital", "Informal arrangement", "External hospital tie-up", "To be decided"]},
                {"en": "What mental health / emotional wellbeing services will be offered?", "mr": "कोणत्या मानसिक आरोग्य / भावनिक कल्याण सेवा उपलब्ध असतील?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 3: Living Spaces & Community Life  |  विभाग ३: राहण्याची जागा आणि सामुदायिक जीवन",
            "questions": [
                {"en": "What room types will be offered?", "mr": "कोणते खोली प्रकार उपलब्ध असतील?", "type": "CHECKBOX", "options": ["Single room (private)", "Double/shared room", "Studio apartment", "1-BHK apartment for independent seniors", "Couple suite", "Assisted living suite (with attached caregiver space)"]},
                {"en": "Will all rooms and corridors be wheelchair accessible?", "mr": "सर्व खोल्या आणि कॉरिडॉर व्हीलचेअरसाठी सुलभ असतील का?", "type": "RADIO", "options": ["Yes, fully accessible throughout", "Yes, ground floor accessible", "Partially accessible", "To be decided"]},
                {"en": "What common spaces are planned?", "mr": "कोणते सामायिक स्थळ नियोजित आहेत?", "type": "CHECKBOX", "options": ["Dining hall with dietary-appropriate menus", "Garden and walking paths (designed for elderly)", "Temple / prayer room / meditation space", "Common TV/recreation lounge", "Library/reading corner", "Activity room (crafts, board games, music)", "Outdoor sitting areas and gazebos", "Vegetable garden for residents to tend"]},
                {"en": "Will there be intergenerational programmes connecting elderly residents with campus students?", "mr": "वृद्ध रहिवासी आणि कॅम्पस विद्यार्थ्यांना जोडणारे आंतरपीढी कार्यक्रम असतील का?", "type": "RADIO", "options": ["Yes, structured weekly interactions", "Yes, informal occasional", "No", "To be decided"]},
                {"en": "What activities and engagement programmes are planned (yoga, bhajans, craft, outings)?", "mr": "कोणते क्रियाकलाप आणि गुंतवणूक कार्यक्रम नियोजित आहेत (योग, भजन, हस्तकला, सहली)?", "type": "PARAGRAPH"},
                {"en": "Family visitation policy and facilities — visiting rooms, guest accommodation?", "mr": "कुटुंब भेट धोरण आणि सुविधा — भेट खोल्या, अतिथी निवास?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 4: Fees, Sustainability & Regulations  |  विभाग ४: शुल्क, टिकाऊपणा आणि नियमन",
            "questions": [
                {"en": "Monthly fee per resident (general / premium)?", "mr": "प्रति रहिवासी मासिक शुल्क (सामान्य / प्रीमियम)?", "type": "TEXT"},
                {"en": "One-time entry deposit / corpus — amount and refund policy?", "mr": "एकवेळ प्रवेश ठेव / कॉर्पस — रक्कम आणि परतावा धोरण?", "type": "PARAGRAPH"},
                {"en": "What does the monthly fee include?", "mr": "मासिक शुल्कात काय समाविष्ट आहे?", "type": "CHECKBOX", "options": ["All meals", "Housekeeping", "Laundry", "Basic medical (nurse, medications)", "Physiotherapy", "Activities and outings", "Wi-Fi and TV", "Electricity and water"]},
                {"en": "Will there be subsidised / free seats for destitute elderly (CSR or government funding)?", "mr": "निराधार वृद्धांसाठी अनुदानित / मुफ्त जागा असतील का (CSR किंवा सरकारी निधी)?", "type": "PARAGRAPH"},
                {"en": "Staffing plan — how many caregivers, nurses, activity coordinators, admin?", "mr": "कर्मचारी योजना — किती काळजीवाहक, परिचारिका, क्रियाकलाप समन्वयक, प्रशासन?", "type": "PARAGRAPH"},
                {"en": "Regulatory compliance — who governs old age homes in Maharashtra? Approvals needed?", "mr": "नियामक अनुपालन — महाराष्ट्रात वृद्धाश्रमांवर कोण नियंत्रण ठेवते? कोणत्या मंजुरी आवश्यक?", "type": "PARAGRAPH"},
                {"en": "Any other important requirements or ideas for the Old Age Home?", "mr": "वृद्धाश्रमासाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा कल्पना?", "type": "PARAGRAPH"},
            ]
        },
    ]
}

CARE_CENTER = {
    "index": 8,
    "title": "Club Deeper – Care Center Planning Questionnaire",
    "active": False,
    "description": (
        "Comprehensive planning questionnaire for the Care Center (toddlers, special needs, day care) at Club Deeper.\n\n"
        "क्लब डीपर केअर सेंटरसाठी (लहान मुले, विशेष गरजा, डे केअर) सर्वसमावेशक नियोजन प्रश्नावली."
    ),
    "sections": [
        {
            "title": "Section 1: Scope & Beneficiaries  |  विभाग १: व्याप्ती आणि लाभार्थी",
            "questions": [
                {"en": "Who will the care centre serve?", "mr": "केअर सेंटर कोणाला सेवा देईल?", "type": "CHECKBOX", "options": ["Infants and toddlers (0–3 years)", "Pre-school children (3–6 years)", "School-age children with special needs", "Adults with physical disabilities", "Adults with intellectual disabilities", "Elderly (day care)", "All of the above"]},
                {"en": "Target capacity for each beneficiary group?", "mr": "प्रत्येक लाभार्थी गटासाठी लक्ष्यित क्षमता?", "type": "PARAGRAPH"},
                {"en": "Will it primarily serve families residing on campus or the surrounding community too?", "mr": "हे प्रामुख्याने कॅम्पसवर राहणाऱ्या कुटुंबांना सेवा देईल की आसपासच्या समुदायालाही?", "type": "RADIO", "options": ["Campus families only (priority)", "Open to surrounding community", "Both, campus families first", "To be decided"]},
                {"en": "Will it operate as day care, residential care, or both?", "mr": "हे डे केअर, निवासी काळजी, किंवा दोन्ही म्हणून कार्य करेल?", "type": "RADIO", "options": ["Day care only (8 AM – 6 PM)", "Residential care (24-hour)", "Both options", "To be decided"]},
                {"en": "Will skill campus students (Early Childhood Care programme) work here as part of training?", "mr": "कौशल्य कॅम्पस विद्यार्थी (बाल काळजी कार्यक्रम) प्रशिक्षणाचा भाग म्हणून येथे काम करतील का?", "type": "RADIO", "options": ["Yes, structured internship", "Yes, occasional assistance", "No", "To be decided"]},
            ]
        },
        {
            "title": "Section 2: Special Needs Services & Therapies  |  विभाग २: विशेष गरजा सेवा आणि उपचार",
            "questions": [
                {"en": "Which special needs categories will be catered to?", "mr": "कोणत्या विशेष गरजा श्रेण्या पूर्ण केल्या जातील?", "type": "CHECKBOX", "options": ["Autism Spectrum Disorder (ASD)", "Down Syndrome", "Cerebral Palsy", "Visual impairment (blind/low vision)", "Hearing impairment (deaf/hard of hearing)", "Intellectual / learning disabilities", "Physical disabilities", "Multiple disabilities", "All categories"]},
                {"en": "What therapies will be offered on-site?", "mr": "ऑन-साइट कोणत्या उपचारपद्धती उपलब्ध असतील?", "type": "CHECKBOX", "options": ["Speech and language therapy", "Occupational therapy", "Physiotherapy", "Applied Behaviour Analysis (ABA)", "Music therapy", "Art therapy", "Sensory integration therapy", "Hydrotherapy (if pool available)"]},
                {"en": "Will there be a trained Special Educator on staff? Qualification requirements?", "mr": "कर्मचारी वर्गात प्रशिक्षित विशेष शिक्षक असेल का? पात्रता आवश्यकता?", "type": "PARAGRAPH"},
                {"en": "Early childhood education programme for toddlers — Montessori, play-based, structured?", "mr": "लहान मुलांसाठी प्रारंभिक बालशिक्षण कार्यक्रम — मॉन्टेसरी, खेळ-आधारित, संरचित?", "type": "RADIO", "options": ["Montessori approach", "Play-based learning", "Structured preschool curriculum", "Hybrid model", "To be decided"]},
                {"en": "Parent counselling and involvement — how will it be structured?", "mr": "पालक समुपदेशन आणि सहभाग — ते कसे संरचित असेल?", "type": "PARAGRAPH"},
                {"en": "Assistive technology devices — communication devices, adapted computers — planned?", "mr": "सहायक तंत्रज्ञान उपकरणे — संप्रेषण उपकरणे, अनुकूलित संगणक — नियोजित?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 3: Infrastructure & Safety  |  विभाग ३: पायाभूत सुविधा आणि सुरक्षा",
            "questions": [
                {"en": "What spaces are essential inside the care centre?", "mr": "केअर सेंटरमध्ये कोणत्या जागा आवश्यक आहेत?", "type": "CHECKBOX", "options": ["Bright, colourful indoor play area", "Sensory garden / outdoor play area", "Individual therapy rooms (each 10x12 ft minimum)", "Nap/rest rooms with individual cots", "Dining area with adapted furniture", "Parent meeting and counselling room", "Medical/first aid room", "Observation room (one-way glass for therapists)", "Staff office and resource room", "Clean and separate toileting/hygiene area"]},
                {"en": "Non-negotiable safety features?", "mr": "अनिवार्य सुरक्षा वैशिष्ट्ये?", "type": "CHECKBOX", "options": ["CCTV in all rooms (accessible to parents via app)", "Padded flooring in play areas", "No sharp corners / rounded furniture", "Secured single entry/exit with biometric/RFID", "Allergy-safe / nut-free environment", "24/7 staff coverage", "Regular fire drills", "First aid trained staff at all times"]},
                {"en": "Caregiver-to-child ratio (toddlers / pre-school / special needs)?", "mr": "काळजीवाहक-ते-मूल गुणोत्तर (लहान मुले / पूर्व-शाळा / विशेष गरजा)?", "type": "TEXT"},
                {"en": "Outdoor/nature play area — sensory garden, sand pit, water play?", "mr": "मैदानी/निसर्ग खेळ क्षेत्र — संवेदी बाग, वाळूचा खड्डा, पाण्याचा खेळ?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 4: Fees, Staffing & Community  |  विभाग ४: शुल्क, कर्मचारी आणि समुदाय",
            "questions": [
                {"en": "Monthly fee for day care (toddlers / pre-school / special needs)?", "mr": "डे केअरसाठी मासिक शुल्क (लहान मुले / पूर्व-शाळा / विशेष गरजा)?", "type": "PARAGRAPH"},
                {"en": "Will services be subsidised for skill campus students' children?", "mr": "कौशल्य कॅम्पस विद्यार्थ्यांच्या मुलांसाठी सेवा अनुदानित असतील का?", "type": "RADIO", "options": ["Yes, heavily subsidised", "Yes, minor discount", "No", "To be decided"]},
                {"en": "Will the centre integrate with the Old Age Home for intergenerational activities?", "mr": "आंतरपीढी क्रियाकलापांसाठी केंद्र वृद्धाश्रमाशी एकत्रित होईल का?", "type": "RADIO", "options": ["Yes, regular intergenerational programmes", "Occasional joint activities", "No", "To be decided"]},
                {"en": "Staffing plan — caregivers, therapists, special educators, admin?", "mr": "कर्मचारी योजना — काळजीवाहक, उपचारतज्ज्ञ, विशेष शिक्षक, प्रशासन?", "type": "PARAGRAPH"},
                {"en": "Any other important requirements or ideas for the Care Center?", "mr": "केअर सेंटरसाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा कल्पना?", "type": "PARAGRAPH"},
            ]
        },
    ]
}

HOSPITAL = {
    "index": 9,
    "title": "Club Deeper – Hospital Planning Questionnaire",
    "active": False,
    "description": (
        "Comprehensive planning questionnaire for the Hospital at Club Deeper Campus.\n\n"
        "क्लब डीपर रुग्णालयासाठी सर्वसमावेशक नियोजन प्रश्नावली."
    ),
    "sections": [
        {
            "title": "Section 1: Vision, Type & Scope  |  विभाग १: दृष्टी, प्रकार आणि व्याप्ती",
            "questions": [
                {"en": "What type and scale of hospital is planned?", "mr": "कोणत्या प्रकारचे आणि किती मोठे रुग्णालय नियोजित आहे?", "type": "RADIO", "options": ["Primary health centre / clinic (< 20 beds)", "Small community hospital (20–50 beds)", "Medium multi-specialty hospital (50–100 beds)", "Full multi-specialty hospital (100+ beds)", "To be decided"]},
                {"en": "Who will the hospital primarily serve?", "mr": "रुग्णालय प्रामुख्याने कोणाला सेवा देईल?", "type": "CHECKBOX", "options": ["Campus students (school + coaching + skill)", "Campus staff and their families", "Residential bungalow community", "Old Age Home and Care Centre residents", "Surrounding rural villages and taluka", "General public (revenue-generating OPD)"]},
                {"en": "What medical specialties will be offered at launch?", "mr": "सुरुवातीला कोणत्या वैद्यकीय विशेषता उपलब्ध असतील?", "type": "CHECKBOX", "options": ["General Medicine", "Paediatrics", "Orthopaedics", "Gynaecology & Obstetrics", "General Surgery", "Ophthalmology (eye)", "ENT", "Dentistry & Oral Surgery", "Dermatology", "Psychiatry & Mental Health", "Cardiology", "Ayurveda / Naturopathy / Homeopathy", "Emergency & Trauma"]},
                {"en": "Will it be a teaching hospital linked to the Skill Campus (nursing, paramedical training)?", "mr": "हे कौशल्य कॅम्पसशी (नर्सिंग, पॅरामेडिकल प्रशिक्षण) जोडलेले शिक्षण रुग्णालय असेल का?", "type": "RADIO", "options": ["Yes, formal teaching hospital", "Yes, internship placement only", "No", "To be decided"]},
                {"en": "Will there be a focus on rural health outreach — mobile medical units, village health camps?", "mr": "ग्रामीण आरोग्य विस्तारावर लक्ष केंद्रित असेल का — मोबाइल वैद्यकीय युनिट, ग्राम आरोग्य शिबिर?", "type": "RADIO", "options": ["Yes, regular mobile health camps", "Yes, periodic quarterly camps", "No", "To be decided"]},
            ]
        },
        {
            "title": "Section 2: Infrastructure & Departments  |  विभाग २: पायाभूत सुविधा आणि विभाग",
            "questions": [
                {"en": "How many inpatient beds are planned at launch and at full capacity?", "mr": "सुरुवातीला आणि पूर्ण क्षमतेवर किती आंतररुग्ण बेड नियोजित आहेत?", "type": "TEXT"},
                {"en": "What diagnostic facilities will be on-site at launch?", "mr": "सुरुवातीला ऑन-साइट कोणत्या निदान सुविधा असतील?", "type": "CHECKBOX", "options": ["Pathology lab (blood tests, urine, etc.)", "Radiology (X-ray)", "Ultrasound", "CT Scan", "MRI", "ECG & Echocardiography", "Pharmacy (24-hour)", "Blood bank / blood storage"]},
                {"en": "Will there be an ICU / HDU / emergency ward?", "mr": "ICU / HDU / आपत्कालीन वार्ड असेल का?", "type": "RADIO", "options": ["Full ICU + Emergency", "Basic HDU (High Dependency Unit)", "Emergency observation only", "No critical care unit", "To be decided"]},
                {"en": "How many operation theatres are planned?", "mr": "किती शस्त्रक्रिया कक्ष नियोजित आहेत?", "type": "TEXT"},
                {"en": "What is the target daily OPD (outpatient) capacity?", "mr": "दैनंदिन OPD (बाह्यरुग्ण) क्षमतेचे लक्ष्य किती?", "type": "TEXT"},
                {"en": "Maternity ward — planned? Delivery rooms, NICU?", "mr": "प्रसूती वार्ड — नियोजित? प्रसूती कक्ष, NICU?", "type": "PARAGRAPH"},
                {"en": "Medical waste management — incinerator, bio-hazard waste handling plan?", "mr": "वैद्यकीय कचरा व्यवस्थापन — इन्सिनरेटर, जैव-धोकादायक कचरा हाताळणी योजना?", "type": "PARAGRAPH"},
                {"en": "Power backup for hospital — critical for life support, OT, ICU (100% backup requirement)?", "mr": "रुग्णालयासाठी वीज बॅकअप — जीवन समर्थन, OT, ICU (१००% बॅकअप आवश्यकता)?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 3: Staffing, Fees & Community Impact  |  विभाग ३: कर्मचारी, शुल्क आणि सामुदायिक प्रभाव",
            "questions": [
                {"en": "How many full-time resident doctors are needed at launch (by specialty)?", "mr": "सुरुवातीला किती पूर्णवेळ निवासी डॉक्टर लागतील (विशेषतानुसार)?", "type": "PARAGRAPH"},
                {"en": "Visiting consultant doctors — how many, which specialties, frequency?", "mr": "भेट देणारे सल्लागार डॉक्टर — किती, कोणत्या विशेषता, वारंवारता?", "type": "PARAGRAPH"},
                {"en": "Nursing staff — how many nurses and paramedics required?", "mr": "नर्सिंग कर्मचारी — किती परिचारिका आणि पॅरामेडिक्स आवश्यक?", "type": "TEXT"},
                {"en": "Will medical services be free / subsidised for campus students and staff?", "mr": "कॅम्पस विद्यार्थी आणि कर्मचाऱ्यांसाठी वैद्यकीय सेवा मुफ्त / अनुदानित असतील का?", "type": "RADIO", "options": ["Yes, fully free for all campus residents", "Yes, heavily subsidised", "OPD free, procedures charged", "All at cost price (no profit)", "To be decided"]},
                {"en": "Will Deepa Coins be accepted for medical bills on campus?", "mr": "कॅम्पसवर वैद्यकीय बिलांसाठी दीपा कॉईन्स स्वीकारले जातील का?", "type": "RADIO", "options": ["Yes", "No", "To be decided"]},
                {"en": "Health insurance empanelment — which schemes (Ayushman Bharat, state schemes, private insurance)?", "mr": "आरोग्य विमा पॅनेल — कोणत्या योजना (आयुष्मान भारत, राज्य योजना, खाजगी विमा)?", "type": "PARAGRAPH"},
                {"en": "Rural health outreach plan — which villages, frequency, services offered?", "mr": "ग्रामीण आरोग्य विस्तार योजना — कोणती गावे, वारंवारता, दिल्या जाणाऱ्या सेवा?", "type": "PARAGRAPH"},
                {"en": "Any other important requirements or ideas for the Hospital?", "mr": "रुग्णालयासाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा कल्पना?", "type": "PARAGRAPH"},
            ]
        },
    ]
}

RURAL_DEV = {
    "index": 10,
    "title": "Club Deeper – Rural Development Center Planning Questionnaire",
    "active": False,
    "description": (
        "Comprehensive planning questionnaire for the Rural Development Center at Club Deeper Campus.\n\n"
        "क्लब डीपर ग्रामीण विकास केंद्रासाठी सर्वसमावेशक नियोजन प्रश्नावली."
    ),
    "sections": [
        {
            "title": "Section 1: Vision, Mission & Focus Areas  |  विभाग १: दृष्टी, अभियान आणि केंद्रबिंदू",
            "questions": [
                {"en": "What is the vision and mission of the Rural Development Center?", "mr": "ग्रामीण विकास केंद्राची दृष्टी आणि अभियान काय आहे?", "type": "PARAGRAPH"},
                {"en": "What are the primary focus areas?", "mr": "प्राथमिक केंद्रबिंदू क्षेत्र कोणते आहेत?", "type": "CHECKBOX", "options": ["Farmer education & agri-technology", "Women empowerment & self-help groups", "Village sanitation & water management", "Digital literacy for rural youth", "Micro-enterprise & livelihood development", "Health & nutrition awareness", "Panchayat / governance training", "Environmental conservation", "Child education & school dropout prevention", "All of the above"]},
                {"en": "Which villages / talukas in the catchment area will be served?", "mr": "सेवा क्षेत्रातील कोणती गावे / तालुके सेवा घेतील?", "type": "PARAGRAPH"},
                {"en": "How many villages does the centre aim to cover in Phase 1?", "mr": "टप्पा १ मध्ये केंद्र किती गावे कव्हर करण्याचे लक्ष्य ठेवते?", "type": "TEXT"},
                {"en": "Will this centre work with government schemes (MGNREGA, PM Kisan, Jal Jeevan Mission, etc.)?", "mr": "हे केंद्र सरकारी योजनांशी काम करेल का (MGNREGA, PM किसान, जल जीवन मिशन इ.)?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 2: Programmes & Outreach  |  विभाग २: कार्यक्रम आणि विस्तार",
            "questions": [
                {"en": "What flagship programmes will be launched in Year 1?", "mr": "वर्ष १ मध्ये कोणते प्रमुख कार्यक्रम सुरू होतील?", "type": "PARAGRAPH"},
                {"en": "Will there be mobile outreach units to reach remote villages?", "mr": "दुर्गम गावांपर्यंत पोहोचण्यासाठी मोबाइल विस्तार युनिट्स असतील का?", "type": "RADIO", "options": ["Yes, dedicated mobile unit(s)", "No, villages come to campus", "Mix", "To be decided"]},
                {"en": "Will campus students participate in village immersion / rural service programmes?", "mr": "कॅम्पस विद्यार्थी गाव विसर्जन / ग्रामीण सेवा कार्यक्रमांमध्ये सहभागी होतील का?", "type": "RADIO", "options": ["Yes, mandatory for all students", "Yes, optional elective", "No", "To be decided"]},
                {"en": "Women's self-help group support — training, micro-credit linkage, product marketing?", "mr": "महिला स्वयं-सहायता गट सहाय्य — प्रशिक्षण, मायक्रो-क्रेडिट लिंकेज, उत्पादन विपणन?", "type": "PARAGRAPH"},
                {"en": "Agricultural extension services — demonstration farms, farmer field schools, soil testing?", "mr": "कृषी विस्तार सेवा — प्रात्यक्षिक शेत, शेतकरी क्षेत्र शाळा, माती परीक्षण?", "type": "PARAGRAPH"},
                {"en": "What partnerships are planned (NGOs, government, corporate CSR, NABARD, ATMA)?", "mr": "कोणत्या भागीदारी नियोजित आहेत (NGO, सरकार, कॉर्पोरेट CSR, NABARD, ATMA)?", "type": "PARAGRAPH"},
                {"en": "How will impact be measured — which metrics (income increase, sanitation coverage, literacy rate)?", "mr": "प्रभाव कसा मोजला जाईल — कोणते मेट्रिक्स (उत्पन्न वाढ, स्वच्छता कव्हरेज, साक्षरता दर)?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 3: Infrastructure, Staffing & Finance  |  विभाग ३: पायाभूत सुविधा, कर्मचारी आणि वित्त",
            "questions": [
                {"en": "What physical infrastructure is required at the campus for the centre?", "mr": "केंद्रासाठी कॅम्पसवर कोणत्या भौतिक पायाभूत सुविधा आवश्यक आहेत?", "type": "CHECKBOX", "options": ["Training hall for villagers visiting campus", "Office and data management room", "Resource library (village-specific books, videos)", "Exhibition / awareness display area", "Demonstration plots (farming, water harvesting)", "Hostel/rest facilities for visiting village participants"]},
                {"en": "Key staff required — rural development officers, community mobilisers, trainers?", "mr": "आवश्यक प्रमुख कर्मचारी — ग्रामीण विकास अधिकारी, समुदाय संघटक, प्रशिक्षक?", "type": "PARAGRAPH"},
                {"en": "Funding model — CSR, government grants, campus cross-subsidy, project-based?", "mr": "निधी मॉडेल — CSR, सरकारी अनुदान, कॅम्पस क्रॉस-सबसिडी, प्रकल्प-आधारित?", "type": "PARAGRAPH"},
                {"en": "Annual budget estimate for operations in Year 1?", "mr": "वर्ष १ मध्ये संचालनासाठी वार्षिक बजेट अंदाज?", "type": "TEXT"},
                {"en": "Any other important requirements or ideas for the Rural Development Center?", "mr": "ग्रामीण विकास केंद्रासाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा कल्पना?", "type": "PARAGRAPH"},
            ]
        },
    ]
}

TRAINING_CENTER = {
    "index": 11,
    "title": "Club Deeper – Training Center Planning Questionnaire",
    "active": False,
    "description": (
        "Comprehensive planning questionnaire for the Training Center at Club Deeper Campus.\n\n"
        "क्लब डीपर प्रशिक्षण केंद्रासाठी सर्वसमावेशक नियोजन प्रश्नावली."
    ),
    "sections": [
        {
            "title": "Section 1: Vision, Purpose & Target Clients  |  विभाग १: दृष्टी, उद्देश आणि लक्ष्य ग्राहक",
            "questions": [
                {"en": "What is the primary purpose of the Training Center?", "mr": "प्रशिक्षण केंद्राचा प्राथमिक उद्देश काय आहे?", "type": "CHECKBOX", "options": ["Corporate training & workshops", "Teacher/faculty professional development", "Leadership & management programmes", "Entrepreneurship and startup bootcamps", "Government / municipal staff training", "NGO capacity building", "Defence / paramilitary training", "Hosting conferences and seminars for revenue"]},
                {"en": "Who are the primary client segments?", "mr": "प्राथमिक ग्राहक विभाग कोण आहेत?", "type": "PARAGRAPH"},
                {"en": "Will the centre also serve as the internal training facility for Club Deeper's own staff and teachers?", "mr": "हे केंद्र क्लब डीपरच्या स्वतःच्या कर्मचारी आणि शिक्षकांसाठी अंतर्गत प्रशिक्षण सुविधा म्हणूनही काम करेल का?", "type": "RADIO", "options": ["Yes, primary internal use", "Yes, secondary use", "No, purely commercial", "To be decided"]},
                {"en": "What is the revenue model?", "mr": "महसूल मॉडेल काय आहे?", "type": "RADIO", "options": ["Fee-based (corporate clients pay market rate)", "Government-funded training contracts", "Hybrid (some paid, some subsidised)", "Non-profit / CSR supported", "To be decided"]},
                {"en": "What is the target annual revenue from the training centre?", "mr": "प्रशिक्षण केंद्रातून लक्ष्यित वार्षिक महसूल किती?", "type": "TEXT"},
            ]
        },
        {
            "title": "Section 2: Infrastructure & Facilities  |  विभाग २: पायाभूत सुविधा आणि सुविधा",
            "questions": [
                {"en": "How many training halls/breakout rooms are needed? Capacity per room?", "mr": "किती प्रशिक्षण हॉल/ब्रेकआउट खोल्या लागतील? प्रति खोली क्षमता?", "type": "TEXT"},
                {"en": "Main conference/seminar hall capacity?", "mr": "मुख्य परिषद/चर्चासत्र हॉलची क्षमता?", "type": "TEXT"},
                {"en": "AV and technology setup required in training rooms?", "mr": "प्रशिक्षण खोल्यांमध्ये AV आणि तंत्रज्ञान व्यवस्था आवश्यक?", "type": "CHECKBOX", "options": ["Interactive smart board", "Video conferencing (Zoom/Teams compatible)", "Recording setup for session capture", "Simultaneous translation facility", "Voting/polling keypads for interactive sessions", "Stage and podium for conferences"]},
                {"en": "Will there be residential accommodation for outstation training participants?", "mr": "बाहेरगावाहून येणाऱ्या प्रशिक्षण सहभागींसाठी निवासाची व्यवस्था असेल का?", "type": "RADIO", "options": ["Yes, dedicated guest rooms / cottages", "Shared with campus hostel", "No, participants arrange own accommodation", "To be decided"]},
                {"en": "Dining / hospitality arrangement for training participants?", "mr": "प्रशिक्षण सहभागींसाठी जेवण / आतिथ्य व्यवस्था?", "type": "RADIO", "options": ["Full board (3 meals/day included)", "Lunch and tea breaks only", "Participants arrange own meals", "Separate training centre dining facility", "To be decided"]},
                {"en": "Will the centre be available for private event bookings (weddings, corporate events)?", "mr": "केंद्र खाजगी कार्यक्रम बुकिंगसाठी (लग्न, कॉर्पोरेट कार्यक्रम) उपलब्ध असेल का?", "type": "RADIO", "options": ["Yes, major revenue stream", "Yes, when not used for training", "No, training only", "To be decided"]},
                {"en": "Any other important requirements or ideas for the Training Center?", "mr": "प्रशिक्षण केंद्रासाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा कल्पना?", "type": "PARAGRAPH"},
            ]
        },
    ]
}

if __name__ == "__main__":
    run_batch("Social Projects", [OLD_AGE_HOME, CARE_CENTER, HOSPITAL, RURAL_DEV, TRAINING_CENTER])
