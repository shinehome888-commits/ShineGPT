import streamlit as st

# ------------------- SESSION STATE -------------------
if 'mode' not in st.session_state:
    st.session_state.mode = None  # None, 'sms', 'online'
if 'show_about' not in st.session_state:
    st.session_state.show_about = False

# ------------------- 50 REAL LESSONS ON 4TH INDUSTRIAL REVOLUTION (4IR) -------------------
lessons = {
    1: "The 4th Industrial Revolution (4IR) is the fusion of digital, physical, and biological technologies that is transforming how we live, work, and relate to one another.",
    2: "AI (Artificial Intelligence) is at the heart of 4IR — machines that learn, reason, and make decisions like humans — without being explicitly programmed.",
    3: "Machine Learning is a subset of AI that uses data to train systems to recognize patterns — like identifying spam emails or recommending videos.",
    4: "Big Data refers to massive volumes of structured and unstructured information — from social media, sensors, and transactions — that can be analyzed to reveal insights.",
    5: "IoT (Internet of Things) connects everyday objects — fridges, cars, lights — to the internet to collect and share data, making homes and cities smarter.",
    6: "Cloud computing lets us store and access data and software over the internet — no need for powerful local computers, making technology accessible to all.",
    7: "5G networks are the backbone of 4IR — offering ultra-fast, low-latency connections that enable real-time remote surgery, autonomous vehicles, and smart factories.",
    8: "Blockchain is a secure, decentralized digital ledger that records transactions across many computers — making it tamper-proof and transparent.",
    9: "Cryptocurrency like Bitcoin uses blockchain to enable peer-to-peer money transfers without banks — giving financial power to the unbanked.",
    10: "Smart contracts are self-executing agreements on blockchain — they automatically trigger payments or actions when conditions are met — no middlemen needed.",
    11: "NFTs (Non-Fungible Tokens) use blockchain to prove ownership of unique digital items — art, music, or even virtual land — creating new economies.",
    12: "Data privacy is critical in 4IR — your location, habits, and health data are valuable. You have the right to control who uses it.",
    13: "Digital literacy means knowing how to use technology safely, ethically, and effectively — a basic skill for the 21st century, like reading and writing.",
    14: "Automation replaces repetitive tasks with machines — from factory robots to chatbots — freeing humans for creative, strategic, and caring work.",
    15: "AI in healthcare can analyze X-rays faster than doctors, predict disease outbreaks, and personalize treatment — saving lives in remote villages.",
    16: "Big Data helps farmers predict crop yields by combining satellite images, weather data, and soil sensors — reducing hunger and waste.",
    17: "Cities use Big Data to optimize traffic lights, reduce pollution, and plan public transport — making urban life cleaner and less stressful.",
    18: "Big Data detects fraud in banking by spotting unusual spending patterns — protecting people’s savings even when they’re offline.",
    19: "In education, Big Data helps teachers identify which students are struggling — so they can get help before falling behind.",
    20: "Big Data tracks the spread of diseases by analyzing search trends, hospital records, and mobile location data — helping stop pandemics early.",
    21: "Blockchain can record land ownership in countries with weak paperwork — protecting farmers from being kicked off their own land.",
    22: "Blockchain can verify academic certificates — eliminating fake degrees and saving schools and employers time and money.",
    23: "Blockchain can track food from farm to table — so you know your vegetables are safe, organic, and not stolen from another country.",
    24: "Blockchain can record carbon credits — proving companies are actually reducing emissions, not just claiming it.",
    25: "Decentralized Finance (DeFi) lets people lend, borrow, and earn interest without banks — using only a smartphone and internet.",
    26: "Crypto wallets give people control over their money — no government or bank can freeze your account or charge hidden fees.",
    27: "Digital identity on blockchain lets refugees prove who they are — even without a passport — so they can access education, healthcare, and jobs.",
    28: "AI-powered chatbots can answer questions in local languages — helping people in rural areas get information without needing to read.",
    29: "Edge AI runs AI models directly on phones or sensors — no internet needed — perfect for areas with poor connectivity.",
    30: "Low-power devices like solar-powered tablets can run AI and blockchain apps — bringing 4IR tech to villages without electricity.",
    31: "Digital twins are virtual copies of real objects — like a factory or a bridge — used to predict failures and save billions in repairs.",
    32: "3D printing turns digital designs into physical objects — letting communities print tools, medical parts, or even homes — on demand.",
    33: "Robotics combined with AI can deliver medicine to remote clinics — saving lives in places where ambulances can’t reach.",
    34: "Drones with AI can monitor forests, detect fires, and count wildlife — helping protect nature without humans needing to go in.",
    35: "Augmented Reality (AR) lets you see digital information overlaid on the real world — helping mechanics fix machines or students learn anatomy.",
    36: "Virtual Reality (VR) creates immersive learning — students can walk inside a human cell or visit ancient Rome — without leaving the classroom.",
    37: "Digital payment systems like mobile money let farmers sell crops and get paid instantly — no cash, no middlemen, no delays.",
    38: "Online marketplaces connect small artisans to global buyers — turning local crafts into global income, even without a bank account.",
    39: "AI can detect fake news by analyzing how stories spread — helping communities avoid misinformation and build trust.",
    40: "Ethical AI means building systems that are fair, transparent, and don’t discriminate — especially against women, minorities, or the poor.",
    41: "Bias in AI happens when training data reflects old inequalities — like hiring systems that favor men — and we must fix it before it harms people.",
    42: "Digital rights mean having control over your data, your voice, and your identity — not letting corporations own your digital life.",
    43: "The digital divide is the gap between those with access to technology and those without — 4IR must include everyone, not just the connected.",
    44: "Open-source software lets anyone use, modify, and share code — empowering communities to build their own tools, not depend on foreign companies.",
    45: "Digital citizenship means using technology responsibly — respecting others, protecting privacy, and fighting misinformation — online and offline.",
    46: "4IR can reduce poverty by creating new jobs in tech, data, and green energy — but only if we train people to use it.",
    47: "Girls and women must be included in 4IR — coding, AI, and blockchain are not male domains. Diversity makes innovation stronger.",
    48: "4IR is not about replacing humans — it’s about empowering them. Technology should serve people, not control them.",
    49: "You don’t need a university degree to learn 4IR skills — free online lessons, SMS-based apps like ShineGPT, and community labs can teach anyone.",
    50: "ShineGPT proves that 4IR doesn’t require internet or money — just curiosity, courage, and the will to learn. Keep going — you’re changing the future."
}

