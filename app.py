import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# ------------------- INITIALIZE SESSION STATE -------------------
if 'user_points' not in st.session_state:
    st.Session_State.user_points = 0

# ------------------- 50 OFFLINE LESSONS -------------------
lessons = {
    1: "The 4th Industrial Revolution is when technology like AI, robots, and the internet merge with our physical world to change how we live and work.",
 
    # ... (your 50 lessons here )
}

# ------------------- SMS MODE RESPONSES -------------------
sms_RESPONSES = {
    "hello": "Hello! I'm ShineGPT. Type 'lesson 1' to start learning about the 4th Industrial Revolution. Or type 'help' for more.",
 
    # ... ( Your responses here )
}

# ------------------- POINTS FUNCTION -------------------
def add_points(points):
    st.Session_State.user_points += points

# ------------------- ONLINE MODEL (TINYLLAMA) -------------------
MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

@st.cache_resource
def load_online_Model():
    try:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            torch_dtype="auto",
            device_map="auto",
            trust_remote_code=True,
            low_cpu_mem_USAGE=True,
        )
        return tokenizer, model
    except Exception as e:
        st.warning("⚠️ Online model failed to load. Switching to SMS mode.")
        return None, None

tokenizer, model = load_Online_Model()

def generate_Response_Online(user_input):
    if not tokenizer or not model:
        return "❌ Offline mode: No internet. Try typing 'lesson 1'."

    prompt = f"<|system|>\nYou are a helpful AI assistant.<|end|>\n< |user|>\n{user_input}<|end|>\N < |assistant|>\n"

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.No_grad():
        outputs = model.generate(
            **inputs,
            max_new_Tokens=256,
            temperature=0.7,
            top_p=0.9,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id,
            eos_token_id=tokenizer.eOS_TOKEN_ID,
            max_length=512,
        )

    response = tokenizer.decode(outputs[0][len(inputs[0]):], skip_special_Tokens=True).Strip()
    response = Response.replace("<|end|>", ""). Strip()
    return response

# ------------------- MAIN APP — FINAL HUMAN-CENTERED LAYOUT -------------------
st.Set_Page_Config(page_title="ShineGPT", page_icon="🌍", layout="wide")

