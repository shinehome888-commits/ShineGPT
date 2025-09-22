import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# ------------------- INITIALIZE SESSION STATE -------------------
if 'user_points' not in st.session_state:
    st.session_state.user_points = {}

# ------------------- 50 OFFLINE LESSONS (FOR SMS MODE ONLY) -------------------
lessons = {
    1: "The 4th Industrial Revolution is when technology like AI, robots, and the internet merge with our physical world to change how we live and work.",
    2: "The 1st Industrial Revolution used steam engines. The 2nd used electricity. The 3rd used computers. The 4th uses smart systems.",
    3: "The 4th Industrial Revolution started around 2010 — when phones became powerful, internet became global, and machines started learning on their own.",
    4: "Unlike past revolutions, the 4IR is not just about machines — it’s about people, data, and connection working together as one system.",
    5: "In the 4IR, your fridge, car, or school bag can talk to the internet — this is called the Internet of Things (IoT).",
    6: "The 4IR makes things faster, smarter, and cheaper — but it also changes jobs, schools, and even how we think.",
    7: "Artificial Intelligence (AI) is the brain of the 4IR — it lets machines learn from data without being told exactly what to do.",
    8: "Robotics in the 4IR are not just metal arms — they are soft, smart, and can help doctors, farmers, and teachers.",
    9: "Big Data means collecting huge amounts of information — like how many students walk to school — to find patterns and make better decisions.",
    10: "Cloud computing means storing files and running apps on the internet instead of on your phone or computer — so you can use them anywhere.",
    11: "Blockchain is a digital notebook that everyone can see but no one can cheat — it helps keep records safe without banks or governments.",
    12: "Cybersecurity is protecting your data, phone, and identity from hackers in the 4IR — because everything is connected.",
    13: "Automation means machines do tasks that humans used to do — like packing boxes or driving trucks — using sensors and AI.",
    14: "3D printing lets you create objects like tools or toys by printing them layer by layer from a digital design — no factory needed.",
    15: "Augmented Reality (AR) adds digital images to your real world — like seeing a robot appear on your desk through your phone camera.",
    16: "Virtual Reality (VR) creates a completely new digital world — you wear glasses and feel like you're inside a game or classroom.",
    17: "Digital twins are virtual copies of real things — like a digital copy of a farm or hospital — used to test changes before making them real.",
    18: "Smart cities use sensors and AI to manage traffic, lights, water, and waste — so they run cleaner and smoother.",
    19: "The 4IR is not just for rich countries — it’s for everyone. Even small villages can use mobile apps to learn, sell goods, or get health advice.",
    20: "The 4IR is not magic — it’s built by people. You can learn to build it too.",
    21: "AI learns by seeing examples — like showing it 1,000 pictures of cats until it knows what a cat looks like.",
    22: "Machine learning is when computers improve themselves over time by practicing — like learning math by solving many problems.",
    23: "Neural networks are computer systems designed to think like human brains — made of layers that pass information forward.",
    24: "Natural Language Processing (NLP) lets AI understand and answer human language — like when you ask shineGPT a question.",
    25: "Chatbots like me are powered by NLP — we read your words and reply based on what we’ve learned from millions of conversations.",
    26: "Generative AI can create new things — like writing stories, drawing pictures, or composing music — from just a few words.",
    27: "Computer vision lets machines ‘see’ and recognize objects — like a phone unlocking with your face or a robot picking fruit.",
    28: "Predictive analytics uses data to guess what will happen next — like predicting if a student will drop out or if a crop will fail.",
    29: "AI doesn’t have feelings — it only follows patterns. But it can help humans make fairer, smarter choices.",
    30: "Bias in AI happens when it learns from unfair data — like thinking only boys can be engineers. We must fix this.",
    31: "Robots in factories now work beside humans — not replacing them, but helping them lift heavy things or check quality.",
    32: "Drones in agriculture fly over farms to check if crops are healthy — saving time and water.",
    33: "Exoskeletons are wearable robots that help workers lift heavy loads — used in warehouses and hospitals.",
    34: "Autonomous vehicles — like self-driving cars — use cameras, radar, and AI to drive without a human steering.",
    35: "Delivery drones carry medicine to remote villages — saving lives when roads are bad or missing.",
    36: "3D-printed prosthetic limbs are cheaper and faster to make — giving children in poor areas new legs or arms.",
    37: "Collaborative robots (cobots) learn from humans — you show them how to do a task once, and they repeat it perfectly.",
    38: "Sensors in shoes can track how a child walks — helping doctors spot health problems early.",
    39: "Smart farming uses soil sensors to know exactly when to water crops — saving water and increasing food supply.",
    40: "Robots in hospitals can deliver medicine, clean rooms, or even guide patients — reducing stress on nurses.",
    41: "IoT means everyday objects — like lamps, clocks, or doors — can connect to the internet and be controlled remotely.",
    42: "A smart thermostat learns your habits and saves energy — turning heat down when you leave home.",
    43: "Smart meters track your electricity use and send data to the power company — helping avoid blackouts.",
    44: "Wearable devices like watches can measure your heart rate, sleep, and steps — helping you stay healthy.",
    45: "In schools, smart boards let teachers share videos, quizzes, and drawings instantly — even without internet later.",
    46: "Smart locks open with your phone or fingerprint — no keys needed — making homes safer and easier to enter.",
    47: "Connected trash bins alert collectors when they are full — making city cleaning faster and cleaner.",
    48: "Livestock wear smart collars that track their health — farmers know if a cow is sick before it shows symptoms.",
    49: "Smart irrigation systems turn water on only when soil is dry — saving up to 50% of water in farms.",
    50: "Every device connected to the internet becomes part of the IoT — and every device needs to be protected."
}

