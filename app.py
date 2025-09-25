import streamlit as st

# ------------------- SESSION STATE -------------------
if 'user_points' not in st.session_state:
    st.session_state.user_points = 0

# ------------------- 50 LESSONS -------------------
lessons = {
    1: "The 4th Industrial Revolution is when technology like AI, robots, and the internet merge with our physical world to change how we live and work.",
    2: "The 1st Industrial Revolution used steam engines. The 2nd used electricity. The 3rd used computers. The 4th uses smart systems.",
    # ... (keep all 50 lessons)
}

# ------------------- SMS RESPONSES -------------------
sms_responses = { -m "Fix: sms_responses is now a proper dict — no more 'set' error"... }  # your responses

# AUTO-GENERATE FOR ALL 50
for i in range(1, 51):
    sms_responses[f"lesson {i}"] = lessons[i] + f"\n\n✨ You earned 10 points! Type 'lesson {i+1}' to continue."

# ------------------- POINTS FUNCTION -------------------
def add_points(points):
    st.session_state.user_points += points

# ------------------- STYLING — FULL-WIDTH INPUT -------------------
st.markdown(
    """
    <style>
    .stTextInput > div > div > input {
        font-size: 1.4rem;
        padding: 20px;
        border-radius: 12px;
        border: 2px solid #D4AF37;
        background-color: #111;
        color: white;
        width: 95% !important;
        max-width: 700px;
        margin: 1.5rem auto;
        display: block;
    }
    .stButton>button {
        background-color: #D32F2F !important;
        color: white !important;
        font-weight: 700;
        font-size: 1.2rem;
        padding: 15px 30px;
        margin: 1.5rem auto;
        display: block;
        width: 90%;
        max-width: 400px;
    }
    .stSuccess {
        max-width: 90%;
        margin: 1.5rem auto;
        padding: 25px;
        background-color: #1a1a1a;
        border-left: 5px solid #D4AF37;
        font-size: 1.4rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------- HEADER -------------------
st.markdown("<h1 style='text-align: center; color: #D4AF37;'>SHINEGPT</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>Learn. Earn Knowledge. Empower Yourself.</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #D32F2F;'>Powered by KS1 Empire Foundation</p>", unsafe_allow_html=True)

# ------------------- SMS MODE UI -------------------
st.header("📱 SMS Mode — No Internet Needed!")
st.info("Type: lesson 1, hello, help, points")

user_input = st.text_input("Type your message:", key="sms_input")
if st.button("Send (SMS)", key="send_sms") and user_input:
    user_input_lower = user_input.strip().lower()
    response = sms_responses.get(user_input_lower, "I don't understand. Try typing 'help'.")
    
    if user_input_lower.startswith("lesson ") and user_input_lower in sms_responses:
        add_points(10)

    st.success(response)

# ------------------- SIDEBAR — POINTS -------------------
st.sidebar.markdown("---")
st.sidebar.subheader("🏆 Your Points")
st.sidebar.write(f"**{st.session_state.user_points}** points")
st.sidebar.info("Earn 10 per lesson. No data cost.")
