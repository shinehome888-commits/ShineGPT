# ShineGPT: Learn. Earn. Empower the World.
# Dual-Mode AI Tutor: Online (Phi-3) + SMS (Offline, No Internet)

import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# ------------------- CONFIG -------------------
MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"

# ------------------- 100-LESSON CURRICULUM ON THE 4TH INDUSTRIAL REVOLUTION -------------------
lessons = {
    1: "The 4th Industrial Revolution is when technology like AI, robots, and the internet merge with our physical world to change how we live and work.",
    2: "The 1st Industrial Revolution used steam engines to make machines. The 2nd used electricity. The 3rd used computers. The 4th uses smart systems.",
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
    50: "Every device connected to the internet becomes part of the IoT — and every device needs to be protected.",
    51: "Big Data is not just big — it’s valuable. When collected wisely, it helps predict diseases, disasters, or economic trends.",
    52: "Data collection in the 4IR happens everywhere — your phone, your card, your search, your ride-hailing app.",
    53: "Data privacy means protecting your personal info — like where you go, who you call, or what you buy — from being sold without permission.",
    54: "Anonymized data removes names and IDs so companies can study patterns without knowing who you are — keeping you safe.",
    55: "Data lakes are giant storage places for raw data — from videos, texts, sounds, and sensors — all kept for future analysis.",
    56: "Data pipelines are like rivers that move data from one place to another — from phones to servers to AI models.",
    57: "Real-time data means information is used immediately — like traffic apps showing accidents as they happen.",
    58: "Predictive maintenance uses data from machines to know when they will break — fixing them before they stop working.",
    59: "In healthcare, Big Data helps doctors find rare diseases by comparing thousands of patient records at once.",
    60: "Big Data helps governments plan better schools, clinics, and roads by seeing where people need them most.",
    61: "Cloud computing lets you store photos, documents, and apps on the internet — so you can access them from any device.",
    62: "You don’t need a powerful phone anymore — because the ‘brain’ of your app lives in the cloud.",
    63: "Public clouds (like Google Cloud) are shared by many users. Private clouds are owned by one company or school.",
    64: "Edge computing means processing data on your device — like your phone — instead of sending it far away to a server.",
    65: "Edge computing saves time and data — perfect for villages with slow internet — because answers come from your own phone.",
    66: "Fog computing is between edge and cloud — small servers near villages process data before sending it to big centers.",
    67: "Serverless computing means you use apps without managing computers — the cloud runs everything automatically.",
    68: "APIs are like messengers between apps — they let your phone talk to weather services, maps, or payment systems.",
    69: "Open data means governments and companies share information freely — like public bus schedules or air quality levels.",
    70: "Digital literacy means knowing how to use, understand, and protect yourself in the digital world — a basic skill now.",
    71: "Blockchain stores information in blocks linked together — each block has a unique code that links to the next one.",
    72: "No one person controls blockchain — it’s maintained by many computers around the world — making it very secure.",
    73: "Transactions on blockchain are permanent — once recorded, they cannot be changed or deleted — like a digital tattoo.",
    74: "Smart contracts are automatic agreements on blockchain — if condition A happens, then action B happens — no lawyer needed.",
    75: "Cryptocurrency is digital money that runs on blockchain — like Bitcoin or Ethereum — no bank required.",
    76: "Mining cryptocurrency uses powerful computers to solve math puzzles — and earns new coins as reward.",
    77: "Wallets store your cryptocurrency — not like a purse, but like a digital key that proves you own your money.",
    78: "Decentralized Finance (DeFi) lets you lend, borrow, or save money without banks — using only your phone and blockchain.",
    79: "NFTs (Non-Fungible Tokens) are unique digital items — like art, music, or collectibles — that you truly own on blockchain.",
    80: "Web3 is the next version of the internet — where users own their data, identity, and content — not big companies.",
    81: "In Web3, you control your profile — you choose who sees your posts, not Facebook or Twitter.",
    82: "DAOs (Decentralized Autonomous Organizations) are groups run by rules on blockchain — members vote using tokens, not leaders.",
    83: "Tokenization means turning real things — like land, books, or solar panels — into digital tokens on blockchain.",
    84: "Zero-knowledge proofs let you prove something is true — without revealing what it is — like proving you’re 18 without showing your ID.",
    85: "Interoperability means different systems can talk to each other — like your phone connecting to a smart meter and a solar panel.",
    86: "The 4IR creates new jobs — like AI trainer, drone operator, cybersecurity analyst, and data ethicist.",
    87: "Old jobs are changing — farmers now use drones, tailors use 3D printers, teachers use VR classrooms.",
    88: "Soft skills like creativity, empathy, and teamwork are more important than ever — because machines can’t replace them.",
    89: "Lifelong learning means you never stop studying — because technology changes fast, and you must change with it.",
    90: "Coding is not just for engineers — anyone can learn to give instructions to computers — even to solve local problems.",
    91: "Digital entrepreneurship means starting a business online — selling crafts, teaching skills, or creating apps from your phone.",
    92: "Remote work is possible anywhere — with internet — so you can work for a company in Europe while living in a village.",
    93: "The 4IR can widen inequality — if only rich people get access to tech. That’s why shineGPT exists.",
    94: "Digital inclusion means making sure everyone — women, disabled people, rural communities — can use and benefit from technology.",
    95: "Ethical AI means building technology that is fair, transparent, and respects human rights — not just profitable.",
    96: "You are not just a user of the 4IR — you are its builder. Learn now, so you can shape it later.",
    97: "Start small: Learn one thing today. Teach one person tomorrow. Build one solution next week.",
    98: "Your voice matters. If you see a problem — use tech to fix it. Maybe your idea will become the next shineGPT.",
    99: "The future isn’t something that happens to you — it’s something you create. With curiosity, courage, and kindness.",
    100: "You are the generation that will decide: Will technology serve humanity — or will humanity serve technology? Choose wisely."
}