# ------------------- SMS MODE RESPONSES -------------------
sms_responses = {
    "hello": "Hello! I'm ShineGPT. Type 'lesson 1' to start learning about the 4th Industrial Revolution. Or type 'sms help' for more.",
    "hi": "Hi there! Type 'lesson 1' to begin your first lesson.",
    "help": "Type: 'lesson 1', 'lesson 2', ..., 'lesson 50' to learn. Or 'sms help' to see this again.",
    "sms help": "📱 SMS MODE: No internet needed! Just type:\n- 'lesson 1'\n- 'lesson 2'\n- ... up to 'lesson 50'\n- 'hello'\n- 'help'",
    "thank you": "You're welcome! Keep learning. Type 'lesson 1' to continue.",
    "thanks": "You're welcome! Learning is power. Try 'lesson 1'.",
    "bye": "Goodbye! Come back soon. Remember: Knowledge is your superpower.",
    "points": "You have 0 points. Earn 10 per lesson. Type 'lesson 1' to start!",
}

# AUTO-GENERATE LESSON RESPONSES FOR ALL 50 LESSONS
for i in range(1, 51):
    lesson_text = lessons.get(i, "Lesson not found.")
    sms_responses[f"lesson {i}"] = lesson_text + f"\n\n✨ You earned 10 points! Type 'lesson {i+1}' to continue."

# ------------------- POINTS FUNCTIONS -------------------
def get_user_points(user):
    if user not in st.session_state.user_points:
        st.session_state.user_points[user] = 0
    return st.session_state.user_points[user]

def add_points(user, points):
    if user not in st.session_state.user_points:
        st.session_state.user_points[user] = 0
    st.session_state.user_points[user] += points

# ------------------- ONLINE MODEL (TINYLLAMA) -------------------
MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

@st.cache_resource
def load_online_model():
    try:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            torch_dtype="auto",
            device_map="auto",
            trust_remote_code=True,
            low_cpu_mem_usage=True,
        )
        return tokenizer, model
    except Exception as e:
        st.warning("⚠️ Online model failed to load: " + str(e) + ". Switching to SMS mode.")
        return None, None

tokenizer, model = load_online_model()

def generate_response_online(user_input):
    if not tokenizer or not model:
        return "❌ Offline mode: No internet. Try typing 'sms help'."

    prompt = f"<|system|>\nYou are a helpful AI assistant.<|end|>\n<|user|>\n{user_input}<|end|>\n<|assistant|>\n"

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=256,
            temperature=0.7,
            top_p=0.9,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id,
            eos_token_id=tokenizer.eos_token_id,
            max_length=512,
        )

    response = tokenizer.decode(outputs[0][len(inputs[0]):], skip_special_tokens=True).strip()
    response = response.replace("<|end|>", "").strip()
    return response

# ------------------- MAIN APP — BRAND-COMPLIANT THEME -------------------
st.set_page_config(page_title="ShineGPT", page_icon="🌍", layout="centered")

