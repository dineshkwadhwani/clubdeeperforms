"""
Club Deeper – Batch 7: INFRASTRUCTURE
Project: Internal Roads & Campus Infrastructure

Run:  python3 batch7_infrastructure.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import run_batch

INFRASTRUCTURE = {
    "index": 20,
    "title": "Club Deeper – Internal Roads & Campus Infrastructure Planning Questionnaire",
    "active": False,
    "description": (
        "Comprehensive planning questionnaire for Campus-wide Infrastructure at Club Deeper.\n\n"
        "क्लब डीपर कॅम्पसव्यापी पायाभूत सुविधांसाठी सर्वसमावेशक नियोजन प्रश्नावली."
    ),
    "sections": [
        {
            "title": "Section 1: Roads & Circulation  |  विभाग १: रस्ते आणि वाहतूक",
            "questions": [
                {"en": "What is the total internal road length planned across the 50-acre campus?", "mr": "५० एकर कॅम्पसमध्ये नियोजित एकूण अंतर्गत रस्त्याची लांबी किती?", "type": "TEXT"},
                {"en": "What road widths are planned for main spine road, secondary roads, and service lanes?", "mr": "मुख्य रस्ता, दुय्यम रस्ते आणि सेवा मार्गांसाठी कोणती रस्त्याची रुंदी नियोजित आहे?", "type": "PARAGRAPH"},
                {"en": "Road surface material for main internal roads?", "mr": "मुख्य अंतर्गत रस्त्यांसाठी रस्त्याचे पृष्ठभाग साहित्य?", "type": "RADIO", "options": ["Bituminous/asphalt (blacktop)", "Concrete (PQC)", "Interlocking paving blocks", "Gravel (for farm/service roads)", "Mix depending on zone", "To be decided"]},
                {"en": "Will footpaths / pedestrian walkways be separate from vehicle roads throughout campus?", "mr": "कॅम्पसमध्ये पादचारी मार्ग वाहन रस्त्यांपासून वेगळे असतील का?", "type": "RADIO", "options": ["Yes, fully separated throughout", "Yes, in main zones only", "No, shared roads", "To be decided"]},
                {"en": "Will there be dedicated cycling tracks on campus?", "mr": "कॅम्पसवर समर्पित सायकल ट्रॅक असतील का?", "type": "RADIO", "options": ["Yes, full cycling network", "Yes, partial routes", "No", "To be decided"]},
                {"en": "What is the vehicle access policy on campus (private cars, shared EV carts, bikes)?", "mr": "कॅम्पसवर वाहन प्रवेश धोरण काय आहे (खाजगी कार, सामायिक EV कार्ट, बाइक)?", "type": "PARAGRAPH"},
                {"en": "Internal campus transport — will there be electric golf carts / shuttle buses?", "mr": "अंतर्गत कॅम्पस वाहतूक — इलेक्ट्रिक गोल्फ कार्ट / शटल बस असतील का?", "type": "RADIO", "options": ["Yes, EV golf carts throughout", "Yes, mini electric shuttle buses", "No, walking and cycling only", "To be decided"]},
                {"en": "Parking plan — zones, capacity, EV charging bays?", "mr": "पार्किंग योजना — क्षेत्र, क्षमता, EV चार्जिंग बे?", "type": "PARAGRAPH"},
                {"en": "Emergency vehicle access — fire engine and ambulance turning circles at each building?", "mr": "आपत्कालीन वाहन प्रवेश — प्रत्येक इमारतीत अग्निशामक दल आणि रुग्णवाहिका वळण वर्तुळे?", "type": "RADIO", "options": ["Yes, all buildings have emergency vehicle access", "Yes, main buildings only", "Not specifically planned", "To be decided"]},
                {"en": "Signage system on campus — wayfinding boards, building names, emergency signs?", "mr": "कॅम्पसवर साइनेज प्रणाली — मार्गदर्शन फलक, इमारतींची नावे, आपत्कालीन चिन्हे?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 2: Water Supply & Wastewater  |  विभाग २: पाणी पुरवठा आणि सांडपाणी",
            "questions": [
                {"en": "Primary water source for the campus?", "mr": "कॅम्पससाठी प्राथमिक पाण्याचा स्रोत?", "type": "CHECKBOX", "options": ["Borewell(s) on campus property", "Khadakwasla backwater lift irrigation line (official sanction needed)", "Government water supply (gram panchayat / MIDC)", "Rainwater harvesting (supplementary)", "Mix of sources"]},
                {"en": "Total daily water demand estimate (litres) at full campus capacity?", "mr": "पूर्ण कॅम्पस क्षमतेवर दैनंदिन एकूण पाण्याची मागणी (लिटर)?", "type": "TEXT"},
                {"en": "Water storage capacity — overhead tanks and underground sumps (total KL)?", "mr": "पाणी साठवण क्षमता — उच्च टाक्या आणि भूमिगत सम्प (एकूण KL)?", "type": "TEXT"},
                {"en": "Water treatment — filtration, RO for drinking water, UV disinfection?", "mr": "पाणी शुद्धीकरण — फिल्ट्रेशन, पिण्याच्या पाण्यासाठी RO, UV निर्जंतुकीकरण?", "type": "PARAGRAPH"},
                {"en": "STP (Sewage Treatment Plant) — capacity in KLD, technology (MBR, SBR, UASB)?", "mr": "STP (सांडपाणी प्रक्रिया प्लांट) — KLD मध्ये क्षमता, तंत्रज्ञान (MBR, SBR, UASB)?", "type": "PARAGRAPH"},
                {"en": "What will treated wastewater be reused for (irrigation, toilet flushing, gardening)?", "mr": "प्रक्रिया केलेले सांडपाणी कशासाठी पुनर्वापर केले जाईल (सिंचन, शौचालय फ्लशिंग, बागकाम)?", "type": "PARAGRAPH"},
                {"en": "Rainwater harvesting plan — rooftop collection, percolation pits, recharge wells?", "mr": "पावसाचे पाणी संकलन योजना — छतावर संकलन, गळती खड्डे, रिचार्ज विहिरी?", "type": "PARAGRAPH"},
                {"en": "Stormwater drainage — open drains, underground, or retention pond?", "mr": "पावसाचे पाणी निचरा — उघड्या नाल्या, भूमिगत, किंवा धारण तलाव?", "type": "RADIO", "options": ["Open concrete drains", "Underground stormwater pipes", "Retention pond / percolation", "Mix", "To be decided"]},
            ]
        },
        {
            "title": "Section 3: Power, Solar & Backup  |  विभाग ३: वीज, सौर आणि बॅकअप",
            "questions": [
                {"en": "Total connected load estimate for the entire campus (KVA)?", "mr": "संपूर्ण कॅम्पससाठी एकूण जोडलेल्या भाराचा अंदाज (KVA)?", "type": "TEXT"},
                {"en": "MSEDCL service connection — HT or LT? Dedicated feeder?", "mr": "MSEDCL सेवा कनेक्शन — HT किंवा LT? समर्पित फीडर?", "type": "RADIO", "options": ["HT connection (33KV or 11KV)", "LT connection (415V)", "Dedicated MSEDCL feeder", "To be decided"]},
                {"en": "Solar power target — how many KWp on rooftop?", "mr": "सौर ऊर्जा लक्ष्य — छतावर किती KWp?", "type": "TEXT"},
                {"en": "Will there be ground-mounted solar in addition to rooftop?", "mr": "छतावर सौर ऊर्जेव्यतिरिक्त जमिनीवर सौर ऊर्जा असेल का?", "type": "RADIO", "options": ["Yes, large ground-mount array", "Rooftop only", "To be decided"]},
                {"en": "DG generator sets — how many, total KVA, which loads on backup?", "mr": "DG जनरेटर सेट — किती, एकूण KVA, कोणत्या भारांना बॅकअप?", "type": "PARAGRAPH"},
                {"en": "Battery storage (BESS) for solar power — planned?", "mr": "सौर ऊर्जेसाठी बॅटरी स्टोरेज (BESS) — नियोजित?", "type": "RADIO", "options": ["Yes, large BESS for campus", "Yes, small BESS for critical loads", "No", "Future phase", "To be decided"]},
                {"en": "EV charging infrastructure — how many charging points, which zones?", "mr": "EV चार्जिंग पायाभूत सुविधा — किती चार्जिंग पॉइंट, कोणते क्षेत्र?", "type": "PARAGRAPH"},
                {"en": "Energy management system — smart metering, SCADA, campus energy dashboard?", "mr": "ऊर्जा व्यवस्थापन प्रणाली — स्मार्ट मीटरिंग, SCADA, कॅम्पस ऊर्जा डॅशबोर्ड?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 4: Digital Network, Security & Telecom  |  विभाग ४: डिजिटल नेटवर्क, सुरक्षा आणि दूरसंचार",
            "questions": [
                {"en": "Campus-wide fibre optic backbone — planned?", "mr": "कॅम्पसव्यापी फायबर ऑप्टिक बॅकबोन — नियोजित?", "type": "RADIO", "options": ["Yes, full underground fibre throughout", "Yes, fibre to each building, Wi-Fi inside", "Wi-Fi only (no structured cabling)", "To be decided"]},
                {"en": "Internet bandwidth requirement for the entire campus (at full capacity)?", "mr": "संपूर्ण कॅम्पससाठी इंटरनेट बँडविड्थ आवश्यकता (पूर्ण क्षमतेवर)?", "type": "RADIO", "options": ["100 Mbps", "500 Mbps", "1 Gbps dedicated leased line", "Multiple 1 Gbps lines (redundancy)", "To be decided"]},
                {"en": "Wi-Fi coverage — outdoor campus-wide or buildings only?", "mr": "Wi-Fi कव्हरेज — मैदानी कॅम्पसव्यापी किंवा केवळ इमारती?", "type": "RADIO", "options": ["Full outdoor + indoor Wi-Fi coverage", "All buildings + main common areas", "Buildings only", "To be decided"]},
                {"en": "CCTV surveillance — total camera count estimate, NVR storage, remote monitoring?", "mr": "CCTV पाळत — एकूण कॅमेरा संख्येचा अंदाज, NVR स्टोरेज, रिमोट मॉनिटरिंग?", "type": "PARAGRAPH"},
                {"en": "Access control — RFID / biometric entry at which zones (hostel, labs, server room, main gate)?", "mr": "प्रवेश नियंत्रण — कोणत्या क्षेत्रांवर RFID / बायोमेट्रिक प्रवेश (वसतिगृह, लॅब, सर्व्हर रूम, मुख्य दरवाजा)?", "type": "PARAGRAPH"},
                {"en": "PA (public address) system — campus-wide announcements, emergency sirens?", "mr": "PA (सार्वजनिक घोषणा) प्रणाली — कॅम्पसव्यापी घोषणा, आपत्कालीन सायरन?", "type": "PARAGRAPH"},
                {"en": "Campus-wide intercom / IP telephone system — needed?", "mr": "कॅम्पसव्यापी इंटरकॉम / IP टेलिफोन प्रणाली — आवश्यक?", "type": "RADIO", "options": ["Yes, full IP telephone system", "Yes, basic intercom only", "Mobile phones only (no fixed lines)", "To be decided"]},
                {"en": "Data centre / server room location and specifications?", "mr": "डेटा सेंटर / सर्व्हर रूमचे स्थान आणि तपशील?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 5: Waste, Environment & Green Building  |  विभाग ५: कचरा, पर्यावरण आणि हरित इमारत",
            "questions": [
                {"en": "Solid waste management plan — segregation, composting, recycling, disposal?", "mr": "घन कचरा व्यवस्थापन योजना — वेगळे करणे, कंपोस्टिंग, पुनर्वापर, विल्हेवाट?", "type": "PARAGRAPH"},
                {"en": "Biogas plant for organic campus waste — capacity?", "mr": "सेंद्रिय कॅम्पस कचऱ्यासाठी बायोगॅस प्लांट — क्षमता?", "type": "PARAGRAPH"},
                {"en": "Plastic-free campus policy — will single-use plastic be banned?", "mr": "प्लास्टिक-मुक्त कॅम्पस धोरण — एकवेळ वापरलेले प्लास्टिक बंदी असेल का?", "type": "RADIO", "options": ["Yes, complete ban from Day 1", "Yes, phased ban over 1 year", "No formal policy", "To be decided"]},
                {"en": "Green building certification target — GRIHA, LEED, or none?", "mr": "हरित इमारत प्रमाणपत्र लक्ष्य — GRIHA, LEED, किंवा नाही?", "type": "RADIO", "options": ["GRIHA 4-star or above", "LEED Gold or above", "Both", "Green features but no formal certification", "No green certification target", "To be decided"]},
                {"en": "Tree planting plan — how many trees, which species (native/fruit/shade)?", "mr": "वृक्ष लागवड योजना — किती झाडे, कोणती प्रजाती (स्थानिक/फळ/सावली)?", "type": "PARAGRAPH"},
                {"en": "Heat island mitigation — cool roofs, permeable paving, tree canopy targets?", "mr": "उष्णता बेट कमी करणे — थंड छत, पारगम्य फुटपाथ, वृक्ष छत लक्ष्य?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 6: Phasing, Cost & Project Management  |  विभाग ६: टप्पेवार, खर्च आणि प्रकल्प व्यवस्थापन",
            "questions": [
                {"en": "What infrastructure must be 100% complete before any building can be occupied (Phase 0)?", "mr": "कोणत्याही इमारतीत प्रवेश करण्यापूर्वी १००% पूर्ण होणे आवश्यक असलेल्या पायाभूत सुविधा (टप्पा ०)?", "type": "PARAGRAPH"},
                {"en": "Who is the appointed infrastructure consultant / project manager?", "mr": "नियुक्त पायाभूत सुविधा सल्लागार / प्रकल्प व्यवस्थापक कोण आहे?", "type": "TEXT"},
                {"en": "Estimated total infrastructure cost (roads, utilities, power, digital network) — Phase 1?", "mr": "अंदाजित एकूण पायाभूत सुविधा खर्च (रस्ते, उपयुक्तता, वीज, डिजिटल नेटवर्क) — टप्पा १?", "type": "TEXT"},
                {"en": "Is there a master plan / site development plan already prepared?", "mr": "आधीच मास्टर प्लान / साइट डेव्हलपमेंट प्लान तयार आहे का?", "type": "RADIO", "options": ["Yes, complete master plan ready", "Yes, preliminary concept plan only", "No, not yet started", "In progress"]},
                {"en": "Which external agencies / government departments need to be coordinated with for approvals?", "mr": "मंजुरीसाठी कोणत्या बाह्य संस्था / सरकारी विभागांशी समन्वय साधण्याची आवश्यकता आहे?", "type": "PARAGRAPH"},
                {"en": "Any other important requirements, concerns or ideas for Campus Infrastructure?", "mr": "कॅम्पस पायाभूत सुविधांसाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता, चिंता किंवा कल्पना?", "type": "PARAGRAPH"},
            ]
        },
    ]
}

if __name__ == "__main__":
    run_batch("Infrastructure", [INFRASTRUCTURE])
