import streamlit as st
from gtts import gTTS
import io
import base64

# ------------------- SESSION STATE -------------------
if 'user_points' not in st.session_state:
    st.session_state.user_points = 0
if 'current_lesson' not in st.session_state:
    st.session_state.current_lesson = 1

# ------------------- LESSONS -------------------
lessons = {
    1: "The 4th Industrial Revolution is when technology like AI, robots, and the internet merge with our physical world to change how we live and work.",
    2: "AI stands for Artificial Intelligence — machines that can learn, reason, and make decisions like humans.",
    3: "Machine Learning is a subset of AI where computers learn from data without being explicitly programmed.",
    4: "Data is the new oil — it fuels AI systems and helps them understand patterns in the world.",
    5: "Neural networks are computing systems inspired by the human brain, used to recognize patterns.",
    6: "Supervised learning uses labeled data to teach AI models — like showing photos of cats and dogs.",
    7: "Unsupervised learning finds hidden patterns in data without labels — like grouping customers by behavior.",
    8: "Deep Learning uses multi-layered neural networks to solve complex problems like image and speech recognition.",
    9: "Natural Language Processing (NLP) lets machines understand and respond to human language — like chatbots.",
    10: "Computer Vision allows machines to 'see' and interpret images and videos — used in facial recognition.",
    11: "AI ethics means building systems that are fair, transparent, and avoid bias — especially in hiring or policing.",
    12: "Bias in AI happens when training data reflects human prejudices — leading to unfair outcomes.",
    13: "Explainable AI (XAI) helps us understand why an AI made a decision — critical for trust and accountability.",
    14: "Generative AI creates new content — like images, music, or text — using models like GPT and DALL·E.",
    15: "LLM stands for Large Language Model — AI trained on massive text datasets to understand and generate human language.",
    16: "Prompt engineering is the skill of writing clear, effective instructions to get better results from AI.",
    17: "Fine-tuning is when you train a pre-trained AI model on your own data to make it better at a specific task.",
    18: "AI agents are programs that can act autonomously — like scheduling meetings or managing smart homes.",
    19: "Reinforcement learning is when AI learns by trial and error, rewarded for good actions — like training a robot.",
    20: "AI can assist doctors by analyzing X-rays faster and more accurately than humans in some cases.",
    21: "AI-powered translation tools now work in real-time — breaking language barriers for global communication.",
    22: "AI in agriculture helps farmers predict crop yields, detect diseases, and optimize water use.",
    23: "AI chatbots are used in customer service to answer questions 24/7 — reducing wait times and costs.",
    24: "AI can generate personalized learning paths for students based on their progress and weaknesses.",
    25: "AI can detect fake news by analyzing language patterns, sources, and spread behavior.",
    26: "AI doesn't 'think' — it calculates probabilities based on patterns in data it was trained on.",
    27: "AI can help identify endangered species from camera trap images — aiding wildlife conservation.",
    28: "AI is used in music to compose new melodies, remix songs, and even mimic the style of famous artists.",
    29: "AI can write poetry, stories, and even screenplays — but it doesn't feel emotion like humans do.",
    30: "AI assistants like Siri and Alexa use voice recognition and NLP to understand spoken commands.",
    31: "AI can predict traffic jams by analyzing GPS data from millions of phones and cars.",
    32: "AI helps banks detect fraudulent transactions by spotting unusual spending patterns.",
    33: "AI-driven robots are now used in warehouses to pick, pack, and ship orders faster than humans.",
    34: "AI can analyze satellite images to track deforestation, urban growth, and illegal mining.",
    35: "AI models are trained on massive datasets — sometimes containing billions of words or images.",
    36: "Overfitting happens when an AI model memorizes training data instead of learning general patterns.",
    37: "Underfitting happens when an AI model is too simple to capture the underlying patterns in data.",
    38: "Transfer learning lets AI reuse knowledge from one task to improve performance on a new, related task.",
    39: "OpenAI, Google DeepMind, and Meta are leading companies in AI research and development.",
    40: "AI models require huge amounts of electricity to train — raising concerns about their carbon footprint.",
    41: "Edge AI runs AI models directly on devices like phones or sensors — no internet needed.",
    42: "AI can help translate sign language into text or speech — improving accessibility for the deaf community.",
    43: "AI can generate personalized workout plans based on your fitness goals and body metrics.",
    44: "AI tools can now detect early signs of diseases like cancer from medical scans with high accuracy.",
    45: "AI can analyze social media to predict mental health trends and identify people at risk of depression.",
    46: "AI-powered drones are used to deliver medicine to remote villages — saving lives in emergencies.",
    47: "AI can generate realistic fake videos called 'deepfakes' — which can be used for both entertainment and fraud.",
    48: "AI can write code for you — tools like GitHub Copilot suggest entire functions as you type.",
    49: "AI can help teachers grade essays by checking grammar, structure, and relevance — but human review is still key.",
    50: "AI doesn't have consciousness — it simulates understanding but doesn't experience thoughts or feelings."
}

# ------------------- HELPER: GENERATE AUDIO FROM TEXT -------------------
def text_to_audio(text):
    """Convert text to MP3 audio using gTTS and return both bytes and base64 for playback"""
    tts = gTTS(text=text, lang='en', slow=False)
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    audio_bytes = fp.read()
    b64 = base64.b64encode(audio_bytes).decode()
    return audio_bytes, f"audio/mp3;base64,{b64}"

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
- type 'speak' to hear the lesson aloud
- audio automatically downloads when you click "Download"
No internet needed after audio is generated!
        """
    elif user_input_lower == "points":
        response = f"🎉 You have {st.session_state.user_points} points!"
    elif user_input_lower == "hello":
        response = "Hello! 👋 Type 'lesson 1' to begin your journey with ShineGPT."
    elif user_input_lower == "speak":
        if st.session_state.current_lesson <= 50:
            lesson_text = lessons[st.session_state.current_lesson]
            audio_bytes, audio_src = text_to_audio(lesson_text)
            st.markdown(f"""
                <audio controls style="width: 100%;">
                    <source src="{audio_src}" type="audio/mp3">
                    Your browser does not support the audio element.
                </audio>
            """, unsafe_allow_html=True)
            st.download_button(
                label="💾 Download this lesson as MP3",
                data=audio_bytes,
                file_name=f"lesson_{st.session_state.current_lesson}.mp3",
                mime="audio/mp3",
                key=f"download_{st.session_state.current_lesson}"
            )
            response = "🔊 Playing your last lesson aloud. Click 'Download' to save it forever!"
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
st.sidebar.caption("You're learning AI — 50 real lessons. No repeats. No placeholders.")