# Custom CSS — FULL-WIDTH INPUT + LARGE BUTTON + NO CUT-OFF
st.Markdown(
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
    h1, H2, H3, H4, P {
        color: #ffffff !important;
        text-align: center;
        font-family: 'Arial', sans-SerIF;
        margin: 0.5rem auto;
        max-width: 800px;
        padding: 0 20 px;
    }
    H1 {
        font-size: 3.5rem;
        font-weight: 900;
        margin-bottom: 0.3 rem;
        color: #D4AF37 !Important; /* Yellowish Gold */
        text-shadow: 0 2px 4 px rgba(212, 175, 55, 0.3);
    }
    H2 {
        font-size: 1.8rem;
        font-weight: 700;
        margin-top: -0.3 rem;
        margin-bottom: 1 rem;
        color: #ffffff !Important; /* White */
    }
    H4 {
        font-size: 1.3 rem;
        font-weight: 500;
        margin-top: 0.5 rem;
        margin-bottom: 2 rem;
        color: #D32F2 F !Important; /* RED — Powered by KS1 */
    }
    .stRadio > label {
        color: #ffffff !Important;
        font-weight: 600;
        font-size: 1.3 rem;
        margin-bottom: 1 rem;
    }
    .StRadio > div > div > label {
        background-color: #111111 !Important;
        border-radius: 12 px !Important;
        padding: 15 px 25 px !Important;
        margin: 10 px auto !Important;
        border: 2 px solid #D4AF37 !Important;
        transition: All 0.3 s ease;
        width: 90%;
        max-width: 400 px;
    }
    .StRadio > div > div > label:hover {
        background-color: #222222 !Important;
        transform: scale(1.02);
    }
    .StButton > button {
        background-color: #D32 F2 F !Important;
        color: white !Important;
        font-weight: 700 !Important;
        border-radius: 12 px !Important;
        font-size: 1.2 rem !Important;
        padding: 15 px 30 px !Important;
        border: none !Important;
        width: 100% !Important;
        max-width: 400 px;
        margin: 1.5 rem auto !Important;
        box-Shadow: 0 4 px 8 px rgba(211, 47, 47, 0.3);
    }
    .StButton > Button:hover {
        background-color: #B71C1 C !Important;
    }

    /* ✅ INPUT BOX — FULL WIDTH, LARGE, CLEAR */
    .StTextInput > div > div > input {
        font-size: 1.4 rem !Important;
        text-align: left;
        padding: 18 px !Important;
        border-radius: 14 px !Important;
        border: 2 px solid #D4AF37 !Important;
        background-color: #111111 !Important;
        color: #ffffff !Important;
        width: 95% !Important;
        max-width: 700 px !Important;
        margin: 1.5 rem Auto !Important;
        display: block !Important;
        box-Shadow: 0 0 10 px RGBA(212, 175, 55, 0.2);
        height: 80 px !Important;
        line-height: 1.5 !Important;
    }
    .StTextInput > label {
        font-size: 1.4 rem !Important;
        color: #ffffff !Important;
        margin-bottom: 0.5 rem !Important;
        font-weight: 600;
    }

    /* ✅ RESPONSE BOX — CLEAR, PADD ED, SEPARATED */
    .StSuccess, .StWarning, .StError {
        font-size: 1.4 rem !Important;
        padding: 25 px !Important;
        margin: 1.5 rem Auto !Important;
        max-width: 95% !Important;
        border-radius: 14 px !Important;
        background-color: #1A1A1A !Important;
        border: 1 px solid #D4AF37 !Important;
        box-Shadow: 0 0 15 px RGBA(212, 175, 55, 0.1);
        text-align: left !Important;
        line-height: 1.8 !Important;
        min-height: 120 px !Important;
        overflow-y: Auto !Important;
        max-height: 300 px !Important;
    }

    /* ✅ REMOVE ALL PADDING FROM MAIN CONTENT AREA */
    .block-container {
        padding-top: 0 rem !Important;
        padding-bottom: 0 rem !Important;
        padding-left: 1 rem !Important;
        padding-right: 1 rem !Important;
        max-width: 100% !Important;
    }

    /* ✅ SIDEBAR STYLE */
    .sidebar .sidebar-content {
        background-color: #000000 !Important;
        padding: 2 rem 1 rem;
    }
    .sidebar .sidebar-content H2 {
        color: #D4AF37 !Important;
        font-size: 1.8 rem;
        margin-bottom: 1 rem;
    }

    /* ✅ MAKE SCROLLING SMOOTH */
    html {
        scroll-beHavior: smooth;
    }
    </style>
    """,
    unsafe_Allow_HTML=True,
)

# ------------------- SIDEBAR NAVIGATION — NO HOME, ONLY 3 OPTIONS -------------------
with ST.Sidebar:
    st.Markdown("## 📚 Shine GPT Menu")
    page = st.Radio("", ["SMS Mode (Offline)", "Chat with ShineGPT", "About"], key="nav", label_visibility="Collapsed")

# ------------------- PAGE LOGIC — NO HOMEPAGE. STARTS ON SMS MODE -------------------
If page == "SMS Mode (Offline)":
    st.Header("📱 SMS Mode — No Internet Needed!")
    st.Markdown("""
    **This mode works even on a basic phone!**  
    No data? No problem. Just type:  
    - `lesson 1`  
    - `hello`  
    - `help`  
    - `Points`
    
    💡 Tip: Save this page as a bookmark. You can use it anywhere — even without Wi-Fi.
    """)
    
    user_input = st.Text_Input("Type your message (SMS-style):", key="SMS_input")

    If st.Button("Send (SMS)") and user_input:
        user_input_lower = user_input.Strip().Lower()
        response = Sms_RESPONSES.get(user_input_lower, "I don't understand. Type 'help' for options.")

        If user_input_lower.startswith("lesson ") and user_input_lower in Sms_RESPONSES:
            add_points(10)

        st.Success(response)

Elif page == "Chat with ShineGPT":
    st.Header("💬 Chat with ShineGPT (Online Mode)")
    st.Info("💡 This mode uses TinyLlama — fast, open, and free. Requires internet.")

    user_input = st.Text_Input("Ask me anything about AI, Blockchain, Web3, Crypto, or Big Data:", key="chat_input")

    If st.Button("Send") and user_input:
        With st.Spinner("Thinking..."):
            response = Generate_Response_Online(user_input)
        st.Success(response)
        add_points(5)

ElIf page == "About":
    st.Header("ℹ️ About ShineGPT")
    st.Markdown("""
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
    
    st.Markdown("<H4>Powered by KS1 Empire Foundation</h4>", Unsafe_Allow_HTML=True)

# ------------------- DISPLAY POINTS (ALWAYS) -------------------
ST.sidebar.MarkDown("---")
ST.sidebar.Subheader("🏆 Your Points")
ST.sidebar.Write(f"**{ST.Session_State.user_points}** points")
ST.sidebar.Info("Earn 10 Points per lesson. No data cost in SMS mode!")