# ------------------- HELPER FUNCTIONS -------------------
def get_lesson_text(lesson_num):
    return lessons.get(lesson_num, "Lesson not found.")

def add_points(points):
    if 'user_points' not in st.session_state:
        st.session_state.user_points = 0
    st.session_state.user_points += points

# ------------------- STYLING — PURE, CALM, BEAUTIFUL -------------------
st.markdown(
    """
    <style>
    /* Hide Streamlit’s default menu, footer, and header */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Background */
    .main {
        background-color: #0a0a0a;
        color: white;
        font-family: 'Segoe UI', sans-serif;
        padding: 0 !important;
    }

    /* ShineGPT Brand — Centered, Sacred Space */
    .brand-container {
        text-align: center;
        margin: 4rem 1rem 2rem 1rem;
        padding: 0 2rem;
    }
    .brand-container h1 {
        color: #D4AF37 !important;
        font-size: 3.5rem !important;
        font-weight: 900 !important;
        margin: 0 !important;
        font-family: 'Arial', sans-serif;
        letter-spacing: -1px;
        line-height: 1.1;
    }
    .brand-container p {
        color: white !important;
        font-size: 1.6rem !important;
        font-weight: 400 !important;
        margin: 0.8rem 0 0.8rem 0 !important;
        opacity: 0.9;
        line-height: 1.5;
    }
    .brand-footer {
        text-align: center;
        margin-top: 1rem;
        color: #D32F2F !important;
        font-size: 1.4rem !important;
        font-weight: 700 !important;
        opacity: 0.9;
    }

    /* Button Style — Gentle, Big, Friendly */
    .stButton > button {
        background-color: #D32F2F !important;
        color: white !important;
        font-weight: 700 !important;
        font-size: 1.8rem !important;
        padding: 22px 45px !important;
        margin: 2rem auto !important;
        display: block !important;
        width: 85% !important;
        max-width: 550px !important;
        border-radius: 30px !important;
        border: none !important;
        cursor: pointer !important;
        font-family: 'Arial', sans-serif;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #b52828 !important;
        transform: translateY(-3px);
    }

    /* Instruction Text — Soft, Calm */
    .instruction {
        text-align: center;
        color: #ccc;
        font-size: 1.4rem;
        margin: 1.5rem auto;
        max-width: 600px;
        line-height: 1.7;
    }

    /* About Box */
    .about-box {
        background-color: #111;
        padding: 2.5rem;
        border-radius: 20px;
        border-left: 5px solid #D4AF37;
        margin: 2rem auto;
        max-width: 700px;
        color: #e0e0e0;
        font-size: 1.3rem;
        line-height: 1.8;
    }
    .about-box h3 {
        color: #D4AF37 !important;
        margin-bottom: 1.5rem;
    }

    /* Mobile Responsive */
    @media (max-width: 600px) {
        .brand-container h1 { font-size: 2.8rem !important; }
        .brand-container p { font-size: 1.4rem !important; }
        .brand-footer { font-size: 1.2rem !important; }
        .stButton > button { font-size: 1.6rem !important; padding: 20px 40px !important; }
        .instruction { font-size: 1.2rem !important; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------- HOME PAGE — ONLY BRAND AND TWO BUTTONS -------------------
if st.session_state.mode is None and not st.session_state.show_about:
    # ------------------- YOUR BRAND — SACRED SPACE -------------------
    st.markdown(
        """
        <div class="brand-container">
            <h1>SHINEGPT</h1>
            <p>Learn. Earn Knowledge. Empower Yourself.</p>
        </div>
        <div class="brand-footer">
            Powered by KS1 Empire Foundation
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ------------------- TWO BIG, GENTLE BUTTONS -------------------
    col1, col2 = st.columns(2)

    with col1:
        if st.button("📱 SMS Mode", key="btn_sms"):
            st.session_state.mode = 'sms'

    with col2:
        if st.button("🌐 Online Mode", key="btn_online"):
            st.session_state.mode = 'online'

    # ------------------- SOFT INSTRUCTION BELOW -------------------
    st.markdown(
        """
        <div class="instruction">
            No internet? No problem.  
            Just tap a button — and begin.
        </div>
        """,
        unsafe_allow_html=True
    )

# ------------------- SMS MODE — SIMPLE, SAFE, CALM -------------------
elif st.session_state.mode == 'sms':
    st.markdown("<h2 style='text-align: center; color: #D4AF37;'>📱 SMS Mode — No Internet Needed</h2>", unsafe_allow_html=True)
    st.markdown("<div class='instruction'>Write 'lesson 1' to begin your journey.</div>", unsafe_allow_html=True)

    user_input = st.text_input(
        label="",
        placeholder="Type your message...",
        key="sms_input"
    )

    if st.button("Send", key="send_sms"):
        if user_input:
            user_input_lower = user_input.strip().lower()
            
            if user_input_lower == "help":
                response = """
Available commands:
- type 'lesson 1' to start
- type 'lesson 2', 'lesson 3', etc. to continue
- type 'points' to check your earned points
- type 'hello' to greet ShineGPT
No internet needed! All lessons work offline.
                """
                st.success(response)
                
            elif user_input_lower == "points":
                response = f"🎉 You have {st.session_state.user_points} points!"
                st.success(response)
                
            elif user_input_lower == "hello":
                response = "Hello! 👋 Type 'lesson 1' to begin your journey with ShineGPT."
                st.success(response)
                
            elif user_input_lower.startswith("lesson "):
                try:
                    lesson_num = int(user_input_lower.split()[-1])
                    if lesson_num < 1:
                        response = "Start with lesson 1!"
                    elif lesson_num > 50:
                        response = "You've completed all 50 real lessons! 🎉 You're a ShineGPT pioneer! Type 'points' to see your progress."
                    else:
                        response = get_lesson_text(lesson_num) + f"\n\n✨ You earned 10 points! Type 'lesson {lesson_num + 1}' to continue."
                        add_points(10)
                        st.session_state.current_lesson = lesson_num
                    st.success(response)
                except:
                    response = "Type 'lesson 1' to start."
                    st.success(response)
            else:
                response = "I don't understand. Try typing 'lesson 1'."
                st.success(response)

    # ------------------- About Button (Hidden until needed) -------------------
    if st.button("📖 Learn More About ShineGPT", key="about_btn_sms"):
        st.session_state.show_about = True

    # ------------------- Back Button -------------------
    if st.button("⬅️ Back to Home", key="back_home_sms"):
        st.session_state.mode = None

# ------------------- ONLINE MODE — CLEAN, KIND, SIMPLE -------------------
elif st.session_state.mode == 'online':
    st.markdown("<h2 style='text-align: center; color: #D4AF37;'>🌐 Online Mode — Explore the World</h2>", unsafe_allow_html=True)
    st.markdown("<div class='instruction'>Ask ShineGPT anything — like 'What is AI?' or 'How does blockchain work?'</div>", unsafe_allow_html=True)

    user_input = st.text_input(
        label="",
        placeholder="Ask ShineGPT...",
        key="online_input"
    )

    if st.button("Send", key="send_online"):
        if user_input:
            search_term = user_input.replace(" ", "+")
            wikipedia_url = f"https://en.wikipedia.org/wiki/Special:Search?search={search_term}"
            
            st.markdown(f"""
                <div style="margin: 2rem auto; width: 100%; height: 500px; border: 2px solid #D4AF37; border-radius: 16px; overflow: hidden; box-shadow: 0 4px 12px rgba(212, 175, 55, 0.2);">
                    <iframe src="{wikipedia_url}" width="100%" height="100%" frameborder="0" allowfullscreen></iframe>
                </div>
            """, unsafe_allow_html=True)

    if st.button("⬅️ Back to Home", key="back_home_online"):
        st.session_state.mode = None

# ------------------- ABOUT PAGE — ONLY WHEN CLICKED -------------------
if st.session_state.show_about:
    st.markdown("<h2 style='text-align: center; color: #D4AF37;'>📖 About ShineGPT</h2>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class="about-box">
            <h3>Who is ShineGPT?</h3>
            <p>ShineGPT is a free, simple learning tool made for kids and youth like you — especially in places with no internet or slow connections.</p>
            
            <h3>What can you do?</h3>
            <p>📱 In SMS Mode: Type 'lesson 1' to start learning 50 powerful lessons — no internet needed.</p>
            <p>🌐 In Online Mode: Ask anything — and ShineGPT opens a Wikipedia page with the answer.</p>
            
            <h3>Why was it made?</h3>
            <p>Because every child deserves to learn — no matter where they live, or what phone they have.</p>
            
            <h3>Our Promise</h3>
            <p>No ads. No tracking. No paywalls. Just pure, free, kind learning.</p>
            
            <p>💙 Powered by KS1 Empire Foundation — because education should be a light, not a luxury.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("⬅️ Back to Home", key="back_home_about"):
        st.session_state.show_about = False
        st.session_state.mode = None

# ------------------- FOOTER — A WHISPER OF LOVE -------------------
st.markdown("<br><br><p style='text-align: center; color: #888; font-size: 0.9rem;'>ShineGPT — Built with love for every curious mind.</p>", unsafe_allow_html=True)
