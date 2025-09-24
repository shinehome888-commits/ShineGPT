
import streamlit as st
import gzip

# ------------------- INITIALIZE SESSION STATE -------------------
if 'user_points' not in st.session_state:
    st.session_state.user_points = 0

# ------------------- LOAD ONE LESSON FROM GZIPPED FILE -------------------
def get_lesson(lesson_num):
    try:
        with gzip.open("lessons.txt.gz", "rt", encoding="utf-8") as f:
            for line in f:
                num, text = line.strip().split("|", 1)
                if int(num) == lesson_num:
                    return text
        return None
    except Exception as e:
        return f"⚠️ Error loading lesson: {str(e)}"

# ------------------- SMS MODE RESPONSES -------------------
sms_responses = {
    "hello": "Hello! I'm ShineGPT. Type 'lesson 1' to start learning about the 4th Industrial Revolution. Or type 'help'.",
    "hi": "Hi there! Type 'lesson 1' to begin your first lesson.",
    "help": "Type: 'lesson 1', 'lesson 2', ..., 'lesson 1500' to learn. Or 'points' to see your score.",
    "thank you": "You're welcome! Keep learning. Type 'lesson 1' to continue.",
    "thanks": "You're welcome! Learning is power. Try 'lesson 1'.",
    "bye": "Goodbye! Come back soon. Remember: Knowledge is your superpower.",
    "points": f"You have {st.session_state.user_points} points. Earn 10 per lesson. Type 'lesson 1' to start!",
}

# ------------------- POINTS FUNCTION -------------------
def add_points(points):
    st.session_state.user_points += points

# ------------------- MAIN APP — SIMPLE, SCALABLE, POWERFUL -------------------
st.set_page_config(page_title="ShineGPT", page_icon="🌍", layout="centered")

# Custom CSS — Brand Colors: Gold, Red, Black, White
st.markdown(
    """
    <style>
    body {
        background-color: #000000;
        color: #ffffff;
        font-family: 'Arial', sans-serif;
    }
    h1, h2, h3, h4, p {
        color: #ffffff !important;
        text-align: center;
    }
    h1 {
        font-size: 3.5rem;
        font-weight: 900;
        margin-bottom: 0.5rem;
        color: #D4AF37 !important; /* Gold */
    }
    h4 {
        font-size: 1.3rem;
        color: #D32F2F !important; /* Red */
    }
    .stTextInput > div > div > input {
        font-size: 1.4rem;
        padding: 18px;
        border-radius: 12px;
        border: 2px solid #D4AF37;
        background-color: #111111;
        color: white;
        width: 95%;
        max-width: 700px;
        margin: 1.5rem auto;
        display: block;
    }
    .stButton>button {
        background-color: #D32F2F !important;
        color: white !important;
        font-weight: 700;
        border-radius: 12px;
        padding: 15px 30px !important;
        width: 90%;
        max-width: 400px;
        margin: 1.5rem auto;
        display: block;
    }
    .stSuccess {
        max-width: 95%;
        margin: 1.5rem auto;
        padding: 25px;
        background-color: #1a1a1a;
        border-left: 5px solid #D4AF37;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------- HEADER -------------------
st.markdown("<h1>SHINEGPT</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: white;'>Learn. Earn Knowledge. Empower Yourself.</p>", unsafe_allow_html=True)
st.markdown("<p style='color: #D32F2F;'>Powered by KS1 Empire Foundation</p>", unsafe_allow_html=True)

# ------------------- USER INPUT -------------------
user_input = st.text_input("Type: 'lesson 1', 'lesson 500', or 'help' →", key="sms_input")

if st.button("Send"):
    user_input_lower = user_input.strip().lower()

    # Handle keywords
    if user_input_lower in sms_responses:
        response = sms_responses[user_input_lower]
        if "points" in user_input_lower:
            pass  # Points shown in sidebar
        else:
            st.success(response)

    # Handle lesson request
    elif user_input_lower.startswith("lesson "):
        try:
            lesson_num = int(user_input_lower.split(" ")[1])
            if 1 <= lesson_num <= 1500:
                lesson_text = get_lesson(lesson_num)
                if lesson_text:
                    st.success(lesson_text + f"\n\n✨ You earned 10 points!")
                    add_points(10)
                else:
                    st.error("📚 That lesson is coming soon. Try another number.")
            else:
                st.warning("📌 Please choose a lesson between 1 and 1500.")
        except ValueError:
            st.error("❌ Invalid format. Use: lesson 123")
    else:
        st.info("💡 Try typing:\n- 'lesson 1'\n- 'help'\n- 'points'")

# ------------------- SIDEBAR — POINTS COUNTER -------------------
st.sidebar.markdown("---")
st.sidebar.subheader("🏆 Your Points")
st.sidebar.write(f"**{st.session_state.user_points}** points")
st.sidebar.info("Earn 10 per lesson. No data cost.")

st.sidebar.markdown("## 📚 Quick Access")
st.sidebar.write("Try:")
st.sidebar.code("lesson 1")
st.sidebar.code("lesson 500")
st.sidebar.code("lesson 1500")
