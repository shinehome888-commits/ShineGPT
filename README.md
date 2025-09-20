# 🌍 ShineGPT: Learn Without Internet — For Every Child in Africa

![Streamlit](https://img.shields.io/badge/Interface-Streamlit-blue)  
![Offline Mode](https://img.shields.io/badge/SMS--Mode-Offline-green)  
![AI for Good](https://img.shields.io/badge/Mission-Empower-Affordable)

> **No internet? No problem.**  
> ShineGPT teaches AI, Blockchain, Crypto, and the Future of Work — even on a basic phone with only SMS.

---

## 💡 What Is ShineGPT?

**ShineGPT** is an educational AI app created by **KS1 Empire Foundation** to bring digital literacy to children in villages across Africa — where data is expensive, slow, or unavailable.

Unlike most AI apps that need Wi-Fi, shineGPT has a special **SMS/Offline Mode** that works **without any internet connection**. Kids can learn core tech concepts using only text-based prompts — just like sending a message on a Nokia phone.

**Learn. Earn Knowledge. Empower Yourself.**

---

## 📱 Dual-Mode Learning: Online + Offline

| Mode | How It Works | Needs Internet? | Best For |
|------|--------------|------------------|----------|
| **📱 SMS Mode (Offline)** | Type keywords like `lesson 1`, `what is ai`, or `help` → get instant replies from pre-loaded lessons | ❌ **NO** | Villages, buses, schools without power or data |
| **💻 Online Mode** | Uses Qwen2.5-7B AI model to answer complex questions like a tutor | ✅ Yes | Schools with Wi-Fi, tablets, or smartphones |

> ✅ **Both modes work in one app.**  
> Switch between them using the sidebar menu.

---

## 🔧 How to Use ShineGPT

### In SMS/Offline Mode (No Internet!)
Just type these simple commands:

| Command | What Happens |
|--------|---------------|
| `hello` | “Hello! I'm ShineGPT. Type 'lesson 1' to start.” |
| `lesson 1` | Shows Lesson 1 + rewards 10 points |
| `what is ai` | “AI is when machines learn to think like humans…” |
| `what is blockchain` | Explains blockchain in simple terms |
| `help` or `sms help` | Lists all working commands |
| `points` | Shows your earned points |

✅ Works on **any phone** — even if you can’t load a webpage!

### In Online Mode (With Internet)
Ask anything like:
> “Explain Web3 like I’m 12.”  
> “How do I become a coder?”  
> “Is Bitcoin safe?”

The AI responds in real time — powered by Hugging Face’s Qwen2.5 model.

---
# ------------------- 100-LESSON CURRICULUM ON THE 4TH INDUSTRIAL REVOLUTION (OFFLINE SMS MODE) -------------------
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

---
## 🎯 Why This Matters

In rural Africa:
- 60% of students have **no reliable internet**
- Mobile phones are the only digital tool many own
- Data costs more than food in some places

**shineGPT turns every basic phone into a free classroom.**  
No subscriptions. No fees. Just knowledge.

We’re not just building an app — we’re building **equity in education**.

---

## 🛠️ Tech Stack

| Component | Tool |
|---------|------|
| Frontend | [Streamlit](https://streamlit.io/) |
| Offline AI Logic | Pre-loaded lessons + keyword matching |
| Online AI | Hugging Face `Qwen2.5-7B-Instruct` |
| Deployment | Hugging Face Spaces |
| License | MIT |

---

## 📦 Requirements (For Developers)

If you want to run shineGPT locally:

```txt
transformers==4.38.0
torch==2.3.0
accelerate==0.30.1
huggingface-hub==0.21.4
streamlit==1.36.0
