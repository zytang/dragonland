import streamlit as st
import base64

# Page Config
st.set_page_config(
    page_title="Dragonland",
    page_icon="🐉",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to set background image
def set_bg_hack(main_bg):
    main_bg_ext = "png"
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover;
             background-position: center;
             background-repeat: no-repeat;
             background-attachment: fixed;
         }}
         /* Add a semi-transparent overlay to make text readable */
         .stApp::before {{
             content: "";
             position: absolute;
             top: 0;
             left: 0;
             width: 100%;
             height: 100%;
             background: rgba(255, 255, 255, 0.4); /* Gentle white overlay */
             z-index: -1;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# Load Custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("assets/style.css")

# Set Background
try:
    set_bg_hack("assets/hero.png")
except FileNotFoundError:
    st.warning("Hero image not found for background.")

# --- Main Content ---

# 1. Hero Title (Floating)
st.markdown("""
<div class="hero-header">
    <h1 class="hero-title">
        Welcome to Dragonland! 🏰
    </h1>
    <h3 class="hero-subtitle">
        Where Friendship & Imagination Fly High
    </h3>
</div>
""", unsafe_allow_html=True)

# 2. Story Card (Consolidated HTML for Glass Effect)
st.markdown("""
<div class="glass-card full-width-card">
    <div style="text-align: center;">
        <h2 style="color: #FF6B6B; font-size: 2.5rem; margin-bottom: 20px;">The Boy and the Dragon 🌟</h2>
        <div style="font-size: 1.3rem; line-height: 1.8; color: #333;">
            <p>Once upon a time, in a world full of wonder, lived a kind-hearted boy named <strong>Mori</strong>.</p>
            <p>Mori dreamed of a future where everyone was happy and safe. One day, he met <strong>Spark</strong>, a magical dragon who showed him that the real magic is <strong>Kindness</strong> and <strong>Smart Thinking</strong>.</p>
            <p>Together, they traveled to the <strong>City of Tomorrow</strong>, where:</p>
            <div style="display: flex; flex-direction: column; gap: 15px; background: rgba(255,255,255,0.6); padding: 25px; border-radius: 20px; text-align: left; margin-top: 20px;">
                <div style="display: flex; align-items: start; gap: 15px;">
                    <span style="font-size: 1.5rem; line-height: 1;">🤖</span>
                    <span><strong>Technology</strong> helps us do boring chores so we have more time to play!</span>
                </div>
                <div style="display: flex; align-items: start; gap: 15px;">
                    <span style="font-size: 1.5rem; line-height: 1;">🌍</span>
                    <span><strong>Nature</strong> grows wild and free alongside our homes.</span>
                </div>
                <div style="display: flex; align-items: start; gap: 15px;">
                    <span style="font-size: 1.5rem; line-height: 1;">🤝</span>
                    <span><strong>Everyone</strong> is treated like a VIP (Very Important Person)!</span>
                </div>
            </div>
            <p style="margin-top: 30px; font-size: 1.5rem; font-weight: 800; color: #FF6B6B;">Join Mori and Spark on their quest here:</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 3. Action Button (Centered)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Start the Adventure! 🚀", use_container_width=True):
        st.switch_page("pages/1_Gallery.py")

# 4. Metrics (Custom HTML for styling consistency)
st.markdown("""
<div class="glass-card full-width-card" style="margin-top: 40px;">
    <h3 style="text-align: center; margin-bottom: 20px;">🌟 Our Bright Future</h3>
    <div style="display: flex; justify-content: space-around; text-align: center;">
        <div>
            <div style="font-size: 2rem; color: #FF6B6B; font-weight: bold;">100%</div>
            <div style="color: #666;">Happiness</div>
        </div>
        <div>
            <div style="font-size: 2rem; color: #4ECDC4; font-weight: bold;">Infinite</div>
            <div style="color: #666;">Curiosity</div>
        </div>
        <div>
            <div style="font-size: 2rem; color: #FFC107; font-weight: bold;">Together</div>
            <div style="color: #666;">Friends</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
