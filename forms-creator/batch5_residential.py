"""
Club Deeper – Batch 5: RESIDENTIAL COMMUNITY
Projects: Residential Bungalow Complex, Clubhouse

Run:  python3 batch5_residential.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import run_batch

BUNGALOW = {
    "index": 15,
    "title": "Club Deeper – Residential Bungalow Complex Planning Questionnaire",
    "active": False,
    "description": (
        "Comprehensive planning questionnaire for the Residential Bungalow Complex at Club Deeper Campus.\n\n"
        "क्लब डीपर निवासी बंगला संकुलासाठी सर्वसमावेशक नियोजन प्रश्नावली."
    ),
    "sections": [
        {
            "title": "Section 1: Vision, Community Identity & Plot Design  |  विभाग १: दृष्टी, समुदाय ओळख आणि भूखंड रचना",
            "questions": [
                {"en": "What is the name and tagline of the residential community?", "mr": "निवासी समुदायाचे नाव आणि टॅगलाइन काय आहे?", "type": "TEXT"},
                {"en": "What is the vision for the community — who is it designed for?", "mr": "समुदायाची दृष्टी काय आहे — ते कोणासाठी डिझाइन केले आहे?", "type": "PARAGRAPH"},
                {"en": "Total number of bungalow plots planned?", "mr": "नियोजित बंगला भूखंडांची एकूण संख्या?", "type": "RADIO", "options": ["100–150 plots", "150–200 plots", "200–250 plots", "250–300 plots", "To be decided"]},
                {"en": "Plot sizes offered?", "mr": "उपलब्ध भूखंड आकार?", "type": "CHECKBOX", "options": ["1500 sq ft", "2000 sq ft", "2500 sq ft", "3000 sq ft", "3500 sq ft", "4000 sq ft and above", "Multiple sizes (mix)"]},
                {"en": "Will plots be sold with a constructed bungalow or as bare plots?", "mr": "भूखंड बांधलेल्या बंगल्यासह विकले जातील का किंवा रिकामे भूखंड?", "type": "RADIO", "options": ["Bare plots only (buyer builds own bungalow)", "Ready-to-move constructed bungalows", "Both options", "Plot + standard construction package", "To be decided"]},
                {"en": "What building footprint / FSI / construction area is permitted per plot?", "mr": "प्रति भूखंड कोणता बांधकाम ठसा / FSI / बांधकाम क्षेत्र परवानगी आहे?", "type": "TEXT"},
                {"en": "Will there be strict architectural guidelines / design code for all bungalows?", "mr": "सर्व बंगल्यांसाठी कडक स्थापत्य मार्गदर्शक / रचना संहिता असेल का?", "type": "RADIO", "options": ["Yes, strict uniform design code", "Yes, guidelines with flexibility", "No restrictions", "To be decided"]},
                {"en": "What is the phasing plan — Phase 1 plots, Phase 2 plots, Phase 3?", "mr": "टप्पेवार योजना काय आहे — टप्पा १ भूखंड, टप्पा २ भूखंड, टप्पा ३?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 2: Infrastructure Provided Per Plot  |  विभाग २: प्रति भूखंड पुरवलेली पायाभूत सुविधा",
            "questions": [
                {"en": "What infrastructure is provided to each plot boundary?", "mr": "प्रत्येक भूखंडाच्या सीमेपर्यंत कोणत्या पायाभूत सुविधा पुरवल्या जातात?", "type": "CHECKBOX", "options": ["Tarred concrete road frontage", "Water connection (metered)", "Electricity connection (metered)", "Ducted sewer line", "Storm water drain connection", "Underground telecom/internet duct", "Landscaped verge/footpath along road", "Dedicated EV charging provision"]},
                {"en": "What standard of internal roads within the complex (width, material)?", "mr": "संकुलातील अंतर्गत रस्त्यांचा मानक (रुंदी, साहित्य)?", "type": "PARAGRAPH"},
                {"en": "Street lighting — type and energy source?", "mr": "रस्त्यावरील प्रकाश — प्रकार आणि ऊर्जा स्रोत?", "type": "RADIO", "options": ["LED solar street lights", "Grid-powered LED lights", "Mix of solar and grid", "To be decided"]},
                {"en": "Landscaping of common areas — parks, tree-lined avenues, children's play zones?", "mr": "सामायिक क्षेत्रांचे भूदृश्य — उद्याने, वृक्षांनी वेढलेले मार्ग, मुलांचे खेळ क्षेत्र?", "type": "PARAGRAPH"},
                {"en": "Central water supply system — source, storage, treatment, pressure?", "mr": "केंद्रीय पाणी पुरवठा प्रणाली — स्रोत, साठवण, शुद्धीकरण, दाब?", "type": "PARAGRAPH"},
                {"en": "Will there be a dedicated electricity transformer for the residential complex?", "mr": "निवासी संकुलासाठी समर्पित वीज ट्रान्सफॉर्मर असेल का?", "type": "RADIO", "options": ["Yes, dedicated transformer", "Shared with campus", "To be decided"]},
                {"en": "Boundary wall / perimeter fencing for the entire complex?", "mr": "संपूर्ण संकुलासाठी सीमा भिंत / परिमिती कुंपण?", "type": "RADIO", "options": ["Full compound wall (6ft+ brick/RCC)", "Decorative iron railing with masonry pillars", "Green hedge / fencing", "To be decided"]},
                {"en": "Main entrance gate design — boom barrier, security cabin, visitor management?", "mr": "मुख्य प्रवेश द्वार रचना — बूम बॅरियर, सुरक्षा केबिन, अभ्यागत व्यवस्थापन?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 3: Community Rules, Governance & Lifestyle  |  विभाग ३: समुदाय नियम, प्रशासन आणि जीवनशैली",
            "questions": [
                {"en": "Who is the target buyer / resident profile?", "mr": "लक्ष्यित खरेदीदार / रहिवासी प्रोफाइल कोण आहे?", "type": "CHECKBOX", "options": ["DEEPER/Saad Manuskichi Foundation members (priority)", "Tumhi-Aamhi Palak members", "Club Deeper school/institution staff", "Like-minded families from Maharashtra", "NRI / returned Indians", "General public (open sale)"]},
                {"en": "What community rules / deed restrictions will apply?", "mr": "कोणते समुदाय नियम / डीड प्रतिबंध लागू होतील?", "type": "PARAGRAPH"},
                {"en": "Commercial activity restrictions — no shops, home offices allowed, rental rules?", "mr": "व्यावसायिक क्रियाकलाप प्रतिबंध — कोणती दुकाने नाहीत, घरातील कार्यालये परवानगी, भाडे नियम?", "type": "PARAGRAPH"},
                {"en": "Pet policy — allowed, restrictions, common pet park?", "mr": "पाळीव प्राणी धोरण — परवानगी, प्रतिबंध, सामायिक पाळीव प्राणी उद्यान?", "type": "PARAGRAPH"},
                {"en": "Residents' Welfare Association structure — when formed, elections, maintenance fund?", "mr": "रहिवासी कल्याण संघटना रचना — कधी स्थापन, निवडणुका, देखभाल निधी?", "type": "PARAGRAPH"},
                {"en": "Monthly maintenance charge (estimated) — what does it cover?", "mr": "मासिक देखभाल शुल्क (अंदाजित) — त्यात काय समाविष्ट आहे?", "type": "PARAGRAPH"},
                {"en": "Security system — 24-hour guards, ANPR cameras at gate, patrol?", "mr": "सुरक्षा प्रणाली — २४ तास रक्षक, दरवाजावर ANPR कॅमेरे, गस्त?", "type": "PARAGRAPH"},
                {"en": "Visitor management system — advance booking, QR code entry, biometric?", "mr": "अभ्यागत व्यवस्थापन प्रणाली — आगाऊ बुकिंग, QR कोड प्रवेश, बायोमेट्रिक?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 4: Pricing, Legal & Delivery  |  विभाग ४: किंमत, कायदेशीर आणि वितरण",
            "questions": [
                {"en": "Target plot price range per sq ft (Phase 1)?", "mr": "लक्ष्यित भूखंड किंमत श्रेणी प्रति चौ. फुट (टप्पा १)?", "type": "TEXT"},
                {"en": "What is included in the plot price?", "mr": "भूखंड किंमतीत काय समाविष्ट आहे?", "type": "CHECKBOX", "options": ["Plot registration charges", "All internal road and utility infrastructure", "Boundary wall around complex", "Club Deeper amenities membership (Clubhouse, gym, pool)", "Landscaping of common areas", "Nothing extra — bare plot only"]},
                {"en": "Payment plan structure — milestone-linked, EMI, bank loan tie-ups?", "mr": "भरणा योजना रचना — मैलाचा दगड-जोडलेली, EMI, बँक कर्ज करार?", "type": "PARAGRAPH"},
                {"en": "Expected timeline for Phase 1 plot delivery (fully developed with all infra)?", "mr": "टप्पा १ भूखंड वितरणाचा अपेक्षित कालावधी (सर्व पायाभूत सुविधांसह पूर्ण विकसित)?", "type": "TEXT"},
                {"en": "Legal structure of land sale — outright sale, long-term lease, development agreement?", "mr": "जमीन विक्रीची कायदेशीर रचना — स्पष्ट विक्री, दीर्घकालीन भाडेपट्टा, विकास करार?", "type": "RADIO", "options": ["Outright sale (full ownership transfer)", "Long-term lease (30/99 years)", "Development agreement with ownership on completion", "To be decided"]},
                {"en": "NA and layout approval status — current?", "mr": "NA आणि लेआउट मंजुरी स्थिती — सध्याची?", "type": "PARAGRAPH"},
                {"en": "Any other important requirements or ideas for the Residential Bungalow Complex?", "mr": "निवासी बंगला संकुलासाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा कल्पना?", "type": "PARAGRAPH"},
            ]
        },
    ]
}

CLUBHOUSE = {
    "index": 16,
    "title": "Club Deeper – Clubhouse Planning Questionnaire",
    "active": False,
    "description": (
        "Comprehensive planning questionnaire for the Clubhouse at Club Deeper Campus.\n\n"
        "क्लब डीपर क्लबहाऊससाठी सर्वसमावेशक नियोजन प्रश्नावली."
    ),
    "sections": [
        {
            "title": "Section 1: Vision, Character & Members  |  विभाग १: दृष्टी, चरित्र आणि सदस्य",
            "questions": [
                {"en": "What is the name and tagline for the Clubhouse?", "mr": "क्लबहाऊसचे नाव आणि टॅगलाइन काय आहे?", "type": "TEXT"},
                {"en": "What is the clubhouse's character / positioning?", "mr": "क्लबहाऊसचे चरित्र / पोझिशनिंग काय आहे?", "type": "RADIO", "options": ["Premium social club (high-end ambience)", "Family-friendly community club", "Informal gathering place for residents", "Multi-purpose event venue", "To be decided"]},
                {"en": "Who will have clubhouse membership?", "mr": "क्लबहाऊस सदस्यत्व कोणाकडे असेल?", "type": "CHECKBOX", "options": ["Bungalow plot owners (automatic)", "Club Deeper senior staff (included in employment)", "External paid members (revenue)", "Old Age Home residents", "Training Centre corporate clients (temporary)"]},
                {"en": "Membership tiers — individual, family, corporate, honorary?", "mr": "सदस्यत्व स्तर — वैयक्तिक, कुटुंब, कॉर्पोरेट, मानद?", "type": "PARAGRAPH"},
                {"en": "Annual membership fee structure?", "mr": "वार्षिक सदस्यत्व शुल्क रचना?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 2: Facilities & Spaces  |  विभाग २: सुविधा आणि जागा",
            "questions": [
                {"en": "What facilities must the clubhouse include?", "mr": "क्लबहाऊसमध्ये कोणत्या सुविधा असणे आवश्यक आहे?", "type": "CHECKBOX", "options": ["Fine dining restaurant", "Casual café / bistro", "Rooftop bar / lounge (if permitted)", "Banquet hall (weddings, private events)", "Outdoor party lawn / event space", "Swimming pool (club-exclusive)", "Indoor games room (billiards, carrom, chess, table tennis)", "Home theatre / screening room", "Reading lounge / library corner", "Business centre (workstations, meeting room)", "Spa and wellness centre", "Kids' activity room / crèche"]},
                {"en": "Banquet/event hall capacity — seated dinner, theatre, cocktail?", "mr": "बॅन्क्वेट/कार्यक्रम हॉलची क्षमता — बसलेले जेवण, थिएटर, कॉकटेल?", "type": "TEXT"},
                {"en": "Outdoor lawn / event space area?", "mr": "मैदानी लॉन / कार्यक्रम जागेचे क्षेत्र?", "type": "TEXT"},
                {"en": "Restaurant — what cuisine, seating capacity, bar (permitted)?", "mr": "रेस्टॉरंट — कोणते पाककृती, बैठक क्षमता, बार (परवानगी आहे)?", "type": "PARAGRAPH"},
                {"en": "Wellness / spa offerings — massage, steam, sauna, jacuzzi?", "mr": "वेलनेस / स्पा सेवा — मसाज, स्टीम, सॉना, जकुझी?", "type": "PARAGRAPH"},
                {"en": "Children's play and activity area inside clubhouse?", "mr": "क्लबहाऊसमध्ये मुलांचे खेळ आणि क्रियाकलाप क्षेत्र?", "type": "PARAGRAPH"},
                {"en": "Total built-up area of the clubhouse (sq. ft.)?", "mr": "क्लबहाऊसचे एकूण बांधकाम क्षेत्र (चौ. फुट)?", "type": "TEXT"},
            ]
        },
        {
            "title": "Section 3: Events, Operations & Revenue  |  विभाग ३: कार्यक्रम, संचालन आणि महसूल",
            "questions": [
                {"en": "Will the clubhouse be available for non-member private events (weddings, corporate events)?", "mr": "क्लबहाऊस गैर-सदस्य खाजगी कार्यक्रमांसाठी (लग्न, कॉर्पोरेट इव्हेंट) उपलब्ध असेल का?", "type": "RADIO", "options": ["Yes, major revenue stream", "Yes, only on off-peak days", "No, members only", "To be decided"]},
                {"en": "F&B operations — in-house team or outsourced (franchise, caterer)?", "mr": "F&B संचालन — इन-हाऊस टीम किंवा बाहेरून (फ्रँचाइझ, केटरर)?", "type": "RADIO", "options": ["In-house F&B team", "Outsourced to professional caterer", "Franchise brand for restaurant", "Mix", "To be decided"]},
                {"en": "Will Deepa Coins be accepted at the clubhouse?", "mr": "क्लबहाऊसमध्ये दीपा कॉईन्स स्वीकारले जातील का?", "type": "RADIO", "options": ["Yes, for all services", "Yes, for some services", "No", "To be decided"]},
                {"en": "Operating hours — standard, 24/7, or event-based?", "mr": "कार्य तास — मानक, २४/७, किंवा कार्यक्रम-आधारित?", "type": "TEXT"},
                {"en": "What community events / social programmes will be regularly hosted?", "mr": "नियमितपणे कोणते सामुदायिक कार्यक्रम / सामाजिक कार्यक्रम आयोजित केले जातील?", "type": "PARAGRAPH"},
                {"en": "Annual maintenance + staffing budget estimate?", "mr": "वार्षिक देखभाल + कर्मचारी बजेट अंदाज?", "type": "TEXT"},
                {"en": "Any other important requirements or ideas for the Clubhouse?", "mr": "क्लबहाऊससाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा कल्पना?", "type": "PARAGRAPH"},
            ]
        },
    ]
}

if __name__ == "__main__":
    run_batch("Residential Community", [BUNGALOW, CLUBHOUSE])
