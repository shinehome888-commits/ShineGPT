import streamlit as st

# ------------------- SESSION STATE -------------------
if 'user_points' not in st.session_state:
    st.session_state.user_points = 0

# ------------------- 50 LESSONS -------------------
# Replace these with your actual lesson content if needed
lessons = {
    1: "The 4th Industrial Revolution is when technology like AI, robots, and the internet merge with our physical world to change how we live and work.",
    2: "The 1st Industrial Revolution used steam engines. The 2nd used electricity. The 3rd used computers. The 4th uses smart systems.",
    3: "AI stands for Artificial Intelligence — machines that can learn, reason, and make decisions like humans.",
    4: "Machine Learning is a subset of AI where computers learn from data without being explicitly programmed.",
    5: "Data is the new oil — it fuels AI systems and helps them understand patterns in the world.",
    6: "IoT (Internet of Things) connects everyday objects like fridges and lights to the internet to collect and share data.",
    7: "Cloud computing lets you store and access data and programs over the internet instead of your computer’s hard drive.",
    8: "5G is the next generation of mobile networks — faster, more reliable, and supports millions of connected devices.",
    9: "Blockchain is a secure digital ledger that records transactions without needing a central authority like a bank.",
    10: "Robotics combines engineering and AI to build machines that can perform tasks autonomously.",
    11: "Automation replaces manual tasks with machines or software — increasing speed and reducing errors.",
    12: "Digital literacy means knowing how to use technology safely, responsibly, and effectively.",
    13: "Cybersecurity protects your data, devices, and identity from hackers and online threats.",
    14: "Algorithm is a step-by-step set of instructions — like a recipe — that computers follow to solve problems.",
    15: "Big Data refers to extremely large datasets that may be analyzed to reveal patterns, trends, and associations.",
    16: "Augmented Reality (AR) overlays digital information onto the real world — think Pokémon GO or virtual try-ons.",
    17: "Virtual Reality (VR) creates a fully digital environment you can step into using a headset.",
    18: "3D printing turns digital designs into physical objects layer by layer — revolutionizing manufacturing.",
    19: "Biotechnology uses living systems to develop products — like biofuels, medicines, and genetically modified crops.",
    20: "Renewable energy (solar, wind, hydro) is clean and sustainable — key to fighting climate change.",
    21: "Smart cities use sensors and data to improve traffic, energy use, waste management, and public safety.",
    22: "E-learning platforms let you learn anytime, anywhere — even without internet, with offline apps.",
    23: "Digital payment systems like mobile money are transforming finance, especially in developing countries.",
    24: "Open-source software is free to use, modify, and share — empowering innovation worldwide.",
    25: "Ethical AI means building systems that are fair, transparent, and respect human rights.",
    26: "Bias in AI happens when training data reflects unfair human prejudices — leading to discriminatory outcomes.",
    27: "Privacy means controlling who can see your personal data — always read app permissions carefully.",
    28: "Digital footprint is the trail of data you leave behind online — think before you post!",
    29: "Digital divide is the gap between people who have access to technology and those who don’t.",
    30: "Coding is not just for engineers — it’s problem-solving with logic, and anyone can learn it.",
    31: "Python is one of the easiest programming languages to start with — great for beginners and AI.",
    32: "Scratch is a visual coding platform made for kids to learn programming through games and animations.",
    33: "Computational thinking means breaking big problems into small steps — a skill useful in all areas of life.",
    34: "The future of work will demand adaptability, creativity, and digital skills — not just memorization.",
    35: "Gig economy jobs (like Uber or Fiverr) are growing — flexibility is key in the new job market.",
    36: "Remote work is here to stay — tools like Zoom, Slack, and Google Docs make it possible anywhere.",
    37: "Online collaboration tools help teams work together across continents — no need to be in the same room.",
    38: "Digital identity is your online reputation — protect it like your real-world identity.",
    39: "Fake news spreads faster online — always check sources before sharing information.",
    40: "Critical thinking helps you question what you see online and avoid being misled.",
    41: "Entrepreneurship means creating your own opportunities — tech skills give you power to build solutions.",
    42: "You don’t need money to start — just ideas, persistence, and the internet (or offline tools!).",
    43: "STEM education (Science, Technology, Engineering, Math) opens doors to high-impact careers.",
    44: "Girls and women belong in tech too — diversity makes innovation stronger and fairer.",
    45: "Learning never stops — even after school, keep exploring, asking questions, and trying new things.",
    46: "Your phone is a supercomputer — use it to learn, not just scroll.",
    47: "Technology should serve humanity — not control it. Stay in charge of your tools.",
    48: "Small steps lead to big changes. Start with one lesson. You’re already on the right path.",
    49: "ShineGPT is here to help you grow — no data cost, no barriers. Keep going!",
    50: "You’ve completed all 50 lessons! 🎉 You’re now part of the digital generation shaping the future. Keep shining!"
}

# ------------------- SMS RESPONSES -------------------
sms_responses = {}  # Initialize as empty dict

# AUTO-GENERATE FOR ALL 50 LESSONS
for i in range(1, 51):
    lesson_key = f"lesson {i}"
    sms_responses[lesson_key] = lessons[i] + f"\n\n✨ You earned 10 points! Type 'lesson {i+1}' to continue."

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
    else:
        response = sms_responses.get(user_input_lower, "I don't understand. Try typing 'help'.")

    # Award points if user types a valid lesson
    if user_input_lower.startswith("lesson ") and user_input_lower in sms_responses:
        add_points(10)

    st.success(response)

# ------------------- SIDEBAR — POINTS -------------------
st.sidebar.markdown("---")
st.sidebar.subheader("🏆 Your Points")
st.sidebar.write(f"**{st.session_state.user_points}** points")
st.sidebar.info("Earn 10 per lesson. No data cost.")
