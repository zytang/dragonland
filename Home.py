import streamlit as st
import base64
from translations import get_text

# Page Config
st.set_page_config(
    page_title="Dragonland",
    page_icon="🐉",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Language State ---
if 'language' not in st.session_state:
    st.session_state.language = 'en'

def set_language():
    st.session_state.language = st.session_state.lang_select

# Sidebar Language Selector
st.sidebar.markdown("### 🌐 Settings")
lang_options = {'🇺🇸 English': 'en', '🇨🇳 中文 (Chinese)': 'zh'}
# Reverse lookup for formatting
current_fmt = '🇺🇸 English' if st.session_state.language == 'en' else '🇨🇳 中文 (Chinese)'

selected_lang = st.sidebar.radio(
    "Language / 语言",
    options=list(lang_options.keys()),
    index=list(lang_options.keys()).index(current_fmt),
    key="lang_select",
    on_change=set_language
)
# Ensure state sync
st.session_state.language = lang_options[selected_lang]
lang = st.session_state.language

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
st.markdown(f"""
<div class="hero-header">
    <h1 class="hero-title">
        {get_text("home_title", lang)}
    </h1>
    <h3 class="hero-subtitle">
        {get_text("home_subtitle", lang)}
    </h3>
</div>
""", unsafe_allow_html=True)

# 2. Story Card (Consolidated HTML for Glass Effect)
st.markdown(f"""
<div class="glass-card full-width-card">
    <div style="text-align: center;">
        <h2 style="color: #FF6B6B; font-size: 2.5rem; margin-bottom: 20px;">{get_text("story_card_title", lang)}</h2>
        <div style="font-size: 1.3rem; line-height: 1.8; color: #333;">
            <p>{get_text("story_p1", lang)}</p>
            <p>{get_text("story_p2", lang)}</p>
            <p>{get_text("story_p3", lang)}</p>
            <div style="display: flex; flex-direction: column; gap: 15px; background: rgba(255,255,255,0.6); padding: 25px; border-radius: 20px; text-align: left; margin-top: 20px;">
                <div style="display: flex; align-items: start; gap: 15px;">
                    <span style="font-size: 1.5rem; line-height: 1;">🤖</span>
                    <span>{get_text("story_list_1", lang)}</span>
                </div>
                <div style="display: flex; align-items: start; gap: 15px;">
                    <span style="font-size: 1.5rem; line-height: 1;">🌍</span>
                    <span>{get_text("story_list_2", lang)}</span>
                </div>
                <div style="display: flex; align-items: start; gap: 15px;">
                    <span style="font-size: 1.5rem; line-height: 1;">🤝</span>
                    <span>{get_text("story_list_3", lang)}</span>
                </div>
            </div>
            <p style="margin-top: 30px; font-size: 1.5rem; font-weight: 800; color: #FF6B6B;">{get_text("join_quest", lang)}</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 3. Action Button (Centered)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button(get_text("btn_start", lang), use_container_width=True):
        st.switch_page("pages/1_Gallery.py")

# 4. Metrics
st.markdown(f"""
<div class="glass-card full-width-card" style="margin-top: 40px;">
    <h3 style="text-align: center; margin-bottom: 20px;">{get_text("metrics_title", lang)}</h3>
    <div class="metrics-container">
        <div>
            <div style="font-size: 2rem; color: #FF6B6B; font-weight: bold;">{get_text("metric_happiness_val", lang)}</div>
            <div style="color: #666;">{get_text("metric_happiness_label", lang)}</div>
        </div>
        <div>
            <div style="font-size: 2rem; color: #4ECDC4; font-weight: bold;">{get_text("metric_curiosity_val", lang)}</div>
            <div style="color: #666;">{get_text("metric_curiosity_label", lang)}</div>
        </div>
        <div>
            <div style="font-size: 2rem; color: #FFC107; font-weight: bold;">{get_text("metric_friends_val", lang)}</div>
            <div style="color: #666;">{get_text("metric_friends_label", lang)}</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
