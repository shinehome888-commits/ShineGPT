import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# ------------------- INITIALIZE SESSION STATE -------------------
if 'user_points' not in st.session_state:
    st.session_state.user_points = 0

# ------------------- 50 OFFLINE LESSONS -------------------
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
    "hello": "Hello! I'm ShineGPT. Type 'lesson 1' to start learning about the 4th Industrial Revolution. Or type 'help' for more.",
    "hi": "Hi there! Type 'lesson 1' to begin your first lesson.",
    "help": "Type: 'lesson 1', 'lesson 2', ..., 'lesson 50' to learn. Or 'points' to see your score.",
    "thank you": "You're welcome! Keep learning. Type 'lesson 1' to continue.",
    "thanks": "You're welcome! Learning is power. Try 'lesson 1'.",
    "bye": "Goodbye! Come back soon. Remember: Knowledge is your superpower.",
    "points": f"You have {st.session_state.user_points} points. Earn 10 per lesson. Type 'lesson 1' to start!",
}

# AUTO-GENERATE LESSON RESPONSES FOR ALL 50 LESSONS
for i in range(1, 51):
    lesson_text = lessons.get(i, "Lesson not found.")
    sms_responses[f"lesson {i}"] = lesson_text + f"\n\n✨ You earned 10 points! Type 'lesson {i+1}' to continue."

# ------------------- POINTS FUNCTION -------------------
def add_points(points):
    st.session_state.user_points += points

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
        st.warning("⚠️ Online model failed to load. Switching to SMS mode.")
        return None, None

tokenizer, model = load_online_model()

def generate_response_online(user_input):
    if not tokenizer or not model:
        return "❌ Offline mode: No internet. Try typing 'lesson 1'."

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

# ------------------- MAIN APP — FINAL HUMAN-CENTERED LAYOUT -------------------
st.set_page_config(page_title="ShineGPT", page_icon="🌍", layout="centered")

