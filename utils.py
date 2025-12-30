import streamlit as st

def show_language_selector():
    """Displays the language selector in the sidebar and returns the selected language code."""
    if 'language' not in st.session_state:
        st.session_state.language = 'en'
    
    st.sidebar.markdown("### 🌐 Settings")
    
    lang_options = {'🇺🇸 English': 'en', '🇨🇳 中文 (Chinese)': 'zh'}
    
    # Reverse lookup for current selection
    current_fmt = '🇺🇸 English'
    for k, v in lang_options.items():
        if v == st.session_state.language:
            current_fmt = k
            break
            
    selected = st.sidebar.radio(
        "Language / 语言",
        options=list(lang_options.keys()),
        index=list(lang_options.keys()).index(current_fmt),
        key="global_lang_select"
    )
    
    # Update state
    st.session_state.language = lang_options[selected]
    return st.session_state.language
