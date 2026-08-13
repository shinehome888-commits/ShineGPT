import streamlit as st

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

# ------------------- 50 SAMPLE LESSONS (EXPAND AS NEEDED) -------------------
lessons = {
    1: "The 4th Industrial Revolution (4IR) is the fusion of digital, physical, and biological technologies that is transforming how we live, work, and relate to one another.",
    2: "AI (Artificial Intelligence) is at the heart of 4IR — machines that learn, reason, and make decisions like humans — without being explicitly programmed.",
    3: "Machine Learning is a subset of AI that uses data to train systems to recognize patterns — like identifying spam emails or recommending videos.",
    4: "Big Data refers to massive volumes of structured and unstructured information — from social media, sensors, and transactions — that can be analyzed to reveal insights.",
    5: "IoT (Internet of Things) connects everyday objects — fridges, cars, lights — to the internet to collect and share data, making homes and cities smarter.",
    # Add more lessons here...
}

# ------------------- SMS RESPONSES -------------------
sms_responses = {
    "hello": "Hello! I'm ShineGPT. Type 'lesson 1' to start learning.",
    "hi": "Hi there! Type 'lesson 1' to begin your first lesson.",
    "help": "Type: 'lesson 1', 'lesson 2', ..., 'points' to learn or check your score.",
    "thank you": "You're welcome! Keep learning. Type 'lesson 1' to continue.",
    "thanks": "You're welcome! Learning is power. Try 'lesson 1'.",
    "bye": "Goodbye! Come back soon. Remember: Knowledge is your superpower.",
    "points": f"You have {st.session_state.user_points} points. Earn 10 per lesson. Type 'lesson 1' to start!",
}

# Auto-generate lesson responses
for i in range(1, 51):
    lesson_text = lessons.get(i, "Lesson not found.")
    sms_responses[f"lesson {i}"] = lesson_text + f"\n\n✨ You earned 10 points! Type 'lesson {i+1}' to continue."

# ------------------- HELPER FUNCTIONS -------------------
def add_points(points):
    st.session_state.user_points += points

