import streamlit as st

# ------------------- SESSION STATE -------------------
if 'user_points' not in st.session_state:
    st.session_state.user_points = 0
if 'current_lesson' not in st.session_state:
    st.session_state.current_lesson = 1
if 'mode' not in st.session_state:
    st.session_state.mode = 'sms'  # Default: SMS Mode
if 'page' not in st.session_state:
    st.session_state.page = 'home'  # home, about

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
    st.session_state.user_points += points

# ------------------- STYLING — YOUR BRAND, YOUR VISION -------------------
st.markdown(
    """
    <style>
    /* Hide Streamlit’s default menu, footer, and header */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Sidebar styling */
    .css-1d391kg { /* Sidebar container */
        background-color: #111 !important;
        padding-top: 2rem !important;
    }
    .css-1d391kg .css-1v3fvcr { /* Sidebar menu items */
        color: #D4AF37 !important;
        font-size: 1.3rem !important;
        font-weight: 600 !important;
        padding: 12px 20px !important;
        border-radius: 8px !important;
        margin: 5px 0 !important;
        text-align: left !important;
    }
    .css-1d391kg .css-1d391kg:hover {
        background-color: #1a1a1a !important;
    }

    /* Main content area */
    .main {
        padding: 2rem 2rem;
        background-color: #0a0a0a;
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }

    /* ShineGPT Header */
    .brand-header {
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .brand-header h1 {
        color: #D4AF37 !important;
        font-size: 2.8rem !important;
        font-weight: 800 !important;
        margin: 0 !important;
        font-family: 'Arial', sans-serif;
    }
    .brand-header p {
        color: white !important;
        font-size: 1.4rem !important;
        font-weight: 400 !important;
        margin: 0.5rem 0 0.5rem 0 !important;
    }
    .brand-footer {
        text-align: center;
        margin-top: 1rem;
        color: #D32F2F !important;
        font-size: 1.3rem !important;
        font-weight: 700 !important;
    }

    /* Input box */
    .stTextInput > div > div > input {
        font-size: 1.4rem !important;
        padding: 16px 20px !important;
        border: 2px solid #D4AF37 !important;
        border-radius: 20px !important;
        background-color: #111 !important;
        color: white !important;
        width: 100% !important;
        box-shadow: 0 4px 12px rgba(212, 175, 55, 0.2) !important;
    }

    /* Send button — NORMAL SIZE, CLEAN, CENTERED */
    .stButton > button {
        background-color: #D32F2F !important;
        color: white !important;
        font-weight: 700 !important;
        font-size: 1.2rem !important;
        padding: 12px 28px !important;
        margin: 1.5rem auto !important;
        display: block !important;
        width: 80% !important;
        max-width: 400px !important;
        border-radius: 18px !important;
        border: none !important;
        cursor: pointer !important;
        font-family: 'Arial', sans-serif;
    }

    /* Success messages */
    .stSuccess {
        max-width: 90%;
        margin: 1.5rem auto;
        padding: 20px;
        background-color: #1a1a1a;
        border-left: 5px solid #D4AF37;
        font-size: 1.4rem;
        color: #e0e0e0 !important;
    }

    /* iframe container */
    .iframe-container {
        margin: 2rem auto;
        width: 100%;
        height: 500px;
        border: 2px solid #D4AF37;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(212, 175, 55, 0.2);
    }

    /* About page styling */
    .about-content {
        background-color: #111;
        padding: 2rem;
        border-radius: 12px;
        border-left: 4px solid #D4AF37;
        margin: 1rem 0;
        font-size: 1.2rem;
        line-height: 1.7;
        color: #e0e0e0;
    }
    .about-content h2 {
        color: #D4AF37 !important;
        margin-bottom: 1rem;
    }

    /* Mobile responsiveness */
    @media (max-width: 600px) {
        .brand-header h1 { font-size: 2.2rem !important; }
        .brand-header p { font-size: 1.2rem !important; }
        .brand-footer { font-size: 1.1rem !important; }
        .stButton > button { font-size: 1.1rem !important; padding: 10px 24px !important; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------- SIDEBAR — CLEAN NAVIGATION MENU -------------------
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🏠 Home"):
        st.session_state.page = 'home'
    if st.button("📱 SMS Mode"):
        st.session_state.page = 'sms'
    if st.button("🌐 Online Mode"):
        st.session_state.page = 'online'
    if st.button("📖 About ShineGPT"):
        st.session_state.page = 'about'

# ------------------- MAIN CONTENT — BRAND HEADER -------------------
st.markdown(
    """
    <div class="brand-header">
        <h1>SHINEGPT</h1>
        <p>Learn. Earn Knowledge. Empower Yourself.</p>
    </div>
    <div class="brand-footer">
        Powered by KS1 Empire Foundation
    </div>
    """,
    unsafe_allow_html=True,
)

# ------------------- HOME PAGE (DEFAULT) -------------------
if st.session_state.page == 'home':
    st.header("Welcome to ShineGPT")
    st.markdown("""
        <div style='text-align: center; color: #ccc; font-size: 1.3rem; padding: 2rem;'>
            Choose a mode to begin your journey.
        </div>
    """, unsafe_allow_html=True)

# ------------------- SMS MODE -------------------
elif st.session_state.page == 'sms':
    st.header("📱 SMS Mode — No Internet Needed")
    st.info("Write 'lesson 1' to start.")

    user_input = st.text_input(
        label="",
        placeholder="Write 'lesson 1' to start...",
        key="sms_input"
    )

    if st.button("Send"):
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
                response = "Hello! 👋 Write 'lesson 1' to begin your journey with ShineGPT."
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
                    response = "Write 'lesson 1' to start."
                    st.success(response)
            else:
                response = "I don't understand. Try writing 'lesson 1'."
                st.success(response)

# ------------------- ONLINE MODE -------------------
elif st.session_state.page == 'online':
    st.header("🌐 Online Mode — Explore the World of 4IR")
    st.info("Ask ShineGPT anything.")

    user_input = st.text_input(
        label="",
        placeholder="Ask ShineGPT...",
        key="online_input"
    )

    if st.button("Send"):
        if user_input:
            # Create a clean Wikipedia search URL
            search_term = user_input.replace(" ", "+")
            wikipedia_url = f"https://en.wikipedia.org/wiki/Special:Search?search={search_term}"

            # Show results in an iframe
            st.markdown(f"""
                <div class="iframe-container">
                    <iframe src="{wikipedia_url}" width="100%" height="500" frameborder="0" allowfullscreen></iframe>
                </div>
            """, unsafe_allow_html=True)

            # Optional: Add a note
            st.markdown(
                "<p style='text-align: center; color: #888; font-size: 1rem;'>💡 Tip: Use Wikipedia for clear explanations. Use Google Scholar for research.</p>",
                unsafe_allow_html=True
            )

# ------------------- ABOUT PAGE -------------------
elif st.session_state.page == 'about':
    st.header("📖 About ShineGPT")
    st.markdown(
        """
        <div class="about-content">
            <h2>Who We Are</h2>
            <p>ShineGPT is a free, offline-friendly learning tool built by the <strong>KS1 Empire Foundation</strong> to empower learners in low-connectivity communities around the world.</p>

            <h2>Our Mission</h2>
            <p>We believe that knowledge should not be locked behind paywalls, expensive devices, or fast internet. ShineGPT brings the power of the 4th Industrial Revolution — AI, Blockchain, Big Data, and Digital Ethics — to anyone with a basic phone and a curious mind.</p>

            <h2>How It Works</h2>
            <p><strong>📱 SMS Mode:</strong> 50 powerful, offline lessons. Type 'lesson 1' to begin. No internet needed.</p>
            <p><strong>🌐 Online Mode:</strong> When you have internet, ask ShineGPT anything. It opens a clean Wikipedia search — no ads, no tracking, no login.</p>

            <h2>Why We Built This</h2>
            <p>We’ve met teachers in villages with no textbooks. Students in refugee camps with no Wi-Fi. Young people who dream of becoming engineers but have no access to resources. ShineGPT was built for them.</p>

            <h2>Our Promise</h2>
            <p>No ads. No tracking. No data collection. No paywalls. Just pure, free, ethical education — for everyone.</p>

            <p>© 2025 KS1 Empire Foundation — All rights reserved.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ------------------- FOOTER -------------------
st.markdown("<br><br><p style='text-align: center; color: #888; font-size: 0.9rem;'>ShineGPT — Built for the world that needs it most.</p>", unsafe_allow_html=True)
