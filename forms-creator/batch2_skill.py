"""
Club Deeper – Batch 2: SKILL CAMPUS
Projects: Skill Campus (25–30 Units), Software Development Park

Run:  python3 batch2_skill.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import run_batch

SKILL_CAMPUS = {
    "index": 5,
    "title": "Club Deeper – Skill Campus (25–30 Skill Units) Planning Questionnaire",
    "active": False,
    "description": (
        "Comprehensive planning questionnaire for the Skill Development Campus at Club Deeper.\n\n"
        "क्लब डीपर कौशल्य विकास कॅम्पससाठी सर्वसमावेशक नियोजन प्रश्नावली."
    ),
    "sections": [
        {
            "title": "Section 1: Vision & Skill Framework  |  विभाग १: दृष्टी आणि कौशल्य फ्रेमवर्क",
            "questions": [
                {"en": "What is the vision statement for the Skill Campus?", "mr": "कौशल्य कॅम्पसचे ध्येय वाक्य काय आहे?", "type": "PARAGRAPH"},
                {"en": "List the 25–30 skill competencies planned. Which 15 are highest priority for Phase 1?", "mr": "नियोजित २५–३० कौशल्य क्षमतांची यादी करा. टप्पा १ साठी कोणत्या १५ सर्वोच्च प्राधान्याच्या आहेत?", "type": "PARAGRAPH"},
                {"en": "Which broad skill sectors will be covered?", "mr": "कोणते व्यापक कौशल्य क्षेत्र समाविष्ट केले जातील?", "type": "CHECKBOX", "options": ["Healthcare & Nursing", "IT & Software Development", "Construction, Plumbing & Electrical", "Agriculture & Horticulture", "Hospitality, Catering & Food Service", "Beauty, Wellness & Salon", "Retail, Logistics & Supply Chain", "Automotive & Mechanical", "Handicrafts, Textiles & Fashion", "Media, Photography & Video Production", "Financial Literacy & Accounting", "Early Childhood Care & Education", "Security Services", "Two-wheeler / EV Repair"]},
                {"en": "Will skill programmes be aligned with NSQF (National Skill Qualification Framework)?", "mr": "कौशल्य कार्यक्रम NSQF (राष्ट्रीय कौशल्य पात्रता फ्रेमवर्क) शी सुसंगत असतील का?", "type": "RADIO", "options": ["Yes, all programmes NSQF aligned", "Some programmes NSQF aligned", "No, own certification", "To be decided"]},
                {"en": "Will the campus seek Skill University / Polytechnic affiliation?", "mr": "कॅम्पस कौशल्य विद्यापीठ / पॉलिटेक्निक संलग्नता मिळवेल का?", "type": "RADIO", "options": ["Yes, Skill University (long-term goal)", "Yes, partner with existing polytechnic", "No, standalone certification", "To be decided"]},
                {"en": "Will industry partnerships be mandatory for each skill unit (for tools, training, placement)?", "mr": "प्रत्येक कौशल्य युनिटसाठी उद्योग भागीदारी अनिवार्य असेल का?", "type": "RADIO", "options": ["Yes, mandatory for each unit", "Yes, for selected units", "No, purely campus-run", "To be decided"]},
                {"en": "What government schemes will the Skill Campus tap into (PMKVY, DDU-GKY, State schemes)?", "mr": "कौशल्य कॅम्पस कोणत्या सरकारी योजनांशी जोडेल (PMKVY, DDU-GKY, राज्य योजना)?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 2: Student Profile & Admission  |  विभाग २: विद्यार्थी प्रोफाइल आणि प्रवेश",
            "questions": [
                {"en": "Minimum educational qualification for admission (per skill type)?", "mr": "प्रवेशासाठी किमान शैक्षणिक पात्रता (कौशल्य प्रकारानुसार)?", "type": "PARAGRAPH"},
                {"en": "Target age range for skill students?", "mr": "कौशल्य विद्यार्थ्यांसाठी लक्ष्यित वयोगट?", "type": "TEXT"},
                {"en": "Total student capacity at full operation?", "mr": "पूर्ण कार्यावर एकूण विद्यार्थी क्षमता?", "type": "TEXT"},
                {"en": "Will the Skill Campus primarily serve rural youth?", "mr": "कौशल्य कॅम्पस प्रामुख्याने ग्रामीण युवकांना सेवा देईल का?", "type": "RADIO", "options": ["Yes, primarily rural youth", "Mix of rural and urban", "No specific preference", "To be decided"]},
                {"en": "Programme duration per skill (short 3-month, 6-month, 1-year, 2-year)?", "mr": "प्रति कौशल्य कार्यक्रम कालावधी (लघु ३ महिने, ६ महिने, १ वर्ष, २ वर्षे)?", "type": "PARAGRAPH"},
                {"en": "Will there be a selection/screening process for admission to skill programmes?", "mr": "कौशल्य कार्यक्रमांसाठी प्रवेशाची निवड/स्क्रीनिंग प्रक्रिया असेल का?", "type": "PARAGRAPH"},
                {"en": "Will residential accommodation be provided to all skill students?", "mr": "सर्व कौशल्य विद्यार्थ्यांना निवासाची सोय उपलब्ध असेल का?", "type": "RADIO", "options": ["Yes, all skill students residential", "Optional residential", "Day scholars only", "Mix", "To be decided"]},
            ]
        },
        {
            "title": "Section 3: Campus Service Integration  |  विभाग ३: कॅम्पस सेवा एकत्रीकरण",
            "questions": [
                {"en": "Which campus services will skill students provide as part of their live training?", "mr": "प्रशिक्षणाचा भाग म्हणून कौशल्य विद्यार्थी कोणत्या कॅम्पस सेवा पुरवतील?", "type": "CHECKBOX", "options": ["Canteen / food service", "Laundry services", "Barber / hair & beauty services", "Plumbing & electrical maintenance", "Gardening & horticulture", "IT support & helpdesk", "Healthcare assistance (nursing/first aid)", "Construction & civil maintenance", "Security services", "Animal husbandry assistance", "Housekeeping for residential areas", "Event management support"]},
                {"en": "Will skill students be compensated for campus services rendered?", "mr": "कॅम्पस सेवांसाठी कौशल्य विद्यार्थ्यांना भरपाई मिळेल का?", "type": "RADIO", "options": ["Yes, paid in Deepa Coins", "Yes, paid in cash/stipend", "Yes, as fee waiver/reduction", "No, part of training requirement", "To be decided"]},
                {"en": "How will service quality from skill students be monitored and graded?", "mr": "कौशल्य विद्यार्थ्यांकडून सेवेची गुणवत्ता कशी तपासली आणि श्रेणीबद्ध केली जाईल?", "type": "PARAGRAPH"},
                {"en": "Will campus service hours count towards certification hours?", "mr": "कॅम्पस सेवा तास प्रमाणपत्र तासांसाठी गणले जातील का?", "type": "RADIO", "options": ["Yes, fully count", "Yes, partially count", "No, separate", "To be decided"]},
                {"en": "Who supervises skill students providing campus services — industry trainers, campus supervisors, or both?", "mr": "कॅम्पस सेवा पुरवणाऱ्या कौशल्य विद्यार्थ्यांवर कोण देखरेख करते — उद्योग प्रशिक्षक, कॅम्पस पर्यवेक्षक, किंवा दोन्ही?", "type": "RADIO", "options": ["Industry trainers", "Campus supervisors", "Both", "To be decided"]},
            ]
        },
        {
            "title": "Section 4: Infrastructure & Training Workshops  |  विभाग ४: पायाभूत सुविधा आणि प्रशिक्षण कार्यशाळा",
            "questions": [
                {"en": "How many training workshops/labs are needed for Phase 1 (15 skill units)?", "mr": "टप्पा १ साठी (१५ कौशल्य युनिट) किती प्रशिक्षण कार्यशाळा/लॅब लागतील?", "type": "TEXT"},
                {"en": "What is the standard size of each training workshop (sq. ft.)?", "mr": "प्रत्येक प्रशिक्षण कार्यशाळेचा मानक आकार (चौ. फुट)?", "type": "TEXT"},
                {"en": "Detailed equipment/tools requirement for top 5 priority skill units?", "mr": "शीर्ष ५ प्राधान्य कौशल्य युनिट्ससाठी सविस्तर उपकरणे/साधनांची आवश्यकता?", "type": "PARAGRAPH"},
                {"en": "Will there be a demonstration kitchen for culinary/food service skills?", "mr": "स्वयंपाक/अन्न सेवा कौशल्यांसाठी प्रात्यक्षिक स्वयंपाकघर असेल का?", "type": "RADIO", "options": ["Yes, fully equipped demonstration kitchen", "Basic cooking lab", "Use main campus canteen kitchen", "No", "To be decided"]},
                {"en": "Beauty/salon training unit — full salon setup with equipment?", "mr": "सौंदर्य/सलून प्रशिक्षण युनिट — उपकरणांसह पूर्ण सलून सेटअप?", "type": "RADIO", "options": ["Yes, professional salon setup", "Basic training unit", "No", "To be decided"]},
                {"en": "IT training lab for basic computer skills — size, software, internet access?", "mr": "मूलभूत संगणक कौशल्यांसाठी IT प्रशिक्षण लॅब — आकार, सॉफ्टवेअर, इंटरनेट प्रवेश?", "type": "PARAGRAPH"},
                {"en": "Construction/civil trades training area — size, tools, safety equipment?", "mr": "बांधकाम/सिव्हिल ट्रेड प्रशिक्षण क्षेत्र — आकार, साधने, सुरक्षा उपकरणे?", "type": "PARAGRAPH"},
                {"en": "Will skill workshops be accessible to the surrounding community for upskilling (evenings/weekends)?", "mr": "कौशल्य वर्कशॉप आसपासच्या समुदायासाठी कौशल्य वाढवण्यासाठी (संध्याकाळ/आठवडे अखेर) उपलब्ध असतील का?", "type": "RADIO", "options": ["Yes, community access programme", "Occasionally for special programmes", "No, students only", "To be decided"]},
            ]
        },
        {
            "title": "Section 5: Placement, Entrepreneurship & Impact  |  विभाग ५: नियुक्ती, उद्योजकता आणि प्रभाव",
            "questions": [
                {"en": "Will there be a dedicated placement cell?", "mr": "समर्पित नियुक्ती कक्ष असेल का?", "type": "RADIO", "options": ["Yes, dedicated placement cell", "Shared with education division", "Industry partners handle placement", "No formal placement support", "To be decided"]},
                {"en": "Target placement rate within 3 months of programme completion?", "mr": "कार्यक्रम पूर्ण झाल्यानंतर ३ महिन्यांत लक्ष्यित नियुक्ती दर?", "type": "TEXT"},
                {"en": "Which industries/companies will be targeted as placement partners?", "mr": "कोणत्या उद्योग/कंपन्यांना नियुक्ती भागीदार म्हणून लक्ष्यित केले जाईल?", "type": "PARAGRAPH"},
                {"en": "Will there be entrepreneurship support — startup incubation, micro-credit, mentoring?", "mr": "उद्योजकता सहाय्य असेल का — स्टार्टअप इनक्युबेशन, मायक्रो-क्रेडिट, मार्गदर्शन?", "type": "CHECKBOX", "options": ["Startup incubation programme", "Micro-credit / seed funding links", "Business plan competition", "Mentoring by successful entrepreneurs", "Market linkage support", "No formal entrepreneurship support"]},
                {"en": "How will impact be measured (placement rate, income increase, business starts)?", "mr": "प्रभाव कसा मोजला जाईल (नियुक्ती दर, उत्पन्न वाढ, व्यवसाय सुरुवात)?", "type": "PARAGRAPH"},
                {"en": "Will skill graduates be given preference for employment within Club Deeper campus services?", "mr": "कौशल्य पदवीधरांना क्लब डीपर कॅम्पस सेवांमध्ये रोजगारासाठी प्राधान्य दिले जाईल का?", "type": "RADIO", "options": ["Yes, first preference", "Yes, equal consideration", "No formal preference", "To be decided"]},
                {"en": "Fee structure — will skill programmes be subsidised or free for rural students?", "mr": "शुल्क रचना — कौशल्य कार्यक्रम ग्रामीण विद्यार्थ्यांसाठी अनुदानित किंवा मुफ्त असतील का?", "type": "PARAGRAPH"},
                {"en": "Any other important requirements or ideas for the Skill Campus?", "mr": "कौशल्य कॅम्पससाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा कल्पना?", "type": "PARAGRAPH"},
            ]
        },
    ]
}

SOFTWARE_PARK = {
    "index": 6,
    "title": "Club Deeper – Software Development Park Planning Questionnaire",
    "active": False,
    "description": (
        "Comprehensive planning questionnaire for the Software Development Park at Club Deeper Campus.\n\n"
        "क्लब डीपर सॉफ्टवेअर डेव्हलपमेंट पार्कसाठी सर्वसमावेशक नियोजन प्रश्नावली."
    ),
    "sections": [
        {
            "title": "Section 1: Vision, Model & Purpose  |  विभाग १: दृष्टी, मॉडेल आणि उद्देश",
            "questions": [
                {"en": "What is the primary purpose and vision of the Software Development Park?", "mr": "सॉफ्टवेअर डेव्हलपमेंट पार्कचा प्राथमिक उद्देश आणि दृष्टी काय आहे?", "type": "PARAGRAPH"},
                {"en": "What are the multiple roles this park will play?", "mr": "हे पार्क कोणकोणती भूमिका बजावेल?", "type": "CHECKBOX", "options": ["Training centre for software/IT skills (for skill students)", "Development centre for Club Deeper's own ERP (Eduval)", "Incubator for student/faculty startups", "Commercial co-working space (revenue from external companies)", "Research & development centre", "Remote work facility for professionals in the residential community"]},
                {"en": "Will external companies be invited to set up satellite offices here?", "mr": "बाह्य कंपन्यांना येथे उपग्रह कार्यालये स्थापन करण्यासाठी आमंत्रित केले जाईल का?", "type": "RADIO", "options": ["Yes, primary revenue model", "Yes, secondary income", "No, internal use only", "To be decided"]},
                {"en": "What technology domains/verticals will be the focus?", "mr": "कोणते तंत्रज्ञान क्षेत्र/वर्टिकल्स केंद्रबिंदू असतील?", "type": "CHECKBOX", "options": ["Web & Mobile Development", "Artificial Intelligence & ML", "EdTech solutions", "HealthTech & Hospital Management", "AgriTech", "Cybersecurity", "Data Analytics & BI", "ERP & Enterprise Software", "No specific focus — all domains"]},
                {"en": "What is the long-term vision — a mini IT park, a training hub, or both?", "mr": "दीर्घकालीन दृष्टी काय आहे — एक मिनी IT पार्क, प्रशिक्षण केंद्र, किंवा दोन्ही?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 2: Infrastructure & Technical Setup  |  विभाग २: पायाभूत सुविधा आणि तांत्रिक व्यवस्था",
            "questions": [
                {"en": "Total workstation/seating capacity planned?", "mr": "एकूण वर्कस्टेशन/बैठक क्षमता नियोजित?", "type": "TEXT"},
                {"en": "Internet bandwidth requirement (minimum)?", "mr": "इंटरनेट बँडविड्थ आवश्यकता (किमान)?", "type": "RADIO", "options": ["100 Mbps", "500 Mbps", "1 Gbps dedicated leased line", "Above 1 Gbps", "To be decided"]},
                {"en": "Will there be a dedicated on-premise server room / data centre?", "mr": "समर्पित ऑन-प्रिमाइस सर्व्हर रूम / डेटा सेंटर असेल का?", "type": "RADIO", "options": ["Yes, full on-premise data centre", "Yes, small server room", "Cloud-only, no on-premise hardware", "Hybrid (edge server + cloud)", "To be decided"]},
                {"en": "Power requirement and backup (UPS, generator) — 24/7 uptime expected?", "mr": "वीज आवश्यकता आणि बॅकअप — 24/7 अपटाइम अपेक्षित आहे का?", "type": "PARAGRAPH"},
                {"en": "Meeting and collaboration rooms — how many, capacity, video conferencing setup?", "mr": "बैठक आणि सहयोग कक्ष — किती, क्षमता, व्हिडिओ कॉन्फरन्सिंग व्यवस्था?", "type": "PARAGRAPH"},
                {"en": "Will the park operate 24/7 or business hours only?", "mr": "पार्क 24/7 कार्य करेल की केवळ कामाच्या वेळेत?", "type": "RADIO", "options": ["24/7 for residential developers", "Standard business hours (9 AM – 7 PM)", "Extended hours (7 AM – 11 PM)", "To be decided"]},
                {"en": "Amenities required — pantry, lounge, nap rooms, recreation area?", "mr": "आवश्यक सुविधा — पॅन्ट्री, लाउंज, नॅप रूम, मनोरंजन क्षेत्र?", "type": "PARAGRAPH"},
                {"en": "Will there be a hardware/maker lab (3D printers, electronics workbenches)?", "mr": "हार्डवेअर/मेकर लॅब (3D प्रिंटर, इलेक्ट्रॉनिक्स वर्कबेंच) असेल का?", "type": "RADIO", "options": ["Yes", "No", "Future phase", "To be decided"]},
            ]
        },
        {
            "title": "Section 3: Training, Talent & Startup Ecosystem  |  विभाग ३: प्रशिक्षण, प्रतिभा आणि स्टार्टअप इकोसिस्टम",
            "questions": [
                {"en": "What IT/software skills will be taught to Skill Campus students here?", "mr": "येथे कौशल्य कॅम्पस विद्यार्थ्यांना कोणती IT/सॉफ्टवेअर कौशल्ये शिकवली जातील?", "type": "PARAGRAPH"},
                {"en": "What certifications will students earn (industry certificates, government NSQF, etc.)?", "mr": "विद्यार्थी कोणती प्रमाणपत्रे मिळवतील (उद्योग प्रमाणपत्रे, सरकारी NSQF इ.)?", "type": "PARAGRAPH"},
                {"en": "Will there be a startup incubation programme — duration, mentoring, seed funding?", "mr": "स्टार्टअप इनक्युबेशन कार्यक्रम असेल का — कालावधी, मार्गदर्शन, बीज निधी?", "type": "PARAGRAPH"},
                {"en": "Will Eduval (Club Deeper's software partner) have a permanent development office here?", "mr": "Eduval (क्लब डीपरचे सॉफ्टवेअर भागीदार) येथे कायमस्वरूपी विकास कार्यालय असेल का?", "type": "RADIO", "options": ["Yes, dedicated Eduval office", "Shared space", "No, Eduval works remotely", "To be decided"]},
                {"en": "Revenue model for the park (co-working fees, training fees, product revenue, grants)?", "mr": "पार्कसाठी महसूल मॉडेल (को-वर्किंग शुल्क, प्रशिक्षण शुल्क, उत्पादन महसूल, अनुदान)?", "type": "PARAGRAPH"},
                {"en": "Any other important requirements or ideas for the Software Development Park?", "mr": "सॉफ्टवेअर डेव्हलपमेंट पार्कसाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा कल्पना?", "type": "PARAGRAPH"},
            ]
        },
    ]
}

if __name__ == "__main__":
    run_batch("Skill Campus", [SKILL_CAMPUS, SOFTWARE_PARK])
