import streamlit as st
import random
import translations
import importlib
importlib.reload(translations)
import translations
import importlib
importlib.reload(translations)
from translations import get_text
from utils import show_language_selector

st.set_page_config(page_title="Dragon Playground", page_icon="🎮", layout="wide")

lang = show_language_selector()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("assets/style.css")

st.title(get_text("playground_title", lang))
st.markdown(f"### {get_text('playground_subtitle', lang)}")

tab1, tab2, tab3, tab4 = st.tabs([
    get_text("tab_math", lang), 
    get_text("tab_friend", lang), 
    get_text("tab_name", lang), 
    get_text("tab_color", lang)
])

# --- Game 1: Dragon Math ---
with tab1:
    st.header(get_text("math_q", lang))
    
    if 'math_num' not in st.session_state:
        st.session_state.math_num = random.randint(1, 10)
    
    target = st.session_state.math_num
    
    # Display dragons
    st.markdown(f"<div style='font-size: 3rem; text-align: center;'>{'🐉' * target}</div>", unsafe_allow_html=True)
    
    answer = st.number_input(get_text("math_input_label", lang), min_value=1, max_value=20, step=1)
    
    if st.button(get_text("math_check", lang), key="check_math"):
        if answer == target:
            st.balloons()
            st.success(get_text("math_correct", lang))
            st.session_state.math_num = random.randint(1, 10) # Reset
        else:
            st.error(get_text("math_wrong", lang))

# --- Game 2: Friendship ---
with tab2:
    st.subheader(get_text("friend_q", lang))
    
    col_a, col_b = st.columns(2)
    
    if col_a.button(get_text("friend_opt1", lang)):
        st.success(get_text("friend_fb1", lang))
        st.balloons()
        
    if col_b.button(get_text("friend_opt2", lang)):
        st.warning(get_text("friend_fb2", lang))

    st.markdown("---")
    st.write(get_text("friend_magic", lang))
    
    # Magic words are universal, but we can localize labels if needed.
    # For now keeping English buttons as they are simple words, or we could add Chinese.
    # Let's keep them bilingual-ish or just simple.
    m1, m2, m3 = st.columns(3)
    m1.button(get_text("magic_please", lang))
    m2.button(get_text("magic_thank_you", lang))
    m3.button(get_text("magic_sorry", lang))

# --- Game 3: Name Creator ---
with tab3:
    st.header(get_text("tab_name", lang))
    
    prefixes = ["Glitter", "Thunder", "Star", "Moon", "Rainbow", "Little", "Brave"]
    suffixes = ["Wing", "Scale", "Claw", "Heart", "Breath", "Tail", "Toe"]
    
    # Simple Chinese equivalents
    prefixes_zh = ["闪闪", "雷霆", "星光", "月亮", "彩虹", "小小", "勇敢"]
    suffixes_zh = ["之翼", "鳞片", "利爪", "之心", "吐息", "尾巴", "脚趾"]
    
    c1, c2 = st.columns(2)
    
    if lang == 'zh':
        p = c1.selectbox(get_text("name_prefix", lang), prefixes_zh)
        s = c2.selectbox(get_text("name_suffix", lang), suffixes_zh)
        full_name = p + s
    else:
        p = c1.selectbox(get_text("name_prefix", lang), prefixes)
        s = c2.selectbox(get_text("name_suffix", lang), suffixes)
        full_name = p + " " + s
        
    st.markdown(f"### {get_text('name_result', lang).format(full_name)}")

# --- Game 4: Color Match ---
with tab4:
    # Randomly pick an element
    # Structure: (key, Display Name, Expected Color Emoji, Color Name Key)
    elements = [
        ("fire", get_text("color_fire", lang), "🟥", "color_red"), 
        ("water", get_text("color_water", lang), "🟦", "color_blue"), 
        ("nature", get_text("color_nature", lang), "🟩", "color_green")
    ]
    
    if 'target_elem' not in st.session_state:
        st.session_state.target_elem = random.choice(elements)
    
    elem_key, elem_name, correct_emoji, _ = st.session_state.target_elem
    
    st.subheader(get_text("color_q", lang).format(elem_name))
    
    st.write(get_text("color_instruction", lang))

    # Better UI: 3 Buttons with Color Emojis
    b1, b2, b3 = st.columns(3)
    cols = [b1, b2, b3]
    
    # Shuffle options for fun? Or keep fixed? Fixed is easier for now.
    for i, (key, name, emoji, color_key) in enumerate(elements):
        with cols[i]:
            # Use the emoji directly as the button label for big visual target
            color_label = get_text(color_key, lang)
            if st.button(f"{emoji} {color_label}", key=f"btn_color_{key}", use_container_width=True):
                if key == elem_key:
                    st.success(get_text("color_correct", lang))
                    st.balloons()
                    # Pick new target
                    st.session_state.target_elem = random.choice(elements)
                    st.rerun()
                else:
                    st.error(get_text("color_wrong", lang))