# ------------------- SMS MODE RESPONSES (NO INTERNET NEEDED) -------------------
sms_responses = {
    "hello": "Hello! I'm ShineGPT. Type 'lesson 1' to start learning about the 4th Industrial Revolution. Or type 'sms help' for more.",
    "hi": "Hi there! Type 'lesson 1' to begin your first lesson.",
    "help": "Type: 'lesson 1', 'lesson 2', ..., 'lesson 100' to learn. Or 'sms help' to see this again.",
    "sms help": "📱 SMS MODE: No internet needed! Just type:\n- 'lesson 1'\n- 'lesson 2'\n- ... up to 'lesson 100'\n- 'hello'\n- 'help'",
    "thank you": "You're welcome! Keep learning. Type 'lesson 1' to continue.",
    "thanks": "You're welcome! Learning is power. Try 'lesson 1'.",
    "bye": "Goodbye! Come back soon. Remember: Knowledge is your superpower.",
    "what is ai": "AI is when machines learn to think like humans — like me! It helps us solve big problems.",
    "what is blockchain": "Blockchain is a digital notebook that everyone can see, but no one can cheat. It keeps records safe.",
    "what is crypto": "Cryptocurrency is digital money. Like Bitcoin. No bank needed — just your phone and trust.",
    "what is web3": "Web3 is the internet you own. Not Facebook or Google. YOU control your data.",
    "what is bitcoin": "Bitcoin is the first digital money. Created in 2009. No government controls it.",
    "what is big data": "Big Data means collecting lots of information — like how many kids go to school — to help make better decisions.",
    "what is iot": "IoT = Internet of Things. Your fridge, watch, or light bulb connected to the internet to help you.",
    "what is metaverse": "The Metaverse is a 3D internet world. You can walk around, meet friends, and work — all in a game-like space.",
    "what is future of work": "Future jobs will need AI, blockchain, and coding skills. Learn now — so you can earn later.",
    "points": "You have 0 points. Earn 10 per lesson. Type 'lesson 1' to start!",
}