# ------------------- STYLING — DARK THEME, LOGO FOCUSED -------------------
st.markdown(
    """
    <style>
    /* Hide Streamlit chrome */
    #MainMenu, footer, header {visibility: hidden;}
    
    /* DARK BACKGROUND — YOUR BRAND */
    .main {
        background-color: #000000 !important;
        color: #ffffff !important;
        font-family: 'Segoe UI', Arial, sans-serif;
    }
    
    /* Logo container — centered */
    .brand-box {
        text-align: center;
        padding: 2rem 1rem;
        margin: 1rem auto;
        max-width: 400px;
    }
    
    /* Logo with 3D gold glow */
    .logo-img {
        max-width: 300px;
        height: auto;
        display: block;
        margin: 0 auto 1rem auto;
        /* 3D depth via layered drop-shadows */
        filter: 
            drop-shadow(0 1px 0 #b89e2c)
            drop-shadow(0 2px 0 #a68d27)
            drop-shadow(0 3px 0 #947c22)
            drop-shadow(0 4px 0 #826b1d)
            drop-shadow(0 5px 0 #705a18)
            drop-shadow(0 0 25px rgba(212, 175, 55, 0.4));
        /* Gentle floating animation */
        animation: float 6s ease-in-out infinite;
    }
    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-6px); }
    }
    
    /* Trademark text — red, bold */
    .trademark {
        color: #D32F2F !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        margin-top: 0.5rem !important;
        text-align: center !important;
    }
    
    /* Input box — dark theme, gold border */
    .stTextInput input {
        font-size: 1.3rem !important;
        padding: 14px !important;
        border: 2px solid #D4AF37 !important;
        border-radius: 12px !important;
        background-color: #111111 !important;
        color: #ffffff !important;
        width: 100% !important;
        max-width: 500px;
        margin: 1rem auto !important;
        display: block !important;
    }
    
    /* Send button — red, bold */
    .stButton button {
        background-color: #D32F2F !important;
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
    .stButton button:hover {
        background-color: #B71C1C !important;
    }
    
    /* Response box — dark, readable */
    .stSuccess, .answer-box {
        background-color: #1a1a1a !important;
        border-left: 4px solid #D4AF37 !important;
        border-radius: 8px !important;
        padding: 16px !important;
        margin: 1rem auto !important;
        max-width: 600px !important;
        color: #ffffff !important;
        font-size: 1.2rem !important;
    }
    
    /* Points display — gold */
    .points {
        color: #D4AF37 !important;
        font-weight: 800 !important;
        font-size: 1.5rem !important;
        text-align: center !important;
    }
    
    /* Headers — gold */
    h2, h3 {
        color: #D4AF37 !important;
        text-align: center;
    }
    
    /* Body text — white on dark */
    p, li, div {
        color: #ffffff !important;
    }
    
    /* Sidebar — dark */
    .sidebar .sidebar-content {
        background-color: #000000 !important;
        border-right: 1px solid #333;
    }
    
    /* Mobile responsive */
    @media (max-width: 600px) {
        .logo-img { max-width: 220px !important; }
        .stButton button { width: 70% !important; }
        .stTextInput input { font-size: 1.2rem !important; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------- HOME PAGE — LOGO ONLY + TRADEMARK -------------------
if st.session_state.mode is None and not st.session_state.show_about:
    # Logo section — NO text title, just your image
    st.markdown(
        """
        <div class="brand-box">
            <img 
                src="https://i.ibb.co/rKkwTtgw/IMG-7801.jpg" 
                alt="ShineGPT Logo" 
                class="logo-img"
                onerror="this.style.display='none';"
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
    
    st.markdown("<p style='text-align:center; color:#ccc; margin:1.5rem 0;'>Type 'lesson 1' to begin learning. 50+ lessons available.</p>", unsafe_allow_html=True)
    
    if st.button("📖 About", key="btn_about"):
        st.session_state.show_about = True
        st.rerun()

# ------------------- SMS MODE -------------------
elif st.session_state.mode == 'sms':
    st.markdown("<h2 style='text-align:center;'>📱 SMS Mode — No Internet Needed</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#ccc;'>Type 'lesson 1', 'help', or 'points'</p>", unsafe_allow_html=True)

    # Show message history
    for msg in st.session_state.messages:
        if msg["role"] == "shingpt":
            st.markdown(f"<div class='answer-box'>{msg['content']}</div>", unsafe_allow_html=True)
    
    # Input + Send
    user_input = st.text_input("", placeholder="Type your message...", key="sms_input")
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
    st.markdown("<h2 style='text-align:center;'>🌐 Online Mode</h2>", unsafe_allow_html=True)
    st.info("Coming soon! For now, use SMS Mode to learn.")
    if st.button("← Home", key="back_online"):
        st.session_state.mode = None
        st.rerun()

# ------------------- ABOUT PAGE -------------------
elif st.session_state.show_about:
    st.markdown("<h2 style='text-align:center;'>📖 About ShineGPT</h2>", unsafe_allow_html=True)
    st.markdown("""
    ShineGPT is a free, nonprofit educational app by **KS1 Empire Global Foundation**.  
    Learn AI, Blockchain, Web3, IoT, and more — even without internet.  
    Earn points. Grow your knowledge. Empower your future.  
    Built with love for every curious mind in Africa and beyond. 🌍✨
    """, unsafe_allow_html=False)
    if st.button("← Home", key="back_about"):
        st.session_state.show_about = False
        st.rerun()

# ------------------- SIDEBAR — POINTS -------------------
st.sidebar.markdown("---")
st.sidebar.subheader("🏆 Your Points")
st.sidebar.markdown(f"<div class='points'>{st.session_state.user_points}</div>", unsafe_allow_html=True)
st.sidebar.info("Earn 10 points per lesson. No data cost in SMS Mode.")

# ------------------- FOOTER WATERMARK -------------------
st.markdown(
    "<br><p style='text-align:center; color:#666; font-size:0.8rem;'>"
    "@2026 ShineGPT - A nonprofit project by KS1 Empire Global Foundation (KS1EGF).<br>"
    "Built With Love For Every Curious Mind."
    "</p>",
    unsafe_allow_html=True
)
