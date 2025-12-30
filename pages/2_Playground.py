import streamlit as st
import random

st.set_page_config(page_title="Dragon Playground", page_icon="🎮", layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("assets/style.css")

st.title("Dragon Playground 🎪")
st.markdown("Let's play and learn with our dragon friends!")

tab1, tab2, tab3, tab4 = st.tabs(["123 Math", "❤️ Friendship", "🔤 Name Creator", "🎨 Colors"])

# --- Game 1: Dragon Math ---
with tab1:
    st.header("Count with Spark! 🔢")
    
    # Initialize session state for the math game
    if 'num1' not in st.session_state:
        st.session_state.num1 = random.randint(1, 5)
        st.session_state.num2 = random.randint(1, 5)
        st.session_state.score = 0

    col1, col2 = st.columns(2)
    
    with col1:
        st.info(f"If you have **{st.session_state.num1}** Fire Dragons...")
        st.write("🔥" * st.session_state.num1)
        
        st.info(f"...and **{st.session_state.num2}** Water Dragons...")
        st.write("💧" * st.session_state.num2)

    with col2:
        st.subheader("How many do you have in total?")
        
        # User input
        answer = st.number_input("Type your answer here:", min_value=0, max_value=20, step=1)
        
        if st.button("Check Math Answer! ✅"):
            correct_sum = st.session_state.num1 + st.session_state.num2
            if answer == correct_sum:
                st.balloons()
                st.success(f"Great job! {st.session_state.num1} + {st.session_state.num2} = {correct_sum}")
                st.session_state.score += 1
                # Reset for next question
                st.session_state.num1 = random.randint(1, 5)
                st.session_state.num2 = random.randint(1, 5)
                st.rerun()
            else:
                st.warning("Oops! Try counting the emojis again. You can do it!")

    st.write(f"**Your Score:** {st.session_state.score} Stars ⭐")

# --- Game 2: Friendship & Words ---
with tab2:
    st.header("Learning to be a Friend 🤝")
    
    st.markdown("### Scenario 1: Meeting a New Dragon")
    st.write("You meet a shy little Forest Dragon named Terra. What should you do?")
    
    # Friendship Quiz
    friendship_q = st.radio(
        "Choose the best action:",
        ["Roar very loudly to show you are strong! 🦁",
         "Smile gently and say 'Hello!' 👋",
         "Take her toys without asking. 🧸"],
        index=None
    )
    
    if friendship_q == "Smile gently and say 'Hello!' 👋":
        st.snow()
        st.success("That's right! Being gentle makes new friends feel safe.")
    elif friendship_q: # Answered but wrong
        st.error("Oh no! That might scare the little dragon. Try being gentler.")
        
    st.markdown("---")
    st.markdown("### Magic Words")
    st.write("Dragons love magic words. Can you find them?")
    
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("Please"):
            st.success("Correct! 'Please' is a magic word.")
    with col_b:
        if st.button("Gimme!"):
            st.warning("That's not very polite!")
            
    col_c, col_d = st.columns(2)
    with col_c:
        if st.button("Thank You"):
            st.success("Correct! Always say thank you.")
    with col_d:
        if st.button("Go Away"):
            st.warning("That's not nice!")

# --- Game 3: Dragon Name Creator ---
with tab3:
    st.header("Create a Dragon Name! 🐲")
    st.write("Pick two magic sounds to make a new name.")
    
    col_n1, col_n2 = st.columns(2)
    with col_n1:
        part1 = st.selectbox("First Part", ["Spark", "Glitter", "Thunder", "Moon", "Star"])
    with col_n2:
        part2 = st.selectbox("Second Part", ["wing", "scale", "claw", "breath", "heart"])
        
    full_name = part1 + part2
    st.markdown(f"### Your dragon's name is: **{full_name}**!")
    if st.button("Adopt this Dragon! 🥚"):
        st.success(f"Congratulations! You adopted {full_name}!")

# --- Game 4: Color Match ---
with tab4:
    st.header("Match the Dragon to its Element! 🎨")
    
    target_dragon = random.choice(["Fire 🔥", "Water 💧", "Nature 🌿"])
    st.info(f"Which color matches a **{target_dragon}** Dragon?")
    
    col_c1, col_c2, col_c3 = st.columns(3)
    
    with col_c1:
        if st.button("Red 🔴"):
            if "Fire" in target_dragon: st.success("Correct! Red for Fire!"); st.balloons()
            else: st.error("Not quite!")
            
    with col_c2:
        if st.button("Blue 🔵"):
            if "Water" in target_dragon: st.success("Correct! Blue for Water!"); st.balloons()
            else: st.error("Not quite!")
            
    with col_c3:
        if st.button("Green 🟢"):
            if "Nature" in target_dragon: st.success("Correct! Green for Nature!"); st.balloons()
            else: st.error("Not quite!")