# Custom CSS — FOCUS ON INPUT + RESPONSE VISIBILITY
st.markdown(
    """
    <style>
    body {
        background-color: #000000;
        color: #ffffff;
        font-family: 'Arial', sans-serif;
    }
    .main > div {
        padding-top: 1rem;
    }
    h1, h2, h3, h4, p {
        color: #ffffff !important;
        text-align: center;
        font-family: 'Arial', sans-serif;
        margin: 0.5rem auto;
        max-width: 800px;
        padding: 0 20px;
    }
    h1 {
        font-size: 3.5rem;
        font-weight: 900;
        margin-bottom: 0.3rem;
        color: #D4AF37 !important; /* Yellowish Gold */
        text-shadow: 0 2px 4px rgba(212, 175, 55, 0.3);
    }
    h2 {
        font-size: 1.8rem;
        font-weight: 700;
        margin-top: -0.3rem;
        margin-bottom: 1rem;
        color: #ffffff !important; /* White */
    }
    h4 {
        font-size: 1.3rem;
        font-weight: 500;
        margin-top: 0.5rem;
        margin-bottom: 2rem;
        color: #D32F2F !important; /* RED — Powered by KS1 */
    }
    .stRadio > label {
        color: #ffffff !important;
        font-weight: 600;
        font-size: 1.3rem;
        margin-bottom: 1rem;
    }
    .stRadio > div > div > label {
        background-color: #111111 !important;
        border-radius: 12px !important;
        padding: 15px 25px !important;
        margin: 10px auto !important;
        border: 2px solid #D4AF37 !important;
        transition: all 0.3s ease;
        width: 90%;
        max-width: 400px;
    }
    .stRadio > div > div > label:hover {
        background-color: #222222 !important;
        transform: scale(1.02);
    }
    .stButton>button {
        background-color: #D32F2F !important;
        color: white !important;
        font-weight: 700 !important;
        border-radius: 12px !important;
        font-size: 1.2rem !important;
        padding: 15px 30px !important;
        border: none !important;
        width: 90% !important;
        max-width: 400px;
        margin: 1.5rem auto !important;
        box-shadow: 0 4px 8px rgba(211, 47, 47, 0.3);
    }
    .stButton>button:hover {
        background-color: #B71C1C !important;
    }

    /* ✅ INPUT BOX — FULL WIDTH, LARGE, CLEAR */
    .stTextInput > div > div > input {
        font-size: 1.4rem !important;
        text-align: left;
        padding: 18px !important;
        border-radius: 14px !important;
        border: 2px solid #D4AF37 !important;
        background-color: #111111 !important;
        color: #ffffff !important;
        width: 95% !important;
        max-width: 700px !important;
        margin: 1.5rem auto !important;
        display: block !important;
        box-shadow: 0 0 10px rgba(212, 175, 55, 0.2);
    }
    .stTextInput > label {
        font-size: 1.4rem !important;
        color: #ffffff !important;
        margin-bottom: 0.5rem !important;
        font-weight: 600;
    }

    /* ✅ RESPONSE BOX — CLEAR, PADDDED, SEPARATED */
    .stSuccess, .stWarning, .stError {
        font-size: 1.4rem !important;
        padding: 20px !important;
        margin: 1.5rem auto !important;
        max-width: 90% !important;
        border-radius: 14px !important;
        background-color: #1a1a1a !important;
        border: 1px solid #D4AF37 !important;
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.1);
        text-align: left !important;
        line-height: 1.7 !important;
    }
    .stSuccess::before, .stWarning::before, .stError::before {
        font-size: 1.6rem !important;
    }

    .sidebar .sidebar-content {
        background-color: #000000 !important;
        padding: 2rem 1rem;
    }
    .sidebar .sidebar-content h2 {
        color: #D4AF37 !important;
        font-size: 1.8rem;
        margin-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------- SIDEBAR NAVIGATION — NO HOME, ONLY 3 OPTIONS -------------------
with st.sidebar:
    st.markdown("## 📚 ShineGPT Menu")
    page = st.radio("", ["SMS Mode (Offline)", "Chat with ShineGPT", "About"], key="nav", label_visibility="collapsed")

# ------------------- PAGE LOGIC — NO HOMEPAGE. STARTS ON SMS MODE -------------------
if page == "SMS Mode (Offline)":
    st.header("📱 SMS Mode — No Internet Needed!")
    st.markdown("""
    **This mode works even on a basic phone!**  
    No data? No problem. Just type:  
    - `lesson 1`  
    - `hello`  
    - `help`  
    - `points`
    
    💡 Tip: Save this page as a bookmark. You can use it anywhere — even without Wi-Fi.
    """)
    
    user_input = st.text_input("Type your message (SMS-style):", key="sms_input")

    if st.button("Send (SMS)") and user_input:
        user_input_lower = user_input.strip().lower()
        response = sms_responses.get(user_input_lower, "I don't understand. Type 'help' for options.")

        if user_input_lower.startswith("lesson ") and user_input_lower in sms_responses:
            add_points(10)

        st.success(response)

elif page == "Chat with ShineGPT":
    st.header("💬 Chat with ShineGPT (Online Mode)")
    st.info("💡 This mode uses TinyLlama — fast, open, and free. Requires internet.")

    user_input = st.text_input("Ask me anything about AI, Blockchain, Web3, Crypto, or Big Data:", key="chat_input")

    if st.button("Send") and user_input:
        with st.spinner("Thinking..."):
            response = generate_response_online(user_input)
        st.success(response)
        add_points(5)

elif page == "About":
    st.header("ℹ️ About ShineGPT")
    st.markdown("""
    ShineGPT is an educational AI app created by **KS1 Empire Foundation**.  
    It teaches young people in Africa and beyond about **AI, Blockchain, Crypto, Web3, IoT, and Big Data**.
    
    🌍 **Dual-Mode Learning**:  
    - 📱 **SMS Mode**: Works with zero internet — perfect for villages.  
    - 💻 **Online Mode**: Uses TinyLlama — open, free, and no login required.
    
    Our mission:  
    **Learn. Earn Knowledge. Empower Yourself.**
    
    This app is designed for children in villages where:
    - Internet is slow or expensive  
    - Books are scarce  
    - Teachers are few  
    - But curiosity is endless
    
    No login. No account. No cost.  
    Just knowledge — free, forever.
    """)
    
    st.markdown("<h4>Powered by KS1 Empire Foundation</h4>", unsafe_allow_html=True)

# ------------------- DISPLAY POINTS (ALWAYS) -------------------
st.sidebar.markdown("---")
st.sidebar.subheader("🏆 Your Points")
st.sidebar.write(f"**{st.session_state.user_points}** points")
st.sidebar.info("Earn 10 points per lesson. No data cost in SMS mode!")
