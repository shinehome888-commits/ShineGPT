import streamlit as st

# ------------------- SET PAGE CONFIG -------------------
st.set_page_config(
    page_title="ShineGPT",
    page_icon="🌍",
    layout="centered"
)

# ------------------- HOME PAGE LAYOUT -------------------
st.markdown("<h1 style='text-align: center; color: #D4AF37;'>SHINEGPT</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>Learn. Earn Knowledge. Empower Yourself.</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #D32F2F;'>Powered by KS1 Empire Foundation</p>", unsafe_allow_html=True)

# Just show this — nothing else
st.write("")
st.info("✅ This is the foundation. If you see this, the app is working.")
