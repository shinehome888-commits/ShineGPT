import streamlit as st

# ------------------- SET PAGE CONFIG -------------------
st.set_page_config(
    page_title="ShineGPT",
    page_icon="🌍",
    layout="centered"
)

# ------------------- DISPLAY MAIN MESSAGE -------------------
st.markdown(
    """
    <div style="text-align: center; padding: 50px;">
        <h1 style="color: #D4AF37; font-size: 4rem;">SHINEGPT</h1>
        <p style="color: white; font-size: 1.5rem;">Learn. Earn Knowledge. Empower Yourself.</p>
        <p style="color: #D32F2F; font-size: 1.3rem;">Powered by KS1 Empire Foundation</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ------------------- INFO BOX (ONLY) -------------------
st.info("✅ This is a clean test of your app. If you see this, the foundation works.")