# AUTO-GENERATE LESSON RESPONSES FOR ALL 100 LESSONS
for i in range(1, 101):
    lesson_text = lessons.get(i, "Lesson not found.")
    sms_responses[f"lesson {i}"] = lesson_text + f"\n\n✨ You earned 10 points! Type 'lesson {i+1}' to continue."

# ------------------- AUDIO FEATURES -------------------
import soundfile as sf
from io import BytesIO
from coqui_tts.api import TTS
import torch

# Initialize TTS model (small, fast, offline)
tts_model = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

def text_to_speech(text):
    """Convert text to audio file in memory"""
    try:
        wav = tts_model.tts(text)
        buffer = BytesIO()
        sf.write(buffer, wav, 22050, format='WAV')
        buffer.seek(0)
        return buffer.read()
    except Exception as e:
        st.warning(f"⚠️ Could not generate voice: {e}")
        return None

def play_audio(audio_bytes):
    """Play audio in Streamlit"""
    if audio_bytes:
        st.audio(audio_bytes, format="audio/wav")

# ------------------- LOAD ONLINE MODEL (IF NEEDED) -------------------
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

# ------------------- CHAT BOT FUNCTION -------------------
def generate_response_online(user_input):
    if not tokenizer or not model:
        return "❌ Offline mode: No internet. Try typing 'sms help'."

    prompt = f"<|user|>\n{user_input}<|end|><|assistant|>"
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=256,
            temperature=0.7,
            top_p=0.9,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id,
            eos_token_id=tokenizer.eos_token_id
        )

    response = tokenizer.decode(outputs[0][len(inputs[0]):], skip_special_tokens=True).strip()
    return response

# ------------------- TRACK USER POINTS -------------------
if 'user_points' not in st.session_state:
    st.session_state.user_points = {}

def get_user_points(user):
    if user not in st.session_state.user_points:
        st.session_state.user_points[user] = 0
    return st.session_state.user_points[user]

def add_points(user, points):
    st.session_state.user_points[user] += points

# ------------------- MAIN APP -------------------
st.set_page_config(page_title="ShineGPT", page_icon="🌍", layout="wide")

st.title("🌟 ShineGPT – Learn. Earn Knowledge. Empower Yourself.")
st.write("Powered by KS1 Empire Foundation")
st.markdown("---")

page = st.sidebar.radio("📚 Navigate", ["Lessons", "Chat with ShineGPT", "About", "SMS Mode (Offline)"])

if page == "Lessons":
    st.header("📘 ShineGPT Lessons")
    for i, lesson in lessons.items():
        with st.expander(f"Lesson {i}"):
            st.write(lesson)

elif page == "Chat with ShineGPT":
    st.header("💬 Chat with ShineGPT (Online Mode)")
    st.info("💡 Say your question out loud — then type it here! Your phone can convert speech to text. Then listen to the answer.")

    user_input = st.text_input("Type your question here:", key="chat_input")

    if st.button("Send") and user_input:
        with st.spinner("Thinking..."):
            response = generate_response_online(user_input)
        st.success(response)

        # Generate voice reply
        audio_data = text_to_speech(response)
        if audio_data:
            st.markdown("🔊 **Listen to the answer:**")
            play_audio(audio_data)

        add_points("online_user", 5)

elif page == "SMS Mode (Offline)":
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

elif page == "About":
    st.header("ℹ️ About ShineGPT")
    st.write("""
    ShineGPT is an educational AI app created by **KS1 Empire Foundation**.  
    It teaches young people in Africa and beyond about **AI, Blockchain, Crypto, Web3, IoT, and Big Data**.  

    🌍 **Special Feature**:  
    We built an **SMS Mode** so kids in villages with **no internet** can still learn for free —  
    using only text messages on basic phones.

    Our mission:  
    **Learn. Earn Knowledge. Empower Yourself.**
    """)

st.sidebar.markdown("---")
st.sidebar.subheader("🏆 Your Points")
st.sidebar.write(f"**{get_user_points('online_user')}** points (Online)")
st.sidebar.write(f"**{get_user_points('sms_user')}** points (SMS)")
st.sidebar.info("Earn 10 points per lesson. No data cost in SMS mode!")
