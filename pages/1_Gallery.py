import streamlit as st
import os
from i18n import get_text
from utils import show_language_selector

st.set_page_config(page_title="Dragon Gallery", page_icon="🖼️", layout="wide")

# Determine Language via Sidebar
lang = show_language_selector()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("assets/style.css")

# --- Language Consistency Check ---
# If user refreshed directly here, we might want the sidebar simple toggle again or just rely on session state persistence.
# For simplicity, we assume they enter via Home or state persists.

st.title(get_text("gallery_title", lang))
st.markdown(get_text("gallery_subtitle", lang))

# --- Story Modal Function ---
# --- Card Function ---
def dragon_card(name, title, img_path, food, superpower, story_text, col, key_id):
    with col:
        st.markdown(f"""
        <div class="dragon-card">
            <h3 class="dragon-name">{name}</h3>
            <p>{title}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if os.path.exists(img_path):
            st.image(img_path, use_container_width=True)
        else:
            st.warning(get_text("img_hatching", lang).format(name))
        
        # Story Expander (Compatible with all mobile versions)
        expander_label = get_text("btn_read_story", lang).format(name.split()[0])
        with st.expander(expander_label):
            st.subheader(f"{name} & Mori")
            st.markdown(f"_{story_text}_")

        st.markdown(f"""
        <div style="background-color: #f0f2f6; padding: 10px; border-radius: 10px; text-align: left; margin-top: 10px;">
            <p><strong>{get_text("food_label", lang)}</strong> {food}</p>
            <p><strong>{get_text("power_label", lang)}</strong> {superpower}</p>
        </div>
        """, unsafe_allow_html=True)

# --- Stories & Keys ---
# We retrieve them dynamically based on language
dragons = [
    ("ignis", "assets/dragon_fire.png", "btn_ignis"),
    ("aqua", "assets/dragon_water.png", "btn_aqua"),
    ("terra", "assets/dragon_nature.png", "btn_terra"),
    # Row 2
    ("frosty", "assets/dragon_ice.png", "btn_frosty"),
    ("aurelius", "assets/dragon_gold.png", "btn_aurelius")
]

# Layout
col1, col2, col3 = st.columns(3)
col4, col5 = st.columns([1, 1])
cols = [col1, col2, col3, col4, col5]

for i, (key, img, btn_id) in enumerate(dragons):
    name = get_text(f"{key}_name", lang)
    title = get_text(f"{key}_title", lang)
    food = get_text(f"{key}_food", lang)
    power = get_text(f"{key}_power", lang)
    story = get_text(f"{key}_story", lang)
    
    # Decide column
    current_col = cols[i]
    
    dragon_card(name, title, img, food, power, story, current_col, btn_id)

st.markdown("---")
st.subheader(get_text("vote_label", lang))
# For voting options, we just use the keys or localized names. Let's use localized names.
dragon_names_map = {get_text(f"{k}_name", lang).split()[0]: k for k, _, _ in dragons}
vote = st.radio(get_text("vote_placeholder", lang), list(dragon_names_map.keys()), horizontal=True)

if vote:
    st.balloons()
    st.success(get_text("vote_success", lang).format(vote))
