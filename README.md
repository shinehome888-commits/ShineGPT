# 🌍 ShineGPT: Learn Without Internet — For Every Child in Africa
name:%20Check%20shineGPT%20App%0A%0Aon%3A%0A%20%20push%3A%0A%20%20%20%20branches%3A%20%5B%20main%20%5D%0A%20%20pull_request%3A%0A%20%20%20%20branches%3A%20%5B%20main%20%5D%0A%0Ajobs%3A%0A%20%20check-code%3A%0A%20%20%20%20runs-on%3A%20ubuntu-latest%0A%0A%20%20%20%20steps%3A%0A%20%20%20%20%20%20-%20name%3A%20Checkout%20code%0A%20%20%20%20%20%20%20%20uses%3A%20actions/checkout@v4%0A%0A%20%20%20%20%20%20-%20name:%20Set%20up%20Python%0A%20%20%20%20%20%20%20%20uses:%20actions/setup-python@v5%0A%20%20%20%20%20%20%20%20with:%0A%20%20%20%20%20%20%20%20%20%20python-version:%20'3.10'%0A%0A%20%20%20%20%20%20-%20name:%20Install%20dependencies%0A%20%20%20%20%20%20%20%20run:%20%7C%0A%20%20%20%20%20%20%20%20%20%20pip%20install%20--upgrade%20pip%0A%20%20%20%20%20%20%20%20%20%20pip%20install%20-r%20requirements.txt%0A%0A%20%20%20%20%20%20-%20name:%20Check%20Python%20syntax%0A%20%20%20%20%20%20%20%20run:%20%7C%0A%20%20%20%20%20%20%20%20%20%20python%20-m%20py_compile%20app.py%0A%20%20%20%20%20%20%20%20%20%20echo%20%22%E2%9C%85%20Syntax%20check%20passed!%22%0A%0A%20%20%20%20%20%20-%20name:%20Validate%20requirements.txt%0A%20%20%20%20%20%20%20%20run:%20%7C%0A%20%20%20%20%20%20%20%20%20%20echo%20%22%F0%9F%94%8D%20Checking%20requirements.txt...%22%0A%20%20%20%20%20%20%20%20%20%20grep%20-q%20%22streamlit%22%20requirements.txt%20%7C%7C%20%7B%20echo%20%22%E2%9D%8C%20ERROR:%20requirements.txt%20missing%20streamlit%22;%20exit%201;%20%7D%0A%20%20%20%20%20%20%20%20%20%20grep%20-q%20%22transformers%22%20requirements.txt%20%7C%7C%20%7B%20echo%20%22%E2%9D%8C%20ERROR:%20requirements.txt%20missing%20transformers%22;%20exit%201;%20%7D%0A%20%20%20%20%20%20%20%20%20%20grep%20-q%20%22torch%22%20requirements.txt%20%7C%7C%20%7B%20echo%20%22%E2%9D%8C%20ERROR:%20requirements.txt%20missing%20torch%22;%20exit%201;%20%7D%0A%20%20%20%20%20%20%20%20%20%20echo%20%22%E2%9C%85%20requirements.txt%20is%20complete!%22%0A%0A%20%20%20%20%20%20-%20name:%20Check%20README.md%20exists%0A%20%20%20%20%20%20%20%20run:%20%7C%0A%20%20%20%20%20%20%20%20%20%20if%20%5B%20!%20-f%20README.md%20%5D;%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20echo%20%22%E2%9D%8C%20ERROR:%20README.md%20is%20missing!%22%0A%20%20%20%20%20%20%20%20%20%20%20%20exit%201%0A%20%20%20%20%20%20%20%20%20%20fi%0A%20%20%20%20%20%20%20%20%20%20echo%20%22%E2%9C%85%20README.md%20found!%22%0A%0A%20%20%20%20%20%20-%20name:%20Check%20LICENSE%20exists%0A%20%20%20%20%20%20%20%20run:%20%7C%0A%20%20%20%20%20%20%20%20%20%20if%20%5B%20!%20-f%20LICENSE%20%5D;%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20echo%20%22%E2%9D%8C%20ERROR:%20LICENSE%20is%20missing!%22%0A%20%20%20%20%20%20%20%20%20%20%20%20exit%201%0A%20%20%20%20%20%20%20%20%20%20fi%0A%20%20%20%20%20%20%20%20%20%20echo%20%22%E2%9C%85%20LICENSE%20found!%22%0A%0A%20%20%20%20%20%20-%20name:%20Check%20lesson%20100%20works%20in%20code%0A%20%20%20%20%20%20%20%20run:%20%7C%0A%20%20%20%20%20%20%20%20%20%20python%20-c%20%22%0Aimport%20sys%0Aimport%20os%0Asys.path.append(os.getcwd())%0Afrom%20app%20import%20lessons%0Aif%20len(lessons)%20%3C%20100:%0A%20%20%20%20print('%E2%9D%8C%20ERROR:%20Only',%20len(lessons),%20'lessons%20found.%20Need%20100!')%0A%20%20%20%20sys.exit(1)%0Aprint('%E2%9C%85%20All%20100%20lessons%20loaded%20successfully!')%0A%22

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

## 📘 The 10 Lessons (Offline Content)

All 10 lessons are stored locally — no internet needed:

1. **What is the 4th Industrial Revolution?**  
   Technologies like AI, blockchain, and IoT merging digital, physical, and biological worlds.

2. **Understanding Artificial Intelligence (AI)**  
   Machines learning to perform tasks that normally require human intelligence.

3. **Blockchain Basics**  
   A decentralized digital ledger that records transactions securely across many computers.

4. **What is Cryptocurrency?**  
   Digital money powered by blockchain — like Bitcoin and Ethereum.

5. **Web3 Introduction**  
   The next version of the internet where users own their data, identity, and assets.

6. **The Power of Big Data**  
   Large sets of information analyzed to reveal patterns and make better decisions.

7. **Decentralized Finance (DeFi)**  
   Financial services built on blockchain — no banks or middlemen needed.

8. **The Internet of Things (IoT)**  
   Everyday devices like fridges, watches, and cars connected to the internet.

9. **Metaverse and Virtual Worlds**  
   3D digital spaces where people meet, work, and play together.

10. **The Future of Work**  
    Skills in AI, blockchain, and coding will drive new opportunities in the global economy.

> 💡 Each lesson gives **+10 points**. Collect them all!

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
