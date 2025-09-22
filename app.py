import streamlit as st

# ------------------- INITIALIZE SESSION STATE -------------------
if 'user_points' not in st.session_state:
    st.session_state.user_points = 0

# ------------------- LOAD LESSONS FROM FILE (LAZY LOAD) -------------------
# This file is ~150MB — but we only load ONE line at a time
LESSONS_FILE = "lessons.txt"

def get_lesson(lesson_num):
    """Fetch one lesson by number — no memory overload"""
    try:
        with open(LESSONS_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                num, text = line.strip().split('|', 1)
                if int(num) == lesson_num:
                    return text
        return None
    except Exception:
        return None

# ------------------- SMS MODE RESPONSES -------------------
sms_responses = {
    "hello": "Hello! I'm ShineGPT. Type 'lesson 1' to start learning. Or type 'sms help' for more.",
    "hi": "Hi there! Type 'lesson 1' to begin your first lesson.",
    "help": "Type: 'lesson 1', 'lesson 2', ..., 'lesson 1000000' to learn. Or 'sms help' to see this again.",
    "sms help": "📱 SMS MODE: No internet needed! Just type:\n- 'lesson 1'\n- 'lesson 2'\n- ... up to 'lesson 1000000'\n- 'hello'\n- 'help'",
    "thank you": "You're welcome! Keep learning. Type 'lesson 1' to continue.",
    "thanks": "You're welcome! Learning is power. Try 'lesson 1'.",
    "bye": "Goodbye! Come back soon. Remember: Knowledge is your superpower.",
    "points": f"You have {st.session_state.user_points} points. Earn 10 per lesson. Type 'lesson 1' to start!",
}

# ------------------- MAIN APP -------------------
st.set_page_config(page_title="ShineGPT", page_icon="🌍", layout="centered")

# ------------------- HOMEPAGE LAYOUT -------------------
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.markdown("<h1 style='color: #D4AF37; font-weight: 900;'>SHINEGPT</h1>", unsafe_allow_html=True)

    st.markdown("<h2 style='color: #ffffff;'>Learn. Earn Knowledge. Empower Yourself.</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #ffffff;'>Powered by KS1 Empire Foundation</h4>", unsafe_allow_html=True)

    # ✅ ONLY SHOW ON HOME PAGE
    if st.session_state.get('page', 'home') == 'home':
        st.markdown(
            "<div style='margin-top: 40px; margin-bottom: 40px;'><strong style='color: #ffffff; font-size: 1.5rem;'>Use the menu on the left</strong></div>",
            unsafe_allow_html=True
        )

# ------------------- SIDEBAR NAVIGATION -------------------
with st.sidebar:
    st.markdown("## 📚 ShineGPT Menu")
    page = st.radio("", ["Home", "SMS Mode (Offline)", "About"], key="nav", label_visibility="collapsed")

# ------------------- PAGE LOGIC -------------------
if page == "Home":
    st.session_state.page = "home"

elif page == "SMS Mode (Offline)":
    st.session_state.page = "sms_mode"
    st.header("📱 SMS Mode — No Internet Needed!")
    st.markdown("""
    **This mode works even on a basic phone!**  
    No data? No problem. Just type:  
    - `lesson 1`  
    - `lesson 100`  
    - `lesson 1000000`  
    - `help`  
    - `points`
    
    💡 Tip: Save this page as a bookmark. You can use it anywhere — even without Wi-Fi.
    
    📚 You have access to **1,000,000 lessons** — one for every child on Earth.
    """)

    user_input = st.text_input("Type your message (SMS-style):", key="sms_input")

    if st.button("Send (SMS)") and user_input:
        user_input_lower = user_input.strip().lower()

        # Handle lesson request
        if user_input_lower.startswith("lesson "):
            try:
                lesson_num = int(user_input_lower.split(" ")[1])
                if 1 <= lesson_num <= 1000000:
                    lesson_text = get_lesson(lesson_num)
                    if lesson_text:
                        st.success(lesson_text + f"\n\n✨ You earned 10 points! Type 'lesson {lesson_num + 1}' to continue.")
                        st.session_state.user_points += 10
                    else:
                        st.error("Lesson not found. Try a number between 1 and 1,000,000.")
                else:
                    st.error("Please type a lesson number between 1 and 1,000,000.")
            except:
                st.error("Type: lesson 123 — where 123 is a number.")

        # Handle other commands
        else:
            response = sms_responses.get(user_input_lower, "I don't understand. Try typing 'sms help'.")
            st.success(response)

elif page == "About":
    st.session_state.page = "about"
    st.header("ℹ️ About ShineGPT")
    st.write("""
    ShineGPT is an educational AI app created by **KS1 Empire Foundation**.  
    It teaches young people in Africa and beyond about **AI, Blockchain, Crypto, Web3, IoT, Big Data, and much more** —  
    with **1,000,000 free, offline lessons** — no internet needed.

    🌍 This is not just an app.  
    It’s a **library**.  
    It’s a **future**.  
    It’s **knowledge for every child** — no matter where they live.

    Our mission:  
    **Learn. Earn Knowledge. Empower Yourself.**
    """)

# ------------------- DISPLAY POINTS (ALWAYS) -------------------
st.sidebar.markdown("---")
st.sidebar.subheader("🏆 Your Points")
st.sidebar.write(f"**{st.session_state.user_points}** points")
st.sidebar.info("Earn 10 points per lesson. No data cost in SMS mode!")
