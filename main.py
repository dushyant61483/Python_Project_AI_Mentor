import streamlit as st
import frontend as ui
from backend import get_ai_response

st.set_page_config(
    page_title="Varion-AI",
    layout="centered",
    page_icon="✨"
)

ui.inject_modern_css()
ui.render_sidebar()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "mode" not in st.session_state:
    st.session_state.mode = "General Mentor"

is_active = len(st.session_state.messages) > 0
ui.render_header(is_minimized=is_active)

ui.render_chat(st.session_state.messages)

prompt = st.chat_input("Ask your mentor anything...")

if prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    ui.render_chat([{"role": "user", "content": prompt}])

    with st.spinner("Varion is thinking..."):
        response = get_ai_response(
            st.session_state.messages,
            mode=st.session_state.get("mode")
        )

    full_text = ui.render_assistant_response(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": full_text
    })


st.markdown("<div style='height: 120px'></div>", unsafe_allow_html=True)
