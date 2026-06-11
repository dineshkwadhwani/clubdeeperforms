"""
Club Deeper – Batch 1: EDUCATION CAMPUS
Projects: CBSE/State School (K12), Coaching Center (NEET/JEE/CET),
          Library, Study Center (UPSC/MPSC)

Run:  python3 batch1_education.py
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import run_batch

# ═══════════════════════════════════════════════════════════════════
# PROJECT 1 — CBSE / STATE SCHOOL (K12)
# ═══════════════════════════════════════════════════════════════════
SCHOOL = {
    "index": 1,
    "title": "Club Deeper – CBSE/State School (K12) Planning Questionnaire",
    "active": True,
    "description": (
        "Comprehensive planning questionnaire for the CBSE/State School (Classes 5–12) "
        "at Club Deeper Campus. Please answer every question as thoroughly as possible.\n\n"
        "क्लब डीपर कॅम्पसमधील CBSE/राज्य शाळा (इयत्ता ५–१२) साठी सर्वसमावेशक नियोजन प्रश्नावली."
    ),
    "sections": [
        {
            "title": "Section 1: Vision, Identity & Philosophy  |  विभाग १: दृष्टी, ओळख आणि तत्त्वज्ञान",
            "questions": [
                {"en": "What is the proposed name of the school?", "mr": "शाळेचे प्रस्तावित नाव काय आहे?", "type": "TEXT"},
                {"en": "What is the school's vision statement (1–2 sentences)?", "mr": "शाळेचे ध्येय वाक्य काय आहे? (१–२ वाक्ये)", "type": "PARAGRAPH"},
                {"en": "What is the school's mission statement?", "mr": "शाळेचे अभियान वाक्य काय आहे?", "type": "PARAGRAPH"},
                {"en": "What are the 3–5 core values the school will be built upon?", "mr": "शाळा कोणत्या ३–५ मूल्यांवर उभी केली जाईल?", "type": "PARAGRAPH"},
                {"en": "What affiliation is preferred?", "mr": "कोणती संलग्नता अपेक्षित आहे?", "type": "RADIO", "options": ["CBSE only", "Maharashtra State Board only", "Both CBSE and State Board", "ICSE", "To be decided"]},
                {"en": "What is the intended brand positioning of the school?", "mr": "शाळेचे ब्रँड पोझिशनिंग काय असेल?", "type": "RADIO", "options": ["Elite residential, premium fees", "Quality education, moderate fees", "Affordable / rural-focused", "Mixed model", "To be decided"]},
                {"en": "What pedagogy focus is intended?", "mr": "शिक्षण पद्धतीचा केंद्रबिंदू काय असेल?", "type": "RADIO", "options": ["STEM-focused", "Arts & Humanities", "Sports excellence", "Holistic / no specific focus", "NEP 2020 competency-based", "To be decided"]},
                {"en": "What languages of instruction will be offered?", "mr": "शिक्षणाचे माध्यम कोणते असेल?", "type": "CHECKBOX", "options": ["English medium", "Marathi medium", "Semi-English", "Bilingual (English + Marathi)", "Hindi medium"]},
                {"en": "What is the target student demographic?", "mr": "लक्ष्यित विद्यार्थी वर्ग कोण आहे?", "type": "CHECKBOX", "options": ["Local rural students", "Urban students from Pune/PCMC", "Students from across Maharashtra", "NRI / international students", "All backgrounds equally"]},
                {"en": "What is the school motto (proposed)?", "mr": "शाळेचे ब्रीदवाक्य (प्रस्तावित) काय आहे?", "type": "TEXT"},
                {"en": "Will the school have a specific focus on any competitive exam preparation alongside regular schooling?", "mr": "नियमित शिक्षणासोबत शाळा कोणत्या स्पर्धा परीक्षांवर लक्ष केंद्रित करेल?", "type": "CHECKBOX", "options": ["NEET (Medical entrance)", "JEE (Engineering entrance)", "MHT-CET", "UPSC/MPSC foundation", "Olympiads (Math/Science)", "No specific focus"]},
                {"en": "What is the 5-year student strength target (year-by-year)?", "mr": "५ वर्षांचे विद्यार्थी संख्येचे वर्षनिहाय लक्ष्य काय आहे?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 2: Academic Structure & Curriculum  |  विभाग २: शैक्षणिक रचना आणि अभ्यासक्रम",
            "questions": [
                {"en": "Which classes will be offered at launch and what is the phased expansion plan?", "mr": "सुरुवातीला कोणत्या इयत्ता असतील आणि टप्पेवार विस्तार योजना काय आहे?", "type": "PARAGRAPH"},
                {"en": "How many sections per class? How many students per section?", "mr": "प्रति वर्ग किती तुकड्या? प्रति तुकडी किती विद्यार्थी?", "type": "TEXT"},
                {"en": "What streams will be offered at Classes 11–12?", "mr": "इयत्ता ११–१२ साठी कोणते प्रवाह उपलब्ध असतील?", "type": "CHECKBOX", "options": ["Science – PCM (Physics, Chemistry, Math)", "Science – PCB (Physics, Chemistry, Biology)", "Commerce with Math", "Commerce without Math", "Arts / Humanities", "Vocational streams (CBSE skill subjects)", "All streams"]},
                {"en": "Will NEET/JEE/MHT-CET coaching be integrated into the school timetable or run as a separate programme?", "mr": "NEET/JEE/MHT-CET कोचिंग शाळेच्या वेळापत्रकात एकत्रित असेल की वेगळ्या कार्यक्रमात?", "type": "RADIO", "options": ["Fully integrated into school timetable", "Separate after-school coaching programme", "Separate coaching centre will handle it", "Not planned", "To be decided"]},
                {"en": "Will the school follow NEP 2020 framework from launch?", "mr": "शाळा सुरुवातीपासून NEP 2020 अनुसरेल का?", "type": "RADIO", "options": ["Yes, fully from Day 1", "Gradual transition over 2–3 years", "No, follow existing CBSE/State curriculum", "To be decided"]},
                {"en": "What optional/elective subjects will be offered at the secondary level (Classes 9–10)?", "mr": "माध्यमिक स्तरावर (इयत्ता ९–१०) कोणते वैकल्पिक विषय उपलब्ध असतील?", "type": "PARAGRAPH"},
                {"en": "Will there be a vocational education stream (CBSE skill subjects) — IT, tourism, retail, agriculture, etc.?", "mr": "व्यावसायिक शिक्षण प्रवाह असेल का — IT, पर्यटन, किरकोळ, शेती इ.?", "type": "RADIO", "options": ["Yes, from Class 9 onwards", "Yes, from Class 11 onwards", "No", "To be decided"]},
                {"en": "How many working days per academic year? What are the school hours (start and end time)?", "mr": "शैक्षणिक वर्षात किती कार्य दिवस? शाळेचे वेळ काय असेल?", "type": "TEXT"},
                {"en": "What is the academic calendar structure?", "mr": "शैक्षणिक दिनदर्शिकेची रचना कशी असेल?", "type": "RADIO", "options": ["Annual (one set of board exams)", "Two-term system", "Three-term system", "Semester system", "To be decided"]},
                {"en": "What is the internal vs external assessment split for Classes 9–10 and Classes 11–12?", "mr": "इयत्ता ९–१० आणि ११–१२ साठी अंतर्गत आणि बाह्य मूल्यांकनाचे प्रमाण काय असेल?", "type": "PARAGRAPH"},
                {"en": "Will entrance/screening tests be conducted for admissions? For which classes?", "mr": "प्रवेशासाठी प्रवेश/स्क्रीनिंग परीक्षा होतील का? कोणत्या इयत्तांसाठी?", "type": "PARAGRAPH"},
                {"en": "Will there be provision for students with special educational needs (inclusive education)?", "mr": "विशेष शैक्षणिक गरजा असलेल्या विद्यार्थ्यांसाठी सर्वसमावेशक शिक्षणाची तरतूद असेल का?", "type": "RADIO", "options": ["Yes, full inclusive education with special educators", "Yes, limited support", "No", "To be decided"]},
                {"en": "Will there be gifted/advanced learner programmes for high-achieving students?", "mr": "उच्च कामगिरी करणाऱ्या विद्यार्थ्यांसाठी प्रतिभावान/प्रगत शिक्षार्थी कार्यक्रम असतील का?", "type": "RADIO", "options": ["Yes", "No", "To be decided"]},
                {"en": "What co-curricular activities will be mandatory vs optional?", "mr": "कोणत्या सह-अभ्यासक्रम क्रियाकलाप अनिवार्य विरुद्ध ऐच्छिक असतील?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 3: Classrooms & Teaching Spaces  |  विभाग ३: वर्गखोल्या आणि शिक्षण जागा",
            "questions": [
                {"en": "Total number of classrooms required at full capacity?", "mr": "पूर्ण क्षमतेवर एकूण किती वर्गखोल्या लागतील?", "type": "TEXT"},
                {"en": "What is the preferred standard classroom size (sq. ft.)?", "mr": "मानक वर्गखोलीचा पसंतीचा आकार (चौ. फुट)?", "type": "TEXT"},
                {"en": "What type of classroom furniture is preferred?", "mr": "वर्गखोलीतील फर्निचरचा पसंतीचा प्रकार कोणता?", "type": "RADIO", "options": ["Traditional fixed bench-desk", "Individual movable desks and chairs", "Tablet arm chairs", "Cluster/pod arrangement for group work", "Mix of traditional and flexible"]},
                {"en": "Will all classrooms have smart boards/interactive displays from Day 1?", "mr": "सर्व वर्गखोल्यांमध्ये पहिल्या दिवसापासून स्मार्ट बोर्ड/इंटरेक्टिव डिस्प्ले असतील का?", "type": "RADIO", "options": ["Yes, all classrooms from Day 1", "Phase 1: senior classes only (9–12)", "Phase 2 onwards for all classes", "No, whiteboards/blackboards only", "To be decided"]},
                {"en": "What AV equipment is needed per classroom?", "mr": "प्रति वर्गखोलीत कोणती AV उपकरणे लागतील?", "type": "CHECKBOX", "options": ["Projector and screen", "Interactive flat panel/smart board", "Document camera/visualiser", "Speakers and microphone", "Student response system (clickers)", "Wi-Fi access point", "CCTV camera"]},
                {"en": "What ventilation/climate system is preferred for classrooms?", "mr": "वर्गखोल्यांसाठी पसंतीची हवामान प्रणाली कोणती?", "type": "RADIO", "options": ["Natural cross-ventilation only", "Ceiling fans + natural ventilation", "Air conditioning for all classrooms", "AC for senior classes, fans for junior", "Evaporative cooling", "To be decided"]},
                {"en": "Will there be dedicated activity/breakout rooms for group projects and presentations?", "mr": "गट प्रकल्प आणि सादरीकरणासाठी समर्पित क्रियाकलाप/ब्रेकआउट कक्ष असतील का?", "type": "TEXT"},
                {"en": "How many seminar/conference rooms are needed for teacher meetings, parent meetings, and workshops?", "mr": "शिक्षक बैठका, पालक बैठका आणि कार्यशाळांसाठी किती परिसंवाद/परिषद कक्ष लागतील?", "type": "TEXT"},
                {"en": "Will classrooms have built-in student storage (lockers/cubbies)?", "mr": "वर्गखोल्यांमध्ये विद्यार्थ्यांसाठी बिल्ट-इन स्टोरेज (लॉकर/कपाट) असतील का?", "type": "RADIO", "options": ["Yes, in each classroom", "Separate locker room/corridor lockers", "No", "To be decided"]},
                {"en": "What is the preferred corridor/veranda width for the school building?", "mr": "शाळेच्या इमारतीसाठी पसंतीची कॉरिडॉर/व्हरांडा रुंदी किती?", "type": "TEXT"},
                {"en": "Will there be a dedicated room for music, art, dance — or will these share with regular classrooms?", "mr": "संगीत, कला, नृत्यासाठी समर्पित खोली असेल का — किंवा या नियमित वर्गखोल्यांसोबत सामायिक होतील?", "type": "RADIO", "options": ["Separate dedicated rooms for each", "Shared multi-purpose room for arts", "Use regular classrooms with movable furniture", "To be decided"]},
                {"en": "How many floors is the school building planned? Will there be a lift/elevator?", "mr": "शाळेच्या इमारतीला किती मजले नियोजित आहेत? लिफ्ट/एलिव्हेटर असेल का?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 4: Science, Technology & Specialised Labs  |  विभाग ४: विज्ञान, तंत्रज्ञान आणि विशेष प्रयोगशाळा",
            "questions": [
                {"en": "How many Physics labs are required? Separate for senior/junior? Capacity per lab?", "mr": "किती भौतिकशास्त्र प्रयोगशाळा लागतील? वरिष्ठ/कनिष्ठांसाठी वेगळ्या? प्रति प्रयोगशाळा क्षमता?", "type": "PARAGRAPH"},
                {"en": "How many Chemistry labs? What safety equipment is mandatory (fume hoods, fire extinguisher, eyewash)?", "mr": "किती रसायनशास्त्र प्रयोगशाळा? कोणती सुरक्षा उपकरणे अनिवार्य आहेत?", "type": "PARAGRAPH"},
                {"en": "How many Biology labs? What equipment (microscopes, specimens, biosafety)?", "mr": "किती जीवशास्त्र प्रयोगशाळा? कोणती उपकरणे (सूक्ष्मदर्शक, नमुने, जैवसुरक्षा)?", "type": "PARAGRAPH"},
                {"en": "Will there be a combined junior science lab for Classes 5–8?", "mr": "इयत्ता ५–८ साठी एकत्रित कनिष्ठ विज्ञान प्रयोगशाळा असेल का?", "type": "RADIO", "options": ["Yes, one combined lab", "No, separate subject labs from Class 5", "Shared with senior labs on schedule", "To be decided"]},
                {"en": "Will there be a dedicated research/project lab for senior students (Classes 11–12)?", "mr": "वरिष्ठ विद्यार्थ्यांसाठी (इयत्ता ११–१२) समर्पित संशोधन/प्रकल्प प्रयोगशाळा असेल का?", "type": "RADIO", "options": ["Yes", "No", "To be decided"]},
                {"en": "How many computer labs? How many seats per lab? Windows, Linux, or Mac?", "mr": "किती संगणक प्रयोगशाळा? प्रति प्रयोगशाळा किती जागा? Windows, Linux, किंवा Mac?", "type": "PARAGRAPH"},
                {"en": "Will there be a dedicated Robotics / AI / Coding / IoT lab?", "mr": "समर्पित Robotics / AI / Coding / IoT लॅब असेल का?", "type": "RADIO", "options": ["Yes, from Day 1", "Yes, Phase 2 onwards", "No", "To be decided"]},
                {"en": "What equipment is planned for the Robotics/Coding lab?", "mr": "Robotics/Coding लॅबसाठी कोणती उपकरणे नियोजित आहेत?", "type": "PARAGRAPH"},
                {"en": "Will there be a 3D printing / maker space?", "mr": "3D प्रिंटिंग / मेकर स्पेस असेल का?", "type": "RADIO", "options": ["Yes, dedicated maker space", "Yes, 3D printer in computer lab", "No", "To be decided"]},
                {"en": "Will there be a Mathematics lab with manipulatives and interactive tools?", "mr": "मॅनिपुलेटिव्ह आणि इंटरेक्टिव टूल्ससह गणित प्रयोगशाळा असेल का?", "type": "RADIO", "options": ["Yes", "No", "To be decided"]},
                {"en": "Will there be a Language lab with listening booths and pronunciation software?", "mr": "ऐकण्याच्या बूथ आणि उच्चार सॉफ्टवेअरसह भाषा प्रयोगशाळा असेल का?", "type": "RADIO", "options": ["Yes, dedicated language lab", "Digital language learning integrated in computer lab", "No", "To be decided"]},
                {"en": "Will there be a Home Science lab (cooking, nutrition, textiles)?", "mr": "गृहविज्ञान प्रयोगशाळा (स्वयंपाक, पोषण, वस्त्र) असेल का?", "type": "RADIO", "options": ["Yes", "No", "To be decided"]},
                {"en": "Will there be a Commerce/Business Studies lab with accounting software?", "mr": "लेखा सॉफ्टवेअरसह वाणिज्य/व्यवसाय अध्ययन लॅब असेल का?", "type": "RADIO", "options": ["Yes", "No", "To be decided"]},
            ]
        },
        {
            "title": "Section 5: Administrative & Staff Spaces  |  विभाग ५: प्रशासकीय आणि कर्मचारी जागा",
            "questions": [
                {"en": "What is the required size of the Principal's office? Should it have an attached meeting room?", "mr": "मुख्याध्यापकांच्या कार्यालयाचा आवश्यक आकार किती? त्यास जोडलेली बैठक खोली असावी का?", "type": "PARAGRAPH"},
                {"en": "How many Vice Principal positions? Shared or separate offices?", "mr": "किती उपमुख्याध्यापक पदे? सामायिक की स्वतंत्र कार्यालये?", "type": "TEXT"},
                {"en": "Admin/front office size? Reception, waiting area, and visitor lounge requirements?", "mr": "प्रशासन/फ्रंट ऑफिसचा आकार? रिसेप्शन, प्रतीक्षा क्षेत्र आणि अभ्यागत लाउंजची आवश्यकता?", "type": "PARAGRAPH"},
                {"en": "How many staff rooms? Should they be department-wise or combined?", "mr": "किती शिक्षक खोल्या? विभागनिहाय की एकत्रित असाव्यात?", "type": "TEXT"},
                {"en": "Expected number of teaching staff at full capacity?", "mr": "पूर्ण क्षमतेवर अपेक्षित शिक्षण कर्मचाऱ्यांची संख्या?", "type": "TEXT"},
                {"en": "Expected number of non-teaching staff (admin, lab assistants, librarian, IT, accounts, support)?", "mr": "अपेक्षित शिक्षणेतर कर्मचाऱ्यांची संख्या (प्रशासन, प्रयोगशाळा सहाय्यक, ग्रंथपाल, IT, लेखा, सहाय्य)?", "type": "TEXT"},
                {"en": "Will there be a dedicated examination control room?", "mr": "समर्पित परीक्षा नियंत्रण कक्ष असेल का?", "type": "RADIO", "options": ["Yes, separate room", "Part of admin block", "To be decided"]},
                {"en": "IT/server room requirements — size, UPS backup, air conditioning?", "mr": "IT/सर्व्हर रूमची आवश्यकता — आकार, UPS बॅकअप, वातानुकूलन?", "type": "PARAGRAPH"},
                {"en": "How many washrooms for staff (male/female/gender-neutral)? What ratio to staff count?", "mr": "कर्मचाऱ्यांसाठी किती शौचालये (पुरुष/महिला/लिंग-तटस्थ)? कर्मचारी संख्येशी प्रमाण काय?", "type": "TEXT"},
                {"en": "Parent/guardian waiting and meeting area — inside or outside school building?", "mr": "पालक/पाठीराखे प्रतीक्षा आणि बैठक क्षेत्र — शाळेच्या इमारतीच्या आत की बाहेर?", "type": "RADIO", "options": ["Inside building, dedicated room", "Outside building, separate structure", "Combined with reception area", "To be decided"]},
                {"en": "Stationery/store rooms — centralised or per floor?", "mr": "स्टेशनरी/स्टोअर रूम — केंद्रीकृत की प्रति मजला?", "type": "RADIO", "options": ["One centralised store room", "Per floor store rooms", "Both", "To be decided"]},
            ]
        },
        {
            "title": "Section 6: Library & Digital Learning  |  विभाग ६: ग्रंथालय आणि डिजिटल शिक्षण",
            "questions": [
                {"en": "What is the target book collection at launch and at full capacity?", "mr": "सुरुवातीला आणि पूर्ण क्षमतेवर पुस्तक संग्रहाचे लक्ष्य किती?", "type": "TEXT"},
                {"en": "What categories of books should be prioritised?", "mr": "कोणत्या श्रेणीतील पुस्तकांना प्राधान्य द्यावे?", "type": "CHECKBOX", "options": ["NCERT/state board textbooks", "Reference and competitive exam books", "Fiction and literature", "Marathi literature", "Children's picture books", "Research journals and magazines", "Newspapers (Hindi, Marathi, English)"]},
                {"en": "Will there be a digital/e-library with reading terminals?", "mr": "वाचन टर्मिनल्ससह डिजिटल/ई-लायब्ररी असेल का?", "type": "RADIO", "options": ["Yes, full e-library", "Yes, supplementary to physical", "No, physical books only", "To be decided"]},
                {"en": "What seating capacity is required in the library?", "mr": "ग्रंथालयात किती बैठक क्षमता आवश्यक आहे?", "type": "TEXT"},
                {"en": "Will there be a separate junior library for Classes 5–8?", "mr": "इयत्ता ५–८ साठी वेगळी कनिष्ठ ग्रंथालय असेल का?", "type": "RADIO", "options": ["Yes, separate room", "Separate section in same library", "No, combined", "To be decided"]},
                {"en": "What book tracking system is preferred?", "mr": "पुस्तक ट्रॅकिंग प्रणाली कोणती पसंत आहे?", "type": "RADIO", "options": ["RFID-based automated system", "Barcode-based", "Manual register", "Integrated with campus ERP/software", "To be decided"]},
                {"en": "Will the library be open beyond school hours for residential students?", "mr": "निवासी विद्यार्थ्यांसाठी ग्रंथालय शाळेच्या वेळेपलीकडे उघडे असेल का?", "type": "RADIO", "options": ["Yes, open till 9 PM", "Yes, open 24/7 for residential students", "No, school hours only", "To be decided"]},
                {"en": "Will there be an LMS (Learning Management System) for digital content delivery?", "mr": "डिजिटल सामग्री वितरणासाठी LMS (लर्निंग मॅनेजमेंट सिस्टम) असेल का?", "type": "RADIO", "options": ["Yes, custom-built (Eduval)", "Yes, Google Classroom", "Yes, Moodle or similar", "No", "To be decided"]},
            ]
        },
        {
            "title": "Section 7: Sports, Physical Education & Outdoor  |  विभाग ७: क्रीडा, शारीरिक शिक्षण आणि मैदान",
            "questions": [
                {"en": "How much of the 5-acre plot is earmarked for sports and outdoor areas?", "mr": "५ एकर भूखंडापैकी किती क्रीडा आणि मैदानी क्षेत्रासाठी राखीव आहे?", "type": "TEXT"},
                {"en": "Which outdoor sports/grounds are planned?", "mr": "कोणते मैदानी क्रीडा/मैदाने नियोजित आहेत?", "type": "CHECKBOX", "options": ["Cricket (full size)", "Cricket (practice pitches/nets)", "Football", "Basketball court", "Volleyball court", "Athletics/running track", "Kabaddi/Kho-Kho ground", "Badminton (outdoor)"]},
                {"en": "Will there be an indoor sports hall? Size? Which sports?", "mr": "इनडोअर स्पोर्ट्स हॉल असेल का? आकार? कोणते खेळ?", "type": "PARAGRAPH"},
                {"en": "Will there be a gymnasium/fitness centre for students?", "mr": "विद्यार्थ्यांसाठी व्यायामशाळा/फिटनेस सेंटर असेल का?", "type": "RADIO", "options": ["Yes, dedicated students gym", "Yes, shared with campus gym", "No", "To be decided"]},
                {"en": "Will there be a swimming pool? Shared with Club Deeper main pool or school-specific?", "mr": "जलतरण तलाव असेल का? क्लब डीपरच्या मुख्य तलावाशी सामायिक की शाळेसाठी वेगळा?", "type": "RADIO", "options": ["Yes, school-specific pool", "Shared with Club Deeper main pool", "No", "To be decided"]},
                {"en": "Will there be a Yoga/meditation hall?", "mr": "योग/ध्यान हॉल असेल का?", "type": "RADIO", "options": ["Yes, indoor dedicated hall", "Open-air yoga platform", "Both indoor and outdoor", "No", "To be decided"]},
                {"en": "Changing rooms and showers — how many cubicles for boys and girls separately?", "mr": "चेंजिंग रूम आणि शॉवर — मुले आणि मुलींसाठी स्वतंत्रपणे किती क्युबिकल?", "type": "TEXT"},
                {"en": "Sports equipment storage room — size and security requirements?", "mr": "क्रीडा उपकरण स्टोरेज रूम — आकार आणि सुरक्षा आवश्यकता?", "type": "PARAGRAPH"},
                {"en": "Will there be a dedicated sports coaching programme (cricket academy, football, swimming, etc.)?", "mr": "समर्पित क्रीडा कोचिंग कार्यक्रम (क्रिकेट अकादमी, फुटबॉल, जलतरण इ.) असेल का?", "type": "PARAGRAPH"},
                {"en": "PE staff room and coach cabin requirements?", "mr": "PE कर्मचारी खोली आणि प्रशिक्षक केबिनची आवश्यकता?", "type": "TEXT"},
            ]
        },
        {
            "title": "Section 8: Residential & Hostel  |  विभाग ८: निवासी आणि वसतिगृह",
            "questions": [
                {"en": "What percentage of students will be residential vs day scholars at launch?", "mr": "सुरुवातीला किती टक्के विद्यार्थी निवासी विरुद्ध दिवस विद्यार्थी असतील?", "type": "TEXT"},
                {"en": "What dormitory room type is preferred?", "mr": "वसतिगृह खोलीचा पसंतीचा प्रकार कोणता?", "type": "RADIO", "options": ["2-bed rooms", "4-bed rooms", "6-bed rooms", "8-bed dormitory", "Mix of 2-bed and 4-bed", "To be decided"]},
                {"en": "Will boys and girls hostels be separate buildings or separate floors/wings?", "mr": "मुला-मुलींचे वसतिगृह वेगळ्या इमारती की वेगळे मजले/विंग असतील?", "type": "RADIO", "options": ["Completely separate buildings", "Same building, separate floors", "Same building, separate wings with separate access", "To be decided"]},
                {"en": "What warden arrangement is planned? 24-hour coverage?", "mr": "पाळक व्यवस्था काय असेल? २४ तास उपस्थिती?", "type": "PARAGRAPH"},
                {"en": "What common facilities are required in the hostel?", "mr": "वसतिगृहात कोणत्या सामायिक सुविधा आवश्यक आहेत?", "type": "CHECKBOX", "options": ["Self-study hall with individual desks", "Common TV/recreation room", "Indoor games room", "Wi-Fi throughout hostel", "Tuck shop/snack area", "Outdoor sitting/garden area", "Prayer/meditation room"]},
                {"en": "Laundry facility — washing machines, drying area, ironing? Or outsourced to skill students?", "mr": "लाँड्री सुविधा — वॉशिंग मशीन, वाळवण क्षेत्र, इस्त्री? किंवा कौशल्य विद्यार्थ्यांना बाहेरून?", "type": "RADIO", "options": ["Self-service washing machines in hostel", "Managed laundry service by hostel staff", "Outsourced to Skill Campus students", "Mix", "To be decided"]},
                {"en": "In-room storage — individual wardrobes/lockers? Centralised storage?", "mr": "खोलीतील स्टोरेज — वैयक्तिक वॉर्डरोब/लॉकर? केंद्रीकृत स्टोरेज?", "type": "PARAGRAPH"},
                {"en": "Visitor policy — visiting hours, visitor room, parent visit booking protocol?", "mr": "अभ्यागत धोरण — भेट वेळ, अभ्यागत खोली, पालक भेट बुकिंग प्रोटोकॉल?", "type": "PARAGRAPH"},
                {"en": "Will Deepa Coins be used for all hostel services (laundry, canteen, tuck shop)?", "mr": "सर्व वसतिगृह सेवांसाठी (लाँड्री, कॅन्टीन, टक शॉप) दीपा कॉईन्स वापरले जातील का?", "type": "RADIO", "options": ["Yes, Deepa Coins for everything", "Yes, with cash backup", "No, separate billing", "To be decided"]},
                {"en": "Night security protocol for hostel — guards, CCTV inside corridors?", "mr": "वसतिगृहासाठी रात्रीची सुरक्षा प्रोटोकॉल — रक्षक, कॉरिडॉरमध्ये CCTV?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 9: Canteen, Dining & Food Services  |  विभाग ९: कॅन्टीन, जेवण आणि अन्न सेवा",
            "questions": [
                {"en": "Will the canteen serve snacks/beverages only or full meals (breakfast, lunch, dinner)?", "mr": "कॅन्टीन केवळ स्नॅक्स/पेये देईल की पूर्ण जेवण (न्याहारी, दुपारचे जेवण, रात्रीचे जेवण)?", "type": "RADIO", "options": ["Full meals (breakfast, lunch, dinner)", "Lunch and snacks only", "Snacks and beverages only", "Depends on residential vs day scholars", "To be decided"]},
                {"en": "Total seating capacity of the school canteen/dining hall?", "mr": "शाळेच्या कॅन्टीन/जेवणाच्या हॉलची एकूण बैठक क्षमता?", "type": "TEXT"},
                {"en": "Service style — buffet, counter service, pre-ordered thali, or meal plan?", "mr": "सेवा शैली — बुफे, काउंटर सेवा, पूर्व-ऑर्डर थाळी, किंवा मील प्लान?", "type": "RADIO", "options": ["Self-service buffet", "Counter service", "Pre-ordered thali system", "Meal plan (weekly/monthly)", "Mix of options", "To be decided"]},
                {"en": "Dietary policy for the canteen?", "mr": "कॅन्टीनसाठी आहार धोरण काय आहे?", "type": "CHECKBOX", "options": ["Vegetarian only", "Jain options available", "Vegan options available", "Non-vegetarian available", "Allergy labelling mandatory", "No specific dietary policy"]},
                {"en": "Who will run the canteen?", "mr": "कॅन्टीन कोण चालवेल?", "type": "RADIO", "options": ["In-house, campus managed", "Outsourced professional caterer", "Skill Campus students (as training)", "Mix of skill students + professional supervisor", "To be decided"]},
                {"en": "Kitchen infrastructure — size, equipment list, cold storage, LPG/PNG/induction?", "mr": "स्वयंपाकघर पायाभूत सुविधा — आकार, उपकरण यादी, शीत साठवण, LPG/PNG/इंडक्शन?", "type": "PARAGRAPH"},
                {"en": "Will all canteen payments be cashless via Deepa Coins only?", "mr": "सर्व कॅन्टीन देयक केवळ दीपा कॉईन्सद्वारे कॅशलेस असतील का?", "type": "RADIO", "options": ["Yes, Deepa Coins only", "Deepa Coins + cash option", "Cash only", "To be decided"]},
                {"en": "Will there be a separate tuck shop/snack kiosk?", "mr": "वेगळे टक शॉप/स्नॅक कियोस्क असेल का?", "type": "RADIO", "options": ["Yes, separate tuck shop", "Combined with main canteen", "No", "To be decided"]},
                {"en": "Food safety compliance plan — FSSAI, hygiene audit frequency?", "mr": "अन्न सुरक्षा अनुपालन योजना — FSSAI, स्वच्छता ऑडिट वारंवारता?", "type": "PARAGRAPH"},
                {"en": "Meal plan pricing — monthly, quarterly, annual? Included in hostel fee or charged separately?", "mr": "मील प्लान किंमत — मासिक, त्रैमासिक, वार्षिक? वसतिगृह शुल्कात समाविष्ट की वेगळे?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 10: Medical, Counselling & Student Wellness  |  विभाग १०: वैद्यकीय, समुपदेशन आणि विद्यार्थी कल्याण",
            "questions": [
                {"en": "Will there be an on-campus sick bay/medical room? How many beds?", "mr": "कॅम्पसवर सिक बे/वैद्यकीय कक्ष असेल का? किती बेड?", "type": "TEXT"},
                {"en": "Full-time nurse and/or doctor on campus? Visiting doctor schedule?", "mr": "कॅम्पसवर पूर्णवेळ परिचारिका आणि/किंवा डॉक्टर? भेट देणारे डॉक्टर वेळापत्रक?", "type": "PARAGRAPH"},
                {"en": "Emergency vehicle/ambulance tie-up with Club Deeper hospital?", "mr": "क्लब डीपर रुग्णालयाशी आपत्कालीन वाहन/रुग्णवाहिका करार?", "type": "RADIO", "options": ["Yes, dedicated tie-up", "General emergency service", "No specific arrangement", "To be decided"]},
                {"en": "Student counsellor/psychologist — full-time, part-time, or on-call?", "mr": "विद्यार्थी समुपदेशक/मनोवैज्ञानिक — पूर्णवेळ, अर्धवेळ, किंवा मागणीनुसार?", "type": "RADIO", "options": ["Full-time resident counsellor", "Part-time visiting counsellor", "On-call basis", "No", "To be decided"]},
                {"en": "Mental health awareness programmes — frequency and format?", "mr": "मानसिक आरोग्य जागरूकता कार्यक्रम — वारंवारता आणि स्वरूप?", "type": "PARAGRAPH"},
                {"en": "Anti-bullying and anti-ragging policy — how will it be structured and enforced?", "mr": "दादागिरी-विरोधी आणि रॅगिंग-विरोधी धोरण — ते कसे संरचित आणि लागू केले जाईल?", "type": "PARAGRAPH"},
                {"en": "Medical records management — paper or digital (ERP integrated)?", "mr": "वैद्यकीय नोंदी व्यवस्थापन — कागद किंवा डिजिटल (ERP एकत्रित)?", "type": "RADIO", "options": ["Digital, integrated with campus ERP", "Digital, separate system", "Paper-based", "To be decided"]},
                {"en": "Annual/bi-annual health check-up schedule for all students?", "mr": "सर्व विद्यार्थ्यांसाठी वार्षिक/द्विवार्षिक आरोग्य तपासणी वेळापत्रक?", "type": "PARAGRAPH"},
                {"en": "What specific health/wellness programmes will be offered (yoga, nutrition education, eye/dental camps)?", "mr": "कोणते विशिष्ट आरोग्य/कल्याण कार्यक्रम उपलब्ध असतील (योग, पोषण शिक्षण, नेत्र/दंत शिबिर)?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 11: Arts, Culture & Co-Curricular  |  विभाग ११: कला, संस्कृती आणि सह-अभ्यासक्रम",
            "questions": [
                {"en": "Dedicated music room — instruments planned (keyboard, tabla, harmonium, guitar, etc.)?", "mr": "समर्पित संगीत खोली — नियोजित वाद्ये (कीबोर्ड, तबला, हार्मोनियम, गिटार इ.)?", "type": "PARAGRAPH"},
                {"en": "Dance/performing arts studio — size, sprung floor, mirror wall required?", "mr": "नृत्य/परफॉर्मिंग आर्ट्स स्टुडिओ — आकार, स्प्रंग फ्लोर, आरसा भिंत आवश्यक?", "type": "PARAGRAPH"},
                {"en": "Art & craft room — easels, pottery wheel, kiln, drawing tables required?", "mr": "कला आणि हस्तकला खोली — ईझेल, कुंभारकाम चाक, भट्टी, रेखाचित्र टेबल आवश्यक?", "type": "PARAGRAPH"},
                {"en": "Auditorium/assembly hall — indoor or open-air? Seating capacity?", "mr": "सभागृह/सभा हॉल — इनडोअर किंवा मैदानी? बैठक क्षमता?", "type": "PARAGRAPH"},
                {"en": "Will the auditorium have a professional stage, green room, lighting rig, sound system?", "mr": "सभागृहात व्यावसायिक मंच, ग्रीन रूम, लाइटिंग रिग, ध्वनी प्रणाली असेल का?", "type": "PARAGRAPH"},
                {"en": "Annual Day, cultural festivals — on campus or external venue? Budget?", "mr": "वार्षिक दिन, सांस्कृतिक उत्सव — कॅम्पसवर किंवा बाहेरील ठिकाणी? बजेट?", "type": "PARAGRAPH"},
                {"en": "Which student clubs will be offered (robotics, environment, debate, literary, photography, etc.)?", "mr": "कोणते विद्यार्थी क्लब उपलब्ध असतील (रोबोटिक्स, पर्यावरण, वाद, साहित्यिक, छायाचित्रण इ.)?", "type": "PARAGRAPH"},
                {"en": "School newspaper/media club — production room, equipment needed?", "mr": "शाळा वृत्तपत्र/मीडिया क्लब — निर्मिती खोली, आवश्यक उपकरणे?", "type": "PARAGRAPH"},
                {"en": "Community service integration with Club Deeper rural/social programme — mandatory for students?", "mr": "क्लब डीपर ग्रामीण/सामाजिक कार्यक्रमासह सामुदायिक सेवा एकत्रीकरण — विद्यार्थ्यांसाठी अनिवार्य?", "type": "RADIO", "options": ["Yes, mandatory community service hours", "Yes, optional", "No", "To be decided"]},
            ]
        },
        {
            "title": "Section 12: Utilities, Infrastructure & Safety  |  विभाग १२: उपयुक्तता, पायाभूत सुविधा आणि सुरक्षा",
            "questions": [
                {"en": "Total built-up area target for the school block (sq. ft.)?", "mr": "शाळेच्या ब्लॉकचे एकूण बांधकाम क्षेत्र लक्ष्य (चौ. फुट)?", "type": "TEXT"},
                {"en": "Construction material preference — RCC, steel structure, green building, composite?", "mr": "बांधकाम साहित्याची प्राधान्य — RCC, स्टील स्ट्रक्चर, हरित इमारत, संमिश्र?", "type": "RADIO", "options": ["Traditional RCC", "Steel structure", "Green/sustainable building", "Composite (RCC + green features)", "To be decided"]},
                {"en": "Student washroom ratio requirement (1:25? 1:30?). Separate for boys, girls, staff, differently-abled?", "mr": "विद्यार्थी शौचालय प्रमाण आवश्यकता. मुले, मुली, कर्मचारी, अपंगांसाठी वेगळे?", "type": "PARAGRAPH"},
                {"en": "Water source, storage capacity (KL), and water treatment plan?", "mr": "पाण्याचा स्रोत, साठवण क्षमता (KL), आणि पाणी शुद्धीकरण योजना?", "type": "PARAGRAPH"},
                {"en": "Total power requirement (KVA)? Generator backup KVA? UPS for critical areas?", "mr": "एकूण वीज आवश्यकता (KVA)? जनरेटर बॅकअप KVA? अत्यावश्यक क्षेत्रांसाठी UPS?", "type": "PARAGRAPH"},
                {"en": "Solar power — target % of total load from solar? Rooftop or ground-mount?", "mr": "सौर ऊर्जा — एकूण भाराच्या किती % सौर ऊर्जेतून? छतावर की जमिनीवर?", "type": "PARAGRAPH"},
                {"en": "Wi-Fi/network coverage — classrooms, labs, library, hostel, outdoors?", "mr": "Wi-Fi/नेटवर्क कव्हरेज — वर्गखोल्या, प्रयोगशाळा, ग्रंथालय, वसतिगृह, मैदान?", "type": "PARAGRAPH"},
                {"en": "Perimeter security plan — compound wall, CCTV coverage, boom barrier?", "mr": "परिमिती सुरक्षा योजना — संयुक्त भिंत, CCTV कव्हरेज, बूम बॅरियर?", "type": "PARAGRAPH"},
                {"en": "Fire safety requirements — sprinklers, extinguishers, fire exits, fire drill frequency?", "mr": "अग्नी सुरक्षा आवश्यकता — स्प्रिंकलर, अग्निशामक, अग्नी निर्गमन, ड्रिल वारंवारता?", "type": "PARAGRAPH"},
                {"en": "PA system/bell system — digital or traditional? Centralised control?", "mr": "PA प्रणाली/घंटा प्रणाली — डिजिटल किंवा पारंपारिक? केंद्रीकृत नियंत्रण?", "type": "RADIO", "options": ["Digital integrated PA system", "Traditional bell system", "Combination", "To be decided"]},
                {"en": "Waste management — solid waste segregation, organic composting, recycling plan?", "mr": "कचरा व्यवस्थापन — घन कचरा वेगळे करणे, सेंद्रिय कंपोस्टिंग, पुनर्वापर योजना?", "type": "PARAGRAPH"},
                {"en": "Parking plan — staff, visitor, school bus bays? EV charging?", "mr": "पार्किंग योजना — कर्मचारी, अभ्यागत, शाळा बस बे? EV चार्जिंग?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 13: Technology, ERP & Smart Campus  |  विभाग १३: तंत्रज्ञान, ERP आणि स्मार्ट कॅम्पस",
            "questions": [
                {"en": "Which ERP modules must be live from Day 1?", "mr": "कोणते ERP मॉड्यूल पहिल्या दिवसापासून सक्रिय असणे आवश्यक आहे?", "type": "CHECKBOX", "options": ["Student admission & registration", "Fee collection & receipts", "Attendance (student + staff)", "Timetable/scheduling", "Examination & results", "Library management", "Hostel management", "Deepa Coin wallet", "Parent communication portal", "HR & payroll"]},
                {"en": "Mobile app for parents — real-time attendance, results, fee, announcements?", "mr": "पालकांसाठी मोबाइल अॅप — रिअल-टाइम उपस्थिती, निकाल, शुल्क, घोषणा?", "type": "RADIO", "options": ["Yes, full-featured parent app", "Yes, basic notification app", "Web portal only", "No", "To be decided"]},
                {"en": "Digital attendance — biometric, RFID card, facial recognition, or manual?", "mr": "डिजिटल उपस्थिती — बायोमेट्रिक, RFID कार्ड, चेहरा ओळख, किंवा मॅन्युअल?", "type": "RADIO", "options": ["Biometric (fingerprint)", "RFID student ID cards", "Facial recognition", "Manual register + digital entry", "To be decided"]},
                {"en": "Online learning platform — Google Classroom, Moodle, custom LMS, or none?", "mr": "ऑनलाइन शिक्षण व्यासपीठ — Google Classroom, Moodle, कस्टम LMS, किंवा नाही?", "type": "RADIO", "options": ["Google Classroom", "Moodle", "Custom Eduval LMS", "Microsoft Teams for Education", "No online platform", "To be decided"]},
                {"en": "AI-based analytics for student performance monitoring — from Day 1 or phased?", "mr": "विद्यार्थी कामगिरी निरीक्षणासाठी AI-आधारित विश्लेषण — पहिल्या दिवसापासून किंवा टप्पेवार?", "type": "RADIO", "options": ["Day 1 basic analytics", "Phase 2 with AI features", "Not planned", "To be decided"]},
                {"en": "Student ID card system — smart card with RFID for attendance, canteen, library?", "mr": "विद्यार्थी ओळखपत्र प्रणाली — उपस्थिती, कॅन्टीन, ग्रंथालयासाठी RFID स्मार्ट कार्ड?", "type": "RADIO", "options": ["Yes, RFID smart card for all services", "Yes, barcode only", "Simple photo ID card", "To be decided"]},
                {"en": "CCTV — number of cameras, NVR storage duration, remote monitoring?", "mr": "CCTV — कॅमेऱ्यांची संख्या, NVR स्टोरेज कालावधी, रिमोट मॉनिटरिंग?", "type": "PARAGRAPH"},
                {"en": "Cybersecurity for campus network — content filtering for students? Parental controls?", "mr": "कॅम्पस नेटवर्कसाठी सायबर सुरक्षा — विद्यार्थ्यांसाठी सामग्री फिल्टरिंग? पालकीय नियंत्रण?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 14: Transport, HR, Fees & Financials  |  विभाग १४: वाहतूक, HR, शुल्क आणि वित्त",
            "questions": [
                {"en": "Will the school operate its own buses? How many routes? How many buses?", "mr": "शाळा स्वतःच्या बस चालवेल का? किती मार्ग? किती बस?", "type": "PARAGRAPH"},
                {"en": "GPS tracking on all school vehicles from Day 1?", "mr": "पहिल्या दिवसापासून सर्व शाळेच्या वाहनांवर GPS ट्रॅकिंग?", "type": "RADIO", "options": ["Yes", "Phase 2", "No", "To be decided"]},
                {"en": "Teaching staff:student ratio target?", "mr": "शिक्षक:विद्यार्थी गुणोत्तर लक्ष्य?", "type": "TEXT"},
                {"en": "How many resident teaching staff will need on-campus accommodation?", "mr": "किती निवासी शिक्षण कर्मचाऱ्यांना कॅम्पसवर निवासाची सोय लागेल?", "type": "TEXT"},
                {"en": "Salary scale structure — 7th Pay Commission aligned, market-driven, or internal scale?", "mr": "वेतन श्रेणी रचना — 7th Pay Commission शी सुसंगत, बाजार-आधारित, किंवा अंतर्गत श्रेणी?", "type": "RADIO", "options": ["7th Pay Commission aligned", "Market-driven", "Internal scale", "To be decided"]},
                {"en": "Target annual tuition fee range — Classes 5–10?", "mr": "वार्षिक शिक्षण शुल्काचे लक्ष्य — इयत्ता ५–१०?", "type": "TEXT"},
                {"en": "Target annual tuition fee range — Classes 11–12?", "mr": "वार्षिक शिक्षण शुल्काचे लक्ष्य — इयत्ता ११–१२?", "type": "TEXT"},
                {"en": "Annual hostel fee — what does it include (meals, laundry, electricity, etc.)?", "mr": "वार्षिक वसतिगृह शुल्क — त्यात काय समाविष्ट आहे (जेवण, लाँड्री, वीज इ.)?", "type": "PARAGRAPH"},
                {"en": "Development/building fee — one-time or annual?", "mr": "विकास/इमारत शुल्क — एकवेळ किंवा वार्षिक?", "type": "TEXT"},
                {"en": "Scholarship/concession policy — % of seats, eligibility criteria, selection committee?", "mr": "शिष्यवृत्ती/सवलत धोरण — जागांची %, पात्रता निकष, निवड समिती?", "type": "PARAGRAPH"},
                {"en": "Fee payment schedule — quarterly, half-yearly, annual? Late fee policy?", "mr": "शुल्क भरणा वेळापत्रक — त्रैमासिक, अर्धवार्षिक, वार्षिक? उशीरा शुल्क धोरण?", "type": "PARAGRAPH"},
                {"en": "At what student strength does the school become financially self-sustaining (break-even)?", "mr": "कोणत्या विद्यार्थी संख्येवर शाळा आर्थिकदृष्ट्या स्वावलंबी (ब्रेक-इव्हन) होते?", "type": "TEXT"},
            ]
        },
        {
            "title": "Section 15: Regulatory, Compliance & Phasing  |  विभाग १५: नियामक, अनुपालन आणि टप्पे",
            "questions": [
                {"en": "Has CBSE affiliation process been initiated? Expected timeline for provisional affiliation?", "mr": "CBSE संलग्नता प्रक्रिया सुरू झाली आहे का? तात्पुरत्या संलग्नतेसाठी अपेक्षित कालावधी?", "type": "PARAGRAPH"},
                {"en": "NA conversion / education zone land-use approval — current status?", "mr": "NA परिवर्तन / शिक्षण क्षेत्र जमीन वापर मंजुरी — सध्याची स्थिती?", "type": "PARAGRAPH"},
                {"en": "Building plan approvals — which authority? Architect engaged?", "mr": "इमारत योजना मंजुरी — कोणती संस्था? आर्किटेक्ट नियुक्त?", "type": "PARAGRAPH"},
                {"en": "Trust/society registration for school (CBSE requires non-profit body) — status?", "mr": "शाळेसाठी ट्रस्ट/सोसायटी नोंदणी (CBSE ला बिगर-नफा संस्था आवश्यक) — स्थिती?", "type": "PARAGRAPH"},
                {"en": "POCSO compliance training for all staff — schedule?", "mr": "सर्व कर्मचाऱ्यांसाठी POCSO अनुपालन प्रशिक्षण — वेळापत्रक?", "type": "TEXT"},
                {"en": "RTE Act — will the school admit RTE quota students?", "mr": "RTE कायदा — शाळा RTE कोटा विद्यार्थ्यांना प्रवेश देईल का?", "type": "RADIO", "options": ["Yes, comply with RTE", "No, private unaided school", "To be decided"]},
                {"en": "Target launch date / first academic session?", "mr": "लक्ष्यित प्रारंभ तारीख / पहिले शैक्षणिक सत्र?", "type": "TEXT"},
                {"en": "Which classes will be offered in Year 1 and what is the phased class expansion plan?", "mr": "वर्ष १ मध्ये कोणत्या इयत्ता असतील आणि टप्पेवार इयत्ता विस्तार योजना काय आहे?", "type": "PARAGRAPH"},
                {"en": "What is the minimum infrastructure required for Phase 1 launch (non-negotiables)?", "mr": "टप्पा १ सुरुवातीसाठी किमान आवश्यक पायाभूत सुविधा (अनिवार्य) काय आहेत?", "type": "PARAGRAPH"},
                {"en": "Total estimated project cost for school block — Phase 1 and full build-out?", "mr": "शाळेच्या ब्लॉकसाठी अंदाजित एकूण प्रकल्प खर्च — टप्पा १ आणि पूर्ण बांधकाम?", "type": "PARAGRAPH"},
                {"en": "Any other important requirements, ideas, or concerns for the school project?", "mr": "शाळा प्रकल्पासाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता, कल्पना, किंवा चिंता?", "type": "PARAGRAPH"},
            ]
        },
    ]
}

# ═══════════════════════════════════════════════════════════════════
# PROJECT 2 — COACHING CENTER (NEET / JEE / CET)
# ═══════════════════════════════════════════════════════════════════
COACHING = {
    "index": 2,
    "title": "Club Deeper – Coaching Center (NEET/JEE/CET) Planning Questionnaire",
    "active": True,
    "description": (
        "Comprehensive planning questionnaire for the Residential Coaching Center "
        "at Club Deeper Campus.\n\n"
        "क्लब डीपर कॅम्पसमधील निवासी कोचिंग सेंटरसाठी सर्वसमावेशक नियोजन प्रश्नावली."
    ),
    "sections": [
        {
            "title": "Section 1: Vision, Scope & Target Exams  |  विभाग १: दृष्टी, व्याप्ती आणि लक्ष्य परीक्षा",
            "questions": [
                {"en": "What is the name and tagline of the coaching centre?", "mr": "कोचिंग सेंटरचे नाव आणि टॅगलाइन काय आहे?", "type": "TEXT"},
                {"en": "Which competitive exams will the coaching centre prepare students for?", "mr": "कोचिंग सेंटर कोणत्या स्पर्धा परीक्षांसाठी विद्यार्थ्यांना तयार करेल?", "type": "CHECKBOX", "options": ["NEET (Medical)", "JEE Main", "JEE Advanced", "MHT-CET (Engineering)", "MHT-CET (Pharmacy)", "AIIMS", "JIPMER", "Board exams (12th)"]},
                {"en": "Will coaching be residential only, day scholars only, or both?", "mr": "कोचिंग केवळ निवासी, दिवस विद्यार्थी, किंवा दोन्ही असेल?", "type": "RADIO", "options": ["Residential only", "Day scholars only", "Both residential and day scholars", "To be decided"]},
                {"en": "Will this be fully integrated with the K12 school or a standalone centre?", "mr": "हे K12 शाळेशी पूर्णपणे एकत्रित असेल की स्वतंत्र केंद्र?", "type": "RADIO", "options": ["Fully integrated with school timetable", "Separate standalone centre", "Partially integrated (shared facilities)", "To be decided"]},
                {"en": "What is the target student intake per year (batch-wise)?", "mr": "वर्षाला विद्यार्थी प्रवेशाचे लक्ष्य (बॅचनिहाय) किती?", "type": "TEXT"},
                {"en": "What is the programme duration (1-year, 2-year, dropper batch)?", "mr": "कार्यक्रमाचा कालावधी काय आहे (१ वर्ष, २ वर्ष, ड्रॉपर बॅच)?", "type": "CHECKBOX", "options": ["1-year programme (Class 12 + exam)", "2-year programme (Class 11 + 12 + exam)", "1-year dropper batch", "Short-term crash courses (3–6 months)", "All of the above"]},
                {"en": "What is the preferred batch size for coaching?", "mr": "कोचिंगसाठी पसंतीचा बॅच आकार किती?", "type": "RADIO", "options": ["Small (15–20 students)", "Medium (25–35 students)", "Large (40–60 students)", "Subject-wise flexible batches", "To be decided"]},
                {"en": "What is the primary target demographic?", "mr": "प्राथमिक लक्ष्य वर्ग कोण आहे?", "type": "CHECKBOX", "options": ["Rural students from Maharashtra", "Urban students from Pune/Mumbai", "Students from across Maharashtra", "Students from other states", "Economically weaker section students", "All backgrounds equally"]},
                {"en": "What is the vision for student results — target selection rate within 2 years?", "mr": "विद्यार्थ्यांच्या निकालासाठी दृष्टी — २ वर्षांत लक्ष्य निवड दर?", "type": "TEXT"},
            ]
        },
        {
            "title": "Section 2: Academic Programme & Teaching  |  विभाग २: शैक्षणिक कार्यक्रम आणि शिक्षण",
            "questions": [
                {"en": "What is the preferred teaching methodology?", "mr": "पसंतीची शिक्षण पद्धती कोणती?", "type": "CHECKBOX", "options": ["Live classroom teaching (primary)", "Recorded video lectures (supplementary)", "Hybrid live + recorded", "One-on-one mentoring sessions", "AI-based adaptive learning", "Flipped classroom model"]},
                {"en": "How many full-time subject faculty are needed per stream (NEET/JEE)?", "mr": "प्रत्येक प्रवाहासाठी (NEET/JEE) किती पूर्णवेळ विषय शिक्षक लागतील?", "type": "PARAGRAPH"},
                {"en": "Will faculty be resident on campus or visiting?", "mr": "शिक्षक कॅम्पसवर राहतील की भेट देणारे असतील?", "type": "RADIO", "options": ["All faculty resident on campus", "Mix of resident and visiting", "All visiting/daily commuters", "To be decided"]},
                {"en": "How many doubt-clearing sessions per week per subject?", "mr": "प्रत्येक विषयासाठी आठवड्यात किती शंका-निरसन सत्रे?", "type": "TEXT"},
                {"en": "Mock test schedule — frequency and type (full test/subject-wise/chapter-wise)?", "mr": "मॉक टेस्ट वेळापत्रक — वारंवारता आणि प्रकार (पूर्ण परीक्षा/विषयनिहाय/प्रकरणनिहाय)?", "type": "PARAGRAPH"},
                {"en": "Will there be a dedicated CBT (Computer Based Test) lab for NEET/JEE pattern practice?", "mr": "NEET/JEE पॅटर्न सरावासाठी समर्पित CBT (संगणक आधारित परीक्षा) लॅब असेल का?", "type": "RADIO", "options": ["Yes, dedicated CBT lab", "Shared with school computer lab", "No, paper-based tests only", "To be decided"]},
                {"en": "Study material — printed, digital (tablets/e-books), or both?", "mr": "अभ्यास साहित्य — मुद्रित, डिजिटल (टॅबलेट/ई-पुस्तके), किंवा दोन्ही?", "type": "RADIO", "options": ["Printed only", "Digital only (tablets provided)", "Both printed and digital", "To be decided"]},
                {"en": "Will the centre develop its own study material or use third-party content (Aakash, Allen, etc.)?", "mr": "केंद्र स्वतःचे अभ्यास साहित्य तयार करेल की तृतीय-पक्ष सामग्री वापरेल?", "type": "RADIO", "options": ["Own proprietary study material", "Licensed third-party material", "Mix of both", "To be decided"]},
                {"en": "Performance tracking system — individual student dashboards, parent reports, faculty analytics?", "mr": "कामगिरी ट्रॅकिंग प्रणाली — वैयक्तिक विद्यार्थी डॅशबोर्ड, पालक अहवाल, शिक्षक विश्लेषण?", "type": "PARAGRAPH"},
                {"en": "Guest lectures by doctors/engineers/IITians — planned frequency?", "mr": "डॉक्टर/इंजिनिअर/IITians यांचे अतिथी व्याख्याने — नियोजित वारंवारता?", "type": "TEXT"},
                {"en": "Will there be a mentorship programme pairing each student with a faculty mentor?", "mr": "प्रत्येक विद्यार्थ्याला शिक्षक मार्गदर्शकासोबत जोडणारा मेंटॉरशिप कार्यक्रम असेल का?", "type": "RADIO", "options": ["Yes, formal mentorship programme", "Informal basis", "No", "To be decided"]},
            ]
        },
        {
            "title": "Section 3: Infrastructure, Classrooms & Facilities  |  विभाग ३: पायाभूत सुविधा, वर्गखोल्या",
            "questions": [
                {"en": "How many dedicated coaching classrooms are needed? Capacity per room?", "mr": "किती समर्पित कोचिंग वर्गखोल्या लागतील? प्रति खोलीची क्षमता?", "type": "TEXT"},
                {"en": "AV/technology setup required in each coaching classroom?", "mr": "प्रत्येक कोचिंग वर्गखोलीत AV/तंत्रज्ञान व्यवस्था आवश्यक?", "type": "CHECKBOX", "options": ["Large display screen/projector", "Recording setup for lecture capture", "Good acoustics/soundproofing", "Individual student tablets", "High-speed Wi-Fi", "Air conditioning (mandatory for long sessions)"]},
                {"en": "How many exam/test halls? Capacity each? CBT lab size?", "mr": "किती परीक्षा/चाचणी हॉल? प्रत्येकाची क्षमता? CBT लॅबचा आकार?", "type": "TEXT"},
                {"en": "Self-study hall — capacity, hours of operation, individual cubicles or open tables?", "mr": "स्वयं-अध्ययन हॉल — क्षमता, कार्य तास, वैयक्तिक क्युबिकल किंवा खुल्या टेबल?", "type": "PARAGRAPH"},
                {"en": "Will there be a dedicated faculty room for preparation and research?", "mr": "तयारी आणि संशोधनासाठी समर्पित शिक्षक खोली असेल का?", "type": "RADIO", "options": ["Yes, dedicated faculty preparation room", "Shared with school staff room", "No", "To be decided"]},
                {"en": "Library for coaching centre — own dedicated library or shared with school library?", "mr": "कोचिंग सेंटरसाठी ग्रंथालय — स्वतःचे समर्पित ग्रंथालय की शाळेच्या ग्रंथालयाशी सामायिक?", "type": "RADIO", "options": ["Own dedicated coaching library", "Shared with school library", "Small reference room only", "To be decided"]},
                {"en": "What is the required internet bandwidth for the coaching centre (for CBT, video lectures)?", "mr": "कोचिंग सेंटरसाठी आवश्यक इंटरनेट बँडविड्थ (CBT, व्हिडिओ व्याख्यानांसाठी)?", "type": "TEXT"},
            ]
        },
        {
            "title": "Section 4: Residential, Welfare & Daily Routine  |  विभाग ४: निवासी, कल्याण आणि दैनंदिन दिनचर्या",
            "questions": [
                {"en": "Will coaching students share a hostel with school students or have a separate block?", "mr": "कोचिंग विद्यार्थी शाळेच्या विद्यार्थ्यांसोबत वसतिगृह सामायिक करतील की स्वतंत्र ब्लॉक असेल?", "type": "RADIO", "options": ["Completely separate hostel block", "Separate floor in school hostel", "Shared hostel with school students", "To be decided"]},
                {"en": "What is the proposed daily routine structure (wake up, study, meals, exercise, recreation, lights out)?", "mr": "प्रस्तावित दैनंदिन दिनचर्या रचना काय आहे (उठणे, अभ्यास, जेवण, व्यायाम, मनोरंजन, झोपणे)?", "type": "PARAGRAPH"},
                {"en": "Mobile phone policy — allowed, restricted, or completely banned?", "mr": "मोबाइल फोन धोरण — परवानगी, मर्यादित, किंवा पूर्णपणे बंदी?", "type": "RADIO", "options": ["Allowed at all times", "Allowed only during recreation hours", "Allowed only on weekends", "No personal phones, institute tablets provided", "Completely restricted", "To be decided"]},
                {"en": "What recreational and de-stress facilities will be available?", "mr": "कोणत्या मनोरंजन आणि तणाव-मुक्ती सुविधा उपलब्ध असतील?", "type": "CHECKBOX", "options": ["Sports ground access (restricted hours)", "Indoor games room", "Music/entertainment room", "Nature walks on campus", "Weekly movies/events", "Regular yoga/meditation sessions"]},
                {"en": "Stress management and mental health support plan for coaching students?", "mr": "कोचिंग विद्यार्थ्यांसाठी तणाव व्यवस्थापन आणि मानसिक आरोग्य सहाय्य योजना?", "type": "PARAGRAPH"},
                {"en": "Parent communication protocol — frequency, format (app, WhatsApp, written reports)?", "mr": "पालक संवाद प्रोटोकॉल — वारंवारता, स्वरूप (अॅप, WhatsApp, लेखी अहवाल)?", "type": "PARAGRAPH"},
                {"en": "Leave policy for coaching students — home visits, medical leave, emergency?", "mr": "कोचिंग विद्यार्थ्यांसाठी सुट्टी धोरण — घरी भेट, वैद्यकीय रजा, आपत्कालीन?", "type": "PARAGRAPH"},
            ]
        },
        {
            "title": "Section 5: Fees, Admissions & Operations  |  विभाग ५: शुल्क, प्रवेश आणि संचालन",
            "questions": [
                {"en": "Annual coaching fee for residential students?", "mr": "निवासी विद्यार्थ्यांसाठी वार्षिक कोचिंग शुल्क?", "type": "TEXT"},
                {"en": "Annual coaching fee for day scholars?", "mr": "दिवस विद्यार्थ्यांसाठी वार्षिक कोचिंग शुल्क?", "type": "TEXT"},
                {"en": "What does the residential fee include?", "mr": "निवासी शुल्कात काय समाविष्ट आहे?", "type": "CHECKBOX", "options": ["Accommodation (hostel)", "All meals (3 times/day + snacks)", "Study material", "Mock tests", "Laundry", "Medical/first aid", "Wi-Fi and electricity"]},
                {"en": "Scholarship/merit seat policy — number of free/subsidised seats, criteria?", "mr": "शिष्यवृत्ती/गुणवत्ता जागा धोरण — मुफ्त/अनुदानित जागांची संख्या, निकष?", "type": "PARAGRAPH"},
                {"en": "Admission/selection process — entrance test, interview, past marks, or open?", "mr": "प्रवेश/निवड प्रक्रिया — प्रवेश परीक्षा, मुलाखत, मागील गुण, किंवा खुले?", "type": "PARAGRAPH"},
                {"en": "Refund policy for fee in case of student withdrawal?", "mr": "विद्यार्थी माघारीच्या बाबतीत शुल्क परतावा धोरण?", "type": "PARAGRAPH"},
                {"en": "Will the coaching centre track and publicly publish selection results?", "mr": "कोचिंग सेंटर निवड निकाल मागोवा घेईल आणि सार्वजनिकपणे प्रकाशित करेल का?", "type": "RADIO", "options": ["Yes, prominently publish", "Yes, but only internally", "No", "To be decided"]},
                {"en": "Any other important requirements or ideas for the coaching centre?", "mr": "कोचिंग सेंटरसाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा कल्पना?", "type": "PARAGRAPH"},
            ]
        },
    ]
}

# ═══════════════════════════════════════════════════════════════════
# PROJECT 3 — LIBRARY
# ═══════════════════════════════════════════════════════════════════
LIBRARY = {
    "index": 3,
    "title": "Club Deeper – Library Planning Questionnaire",
    "active": False,
    "description": (
        "Comprehensive planning questionnaire for the Campus Library at Club Deeper.\n\n"
        "क्लब डीपर कॅम्पस ग्रंथालयासाठी सर्वसमावेशक नियोजन प्रश्नावली."
    ),
    "sections": [
        {
            "title": "Section 1: Vision, Scope & Beneficiaries  |  विभाग १: दृष्टी, व्याप्ती आणि लाभार्थी",
            "questions": [
                {"en": "What is the name and tagline of the library?", "mr": "ग्रंथालयाचे नाव आणि टॅगलाइन काय आहे?", "type": "TEXT"},
                {"en": "Who will the library serve?", "mr": "ग्रंथालय कोणाला सेवा देईल?", "type": "CHECKBOX", "options": ["School students (Classes 5–12)", "Coaching centre students", "Skill Campus students", "Residential families", "Campus staff and faculty", "UPSC/MPSC study centre students", "General public from surrounding villages"]},
                {"en": "Will there be different membership tiers (student, staff, community, premium)?", "mr": "वेगवेगळ्या सदस्यत्व स्तर असतील का (विद्यार्थी, कर्मचारी, समुदाय, प्रीमियम)?", "type": "PARAGRAPH"},
                {"en": "What is the library's operating philosophy — traditional reference library, open-access lending, or digital-first?", "mr": "ग्रंथालयाचे संचालन तत्त्वज्ञान काय आहे — पारंपारिक संदर्भ, खुले-प्रवेश उधार, किंवा डिजिटल-प्रथम?", "type": "RADIO", "options": ["Traditional reference library (no lending)", "Open-access lending library", "Digital-first with physical backup", "Hybrid model", "To be decided"]},
            ]
        },
        {
            "title": "Section 2: Collection & Resources  |  विभाग २: संग्रह आणि संसाधने",
            "questions": [
                {"en": "Target physical book collection at launch and at full capacity?", "mr": "सुरुवातीला आणि पूर्ण क्षमतेवर भौतिक पुस्तक संग्रहाचे लक्ष्य?", "type": "TEXT"},
                {"en": "What subject categories should be prioritised for initial acquisition?", "mr": "प्रारंभिक संपादनासाठी कोणत्या विषय श्रेणींना प्राधान्य द्यावे?", "type": "PARAGRAPH"},
                {"en": "Annual budget for new book and resource acquisition?", "mr": "नवीन पुस्तक आणि संसाधन संपादनासाठी वार्षिक बजेट?", "type": "TEXT"},
                {"en": "Will the library subscribe to digital databases (JSTOR, NCERT digital, PubMed, etc.)?", "mr": "ग्रंथालय डिजिटल डेटाबेसची सदस्यता घेईल का (JSTOR, NCERT डिजिटल, PubMed इ.)?", "type": "PARAGRAPH"},
                {"en": "Newspaper and magazine subscriptions planned (Hindi, Marathi, English, subject journals)?", "mr": "नियोजित वृत्तपत्र आणि मासिक सदस्यता (हिंदी, मराठी, इंग्रजी, विषय जर्नल)?", "type": "PARAGRAPH"},
                {"en": "Will there be an audio-visual/documentary collection (DVDs, streaming access)?", "mr": "दृक्श्राव्य/माहितीपट संग्रह असेल का (DVDs, स्ट्रीमिंग प्रवेश)?", "type": "RADIO", "options": ["Yes, dedicated AV collection", "Streaming access only", "No", "To be decided"]},
                {"en": "Will Marathi literature and local/regional content be specifically highlighted?", "mr": "मराठी साहित्य आणि स्थानिक/प्रादेशिक सामग्री विशेषतः हायलाइट केली जाईल का?", "type": "RADIO", "options": ["Yes, dedicated Marathi literature section", "Included in general collection", "No", "To be decided"]},
            ]
        },
        {
            "title": "Section 3: Infrastructure & Spaces  |  विभाग ३: पायाभूत सुविधा आणि जागा",
            "questions": [
                {"en": "Total library area required (sq. ft.)?", "mr": "एकूण ग्रंथालय क्षेत्र आवश्यक (चौ. फुट)?", "type": "TEXT"},
                {"en": "Total seating capacity (reading seats) required?", "mr": "एकूण बैठक क्षमता (वाचन जागा) किती आवश्यक आहे?", "type": "TEXT"},
                {"en": "What distinct zones/spaces are needed inside the library?", "mr": "ग्रंथालयात कोणते वेगळे क्षेत्र/जागा आवश्यक आहेत?", "type": "CHECKBOX", "options": ["Silent reading zone", "Group study rooms (soundproofed)", "Digital/e-library terminals area", "Children's/junior reading corner", "Newspaper and periodical reading lounge", "Audio-visual viewing area", "Librarian's office and work area", "Book processing/cataloguing room", "Exhibition/display space", "Storytelling/activity corner for children"]},
                {"en": "Will there be a separate junior library section for younger students?", "mr": "लहान विद्यार्थ्यांसाठी वेगळी कनिष्ठ ग्रंथालय विभाग असेल का?", "type": "RADIO", "options": ["Yes, completely separate room", "Separate section within main library", "No, integrated", "To be decided"]},
                {"en": "How many group study rooms? Capacity per room? Technology setup?", "mr": "किती गट अभ्यास खोल्या? प्रति खोली क्षमता? तंत्रज्ञान व्यवस्था?", "type": "PARAGRAPH"},
                {"en": "What book tracking/management system is preferred?", "mr": "पुस्तक ट्रॅकिंग/व्यवस्थापन प्रणाली कोणती पसंत आहे?", "type": "RADIO", "options": ["RFID-based automated system", "Barcode-based system", "Manual register", "Integrated with campus ERP", "To be decided"]},
            ]
        },
        {
            "title": "Section 4: Operations, Staffing & Community  |  विभाग ४: संचालन, कर्मचारी आणि समुदाय",
            "questions": [
                {"en": "Operating hours (school hours only, extended evenings, or 24/7 for residential students)?", "mr": "कार्य तास (केवळ शाळेचे वेळ, विस्तारित संध्याकाळ, किंवा निवासी विद्यार्थ्यांसाठी 24/7)?", "type": "RADIO", "options": ["School hours only (8 AM – 5 PM)", "Extended evening hours (till 9 PM)", "24/7 for residential students", "To be decided"]},
                {"en": "How many librarian/assistant staff positions are needed?", "mr": "किती ग्रंथपाल/सहाय्यक कर्मचारी पदे आवश्यक आहेत?", "type": "TEXT"},
                {"en": "Will membership be included in school/hostel fees or charged separately?", "mr": "सदस्यत्व शाळा/वसतिगृह शुल्कात समाविष्ट असेल की वेगळे आकारले जाईल?", "type": "RADIO", "options": ["Included in all fees", "Separate nominal annual fee", "Free for all campus residents", "Tiered: free for students, paid for others", "To be decided"]},
                {"en": "Will the library be open to surrounding community/villages or campus-only?", "mr": "ग्रंथालय आसपासच्या समुदाय/गावांसाठी खुले असेल की केवळ कॅम्पससाठी?", "type": "RADIO", "options": ["Campus community only", "Open to all with paid membership", "Community access on specific days/hours", "To be decided"]},
                {"en": "What library programmes/events will be conducted (reading clubs, author visits, book fairs)?", "mr": "कोणते ग्रंथालय कार्यक्रम/उपक्रम आयोजित केले जातील (वाचन क्लब, लेखक भेटी, पुस्तक मेळे)?", "type": "PARAGRAPH"},
                {"en": "Budget for initial setup (furniture, shelving, technology, inaugural collection)?", "mr": "प्रारंभिक उभारणीसाठी बजेट (फर्निचर, शेल्फिंग, तंत्रज्ञान, प्रारंभिक संग्रह)?", "type": "TEXT"},
                {"en": "Any other important requirements or ideas for the library?", "mr": "ग्रंथालयासाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा कल्पना?", "type": "PARAGRAPH"},
            ]
        },
    ]
}

# ═══════════════════════════════════════════════════════════════════
# PROJECT 4 — STUDY CENTER (UPSC/MPSC)
# ═══════════════════════════════════════════════════════════════════
STUDY_CENTER = {
    "index": 4,
    "title": "Club Deeper – Study Center (UPSC/MPSC) Planning Questionnaire",
    "active": False,
    "description": (
        "Comprehensive planning questionnaire for the UPSC/MPSC Study Center "
        "at Club Deeper Campus.\n\n"
        "क्लब डीपर कॅम्पसमधील UPSC/MPSC अभ्यास केंद्रासाठी सर्वसमावेशक नियोजन प्रश्नावली."
    ),
    "sections": [
        {
            "title": "Section 1: Vision, Scope & Target Exams  |  विभाग १: दृष्टी, व्याप्ती आणि लक्ष्य परीक्षा",
            "questions": [
                {"en": "What is the name and tagline of the study centre?", "mr": "अभ्यास केंद्राचे नाव आणि टॅगलाइन काय आहे?", "type": "TEXT"},
                {"en": "Which exams will the study centre focus on?", "mr": "अभ्यास केंद्र कोणत्या परीक्षांवर लक्ष केंद्रित करेल?", "type": "CHECKBOX", "options": ["UPSC Civil Services (IAS/IPS/IFS)", "MPSC State Services", "MPSC Group B/C", "Maharashtra Police Bharti", "Banking exams (IBPS/SBI/RBI)", "Staff Selection Commission (SSC)", "Defence (NDA/CDS/CAPF)", "Judiciary exams", "All competitive exams"]},
                {"en": "Will this centre be residential, day scholars, or both?", "mr": "हे केंद्र निवासी, दिवस विद्यार्थी, किंवा दोन्ही असेल?", "type": "RADIO", "options": ["Residential only", "Day scholars only", "Both", "To be decided"]},
                {"en": "What is the target student intake per batch?", "mr": "प्रति बॅच विद्यार्थी प्रवेशाचे लक्ष्य?", "type": "TEXT"},
                {"en": "What is the primary target demographic?", "mr": "प्राथमिक लक्ष्य वर्ग कोण?", "type": "RADIO", "options": ["Rural youth from Maharashtra (primary focus)", "Graduates from across India", "Economically weaker section aspirants", "All aspirants regardless of background", "To be decided"]},
                {"en": "Is the social mission to specifically uplift rural Maharashtrian aspirants central to this centre's identity?", "mr": "ग्रामीण महाराष्ट्रीयन इच्छुकांना उन्नत करण्याचे सामाजिक उद्दिष्ट या केंद्राच्या ओळखीसाठी केंद्रीय आहे का?", "type": "RADIO", "options": ["Yes, this is the primary mission", "Yes, important but not exclusive", "No, open to all equally", "To be decided"]},
            ]
        },
        {
            "title": "Section 2: Academic Programme  |  विभाग २: शैक्षणिक कार्यक्रम",
            "questions": [
                {"en": "What coaching programmes will be offered?", "mr": "कोणते कोचिंग कार्यक्रम उपलब्ध असतील?", "type": "CHECKBOX", "options": ["Foundation/Prelims integrated course", "Mains-specific writing programme", "Interview preparation (personality test)", "Full integrated course (Prelims + Mains + Interview)", "Short-term crash courses", "Subject-specific modules"]},
                {"en": "Duration of each programme type?", "mr": "प्रत्येक कार्यक्रम प्रकाराचा कालावधी?", "type": "PARAGRAPH"},
                {"en": "Will there be dedicated Marathi medium batches for MPSC?", "mr": "MPSC साठी समर्पित मराठी माध्यमाचे बॅच असतील का?", "type": "RADIO", "options": ["Yes, dedicated Marathi medium batches", "Both Marathi and English medium", "English medium only", "To be decided"]},
                {"en": "Will answer writing practice be a daily structured component?", "mr": "उत्तरलेखन सराव दैनंदिन संरचित घटक असेल का?", "type": "RADIO", "options": ["Yes, daily answer writing with evaluation", "Yes, weekly", "No", "To be decided"]},
                {"en": "Current affairs delivery — daily newspaper sessions, curated notes, online platform, weekly tests?", "mr": "चालू घडामोडी वितरण — दैनंदिन वृत्तपत्र सत्रे, क्युरेटेड नोट्स, ऑनलाइन व्यासपीठ, साप्ताहिक चाचण्या?", "type": "CHECKBOX", "options": ["Daily newspaper reading sessions (mandatory)", "Curated current affairs printed notes", "Online current affairs portal", "Weekly current affairs tests", "Monthly magazine subscription", "Video current affairs sessions"]},
                {"en": "Mock interview programme — frequency, panel composition (retired IAS/IPS, academics)?", "mr": "मॉक मुलाखत कार्यक्रम — वारंवारता, पॅनेल रचना (निवृत्त IAS/IPS, शिक्षणतज्ज्ञ)?", "type": "PARAGRAPH"},
                {"en": "Guest lectures by serving/retired IAS, IPS, IFS, IRS officers — planned frequency?", "mr": "सेवारत/निवृत्त IAS, IPS, IFS, IRS अधिकाऱ्यांचे अतिथी व्याख्याने — नियोजित वारंवारता?", "type": "TEXT"},
                {"en": "Will the centre organise study tours (Parliament, High Court, Collectorate visits)?", "mr": "केंद्र अभ्यास सहली आयोजित करेल का (संसद, उच्च न्यायालय, जिल्हाधिकारी कार्यालय भेटी)?", "type": "RADIO", "options": ["Yes, regular study tours", "Occasional visits", "No", "To be decided"]},
            ]
        },
        {
            "title": "Section 3: Infrastructure  |  विभाग ३: पायाभूत सुविधा",
            "questions": [
                {"en": "How many teaching/lecture rooms? Capacity per room?", "mr": "किती शिक्षण/व्याख्यान कक्ष? प्रति खोली क्षमता?", "type": "TEXT"},
                {"en": "Self-study hall — capacity, individual cubicles or open tables, 24/7 access?", "mr": "स्वयं-अध्ययन हॉल — क्षमता, वैयक्तिक क्युबिकल किंवा खुल्या टेबल, 24/7 प्रवेश?", "type": "PARAGRAPH"},
                {"en": "Dedicated library for the study centre — or shared with the campus library?", "mr": "अभ्यास केंद्रासाठी समर्पित ग्रंथालय — किंवा कॅम्पस ग्रंथालयाशी सामायिक?", "type": "RADIO", "options": ["Own dedicated library with UPSC-specific collection", "Shared with campus library", "Small reference room only", "To be decided"]},
                {"en": "What UPSC/MPSC specific resources must the library stock?", "mr": "ग्रंथालयात UPSC/MPSC विशिष्ट कोणती संसाधने असणे आवश्यक आहे?", "type": "PARAGRAPH"},
                {"en": "Interview preparation room — soundproofed, professional setup?", "mr": "मुलाखत तयारी खोली — ध्वनीरोधक, व्यावसायिक व्यवस्था?", "type": "RADIO", "options": ["Yes, dedicated interview room", "Multipurpose room", "No", "To be decided"]},
                {"en": "Seminar hall for guest lectures and group discussions — capacity?", "mr": "अतिथी व्याख्याने आणि गट चर्चांसाठी परिसंवाद हॉल — क्षमता?", "type": "TEXT"},
            ]
        },
        {
            "title": "Section 4: Fees, Social Impact & Operations  |  विभाग ४: शुल्क, सामाजिक प्रभाव आणि संचालन",
            "questions": [
                {"en": "Target fee for residential UPSC programme (annual)?", "mr": "निवासी UPSC कार्यक्रमासाठी लक्ष्यित शुल्क (वार्षिक)?", "type": "TEXT"},
                {"en": "Target fee for MPSC programme (annual)?", "mr": "MPSC कार्यक्रमासाठी लक्ष्यित शुल्क (वार्षिक)?", "type": "TEXT"},
                {"en": "How many fully subsidised/free seats for economically weaker rural aspirants?", "mr": "आर्थिकदृष्ट्या दुर्बल ग्रामीण इच्छुकांसाठी किती पूर्णपणे अनुदानित/मुफ्त जागा?", "type": "TEXT"},
                {"en": "Funding model for subsidised seats — CSR, foundation grants, government scheme?", "mr": "अनुदानित जागांसाठी निधी मॉडेल — CSR, फाउंडेशन अनुदान, सरकारी योजना?", "type": "PARAGRAPH"},
                {"en": "Will the centre track and celebrate selection results publicly?", "mr": "केंद्र निवड निकाल सार्वजनिकपणे मागोवा घेईल आणि साजरा करेल का?", "type": "RADIO", "options": ["Yes, prominently", "Yes, internally", "No", "To be decided"]},
                {"en": "Alumni network and mentoring by past successful candidates — planned?", "mr": "माजी विद्यार्थी नेटवर्क आणि यशस्वी उमेदवारांद्वारे मार्गदर्शन — नियोजित?", "type": "RADIO", "options": ["Yes, formal alumni mentoring programme", "Informal connections", "No", "To be decided"]},
                {"en": "Any other important requirements or ideas for the study centre?", "mr": "अभ्यास केंद्रासाठी इतर कोणत्याही महत्त्वाच्या आवश्यकता किंवा कल्पना?", "type": "PARAGRAPH"},
            ]
        },
    ]
}

# ═══════════════════════════════════════════════════
if __name__ == "__main__":
    run_batch("Education Campus", [SCHOOL, COACHING, LIBRARY, STUDY_CENTER])
