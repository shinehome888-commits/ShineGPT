import streamlit as st

# 🔧 DEBUG: Remove this line after confirming app is running latest code
st.write("✅ LIVE: ShineGPT loaded with latest code — logo section next 👇")

# ------------------- SESSION STATE -------------------
if 'mode' not in st.session_state:
    st.session_state.mode = None
if 'user_points' not in st.session_state:
    st.session_state.user_points = 0
if 'current_lesson' not in st.session_state:
    st.session_state.current_lesson = 1
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'show_about' not in st.session_state:
    st.session_state.show_about = False

# ------------------- 50 LESSONS (SAMPLE — EXPAND AS NEEDED) -------------------
lessons = {
    1: "The 4th Industrial Revolution (4IR) is the fusion of digital, physical, and biological technologies that is transforming how we live, work, and relate to one another.",
    2: "AI (Artificial Intelligence) is at the heart of 4IR — machines that learn, reason, and make decisions like humans — without being explicitly programmed.",
    3: "Machine Learning is a subset of AI that uses data to train systems to recognize patterns — like identifying spam emails or recommending videos.",
    # Add more lessons as needed...
}

# ------------------- SMS RESPONSES -------------------
sms_responses = {
    "hello": "Hello! I'm ShineGPT. Type 'lesson 1' to start learning.",
    "help": "Type: 'lesson 1', 'lesson 2', ..., 'points', 'hello'",
    "points": f"You have {st.session_state.user_points} points. Earn 10 per lesson!",
}

# Auto-generate lesson responses
for i in range(1, 51):
    sms_responses[f"lesson {i}"] = lessons.get(i, "Lesson not found.") + f"\n\n✨ +10 points!"

# ------------------- HELPER FUNCTIONS -------------------
def add_points(points):
    st.session_state.user_points += points

