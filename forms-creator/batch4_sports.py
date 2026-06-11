"""
Club Deeper – Batch 4: SPORT & CULTURAL CENTER
Projects: Cricket & Football Ground, Indoor Games Facility, Gymnasium & Swimming Pool

Run:  python3 batch4_sports.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import run_batch

CRICKET_FOOTBALL = {
    "index": 12,
    "title": "Club Deeper – Cricket & Football Ground Planning Questionnaire",
    "active": False,
    "description": (
        "Comprehensive planning questionnaire for Cricket and Football facilities at Club Deeper Campus.\n\n"
        "क्लब डीपर क्रिकेट आणि फुटबॉल मैदानासाठी सर्वसमावेशक नियोजन प्रश्नावली."
    ),
    "sections": [
        {
            "title": "Section 1: Cricket Ground – Vision & Standards  |  विभाग १: क्रिकेट मैदान – दृष्टी आणि मानके",
            "questions": [
                {"en": "What standard of cricket ground is planned?", "mr": "क्रिकेट मैदानाचे कोणते मानक नियोजित आहे?", "type": "RADIO", "options": ["Full international-standard ground (135m x 135m)", "District/State level competition ground", "School/college level ground", "Practice ground with multiple pitch strips", "To be decided"]},
                {"en": "What pitch surface is preferred?", "mr": "खेळपट्टीचा कोणता पृष्ठभाग पसंत आहे?", "type": "RADIO", "options": ["Natural turf (red soil)", "Natural turf (black cotton soil)", "Synthetic/artificial turf pitch", "Main turf + synthetic practice pitches", "To be decided"]},
                {"en": "How many practice pitches / nets are planned? Covered or open?", "mr": "किती सराव खेळपट्ट्या / नेट्स नियोजित आहेत? झाकलेल्या किंवा उघड्या?", "type": "TEXT"},
                {"en": "Will there be a bowling machine in the nets?", "mr": "नेट्समध्ये बॉलिंग मशीन असेल का?", "type": "RADIO", "options": ["Yes", "No", "Future phase", "To be decided"]},
                {"en": "Floodlights/lights for evening play — planned?", "mr": "संध्याकाळच्या खेळासाठी फ्लडलाइट्स/दिवे — नियोजित?", "type": "RADIO", "options": ["Yes, full floodlights (LED)", "Yes, basic lighting", "No", "To be decided"]},
                {"en": "Outfield surface — natural grass, artificial turf, or gravel/mud?", "mr": "आउटफील्ड पृष्ठभाग — नैसर्गिक गवत, कृत्रिम टर्फ, किंवा खडी/माती?", "type": "RADIO", "options": ["Natural grass outfield (irrigated)", "Artificial turf outfield", "Compacted clay/mud", "To be decided"]},
                {"en": "Boundary — permanent concrete wall, rope, or portable boards?", "mr": "बाउंड्री — कायमस्वरूपी काँक्रीट भिंत, दोरी, किंवा पोर्टेबल बोर्ड?", "type": "RADIO", "options": ["Permanent concrete boundary wall with ad panels", "Rope boundary on pegs", "Portable advertising boards", "To be decided"]},
            ]
        },
        {
            "title": "Section 2: Cricket Academy & Operations  |  विभाग २: क्रिकेट अकादमी आणि संचालन",
            "questions": [
                {"en": "Will there be a cricket coaching academy?", "mr": "क्रिकेट कोचिंग अकादमी असेल का?", "type": "RADIO", "options": ["Yes, full-time residential academy", "Yes, part-time / weekend coaching", "Yes, integrated with school PE programme", "No", "To be decided"]},
                {"en": "What level of tournaments will be hosted?", "mr": "कोणत्या स्तराच्या स्पर्धा आयोजित केल्या जातील?", "type": "CHECKBOX", "options": ["School/college inter-campus tournaments", "District level tournaments", "State level (BCCI affiliated)", "Corporate/community leagues", "Annual Club Deeper invitational", "No formal tournaments planned"]},
                {"en": "Spectator seating capacity required?", "mr": "प्रेक्षक बैठक क्षमता आवश्यक?", "type": "RADIO", "options": ["No permanent seating (temporary chairs for events)", "Small permanent stand (200–500)", "Medium stand (500–2000)", "To be decided"]},
                {"en": "Scoreboard — manual, electronic, or digital LED?", "mr": "स्कोअरबोर्ड — मॅन्युअल, इलेक्ट्रॉनिक, किंवा डिजिटल LED?", "type": "RADIO", "options": ["Manual scoreboard", "Electronic scoreboard", "Digital LED display", "To be decided"]},
                {"en": "Will external teams/clubs be allowed to use the ground (rental revenue)?", "mr": "बाह्य संघ/क्लबांना मैदान वापरण्याची परवानगी असेल का (भाडे महसूल)?", "type": "RADIO", "options": ["Yes, primary revenue stream", "Yes, when campus is not using", "No, campus exclusive", "To be decided"]},
                {"en": "Player facilities — changing rooms, showers, equipment store, umpire room?", "mr": "खेळाडू सुविधा — चेंजिंग रूम, शॉवर, उपकरण स्टोर, पंच कक्ष?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 3: Football Ground  |  विभाग ३: फुटबॉल मैदान",
            "questions": [
                {"en": "What standard of football ground is planned?", "mr": "फुटबॉल मैदानाचे कोणते मानक नियोजित आहे?", "type": "RADIO", "options": ["FIFA standard (105m x 68m)", "Standard club/school level (90m x 60m)", "Recreational/informal", "To be decided"]},
                {"en": "Turf surface for football ground?", "mr": "फुटबॉल मैदानासाठी टर्फ पृष्ठभाग?", "type": "RADIO", "options": ["Natural grass (irrigated)", "Artificial turf (FIFA approved)", "Artificial turf (basic)", "Compacted clay/mud", "To be decided"]},
                {"en": "Will there be a separate 5-a-side / futsal court?", "mr": "वेगळे ५-वि-५ / फुटसल कोर्ट असेल का?", "type": "RADIO", "options": ["Yes", "No", "To be decided"]},
                {"en": "Goal posts — permanent or portable?", "mr": "गोलपोस्ट — कायमस्वरूपी किंवा पोर्टेबल?", "type": "RADIO", "options": ["Permanent fixed goal posts", "Portable/movable", "To be decided"]},
                {"en": "Will the football ground share space with cricket outfield or be separate?", "mr": "फुटबॉल मैदान क्रिकेट आउटफील्डशी जागा सामायिक करेल का की वेगळे असेल?", "type": "RADIO", "options": ["Completely separate ground", "Shared outfield area (used alternately)", "To be decided"]},
                {"en": "Football coaching programme — school students, community, or dedicated club?", "mr": "फुटबॉल कोचिंग कार्यक्रम — शाळा विद्यार्थी, समुदाय, किंवा समर्पित क्लब?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 4: Athletics, Other Outdoor & Maintenance  |  विभाग ४: अॅथलेटिक्स, इतर मैदानी आणि देखभाल",
            "questions": [
                {"en": "Will there be an athletics / running track? Full 400m or shorter?", "mr": "अॅथलेटिक्स / धावण्याचा ट्रॅक असेल का? पूर्ण ४०० मीटर किंवा लहान?", "type": "RADIO", "options": ["Full 400m track (synthetic)", "Full 400m track (cinder/clay)", "200m track", "Simple running path (not a formal track)", "No track", "To be decided"]},
                {"en": "Other outdoor courts — basketball, volleyball, kabaddi, kho-kho?", "mr": "इतर मैदानी कोर्ट — बास्केटबॉल, व्हॉलीबॉल, कबड्डी, खो-खो?", "type": "PARAGRAPH"},
                {"en": "Groundsman / maintenance plan — full-time groundsman, equipment?", "mr": "मैदान कर्मचारी / देखभाल योजना — पूर्णवेळ मैदान कर्मचारी, उपकरणे?", "type": "PARAGRAPH"},
                {"en": "Irrigation system for grounds — drip, sprinkler, or manual watering?", "mr": "मैदानासाठी सिंचन प्रणाली — ठिबक, स्प्रिंकलर, किंवा मॅन्युअल पाणी देणे?", "type": "RADIO", "options": ["Automatic sprinkler system", "Drip irrigation", "Manual watering by staff", "To be decided"]},
                {"en": "Annual maintenance budget estimate for all outdoor sports facilities?", "mr": "सर्व मैदानी क्रीडा सुविधांसाठी वार्षिक देखभाल बजेट अंदाज?", "type": "TEXT"},
                {"en": "Any other important requirements or ideas for outdoor sports?", "mr": "मैदानी क्रीडासाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा कल्पना?", "type": "PARAGRAPH"},
            ]
        },
    ]
}

INDOOR_GAMES = {
    "index": 13,
    "title": "Club Deeper – Indoor Games Facility Planning Questionnaire",
    "active": False,
    "description": (
        "Comprehensive planning questionnaire for the Indoor Games Facility at Club Deeper Campus.\n\n"
        "क्लब डीपर इनडोअर गेम्स सुविधेसाठी सर्वसमावेशक नियोजन प्रश्नावली."
    ),
    "sections": [
        {
            "title": "Section 1: Sports & Games Mix  |  विभाग १: क्रीडा आणि खेळ मिश्रण",
            "questions": [
                {"en": "Which indoor sports will be accommodated? (Select all planned)", "mr": "कोणते इनडोअर क्रीडा सामावले जातील? (सर्व नियोजित निवडा)", "type": "CHECKBOX", "options": ["Badminton", "Table Tennis", "Squash", "Basketball (indoor)", "Volleyball (indoor)", "Kabaddi (indoor)", "Boxing / Martial Arts / Taekwondo", "Wrestling / Kushti", "Gymnastics", "Carrom", "Chess", "Billiards / Snooker", "Archery range", "Shooting range (air rifle)"]},
                {"en": "How many badminton courts are needed? BWF standard or recreational?", "mr": "किती बॅडमिंटन कोर्ट लागतील? BWF मानक किंवा मनोरंजनाचे?", "type": "TEXT"},
                {"en": "How many table tennis tables are needed?", "mr": "किती टेबल टेनिस टेबल लागतील?", "type": "TEXT"},
                {"en": "Will there be a squash court? How many?", "mr": "स्क्वॉश कोर्ट असेल का? किती?", "type": "TEXT"},
                {"en": "Will the facility be used for competitive tournaments or primarily recreational?", "mr": "सुविधा स्पर्धात्मक स्पर्धांसाठी वापरली जाईल की प्रामुख्याने मनोरंजनासाठी?", "type": "RADIO", "options": ["Both competitive and recreational", "Competitive primarily", "Recreational primarily", "To be decided"]},
                {"en": "Will the indoor hall be multi-purpose (events, exams, cultural programmes)?", "mr": "इनडोअर हॉल बहुउद्देशीय (कार्यक्रम, परीक्षा, सांस्कृतिक कार्यक्रम) असेल का?", "type": "RADIO", "options": ["Yes, fully multi-purpose", "Yes, but sports-primary", "No, sports only", "To be decided"]},
            ]
        },
        {
            "title": "Section 2: Infrastructure & Technical  |  विभाग २: पायाभूत सुविधा आणि तांत्रिक",
            "questions": [
                {"en": "Total area required for the main indoor sports hall (sq. ft.)?", "mr": "मुख्य इनडोअर स्पोर्ट्स हॉलसाठी आवश्यक एकूण क्षेत्रफळ (चौ. फुट)?", "type": "TEXT"},
                {"en": "Flooring specification per sport area?", "mr": "प्रति क्रीडा क्षेत्र फ्लोअरिंग तपशील?", "type": "PARAGRAPH"},
                {"en": "Ceiling height requirement (badminton needs minimum 9m clear height)?", "mr": "छताची उंची आवश्यकता (बॅडमिंटनला किमान ९ मीटर स्पष्ट उंची लागते)?", "type": "TEXT"},
                {"en": "Ventilation and climate control — natural, fans, evaporative cooling, or AC?", "mr": "वायुवीजन आणि हवामान नियंत्रण — नैसर्गिक, पंखे, इव्हॅपोरेटिव्ह कूलिंग, किंवा AC?", "type": "RADIO", "options": ["Natural ventilation only", "Ceiling fans + natural", "Evaporative cooling", "Full air conditioning", "To be decided"]},
                {"en": "Lighting specification for sports (lux levels for badminton, TT, boxing)?", "mr": "क्रीडासाठी प्रकाश तपशील (बॅडमिंटन, TT, बॉक्सिंगसाठी lux पातळी)?", "type": "PARAGRAPH"},
                {"en": "Spectator seating — permanent, retractable, or no seating?", "mr": "प्रेक्षक बैठक — कायमस्वरूपी, मागे घेता येणारे, किंवा बैठक नाही?", "type": "RADIO", "options": ["Permanent tiered seating", "Retractable/foldable bleachers", "No permanent seating (chairs arranged for events)", "To be decided"]},
                {"en": "Equipment storage room — size, lockable, humidity controlled?", "mr": "उपकरण स्टोरेज रूम — आकार, लॉक करण्यायोग्य, आर्द्रता नियंत्रित?", "type": "TEXT"},
                {"en": "Changing rooms and showers — male/female, how many cubicles?", "mr": "चेंजिंग रूम आणि शॉवर — पुरुष/महिला, किती क्युबिकल?", "type": "TEXT"},
            ]
        },
        {
            "title": "Section 3: Coaching, Access & Operations  |  विभाग ३: कोचिंग, प्रवेश आणि संचालन",
            "questions": [
                {"en": "Will there be formal coaching programmes for badminton, TT, squash?", "mr": "बॅडमिंटन, TT, स्क्वॉशसाठी औपचारिक कोचिंग कार्यक्रम असतील का?", "type": "PARAGRAPH"},
                {"en": "Who will have access — students only, campus community, external (paid)?", "mr": "कोणाला प्रवेश असेल — केवळ विद्यार्थी, कॅम्पस समुदाय, बाहेरील (सशुल्क)?", "type": "RADIO", "options": ["Students only", "All campus residents", "Campus residents + external paid members", "Open to public (revenue model)", "To be decided"]},
                {"en": "Will Deepa Coins be used for booking courts and equipment rental?", "mr": "कोर्ट बुकिंग आणि उपकरण भाड्यासाठी दीपा कॉईन्स वापरले जातील का?", "type": "RADIO", "options": ["Yes", "No, free access", "To be decided"]},
                {"en": "Operating hours?", "mr": "कार्य तास?", "type": "TEXT"},
                {"en": "Any other important requirements or ideas for the Indoor Games Facility?", "mr": "इनडोअर गेम्स सुविधेसाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा कल्पना?", "type": "PARAGRAPH"},
            ]
        },
    ]
}

GYM_POOL = {
    "index": 14,
    "title": "Club Deeper – Gymnasium & Swimming Pool Planning Questionnaire",
    "active": False,
    "description": (
        "Comprehensive planning questionnaire for the Gymnasium and Swimming Pool at Club Deeper Campus.\n\n"
        "क्लब डीपर जिम्नॅशियम आणि जलतरण तलावासाठी सर्वसमावेशक नियोजन प्रश्नावली."
    ),
    "sections": [
        {
            "title": "Section 1: Swimming Pool  |  विभाग १: जलतरण तलाव",
            "questions": [
                {"en": "What size swimming pool is planned?", "mr": "कोणत्या आकाराचा जलतरण तलाव नियोजित आहे?", "type": "RADIO", "options": ["Olympic size (50m x 25m)", "Semi-Olympic (25m x 12.5m)", "Recreational pool (20m x 10m)", "Both competition pool + learner pool", "To be decided"]},
                {"en": "Will there be a separate shallow pool/toddler pool for beginners and children?", "mr": "नवशिक्या आणि मुलांसाठी वेगळा उथळ तलाव/टॉडलर पूल असेल का?", "type": "RADIO", "options": ["Yes, dedicated learner/children's pool", "Yes, shallow end in main pool only", "No", "To be decided"]},
                {"en": "Indoor (covered) or outdoor (open) pool?", "mr": "इनडोअर (झाकलेला) किंवा आउटडोअर (उघडा) तलाव?", "type": "RADIO", "options": ["Indoor covered pool", "Outdoor open pool", "Both", "To be decided"]},
                {"en": "Water treatment system — chlorination, salt water, UV, or ozone?", "mr": "पाणी शुद्धीकरण प्रणाली — क्लोरीनेशन, मीठ पाणी, UV, किंवा ओझोन?", "type": "RADIO", "options": ["Traditional chlorination", "Salt water chlorination", "UV + chlorine combination", "Ozone treatment", "To be decided"]},
                {"en": "Who will have pool access?", "mr": "तलावात कोणाला प्रवेश असेल?", "type": "CHECKBOX", "options": ["School students (PE programme)", "Coaching centre students", "Skill campus students", "Residential families / bungalow owners", "General public (paid)", "All campus residents"]},
                {"en": "Will there be a formal swimming coaching and lifeguard training programme?", "mr": "औपचारिक जलतरण कोचिंग आणि जीवरक्षक प्रशिक्षण कार्यक्रम असेल का?", "type": "RADIO", "options": ["Yes, full coaching programme for all ages", "Yes, basic beginner lessons only", "No", "To be decided"]},
                {"en": "Safety plan — certified lifeguards, CCTV, anti-slip, pool cover?", "mr": "सुरक्षा योजना — प्रमाणित जीवरक्षक, CCTV, अँटी-स्लिप, तलाव झाकण?", "type": "PARAGRAPH"},
                {"en": "Changing rooms for pool — male/female, how many cubicles, showers?", "mr": "तलावासाठी चेंजिंग रूम — पुरुष/महिला, किती क्युबिकल, शॉवर?", "type": "TEXT"},
                {"en": "Pool deck / spectator area — chairs, shade, F&B kiosk?", "mr": "पूल डेक / प्रेक्षक क्षेत्र — खुर्च्या, सावली, F&B कियोस्क?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 2: Gymnasium / Fitness Centre  |  विभाग २: जिम्नॅशियम / फिटनेस सेंटर",
            "questions": [
                {"en": "Who will the gymnasium serve?", "mr": "जिम्नॅशियम कोणाला सेवा देईल?", "type": "CHECKBOX", "options": ["School and coaching students", "Skill campus students", "Campus teaching staff", "All campus staff", "Residential bungalow families", "General public (paid membership)"]},
                {"en": "Target simultaneous user capacity?", "mr": "एकाच वेळी वापरकर्त्यांची लक्ष्यित क्षमता?", "type": "TEXT"},
                {"en": "What equipment categories are planned?", "mr": "कोणत्या उपकरण श्रेणी नियोजित आहेत?", "type": "CHECKBOX", "options": ["Cardio machines (treadmill, cycle, elliptical, rowing)", "Free weights (dumbbells, barbells, weight plates)", "Selectorised weight training machines", "Cable machines", "Functional training rig / pull-up bars", "Stretching / foam rolling area", "Boxing bags and speed bags", "CrossFit / HIIT zone"]},
                {"en": "Will there be a separate women's section or mixed gym?", "mr": "वेगळा महिला विभाग असेल की मिश्र जिम?", "type": "RADIO", "options": ["Mixed gym (all genders)", "Separate women's section", "Separate timing for women (not separate space)", "To be decided"]},
                {"en": "Will there be certified personal trainers / fitness instructors on staff?", "mr": "कर्मचारी वर्गात प्रमाणित वैयक्तिक प्रशिक्षक / फिटनेस प्रशिक्षक असतील का?", "type": "RADIO", "options": ["Yes, full-time", "Yes, part-time", "No", "To be decided"]},
                {"en": "Yoga and meditation hall — dedicated room, outdoor platform, or part of gym?", "mr": "योग आणि ध्यान हॉल — समर्पित खोली, मैदानी व्यासपीठ, किंवा जिमचा भाग?", "type": "RADIO", "options": ["Dedicated indoor yoga hall", "Outdoor yoga / meditation platform", "Both", "Yoga classes in gym space (no separate room)", "To be decided"]},
                {"en": "Membership structure — daily, monthly, quarterly, annual? Deepa Coins accepted?", "mr": "सदस्यत्व रचना — दैनंदिन, मासिक, त्रैमासिक, वार्षिक? दीपा कॉईन्स स्वीकारले जातात?", "type": "PARAGRAPH"},
                {"en": "Total gym area required (sq. ft.)?", "mr": "एकूण जिम क्षेत्र आवश्यक (चौ. फुट)?", "type": "TEXT"},
                {"en": "Any other important requirements or ideas for the gym and pool?", "mr": "जिम आणि तलावासाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा कल्पना?", "type": "PARAGRAPH"},
            ]
        },
    ]
}

if __name__ == "__main__":
    run_batch("Sport & Cultural Center", [CRICKET_FOOTBALL, INDOOR_GAMES, GYM_POOL])
