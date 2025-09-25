import streamlit as st
from lessons import lessons  # Only 200 lessons loaded at startup — safe!

# ------------------- SESSION STATE -------------------
if 'user_points' not in st.session_state:
    st.session_state.user_points = 0
if 'current_lesson' not in st.session_state:
    st.session_state.current_lesson = 1  # Start at lesson 1

# ------------------- HELPER: GENERATE LESSON ON DEMAND -------------------
def get_lesson_text(lesson_num):
    """Generate lesson text on-demand if not pre-loaded"""
    if lesson_num in lessons:
        return lessons[lesson_num]
    
    # Generate dynamically for lessons 51-1000 (AI extended)
    if 51 <= lesson_num <= 1000:
        topic = "AI" if lesson_num <= 1000 else "Big Data" if lesson_num <= 1500 else "AI Advanced" if lesson_num <= 2000 else "Blockchain"
        return f"Lesson {lesson_num}: You're learning about {topic} — keep going! This lesson is dynamically generated to save memory."
    
    # For lessons 1001-1500 (AI Advanced)
    elif 1001 <= lesson_num <= 1500:
        return f"Lesson {lesson_num}: You're learning advanced AI concepts — well done for reaching here!"
    
    # For lessons 1501-2000 (Blockchain)
    elif 1501 <= lesson_num <= 2000:
        return f"Lesson {lesson_num}: You're exploring blockchain — you're becoming a tech leader!"
    
    else:
        return "Lesson not found. Type 'lesson 1' to start."

# ------------------- SMS RESPONSES — GENERATED ON-DEMAND -------------------
def get_sms_response(lesson_key):
    """Generate response only when user asks for a lesson"""
    lesson_num = int(lesson_key.split()[-1])
    lesson_text = get_lesson_text(lesson_num)
    return lesson_text + f"\n\n✨ You earned 10 points! Type 'lesson {lesson_num + 1}' to continue."

# ------------------- POINTS FUNCTION -------------------
def add_points(points):
    st.session_state.user_points += points

# ------------------- STYLING — FULL-WIDTH INPUT & BUTTON -------------------
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
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------- HEADER -------------------
st.markdown("<h1>SHINEGPT</h1>", unsafe_allow_html=True)
st.markdown("<p>Learn. Earn Knowledge. Empower Yourself.</p>", unsafe_allow_html=True)
st.markdown("<p style='color: #D32F2F;'>Powered by KS1 Empire Foundation</p>", unsafe_allow_html=True)

# ------------------- SMS MODE UI -------------------
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

    # Custom responses for special commands
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
            elif lesson_num > 2000:
                response = "You've reached the end of the curriculum! 🎉 You're a ShineGPT champion!"
            else:
                response = get_sms_response(user_input_lower)
                add_points(10)
                st.session_state.current_lesson = lesson_num  # Track progress
        except:
            response = "Type 'lesson 1' to start."
    else:
        response = "I don't understand. Try typing 'help'."

    st.success(response)

# ------------------- SIDEBAR — POINTS & PROGRESS -------------------
st.sidebar.markdown("---")
st.sidebar.subheader("🏆 Your Points")
st.sidebar.write(f"**{st.session_state.user_points}** points")
st.sidebar.info("Earn 10 per lesson. No data cost.")

st.sidebar.subheader("📖 Progress")
st.sidebar.write(f"**Lesson {st.session_state.current_lesson}** completed")
st.sidebar.caption("You're learning AI, Big Data, Blockchain & Crypto!")