# ------------------- STYLING — SIMPLE, RELIABLE, WHITE BACKGROUND -------------------
st.markdown(
    """
    <style>
    /* Hide Streamlit chrome */
    #MainMenu, footer, header {visibility: hidden;}
    
    /* PURE WHITE BACKGROUND */
    .main {
        background-color: #ffffff !important;
        color: #000000 !important;
        font-family: 'Segoe UI', Arial, sans-serif;
    }
    
    /* Falling "ShineGPT" text — subtle, non-intrusive */
    .falling-text {
        position: fixed;
        top: -50px;
        left: 50%;
        transform: translateX(-50%);
        color: rgba(212, 175, 55, 0.1);
        font-size: 6rem;
        font-weight: 900;
        pointer-events: none;
        z-index: 1;
        animation: fall 25s linear infinite;
        white-space: nowrap;
    }
    @keyframes fall {
        0% { top: -50px; opacity: 0; }
        10% { opacity: 0.2; }
        90% { opacity: 0.2; }
        100% { top: 100vh; opacity: 0; }
    }
    
    /* Logo container */
    .brand-box {
        text-align: center;
        padding: 2rem 1rem;
        background: #fff;
        border-radius: 16px;
        margin: 1rem auto;
        max-width: 400px;
        box-shadow: 0 4px 12px rgba(212, 175, 55, 0.1);
    }
    
    /* Logo with 3D gold glow */
    .logo-img {
        max-width: 280px;
        height: auto;
        display: block;
        margin: 0 auto 1rem auto;
        /* 3D depth via layered shadows */
        filter: 
            drop-shadow(0 1px 0 #b89e2c)
            drop-shadow(0 2px 0 #a68d27)
            drop-shadow(0 3px 0 #947c22)
            drop-shadow(0 4px 0 #826b1d)
            drop-shadow(0 5px 0 #705a18)
            drop-shadow(0 0 20px rgba(212, 175, 55, 0.3));
        /* Gentle floating animation */
        animation: float 6s ease-in-out infinite;
    }
    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-8px); }
    }
    
    /* Trademark text */
    .trademark {
        color: #D32F2F;
        font-weight: 600;
        font-size: 1rem;
        margin-top: 0.5rem;
        text-align: center;
    }
    
    /* Input box — clean, accessible */
    .stTextInput input {
        font-size: 1.3rem !important;
        padding: 14px !important;
        border: 2px solid #D4AF37 !important;
        border-radius: 12px !important;
        background: #fff !important;
        color: #000 !important;
        width: 100% !important;
        max-width: 500px;
        margin: 1rem auto !important;
        display: block !important;
    }
    
    /* Send button — red, bold */
    .stButton button {
        background: #D32F2F !important;
        color: white !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        padding: 12px 24px !important;
        border-radius: 12px !important;
        border: none !important;
        width: 50% !important;
        max-width: 200px;
        margin: 1rem auto !important;
        display: block !important;
    }
    
    /* Response box — readable */
    .stSuccess, .answer-box {
        background: #f9f9f9 !important;
        border-left: 4px solid #D4AF37 !important;
        border-radius: 8px !important;
        padding: 16px !important;
        margin: 1rem auto !important;
        max-width: 600px !important;
        color: #222 !important;
        font-size: 1.2rem !important;
    }
    
    /* Points display */
    .points {
        color: #D4AF37 !important;
        font-weight: 800 !important;
        font-size: 1.5rem !important;
        text-align: center !important;
    }
    
    /* Mobile responsive */
    @media (max-width: 600px) {
        .falling-text { font-size: 3rem !important; }
        .logo-img { max-width: 200px !important; }
        .stButton button { width: 70% !important; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------- HOME PAGE — LOGO + FALLING TEXT + TRADEMARK -------------------
if st.session_state.mode is None and not st.session_state.show_about:
    # Falling background text
    st.markdown('<div class="falling-text">ShineGPT</div>', unsafe_allow_html=True)
    
    # Logo section with FALLBACK if image fails
    st.markdown(
        """
        <div class="brand-box">
            <img 
                src="https://i.ibb.co/rKkwTtgw/IMG-7801.jpg" 
                alt="ShineGPT Logo" 
                class="logo-img"
                onerror="this.onerror=null; this.src='data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%22280%22 height=%2280%22 viewBox=%220 0 280 80%22><rect width=%22280%22 height=%2280%22 fill=%22%23D4AF37%22/><text x=%2250%%22 y=%2250%%22 dominant-baseline=%22middle%22 text-anchor=%22middle%22 fill=%22white%22 font-size=%2224%22 font-weight=%22bold%22 font-family=%22Arial%22>SHINEGPT</text></svg>';"
            >
            <p class="trademark">Powered by KS1 Empire Global Foundation (KS1EGF)</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Mode buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📱 SMS Mode", key="btn_sms"):
            st.session_state.mode = 'sms'
            st.session_state.messages = []
            st.rerun()
    with col2:
        if st.button("🌐 Online Mode", key="btn_online"):
            st.session_state.mode = 'online'
            st.session_state.messages = []
            st.rerun()
    
    st.markdown("<p style='text-align:center; color:#666; margin:1rem 0;'>Type 'lesson 1' to begin. 50+ lessons available.</p>", unsafe_allow_html=True)
    
    if st.button("📖 About", key="btn_about"):
        st.session_state.show_about = True
        st.rerun()

# ------------------- SMS MODE -------------------
elif st.session_state.mode == 'sms':
    st.markdown("<h2 style='text-align:center; color:#D4AF37;'>📱 SMS Mode</h2>", unsafe_allow_html=True)
    
    # Show message history
    for msg in st.session_state.messages:
        if msg["role"] == "shingpt":
            st.markdown(f"<div class='answer-box'>{msg['content']}</div>", unsafe_allow_html=True)
    
    # Input + Send
    user_input = st.text_input("", placeholder="Type 'lesson 1', 'help', or 'points'...", key="sms_input")
    if st.button("Send", key="send_sms") and user_input:
        txt = user_input.strip().lower()
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        if txt in sms_responses:
            reply = sms_responses[txt]
            if txt.startswith("lesson "):
                add_points(10)
            st.session_state.messages.append({"role": "shingpt", "content": reply})
        else:
            st.session_state.messages.append({"role": "shingpt", "content": "Type 'lesson 1' to start. Or 'help' for commands."})
        st.rerun()
    
    # Back button
    if st.button("← Home", key="back_sms"):
        st.session_state.mode = None
        st.session_state.messages = []
        st.rerun()

# ------------------- ONLINE MODE (PLACEHOLDER) -------------------
elif st.session_state.mode == 'online':
    st.markdown("<h2 style='text-align:center; color:#D4AF37;'>🌐 Online Mode</h2>", unsafe_allow_html=True)
    st.info("Coming soon! For now, use SMS Mode to learn.")
    if st.button("← Home", key="back_online"):
        st.session_state.mode = None
        st.rerun()

# ------------------- ABOUT PAGE -------------------
elif st.session_state.show_about:
    st.markdown("<h2 style='text-align:center; color:#D4AF37;'>📖 About ShineGPT</h2>", unsafe_allow_html=True)
    st.markdown("""
    ShineGPT is a free, nonprofit educational app by **KS1 Empire Global Foundation**.  
    Learn AI, Blockchain, Web3, IoT, and more — even without internet.  
    Earn points. Grow your knowledge. Empower your future.  
    Built with love for every curious mind in Africa and beyond. 🌍✨
    """)
    if st.button("← Home", key="back_about"):
        st.session_state.show_about = False
        st.rerun()

# ------------------- SIDEBAR — POINTS -------------------
st.sidebar.markdown("---")
st.sidebar.subheader("🏆 Your Points")
st.sidebar.markdown(f"<div class='points'>{st.session_state.user_points}</div>", unsafe_allow_html=True)
st.sidebar.info("Earn 10 points per lesson. No data cost in SMS Mode.")
