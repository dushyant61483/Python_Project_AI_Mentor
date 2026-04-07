import streamlit as st
import time


# 🎨 MODERN CHATGPT-LIKE UI
def inject_modern_css():
    st.markdown("""
        <style>

        /* Layout */
        .stMainBlockContainer {
            max-width: 60rem !important;
            padding-top: 2rem;
        }

        .stApp {
            background-color: #0E1117;
            color: #E0E0E0;
            font-family: 'Inter', sans-serif;
        }

        /* USER MESSAGE (RIGHT) */
        .user-wrapper {
            display: flex;
            justify-content: flex-end;
        }

        .user-bubble {
            background-color: #1F6FEB;
            color: white;
            padding: 12px 16px;
            border-radius: 18px 18px 0px 18px;
            max-width: 75%;
            margin-bottom: 10px;
            animation: fadeIn 0.3s ease-in-out;
        }

        /* ASSISTANT MESSAGE (LEFT) */
        .assistant-wrapper {
            display: flex;
            justify-content: flex-start;
        }

        .assistant-bubble {
            background-color: #161B22;
            border: 1px solid #30363D;
            padding: 12px 16px;
            border-radius: 18px 18px 18px 0px;
            max-width: 75%;
            margin-bottom: 10px;
            animation: fadeIn 0.3s ease-in-out;
        }

        /* TABLE FIX */
        table {
            width: 100% !important;
            border-collapse: collapse;
            margin: 10px 0;
            background-color: #161B22;
        }

        th, td {
            padding: 10px !important;
            border: 1px solid #30363D;
            white-space: normal !important;
        }

        th {
            background-color: #21262D;
            color: #58A6FF !important;
        }

        /* 🔥 CHAT INPUT FIXED LIKE CHATGPT */
        section[data-testid="stChatInput"] {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            width: 60rem;
            max-width: 90%;
            z-index: 999;
        }

        section[data-testid="stChatInput"] textarea {
            border-radius: 20px !important;
            padding: 12px !important;
            background-color: #161B22 !important;
            color: white !important;
            border: 1px solid #30363D !important;
        }

        /* Prevent overlap */
        .block-container {
            padding-bottom: 120px;
        }

        /* Animation */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(5px); }
            to { opacity: 1; transform: translateY(0); }
        }

        </style>
    """, unsafe_allow_html=True)


# 🧠 HEADER
def render_header(is_minimized=False):
    if not is_minimized:
        st.markdown("<div style='height: 10vh;'></div>", unsafe_allow_html=True)
        st.markdown("""
            <div style='text-align: center;'>
                <h1 style='font-size: 4rem;'>✨ Varion-AI</h1>
                <p style='color: #8B949E;'>Your Personal Mentor & Career Scout</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style='display: flex; align-items: center;'>
                <h3>✨ Varion-AI</h3>
                <span style='margin-left: 10px; color: #8B949E;'>Mentor Active</span>
            </div>
            <hr>
        """, unsafe_allow_html=True)


# ⚙️ SIDEBAR
def render_sidebar():
    with st.sidebar:
        st.markdown("### 🛠️ Controls")

        mode = st.selectbox(
            "🎯 Mentor Mode",
            ["General Mentor", "Career Roadmap", "Interview Prep", "Coding Help"]
        )
        st.session_state.mode = mode

        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()


# 💬 CHAT DISPLAY
def render_chat(messages):
    for msg in messages:
        if msg["role"] == "user":
            st.markdown(
                f"""
                <div class="user-wrapper">
                    <div class="user-bubble">
                        {msg['content']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div class="assistant-wrapper">
                    <div class="assistant-bubble">
                        {msg['content']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


# ⚡ STREAMING EFFECT
def stream_response(text):
    words = text.split(" ")
    for word in words:
        yield word + " "
        time.sleep(0.02)


# 🤖 ASSISTANT RESPONSE (ANIMATED)
def render_assistant_response(response):
    placeholder = st.empty()
    full_text = ""

    for chunk in stream_response(response):
        full_text += chunk
        placeholder.markdown(
            f"""
            <div class="assistant-wrapper">
                <div class="assistant-bubble">
                    {full_text}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    return full_text