# Custom CSS — Your Brand Colors: GOLD, RED, BLACK, WHITE
st.markdown(
    """
    <style>
    body {
        background-color: #000000;
        color: #ffffff;
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background-color: #D32F2F !important; /* Deep Red */
        color: white !important;
        font-weight: 900 !important;
        border-radius: 12px !important;
        font-size: 1.3rem !important;
        padding: 18px 40px !important;
        border: none !important;
        width: 100% !important;
        box-shadow: 0 4px 8px rgba(211, 47, 47, 0.3);
    }
    .stButton>button:hover {
        background-color: #B71C1C !important; /* Darker Red on hover */
    }
    h1, h2, h3, h4, p {
        color: #ffffff !important;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    h1 {
        font-size: 4rem;
        font-weight: 900;
        margin-bottom: 5px;
        color: #D4AF37 !important; /* Yellowish Gold — Pantone 124 C */
        text-shadow: 0 2px 4px rgba(212, 175, 55, 0.3);
    }
    h2 {
        font-size: 2rem;
        font-weight: 700;
        margin-top: -10px;
        margin-bottom: 5px;
        color: #D4AF37 !important; /* Gold */
    }
    h4 {
        font-size: 1.3rem;
        font-weight: 500;
        margin-top: 5px;
        color: #e0e0e0 !important;
    }
    .stRadio > label {
        color: #ffffff !important;
        font-weight: 600;
    }
    .stRadio > div > div > label {
        background-color: #111111 !important;
        border-radius: 10px !important;
        padding: 10px 20px !important;
        margin: 5px 0 !important;
        border: 1px solid #D4AF37 !important;
    }
    .stRadio > div > div > label:hover {
        background-color: #222222 !important;
    }
    .sidebar .sidebar-content {
        background-color: #000000 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------- HOMEPAGE LAYOUT -------------------
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Display logo — use_container_width instead of use_column_width
    try:
        st.image("logo.png", use_container_width=True)
    except:
        # Fallback: Bold gold text if logo fails
        st.markdown("<h1>SHINEGPT</h1>", unsafe_allow_html=True)

    st.markdown("<h2>Learn. Earn Knowledge. Empower Yourself.</h2>", unsafe_allow_html=True)
    st.markdown("<h4>Powered by KS1 Empire Foundation</h4>", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Main call-to-action button — RED
    if st.button("🚀 Start Learning", type="primary", use_container_width=True):
        st.session_state.page = "sms_mode"
        st.rerun()

# ------------------- SIDEBAR NAVIGATION -------------------
with st.sidebar:
    st.markdown("## 📚 Navigation")
    page = st.radio("Go to", ["Home", "SMS Mode (Offline)", "Chat with ShineGPT", "About"], key="nav")

# ------------------- PAGE LOGIC — FIXED CASE SENSITIVITY -------------------
if 'page' not in st.session_state:
    st.session_state.page = "home"

# ✅ FIXED: Use lowercase for all state keys — consistent with radio button labels
if page == "Home" or st.session_state.page == "home":
    pass  # Already shown above

elif page == "SMS Mode (Offline)" or st.session_state.page == "sms_mode":
    st.session_state.page = "sms_mode"
    st.header("📱 SMS Mode — No Internet Needed!")
    st.markdown("""
    **This mode works even on a basic phone!**  
    No data? No problem. Just type keywords like:  
    - `lesson 1`  
    - `hello`  
    - `what is ai`  
    - `help`  
    - `points`
    
    💡 Tip: Save this page as a bookmark. You can use it anywhere — even without Wi-Fi.
    """)
    
    user_input = st.text_input("Type your message (SMS-style):", key="sms_input")

    if st.button("Send (SMS)") and user_input:
        user_input_lower = user_input.strip().lower()
        response = sms_responses.get(user_input_lower, "I don't understand. Try typing 'sms help'.")

        if user_input_lower.startswith("lesson ") and user_input_lower in sms_responses:
            add_points("sms_user", 10)

        st.success(response)

elif page == "Chat with ShineGPT" or st.session_state.page == "chat_with_shinegpt":
    st.session_state.page = "chat_with_shinegpt"
    st.header("💬 Chat with ShineGPT (Online Mode)")
    st.info("💡 This mode uses TinyLlama — fast, open, and free. Requires internet.")

    user_input = st.text_input("Ask me anything about AI, Blockchain, Web3, Crypto, or Big Data:", key="chat_input")

    if st.button("Send") and user_input:
        with st.spinner("Thinking..."):
            response = generate_response_online(user_input)
        st.success(response)
        add_points("online_user", 5)

elif page == "About" or st.session_state.page == "about":
    st.session_state.page = "about"
    st.header("ℹ️ About ShineGPT")
    st.write("""
    ShineGPT is an educational AI app created by **KS1 Empire Foundation**.  
    It teaches young people in Africa and beyond about **AI, Blockchain, Crypto, Web3, IoT, and Big Data**.  

    🌍 **Dual-Mode Learning**:  
    - 📱 **SMS Mode**: Works with zero internet — perfect for villages.  
    - 💻 **Online Mode**: Uses TinyLlama — open, free, and no login required.  

    Our mission:  
    **Learn. Earn Knowledge. Empower Yourself.**
    """)

# ------------------- DISPLAY POINTS (ALWAYS) -------------------
st.sidebar.markdown("---")
st.sidebar.subheader("🏆 Your Points")
st.sidebar.write(f"**{get_user_points('online_user')}** points (Online)")
st.sidebar.write(f"**{get_user_points('sms_user')}** points (SMS)")
st.sidebar.info("Earn 10 points per lesson. No data cost in SMS mode!")
