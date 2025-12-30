import streamlit as st
import os

st.set_page_config(page_title="Dragon Gallery", page_icon="🖼️", layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("assets/style.css")

st.title("Meet the Dragons! 🐉")
st.markdown("Here are Mori's best friends. Click the buttons to read their stories!")

# --- Story Modal Function ---
@st.dialog("Dragon Tale 📖")
def show_story(name, story, img_path):
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists(img_path):
            st.image(img_path, use_container_width=True)
    with col2:
        st.subheader(f"{name} & Mori")
        st.markdown(f"_{story}_")
        st.markdown("---")
        if st.button("Close", key=f"close_{name}"):
            st.rerun()

# --- Card Function ---
def dragon_card(name, title, img_path, food, superpower, story_text, col, key_id):
    with col:
        st.markdown(f"""
        <div class="dragon-card">
            <h3 class="dragon-name">{name}</h3>
            <p>{title}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Image display
        if os.path.exists(img_path):
            st.image(img_path, use_container_width=True)
        else:
            st.warning(f"Image for {name} is hatching... 🥚")
        
        # "Clickable Image" Simulation -> Button
        # We use a button that looks inviting underneath the image
        if st.button(f"📖 Read {name}'s Story", key=key_id, use_container_width=True):
            show_story(name, story_text, img_path)

        st.markdown(f"""
        <div style="background-color: #f0f2f6; padding: 10px; border-radius: 10px; text-align: left; margin-top: 10px;">
            <p><strong>🍎 Favorite Snack:</strong> {food}</p>
            <p><strong>✨ Superpower:</strong> {superpower}</p>
        </div>
        """, unsafe_allow_html=True)

# --- Stories ---
stories = {
    "ignis": "One night, Mori was afraid of the dark forest. Ignis flew down and lit up the path with gentle, warm flames, showing Mori that the scary shadows were just dancing trees!",
    "aqua": "Mori wanted to see the fish but couldn't swim deep enough. Aqua blew a giant magical bubble around Mori, turning it into a submarine so they could explore the coral reef together!",
    "terra": "Mori found a bird with a broken nest high in a tree. Terra stomped his little foot, and a vine grew instantly to lift Mori up so he could help the bird fix its home.",
    "frosty": "It was a scorching hot day and everyone was sad. Frosty sneezed a glittery ice cloud, turning the town square into a snowy playground for the best summer sled race ever!",
    "aurelius": "Mori lost his favorite toy in the tall grass. Aurelius glowed with a soft golden light, making the hidden toy sparkle so Mori could find it immediately!"
}

# --- Layout ---
col1, col2, col3 = st.columns(3)
col4, col5 = st.columns([1, 1]) # Second row

# Row 1
dragon_card("Ignis 🔥", "The Creative Spark", "assets/dragon_fire.png", "Roasted Marshmallows", "Lighting up ideas!", stories["ignis"], col1, "btn_ignis")
dragon_card("Aqua 💧", "The Calm Friend", "assets/dragon_water.png", "Blueberry Smoothies", "Healing scratches", stories["aqua"], col2, "btn_aqua")
dragon_card("Terra 🌿", "The Nature Guardian", "assets/dragon_nature.png", "Sunlight & Cookies", "Growing flowers instantly", stories["terra"], col3, "btn_terra")

# Row 2 (Centered using columns)
# Used a simpler separate layout for row 2 to avoid alignment issues
with col4:
    pass # Spacer if needed, or just standard flow. 
    # Actually col4, col5 are 50/50.
    
dragon_card("Frosty ❄️", "The Cool Thinker", "assets/dragon_ice.png", "Ice Cream Cones", "Freezing bad moments", stories["frosty"], col4, "btn_frosty")
dragon_card("Aurelius 🪙", "The Golden Heart", "assets/dragon_gold.png", "Pancakes with Syrup", "Making everyone feel special", stories["aurelius"], col5, "btn_aurelius")

st.markdown("---")
st.subheader("Which dragon is your favorite?")
vote = st.radio("Pick one!", ["Ignis", "Aqua", "Terra", "Frosty", "Aurelius"], horizontal=True)
if vote:
    st.balloons()
    st.success(f"Yay! {vote} loves you too! ❤️")
