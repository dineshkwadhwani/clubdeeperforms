"""
Club Deeper – Batch 6: SUSTAINABILITY
Projects: Agriculture & Horticulture, Animal Husbandry, Campus Canteen & Food Services

Run:  python3 batch6_sustainability.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import run_batch

AGRICULTURE = {
    "index": 17,
    "title": "Club Deeper – Agriculture & Horticulture Planning Questionnaire",
    "active": False,
    "description": (
        "Comprehensive planning questionnaire for the Agriculture and Horticulture programme at Club Deeper Campus.\n\n"
        "क्लब डीपर शेती आणि फलोत्पादन कार्यक्रमासाठी सर्वसमावेशक नियोजन प्रश्नावली."
    ),
    "sections": [
        {
            "title": "Section 1: Vision, Land Use & Crops  |  विभाग १: दृष्टी, जमीन वापर आणि पिके",
            "questions": [
                {"en": "What is the primary purpose of the farm?", "mr": "शेताचा प्राथमिक उद्देश काय आहे?", "type": "CHECKBOX", "options": ["Feed the campus (self-sufficiency goal)", "Training ground for Skill Campus students", "Research and demonstration for Rural Development", "Revenue generation (sell surplus produce)", "Community-supported agriculture for residential families", "All of the above"]},
                {"en": "How many acres of the 50-acre campus will be dedicated to agriculture/horticulture?", "mr": "५० एकर कॅम्पसपैकी किती एकर शेती/फलोत्पादनासाठी समर्पित असतील?", "type": "TEXT"},
                {"en": "What crops are planned for the food garden / kitchen garden?", "mr": "खाद्य बाग / किचन बागेत कोणती पिके नियोजित आहेत?", "type": "PARAGRAPH"},
                {"en": "What fruit orchards are planned?", "mr": "कोणत्या फळांच्या बागा नियोजित आहेत?", "type": "PARAGRAPH"},
                {"en": "Will there be a dedicated medicinal plant / herb garden?", "mr": "समर्पित औषधी वनस्पती / औषधी वनस्पती बाग असेल का?", "type": "RADIO", "options": ["Yes, dedicated medicinal garden", "Yes, small section in main garden", "No", "To be decided"]},
                {"en": "What farming method is preferred?", "mr": "शेतीची कोणती पद्धत पसंत आहे?", "type": "RADIO", "options": ["Certified organic (no chemicals)", "Natural farming (zero budget)", "Integrated farming (minimal inputs)", "Conventional with some organic practices", "To be decided"]},
                {"en": "Will there be a poly-house / greenhouse for year-round production?", "mr": "वर्षभर उत्पादनासाठी पॉली-हाऊस / ग्रीनहाऊस असेल का?", "type": "RADIO", "options": ["Yes, full greenhouse setup", "Yes, small poly-house for seedlings", "No", "To be decided"]},
                {"en": "Hydroponics / vertical farming — planned as part of the programme?", "mr": "हायड्रोपोनिक्स / उभी शेती — कार्यक्रमाचा भाग म्हणून नियोजित?", "type": "RADIO", "options": ["Yes, hydroponics unit", "Yes, vertical farming unit", "Both", "No", "To be decided"]},
            ]
        },
        {
            "title": "Section 2: Water, Infrastructure & Equipment  |  विभाग २: पाणी, पायाभूत सुविधा आणि उपकरणे",
            "questions": [
                {"en": "Water source for irrigation — borewell, rainwater harvesting, Khadakwasla lift irrigation?", "mr": "सिंचनासाठी पाण्याचा स्रोत — बोअरवेल, पावसाचे पाणी संकलन, खडकवासला लिफ्ट सिंचन?", "type": "CHECKBOX", "options": ["Borewell on campus", "Rainwater harvesting tanks", "Khadakwasla Backwater lift irrigation (official sanction)", "Treated grey water reuse from campus", "Drip from existing water supply"]},
                {"en": "Irrigation method planned?", "mr": "नियोजित सिंचन पद्धत?", "type": "RADIO", "options": ["Drip irrigation throughout", "Sprinkler irrigation", "Flood irrigation (furrow)", "Mix of drip and sprinkler", "To be decided"]},
                {"en": "What farm equipment / machinery is needed?", "mr": "कोणत्या शेती उपकरणे / यंत्रसामग्री लागतील?", "type": "PARAGRAPH"},
                {"en": "Composting facility — size, method (aerobic, vermicompost, biogas)?", "mr": "कंपोस्टिंग सुविधा — आकार, पद्धत (एरोबिक, व्हर्मिकंपोस्ट, बायोगॅस)?", "type": "PARAGRAPH"},
                {"en": "Farm storage — cold storage for produce, seed storage, equipment shed?", "mr": "शेत साठवण — उत्पादनासाठी शीत साठवण, बीज साठवण, उपकरण शेड?", "type": "PARAGRAPH"},
                {"en": "Soil testing plan — frequency, which lab, remediation if needed?", "mr": "माती परीक्षण योजना — वारंवारता, कोणती प्रयोगशाळा, आवश्यक असल्यास उपाय?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 3: Training, Research & Community  |  विभाग ३: प्रशिक्षण, संशोधन आणि समुदाय",
            "questions": [
                {"en": "Which Skill Campus students will train here and what will they learn?", "mr": "कोणते कौशल्य कॅम्पस विद्यार्थी येथे प्रशिक्षण घेतील आणि ते काय शिकतील?", "type": "PARAGRAPH"},
                {"en": "Will school students have regular farm visits / agricultural education?", "mr": "शाळेतील विद्यार्थ्यांना नियमित शेत भेटी / कृषी शिक्षण असेल का?", "type": "RADIO", "options": ["Yes, regular curriculum-linked visits", "Yes, optional extra-curricular", "No", "To be decided"]},
                {"en": "Will resident families be offered kitchen garden plots for self-growing?", "mr": "रहिवासी कुटुंबांना स्वत: उगवण्यासाठी किचन बाग भूखंड दिले जातील का?", "type": "RADIO", "options": ["Yes, individual resident kitchen garden plots", "Shared community vegetable garden", "No", "To be decided"]},
                {"en": "Farmer demonstration plots for Rural Development Centre — planned?", "mr": "ग्रामीण विकास केंद्रासाठी शेतकरी प्रात्यक्षिक भूखंड — नियोजित?", "type": "RADIO", "options": ["Yes, dedicated demonstration plots", "Yes, general farm serves this purpose", "No", "To be decided"]},
                {"en": "Will there be an Agri-tech lab / sensor-based smart farming demonstration?", "mr": "Agri-tech लॅब / सेन्सर-आधारित स्मार्ट शेती प्रात्यक्षिक असेल का?", "type": "RADIO", "options": ["Yes", "No", "Future phase", "To be decided"]},
                {"en": "How will surplus farm produce be managed?", "mr": "अतिरिक्त शेत उत्पादन कसे व्यवस्थापित केले जाईल?", "type": "RADIO", "options": ["Sell to external market", "Distribute to surrounding villages", "Use in campus canteen only", "All of the above", "To be decided"]},
                {"en": "Full-time farm manager / agronomist required? Qualifications?", "mr": "पूर्णवेळ शेत व्यवस्थापक / कृषीशास्त्रज्ञ आवश्यक? पात्रता?", "type": "PARAGRAPH"},
                {"en": "Budget for farm setup (Year 1) and annual operating cost?", "mr": "शेत उभारणीसाठी (वर्ष १) आणि वार्षिक संचालन खर्चाचे बजेट?", "type": "TEXT"},
                {"en": "Any other important requirements or ideas for Agriculture & Horticulture?", "mr": "शेती आणि फलोत्पादनासाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा कल्पना?", "type": "PARAGRAPH"},
            ]
        },
    ]
}

ANIMAL_HUSBANDRY = {
    "index": 18,
    "title": "Club Deeper – Animal Husbandry Planning Questionnaire",
    "active": False,
    "description": (
        "Comprehensive planning questionnaire for Animal Husbandry at Club Deeper Campus.\n\n"
        "क्लब डीपर पशुपालनासाठी सर्वसमावेशक नियोजन प्रश्नावली."
    ),
    "sections": [
        {
            "title": "Section 1: Vision, Animals & Purpose  |  विभाग १: दृष्टी, प्राणी आणि उद्देश",
            "questions": [
                {"en": "What is the primary purpose of the animal husbandry programme?", "mr": "पशुपालन कार्यक्रमाचा प्राथमिक उद्देश काय आहे?", "type": "CHECKBOX", "options": ["Campus food supply (milk, eggs, poultry)", "Skill training (dairy, poultry, aquaculture)", "Rural development demonstration for farmers", "Revenue generation (sell products)", "Research and breed improvement", "All of the above"]},
                {"en": "Which animal categories are planned?", "mr": "कोणत्या प्राणी श्रेणी नियोजित आहेत?", "type": "CHECKBOX", "options": ["Dairy cattle (local / HF / Jersey)", "Goat farming", "Poultry (layer hens for eggs)", "Poultry (broilers for meat)", "Duck farming", "Fish / aquaculture (pond)", "Bee keeping / apiculture", "Pig farming", "Rabbit farming"]},
                {"en": "Number of animals planned at start (by category)?", "mr": "सुरुवातीला नियोजित प्राण्यांची संख्या (श्रेणीनुसार)?", "type": "PARAGRAPH"},
                {"en": "Daily milk production target from the dairy unit?", "mr": "डेअरी युनिटमधून दैनंदिन दूध उत्पादनाचे लक्ष्य?", "type": "TEXT"},
                {"en": "Will animal products supply the campus canteen exclusively or also sell outside?", "mr": "प्राणी उत्पादने केवळ कॅम्पस कॅन्टीनला पुरवतील की बाहेरही विकतील?", "type": "RADIO", "options": ["Campus canteen exclusively", "Campus first, surplus sold outside", "Both campus and external market", "To be decided"]},
            ]
        },
        {
            "title": "Section 2: Infrastructure & Veterinary  |  विभाग २: पायाभूत सुविधा आणि पशुवैद्यकीय",
            "questions": [
                {"en": "Land area allocated for animal husbandry?", "mr": "पशुपालनासाठी जमीन क्षेत्र दिले गेले आहे?", "type": "TEXT"},
                {"en": "Cattle shed design — size, materials, ventilation, drainage?", "mr": "गोठ्याची रचना — आकार, साहित्य, वायुवीजन, निचरा?", "type": "PARAGRAPH"},
                {"en": "Poultry shed — deep litter or cage system? Size? Biosecurity measures?", "mr": "कुक्कुटपालन शेड — डीप लिटर किंवा पिंजरा प्रणाली? आकार? जैवसुरक्षा उपाय?", "type": "PARAGRAPH"},
                {"en": "Aquaculture ponds — number, size, fish species planned?", "mr": "मत्स्यपालन तलाव — संख्या, आकार, नियोजित मासे प्रजाती?", "type": "PARAGRAPH"},
                {"en": "Fodder production — will campus land be used to grow green fodder?", "mr": "चारा उत्पादन — हिरवा चारा वाढवण्यासाठी कॅम्पसची जमीन वापरली जाईल का?", "type": "RADIO", "options": ["Yes, dedicated fodder plots on campus", "Purchase fodder from outside", "Mix", "To be decided"]},
                {"en": "Milk processing — pasteurisation, chilling, packaging on-site?", "mr": "दूध प्रक्रिया — पाश्चरायझेशन, थंड करणे, ऑन-साइट पॅकेजिंग?", "type": "PARAGRAPH"},
                {"en": "Veterinary care — full-time vet, visiting vet, or tie-up with government vet services?", "mr": "पशुवैद्यकीय सेवा — पूर्णवेळ पशुवैद्य, भेट देणारे पशुवैद्य, किंवा सरकारी पशुवैद्य सेवांशी करार?", "type": "RADIO", "options": ["Full-time resident vet", "Part-time / visiting vet", "Government vet services tie-up", "To be decided"]},
                {"en": "Waste management — biogas from animal waste, slurry for organic farming?", "mr": "कचरा व्यवस्थापन — प्राणी कचऱ्यापासून बायोगॅस, सेंद्रिय शेतीसाठी स्लरी?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 3: Training & Operations  |  विभाग ३: प्रशिक्षण आणि संचालन",
            "questions": [
                {"en": "Which skill students will train in this unit and in what competencies?", "mr": "या युनिटमध्ये कोणते कौशल्य विद्यार्थी प्रशिक्षण घेतील आणि कोणत्या क्षमतांमध्ये?", "type": "PARAGRAPH"},
                {"en": "Staffing — how many herdsmen, poultry workers, fish farm workers needed?", "mr": "कर्मचारी — किती गुराखी, कुक्कुटपालन कामगार, मत्स्यपालन कामगार लागतील?", "type": "TEXT"},
                {"en": "Annual revenue target from animal products (milk, eggs, fish, honey)?", "mr": "प्राणी उत्पादनांतून (दूध, अंडी, मासे, मध) वार्षिक महसूल लक्ष्य?", "type": "TEXT"},
                {"en": "Any other important requirements or ideas for Animal Husbandry?", "mr": "पशुपालनासाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा कल्पना?", "type": "PARAGRAPH"},
            ]
        },
    ]
}

CANTEEN = {
    "index": 19,
    "title": "Club Deeper – Campus Canteen & Food Services Planning Questionnaire",
    "active": False,
    "description": (
        "Comprehensive planning questionnaire for Campus Canteen and Food Services at Club Deeper.\n\n"
        "क्लब डीपर कॅम्पस कॅन्टीन आणि अन्न सेवांसाठी सर्वसमावेशक नियोजन प्रश्नावली."
    ),
    "sections": [
        {
            "title": "Section 1: Scope, Capacity & Service Points  |  विभाग १: व्याप्ती, क्षमता आणि सेवा बिंदू",
            "questions": [
                {"en": "Who are all the dining constituencies to be served from this kitchen?", "mr": "या स्वयंपाकघरातून कोणत्या जेवणाच्या घटकांना सेवा दिली जाईल?", "type": "CHECKBOX", "options": ["School students (residential)", "School students (day scholars — mid-day meal)", "Coaching centre students", "Skill campus students", "All teaching and non-teaching staff", "Residential bungalow families (optional delivery)", "Old Age Home residents", "Training centre participants", "Construction workers during project phase"]},
                {"en": "Total daily covers (meals served) at peak capacity?", "mr": "कमाल क्षमतेवर दैनंदिन एकूण कव्हर (जेवण दिले)?", "type": "TEXT"},
                {"en": "How many distinct canteen / dining halls are needed across campus?", "mr": "कॅम्पसमध्ये किती वेगळ्या कॅन्टीन / जेवण हॉलची आवश्यकता आहे?", "type": "RADIO", "options": ["One centralised mega dining hall", "One main + one hostel dining", "Separate dining per zone (school, skill, staff)", "Multiple small canteens distributed across campus", "To be decided"]},
                {"en": "Meal schedule — how many meals per day, at what times?", "mr": "जेवणाचे वेळापत्रक — दिवसातून किती जेवण, कोणत्या वेळी?", "type": "PARAGRAPH"},
                {"en": "Will there be a separate staff dining area?", "mr": "कर्मचाऱ्यांसाठी वेगळे जेवण क्षेत्र असेल का?", "type": "RADIO", "options": ["Yes, separate staff canteen", "Staff eat in same hall (different section)", "Staff arrange own meals", "To be decided"]},
            ]
        },
        {
            "title": "Section 2: Kitchen Infrastructure  |  विभाग २: स्वयंपाकघर पायाभूत सुविधा",
            "questions": [
                {"en": "Total kitchen area required (sq. ft.)?", "mr": "एकूण स्वयंपाकघर क्षेत्र आवश्यक (चौ. फुट)?", "type": "TEXT"},
                {"en": "Kitchen fuel source — PNG (Piped Natural Gas), LPG bulk, induction, or mix?", "mr": "स्वयंपाकघर इंधन स्रोत — PNG (पाइप्ड नॅचरल गॅस), LPG बल्क, इंडक्शन, किंवा मिश्र?", "type": "RADIO", "options": ["PNG (preferred for safety and cost)", "LPG bulk supply", "Commercial induction cooking", "Mix of LPG + induction", "Solar cooking + backup LPG", "To be decided"]},
                {"en": "Bulk cooking equipment required (industrial steamers, tilting pans, bulk cookers)?", "mr": "बल्क स्वयंपाक उपकरणे आवश्यक (औद्योगिक स्टीमर, टिल्टिंग पॅन, बल्क कुकर)?", "type": "PARAGRAPH"},
                {"en": "Cold storage and refrigeration — walk-in cold room, freezers, vegetable storage?", "mr": "शीत साठवण आणि रेफ्रिजरेशन — वॉक-इन कोल्ड रूम, फ्रीझर, भाजीपाला साठवण?", "type": "PARAGRAPH"},
                {"en": "Dry goods storage area — size, pest control, FIFO tracking?", "mr": "कोरड्या वस्तू साठवण क्षेत्र — आकार, कीटक नियंत्रण, FIFO ट्रॅकिंग?", "type": "PARAGRAPH"},
                {"en": "Dishwashing — manual, semi-automatic, or commercial dishwashing machine?", "mr": "भांडी धुणे — मॅन्युअल, अर्ध-स्वयंचलित, किंवा व्यावसायिक डिशवॉशिंग मशीन?", "type": "RADIO", "options": ["Commercial automatic dishwasher", "Semi-automatic with hot water system", "Manual dishwashing by staff", "To be decided"]},
                {"en": "Waste management from kitchen — bio-gas plant from food waste, composting?", "mr": "स्वयंपाकघरातून कचरा व्यवस्थापन — खाद्य कचऱ्यापासून बायोगॅस प्लांट, कंपोस्टिंग?", "type": "PARAGRAPH"},
                {"en": "Water requirement for kitchen — litres per day estimate?", "mr": "स्वयंपाकघरासाठी पाण्याची आवश्यकता — दररोज लिटरचा अंदाज?", "type": "TEXT"},
            ]
        },
        {
            "title": "Section 3: Deepa Coin System & Menu  |  विभाग ३: दीपा कॉईन प्रणाली आणि मेनू",
            "questions": [
                {"en": "How will the Deepa Coin system work for meal payments?", "mr": "जेवण देयकांसाठी दीपा कॉईन प्रणाली कशी कार्य करेल?", "type": "PARAGRAPH"},
                {"en": "How will students / staff load Deepa Coins (online, at kiosk, from parents)?", "mr": "विद्यार्थी / कर्मचारी दीपा कॉईन्स कसे लोड करतील (ऑनलाइन, कियोस्कवर, पालकांकडून)?", "type": "PARAGRAPH"},
                {"en": "Will there be a fixed meal plan or à la carte ordering?", "mr": "निश्चित मील प्लान असेल का किंवा à la carte ऑर्डरिंग?", "type": "RADIO", "options": ["Fixed thali / meal plan (no choice)", "Fixed plan + choice of 1–2 items", "Full à la carte via app/kiosk", "Hybrid: fixed plan weekdays, choice weekends", "To be decided"]},
                {"en": "Dietary menu requirements?", "mr": "आहारविषयक मेनू आवश्यकता?", "type": "CHECKBOX", "options": ["Vegetarian only (all meals)", "Jain meals on request", "Diabetic / special diet for elderly", "High-protein meals for sports students", "Allergen labelling mandatory", "Region-specific (Maharashtrian cuisine priority)"]},
                {"en": "What is the target meal cost per student per day (all meals)?", "mr": "प्रति विद्यार्थी प्रतिदिन लक्ष्यित जेवण खर्च (सर्व जेवण)?", "type": "TEXT"},
                {"en": "FSSAI registration and food safety audit plan?", "mr": "FSSAI नोंदणी आणि अन्न सुरक्षा ऑडिट योजना?", "type": "PARAGRAPH"},
                {"en": "Who will manage canteen operations — in-house team, Skill Campus students, or outsourced?", "mr": "कॅन्टीन संचालन कोण व्यवस्थापित करेल — इन-हाऊस टीम, कौशल्य कॅम्पस विद्यार्थी, किंवा बाहेरून?", "type": "RADIO", "options": ["In-house professional team", "Skill Campus students under supervision", "Outsourced caterer", "Mix: in-house chef + skill student support", "To be decided"]},
                {"en": "Any other important requirements or ideas for Campus Canteen & Food Services?", "mr": "कॅम्पस कॅन्टीन आणि अन्न सेवांसाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा कल्पना?", "type": "PARAGRAPH"},
            ]
        },
    ]
}

if __name__ == "__main__":
    run_batch("Sustainability", [AGRICULTURE, ANIMAL_HUSBANDRY, CANTEEN])
