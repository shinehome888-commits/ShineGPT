import streamlit as st

# ------------------- SESSION STATE -------------------
if 'user_points' not in st.session_state:
    st.session_state.user_points = 0
if 'current_lesson' not in st.session_state:
    st.session_state.current_lesson = 1
if 'mode' not in st.session_state:
    st.session_state.mode = 'sms'  # Default: SMS Mode

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

# ------------------- STYLING -------------------
st.markdown(
    """
    <style>
    div[data-testid="stTextInput"] > div > div > input {
        font-size: 1.4rem !important;
        padding: 20px 25px !important;
        border: 2px solid #D4AF37 !important;
        border-radius: 20px !important;
        background-color: #0a0a0a !important;
        color: #e0e0e0 !important;
        width: 90% !important;
        max-width: 700px !important;
        margin: 1.5rem auto !important;
        display: block !important;
        box-shadow: 0 4px 10px rgba(212, 175, 55, 0.2) !important;
        caret-color: #D4AF37 !important;
    }
    div[data-testid="stTextInput"] > div > div > input::placeholder {
        color: #666 !important;
        font-style: italic !important;
    }

    .stButton>button {
        background-color: #D32F2F !important;
        color: white !important;
        font-weight: 700 !important;
        font-size: 1.2rem !important;
        padding: 15px 30px !important;
        margin: 1.5rem auto !important;
        display: block !important;
        width: 90% !important;
        max-width: 400px !important;
        border-radius: 15px !important;
        border: none !important;
        cursor: pointer !important;
    }

    .stSuccess {
        max-width: 90%;
        margin: 1.5rem auto;
        padding: 25px;
        background-color: #1a1a1a;
        border-left: 5px solid #D4AF37;
        font-size: 1.4rem;
    }

    h1 {
        color: #D4AF37 !important;
        text-align: center !important;
        font-family: 'Arial', sans-serif;
    }
    p {
        color: white !important;
        text-align: center !important;
        font-size: 1.2rem !important;
    }
    .online-mode {
        background-color: #1a1a1a;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #D4AF37;
        margin: 1rem 0;
    }
    .lesson-card {
        background-color: #111;
        padding: 20px;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #D4AF37;
        color: white;
        font-size: 1.2rem;
    }
    .resource-btn {
        background-color: #222 !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        font-size: 1.3rem !important;
        padding: 15px 25px !important;
        margin: 10px 5px !important;
        border-radius: 12px !important;
        text-align: center !important;
        display: block !important;
        width: 90% !important;
        max-width: 500px !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }
    .resource-btn:hover {
        background-color: #333 !important;
    }
    .iframe-container {
        margin: 2rem auto;
        width: 100%;
        height: 600px;
        border: 2px solid #D4AF37;
        border-radius: 12px;
        overflow: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------- HEADER -------------------
st.markdown("<h1>SHINEGPT</h1>", unsafe_allow_html=True)
st.markdown("<p>Learn. Earn Knowledge. Empower Yourself.</p>", unsafe_allow_html=True)
st.markdown("<p style='color: #D32F2F;'>Powered by KS1 Empire Foundation</p>", unsafe_allow_html=True)

# ------------------- MODE TOGGLE -------------------
col1, col2 = st.columns([3, 1])
with col1:
    st.info("Choose your learning mode:")
with col2:
    st.session_state.mode = st.toggle("🌐 Online Mode", value=False)

# ------------------- SMS MODE (OFFLINE) -------------------
if st.session_state.mode == 'sms':
    st.header("📱 SMS Mode — No Internet Needed!")
    st.info("Type: lesson 1, hello, help, points")

    user_input = st.text_input(
        label="",
        key="sms_input",
        placeholder="Type your message...",
        label_visibility="collapsed"
    )

    if st.button("📩 Send", key="send_sms") and user_input:
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
        elif user_input_lower == "points":
            response = f"🎉 You have {st.session_state.user_points} points!"
        elif user_input_lower == "hello":
            response = "Hello! 👋 Type 'lesson 1' to begin your journey with ShineGPT."
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
            except:
                response = "Type 'lesson 1' to start."
        else:
            response = "I don't understand. Try typing 'help'."

        st.success(response)

# ------------------- ONLINE MODE (EMBEDDED EDUCATIONAL PORTAL) -------------------
else:
    st.header("🌐 Online Mode — Explore the World of 4IR")
    st.info("Click a button below to explore free, trusted educational resources. No login needed.")

    # Resource buttons
    st.markdown("### 📚 Choose a Learning Path:")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🤖 AI & Machine Learning", key="btn_ai", help="Khan Academy’s free AI course"):
            st.session_state.selected_resource = "khan_ai"
    with col2:
        if st.button("🔗 Blockchain & Crypto", key="btn_blockchain", help="Blockchain.org — simple, official intro"):
            st.session_state.selected_resource = "blockchain_org"
    with col3:
        if st.button("📊 Big Data & Analytics", key="btn_bigdata", help="Wikipedia — clear, open explanations"):
            st.session_state.selected_resource = "wikipedia_bigdata"

    col4, col5 = st.columns(2)
    with col4:
        if st.button("🎓 MIT OpenCourseWare", key="btn_mit", help="Free university-level courses"):
            st.session_state.selected_resource = "mit_ocw"
    with col5:
        if st.button("🔬 Google Scholar", key="btn_scholar", help="Academic papers and research"):
            st.session_state.selected_resource = "google_scholar"

    # Show embedded content based on button click
    if 'selected_resource' in st.session_state:
        resource = st.session_state.selected_resource

        urls = {
            "khan_ai": "https://www.khanacademy.org/computing",
            "blockchain_org": "https://www.blockchain.org/",
            "wikipedia_bigdata": "https://en.wikipedia.org/wiki/Big_data",
            "mit_ocw": "https://ocw.mit.edu/search/?q=artificial+intelligence",
            "google_scholar": "https://scholar.google.com/"
        }

        url = urls.get(resource, "https://en.wikipedia.org/wiki/4th_Industrial_Revolution")

        st.markdown(f"""
            <div class="iframe-container">
                <iframe src="{url}" width="100%" height="600" frameborder="0" allowfullscreen></iframe>
            </div>
        """, unsafe_allow_html=True)

        # Add a back button
        if st.button("↩️ Back to Resources", key="back_resources"):
            del st.session_state.selected_resource
            st.rerun()
    else:
        st.markdown("""
            <div style='text-align: center; color: #888; padding: 40px; font-size: 1.2rem;'>
                Click any button above to begin your journey into the 4th Industrial Revolution.
            </div>
        """, unsafe_allow_html=True)

    # Points display
    st.markdown(f"<div style='text-align: center; color: #D4AF37; font-size: 1.5rem; margin: 1rem 0;'>🏆 {st.session_state.user_points} Points</div>", unsafe_allow_html=True)

    # Navigation
    col1, col2 = st.columns(2)
    with col1:
        if st.button("↩️ Back to SMS Mode"):
            st.session_state.mode = 'sms'
            st.rerun()
    with col2:
        if st.button("🔁 Refresh Page"):
            st.rerun()

# ------------------- SIDEBAR — COMMON FOR BOTH MODES -------------------
st.sidebar.markdown("---")
st.sidebar.subheader("🏆 Your Points")
st.sidebar.write(f"**{st.session_state.user_points}** points")
st.sidebar.info("Earn 10 per lesson in SMS mode. Online mode gives you knowledge — no points, but endless learning.")

st.sidebar.subheader("📖 Progress")
st.sidebar.write(f"**Lesson {st.session_state.current_lesson}** completed (SMS Mode)")
st.sidebar.caption("You're learning the 4th Industrial Revolution — AI, Big Data, Blockchain, Crypto & Digital Ethics.")

# ------------------- FOOTER -------------------
st.markdown("---")
st.markdown("<p style='text-align: center; color: #888; font-size: 0.9rem;'>ShineGPT — Built for the world that needs it most. No ads. No tracking. No paywalls.</p>", unsafe_allow_html=True)
