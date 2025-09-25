import streamlit as st

# ------------------- INITIALIZE SESSION STATE -------------------
if 'user_points' not in st.session_state:
    st.session_state.user_points = 0

# ------------------- 50 OFFLINE LESSONS -------------------
lessons = {
    1: "The 4th Industrial Revolution is when technology like AI, robots, and the internet merge with our physical world to change how we live and work.",
    2: "The 1st Industrial Revolution used steam engines. The 2nd used electricity. The 3rd used computers. The 4th uses smart systems.",
    # ... add all other lessons up to 50
}

# ------------------- SMS MODE RESPONSES — MUST BE A DICT — NOT A SET -------------------
sms_responses = {
    "hello": "Hello! I'm ShineGPT. Type 'lesson 1' to start learning about the 4th Industrial Revolution. Or type 'help' for more.",
    "hi": "Hi there! Type 'lesson 1' to begin your first lesson.",
    "help": "Type: 'lesson 1', 'lesson 2', ..., 'lesson 50' to learn. Or 'points' to see your score.",
    "thank you": "You're welcome! Keep learning. Type 'lesson 1' to continue.",
    "thanks": "You're welcome! Learning is power. Try 'lesson 1'.",
    "bye": "Goodbye! Come back soon. Remember: Knowledge is your superpower.",
    "points": f"You have {st.session_state.user_points} points. Earn 10 per lesson. Type 'lesson 1' to start!",
}

# ------------------- ✅ FORCE IT TO STAY A DICT — NO ACCIDENTAL SET -------------------
# Now, safely add lesson responses
for i in range(1, 51):
    lesson_text = lessons.get(i, "Lesson not found.")
    sms_responses[f"lesson {i}"] = (
        lesson_text + f"\n\n✨ You earned 10 points! Type 'lesson {i+1}' to continue."
    )

# ------------------- POINTS FUNCTION -------------------
def add_points(points):
    st.session_state.user_points += points

# ------------------- MAIN APP — CLEAN & WORKING -------------------
st.set_page_config(page_title="ShineGPT", page_icon="🌍", layout="centered")

# Custom CSS — Full-width input box
st.markdown(
    """
    <style>
    .stTextInput > div > div > input {
        font-size: 1.4rem;
        padding: 20px;
        border-radius: 12px;
        border: 2px solid #D4AF37;
        background-color: #111111;
        color: white;
        width: 95% !important;
        max-width: 700px;
        margin: 1.5rem auto;
        display: block;
    }
    .stButton > button {
        background-color: #D32F2F !important;
        color: white !important;
        font-weight: 700;
        border-radius: 12px;
        font-size: 1.2rem;
        padding: 15px 30px;
        margin: 1.5rem auto;
        width: 90%;
        max-width: 400px;
        display: block;
    }
    .stSuccess {
        max-width: 95%;
        margin: 1.5rem auto;
        padding: 25px;
        background-color: #1a1a1a;
        border-left: 5px solid #D4AF37;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------- HEADER -------------------
st.markdown("<h1 style='color: #D4AF37; text-align: center;'>SHINEGPT</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: white; text-align: center;'>Learn. Earn Knowledge. Empower Yourself.</p>", unsafe_allow_html=True)
st.markdown("<p style='color: #D32F2F; text-align: center;'>Powered by KS1 Empire Foundation</p>", unsafe_allow_html=True)

# ------------------- SMS MODE UI -------------------
st.header("📱 SMS Mode — No Internet Needed!")
st.info("Just type: lesson 1, hello, help, points")

user_input = st.text_input("Type your message:", key="sms_input")
if st.button("Send (SMS)", key="send_sms") and user_input:
    user_input_lower = user_input.strip().lower()

    # Ensure we're using dict lookup
    response = sms_responses.get(user_input_lower, "I don't understand. Try typing 'help'.")

    if user_input_lower.startswith("lesson ") and user_input_lower in sms_responses:
        add_points(10)

    st.success(response)

# ------------------- DISPLAY POINTS -------------------
st.sidebar.markdown("---")
st.sidebar.subheader("🏆 Your Points")
st.sidebar.write(f"**{st.session_state.user_points}** points")
st.sidebar.info("Earn 10 points per lesson. No data cost.")
