import streamlit as st
import pyttsx3
from lessons import lessons  # Only 50 real lessons loaded — safe and perfect

# ------------------- SESSION STATE -------------------
if 'user_points' not in st.session_state:
    st.session_state.user_points = 0
if 'current_lesson' not in st.session_state:
    st.session_state.current_lesson = 1

# ------------------- INIT TTS ENGINE -------------------
@st.cache_resource
def init_tts():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)   # Speed
    engine.setProperty('volume', 0.9) # Volume
    return engine

tts_engine = init_tts()

# ------------------- SPEAK FUNCTION -------------------
def speak(text):
    try:
        tts_engine.say(text)
        tts_engine.runAndWait()
    except Exception as e:
        st.warning("🔊 Voice not available on this device (try on mobile).")

# ------------------- SMS RESPONSES -------------------
def get_sms_response(lesson_key):
    lesson_num = int(lesson_key.split()[-1])
    if lesson_num in lessons:
        lesson_text = lessons[lesson_num]
    else:
        if lesson_num > 50:
            return "You've completed all 50 real lessons! 🎉 You're a ShineGPT pioneer! Type 'points' to see your progress."
        else:
            return "Lesson not found. Type 'lesson 1' to start."

    return lesson_text + f"\n\n✨ You earned 10 points! Type 'lesson {lesson_num + 1}' to continue."

# ------------------- POINTS FUNCTION -------------------
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
st.info("Type: lesson 1, hello, help, points, speak")

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
- type 'speak' to hear the lesson aloud (works on mobile)
No internet needed! All lessons work offline.
        """
    elif user_input_lower == "points":
        response = f"🎉 You have {st.session_state.user_points} points!"
    elif user_input_lower == "hello":
        response = "Hello! 👋 Type 'lesson 1' to begin your journey with ShineGPT."
    elif user_input_lower == "speak":
        # Speak the current lesson
        if st.session_state.current_lesson <= 50:
            lesson_text = lessons[st.session_state.current_lesson]
            speak(lesson_text)
            response = "🔊 Playing your last lesson aloud..."
        else:
            response = "You’ve completed all 50 lessons! 🎉 Type 'lesson 1' to restart."
    elif user_input_lower.startswith("lesson "):
        try:
            lesson_num = int(user_input_lower.split()[-1])
            if lesson_num < 1:
                response = "Start with lesson 1!"
            elif lesson_num > 50:
                response = "You've completed all 50 real lessons! 🎉 You're a ShineGPT pioneer! Type 'points' to see your progress."
            else:
                response = get_sms_response(user_input_lower)
                add_points(10)
                st.session_state.current_lesson = lesson_num
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
st.sidebar.caption("You're learning AI, Big Data, Blockchain & Crypto — 50 real lessons. No repeats. No placeholders.")
