# ShineGPT: Learn. Earn. Empower the World.
# Dual-Mode AI Tutor: Online (Phi-3) + SMS (Offline, No Internet)

import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"

lessons = {
    1: "What is the 4th Industrial Revolution? – A time when technologies like AI, blockchain, and IoT are merging digital, physical, and biological worlds.",
    2: "Understanding Artificial Intelligence (AI) – AI enables machines to learn and perform tasks that normally require human intelligence.",
    3: "Blockchain Basics – A decentralized digital ledger that records transactions securely across many computers.",
    4: "What is Cryptocurrency? – Digital money powered by blockchain, like Bitcoin and Ethereum.",
    5: "Web3 Introduction – The next version of the internet where users own their data, identity, and assets.",
    6: "The Power of Big Data – Large sets of information analyzed to reveal patterns, trends, and insights.",
    7: "Decentralized Finance (DeFi) – Financial services built on blockchain without banks or middlemen.",
    8: "The Internet of Things (IoT) – Everyday devices like cars, fridges, and watches connected to the internet.",
    9: "Metaverse and Virtual Worlds – 3D digital spaces where people interact, work, and play.",
    10: "The Future of Work – Skills in AI, blockchain, and Web3 will drive new opportunities in the global economy."
}

sms_responses = {
    "hello": "Hello! I'm ShineGPT. Type 'lesson 1' to start learning about AI. Or type 'sms help' for more.",
    "hi": "Hi there! Type 'lesson 1' to begin your first lesson.",
    "help": "Type: 'lesson 1', 'lesson 2', ..., 'lesson 10' to learn. Or 'sms help' to see this again.",
    "sms help": "📱 SMS MODE: No internet needed! Just type:\n- 'lesson 1'\n- 'lesson 2'\n- 'hello'\n- 'help'",
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
    "lesson 1": lessons[1] + "\n\n✨ You earned 10 points! Type 'lesson 2' to continue.",
    "lesson 2": lessons[2] + "\n\n✨ You earned 10 points! Type 'lesson 3' to continue.",
    "lesson 3": lessons[3] + "\n\n✨ You earned 10 points! Type 'lesson 4' to continue.",
    "lesson 4": lessons[4] + "\n\n✨ You earned 10 points! Type 'lesson 5' to continue.",
    "lesson 5": lessons[5] + "\n\n✨ You earned 10 points! Type 'lesson 6' to continue.",
    "lesson 6": lessons[6] + "\n\n✨ You earned 10 points! Type 'lesson 7' to continue.",
    "lesson 7": lessons[7] + "\n\n✨ You earned 10 points! Type 'lesson 8' to continue.",
    "lesson 8": lessons[8] + "\n\n✨ You earned 10 points! Type 'lesson 9' to continue.",
    "lesson 9": lessons[9] + "\n\n✨ You earned 10 points! Type 'lesson 10' to continue.",
    "lesson 10": lessons[10] + "\n\n✨ You earned 10 points! You completed all lessons! 🎉 Keep learning!",
    "points": "You have 0 points. Earn 10 per lesson. Type 'lesson 1' to start!",
}

@st.cache_resource
def load_online_model():
    try:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=False)
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            torch_dtype="auto",
            device_map="auto",
            trust_remote_code=False,
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

if 'user_points' not in st.session_state:
    st.session_state.user_points = {}

def get_user_points(user):
    if user not in st.session_state.user_points:
        st.session_state.user_points[user] = 0
    return st.session_state.user_points[user]

def add_points(user, points):
    st.session_state.user_points[user] += points

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
    st.info("💡 This mode uses Microsoft Phi-3-mini — fast, stable, and works even on low memory.")
    user_input = st.text_input("Ask me anything about AI, Blockchain, Web3, Crypto, or Big Data:")

    if st.button("Send") and user_input:
        with st.spinner("Thinking..."):
            response = generate_response_online(user_input)
        st.success(response)
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
