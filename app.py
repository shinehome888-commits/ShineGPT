import streamlit as st
import requests
from bs4 import BeautifulSoup
import re

# ------------------- SESSION STATE -------------------
if 'mode' not in st.session_state:
    st.session_state.mode = None  # None, 'sms', 'online'

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

# ------------------- ONLINE MODE: GET TOP GOOGLE RESULT -------------------
def get_google_answer(query):
    try:
        # Clean query for URL
        search_term = query.replace(" ", "+")
        url = f"https://www.google.com/search?q={search_term}&btnI=I%27m+Feeling+Lucky"
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
        }
        
        response = requests.get(url, headers=headers, timeout=8)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Try to find the first paragraph from the top result
        first_paragraph = soup.find('p')
        if first_paragraph:
            text = first_paragraph.get_text().strip()
            # Clean up extra spaces and newlines
            text = re.sub(r'\s+', ' ', text)
            if len(text) > 10:
                return text
        
        # Fallback: try to get the main content div
        main_content = soup.find('div', {'class': ['BNeawe', 's3v9rd', 'AP7Wnd']})
        if main_content:
            text = main_content.get_text().strip()
            text = re.sub(r'\s+', ' ', text)
            if len(text) > 10:
                return text
        
        # Last fallback: return a helpful message
        return f"I found a page about '{query}' — but couldn't extract a clear answer. Try asking again in simple words."
        
    except Exception as e:
        return f"⚠️ Could not connect to the internet. Please check your connection and try again."

# ------------------- STYLING — CLEAN, SMALL, HORIZONTAL BUTTONS -------------------
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

    /* ShineGPT Brand — Centered, Sacred, Unchanged */
    .brand-container {
        text-align: center;
        margin: 5rem 1rem 1rem 1rem;
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

    /* Mode Buttons — BIG, EASY TO TAP */
    .mode-btn {
        background-color: #1a1a1a;
        color: #D4AF37;
        border: 2px solid #D4AF37;
        border-radius: 20px;
        padding: 25px 35px;
        font-size: 1.8rem;
        font-weight: 700;
        cursor: pointer;
        margin: 1.5rem auto;
        display: block;
        width: 85%;
        max-width: 500px;
        box-shadow: 0 4px 10px rgba(212, 175, 55, 0.2);
        transition: all 0.2s ease;
    }
    .mode-btn:hover {
        background-color: #222;
        transform: translateY(-2px);
    }

    /* Mode Description — ONE SIMPLE SENTENCE */
    .mode-desc {
        text-align: center;
        color: #ccc;
        font-size: 1.3rem;
        margin: 0.5rem auto 2rem auto;
        max-width: 600px;
        line-height: 1.6;
    }

    /* Input Box */
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

    /* Send and Back Buttons — SMALL, BOLD, HORIZONTAL */
    .btn-container {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin: 1.5rem auto;
        width: 100%;
        max-width: 600px;
    }
    .btn-container button {
        font-weight: 700 !important;
        font-size: 1.0rem !important;
        padding: 8px 16px !important;
        border-radius: 12px !important;
        border: none !important;
        cursor: pointer !important;
        font-family: 'Arial', sans-serif;
        min-width: 100px;
    }
    .btn-container .send-btn {
        background-color: #D32F2F !important;
        color: white !important;
    }
    .btn-container .back-btn {
        background-color: #222 !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
    }
    .btn-container button:hover {
        opacity: 0.9;
    }

    /* Answer Box */
    .answer-box {
        background-color: #111;
        padding: 20px;
        border-radius: 16px;
        border-left: 4px solid #D4AF37;
        margin: 1.5rem auto;
        max-width: 700px;
        color: #e0e0e0;
        font-size: 1.3rem;
        line-height: 1.7;
        white-space: pre-line;
    }

    /* Mobile Responsive */
    @media (max-width: 600px) {
        .brand-container h1 { font-size: 2.8rem !important; }
        .brand-container p { font-size: 1.4rem !important; }
        .brand-footer { font-size: 1.2rem !important; }
        .mode-btn { font-size: 1.6rem !important; padding: 20px 30px !important; }
        .mode-desc { font-size: 1.2rem !important; }
        .btn-container button { font-size: 0.9rem !important; padding: 6px 14px !important; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------- HOME PAGE — BRAND + TWO WORKING BUTTONS -------------------
if st.session_state.mode is None:
    # ------------------- YOUR BRAND — SACRED, CENTERED, UNCHANGED -------------------
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

    # ------------------- SMS MODE BUTTON + EXPLANATION -------------------
    if st.button("📱 SMS Mode", key="btn_sms", help="No internet? Type 'lesson 1' to start learning."):
        st.session_state.mode = 'sms'

    st.markdown(
        "<div class='mode-desc'>No internet? Type 'lesson 1' to start learning. Works without data.</div>",
        unsafe_allow_html=True
    )

    # ------------------- ONLINE MODE BUTTON + EXPLANATION -------------------
    if st.button("🌐 Online Mode", key="btn_online", help="Have internet? Ask anything — get the best answer from the web."):
        st.session_state.mode = 'online'

    st.markdown(
        "<div class='mode-desc'>Have internet? Ask anything — get the best answer from the web. No login needed.</div>",
        unsafe_allow_html=True
    )

# ------------------- SMS MODE — SIMPLE, FAST, WORKS -------------------
elif st.session_state.mode == 'sms':
    st.markdown("<h2 style='text-align: center; color: #D4AF37;'>📱 SMS Mode — No Internet Needed</h2>", unsafe_allow_html=True)
    st.markdown("<div class='mode-desc'>Type 'lesson 1' to begin. No internet needed.</div>", unsafe_allow_html=True)

    user_input = st.text_input(
        label="",
        placeholder="Type your message...",
        key="sms_input"
    )

    # --- HORIZONTAL BUTTONS: Send and Back ---
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Send", key="send_sms", class_name="send-btn"):
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

    with col2:
        if st.button("← Back", key="back_home_sms", class_name="back-btn"):
            st.session_state.mode = None

# ------------------- ONLINE MODE — FAST, CLEAN, TOP ANSWER FROM ENTIRE INTERNET -------------------
elif st.session_state.mode == 'online':
    st.markdown("<h2 style='text-align: center; color: #D4AF37;'>🌐 Online Mode — Best Answer from the Web</h2>", unsafe_allow_html=True)
    st.markdown("<div class='mode-desc'>Ask anything — like 'What is AI?' — and get the top answer from the internet.</div>", unsafe_allow_html=True)

    user_input = st.text_input(
        label="",
        placeholder="Ask ShineGPT...",
        key="online_input"
    )

    # --- HORIZONTAL BUTTONS: Send and Back ---
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Send", key="send_online", class_name="send-btn"):
            if user_input:
                with st.spinner("🔍 Finding the best answer..."):
                    answer = get_google_answer(user_input)
                
                st.markdown(f"<div class='answer-box'>{answer}</div>", unsafe_allow_html=True)

    with col2:
        if st.button("← Back", key="back_home_online", class_name="back-btn"):
            st.session_state.mode = None

# ------------------- FOOTER WHISPER — LAST WORD -------------------
st.markdown("<br><br><p style='text-align: center; color: #888; font-size: 0.9rem;'>ShineGPT — Built with love for every curious mind.</p>", unsafe_allow_html=True)
