# 🌍 shineGPT — Learn AI Without Internet. Speak. Listen. Grow.

![Streamlit](https://img.shields.io/badge/Interface-Streamlit-blue)  
![Offline Mode](https://img.shields.io/badge/SMS--Mode-Offline-green)  
![Voice Enabled](https://img.shields.io/badge/Voice--Input--Output-Enabled-orange)  
![AI for Good](https://img.shields.io/badge/Mission-Empower-Affordable)

> **No internet? No problem.**  
> shineGPT lets children in African villages **speak** their questions — and **hear** the answers —  
> without Wi-Fi, without data, without cost.

---

## 💡 What Is shineGPT?

shineGPT is not just another AI chatbot.

It’s a **dual-mode AI tutor** built for **children who can’t afford data**,  
who live where the internet is slow — or non-existent.

It has **two ways to learn**:

| Mode | How It Works | Needs Internet? |
|------|--------------|------------------|
| 📱 **SMS Mode** | Type `lesson 1`, `what is ai`, or `help` → get instant text replies | ❌ No |
| 💻 **Online Mode** | Speak your question → AI listens → AI speaks back | ✅ Yes |

Built with **Microsoft Phi-3-mini AI**, **voice recognition**, and **text-to-speech** —  
it turns any phone into a **free, offline classroom**.

> 🎯 **Learn. Earn Knowledge. Empower Yourself.**

---

## 📱 SMS Mode — No Internet, No Problem

Even if your phone has no data, you can still learn:

- Type `lesson 1` → learn what the 4th Industrial Revolution is  
- Type `what is blockchain` → hear: *“Blockchain is a digital notebook that everyone can see, but no one can cheat.”*  
- Type `points` → see how many lessons you’ve completed  

✅ **50 carefully crafted lessons** — from AI to ethics — all stored on your phone.  
✅ No downloads. No servers. No cost.  
✅ Works on a **Nokia 1100** if you open the link in its browser.

---

## 💬 Online Mode — Speak. Listen. Learn.

When you have internet:

1. Click **“Chat with ShineGPT”**  
2. Click **“Start Listening”** → speak: *“What is AI?”*  
3. The AI hears you → thinks → speaks back:  
   > _“AI is when machines learn to think like humans — like me!”_  
4. You hear it — **out loud** — through your phone’s speaker.

No typing. No reading.  
Just **voice to voice**.

Powered by **Microsoft Phi-3-mini** — a small, fast, powerful AI built for edge devices.  
It understands you. It answers you. It *speaks* to you.

---

## 🌍 Why This Matters

In rural Africa:
- 60% of students have **no reliable internet**
- Data costs more than food in some places
- Many children can’t read — but they can speak

shineGPT doesn’t ask them to adapt to technology.

**It adapts to them.**

It meets them where they are —  
with a phone, a voice, and a dream.

---

## 🛠️ Tech Stack

| Component | Tool |
|---------|------|
| Frontend | [Streamlit](https://streamlit.io/) |
| Offline AI | Pre-loaded 50 lessons + keyword matching |
| Online AI | [Microsoft Phi-3-mini-4k-instruct](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct) |
| Deployment | Hugging Face Spaces |

---

## 📦 Requirements

If you want to run shineGPT locally:

```bash
pip install -r requirements.txt
streamlit run app.py
