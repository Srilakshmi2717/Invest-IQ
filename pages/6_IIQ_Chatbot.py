import streamlit as st
import requests
from streamlit_lottie import st_lottie
import json

st.set_page_config(page_title="IIQ Chatbot", layout="wide")
st.title("🧠 IIQ Chatbot")

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

with st.container():
    lottie_animation = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_zrqthn6o.json")
    st_lottie(lottie_animation, speed=1, width=1000, height=300, key="chatbot_lottie")

API_TOKEN = st.secrets["HF_API_TOKEN"]
API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"❌ API Error: {response.status_code} - {response.text}")
        return None

# Keep chat history
if "history" not in st.session_state:
    st.session_state.history = []

if "full_conversation" not in st.session_state:
    st.session_state.full_conversation = ""

col1, col2 = st.columns([4, 1])  

with col1:
    # Chat display area (Dark-themed bubbles)
    for sender, message in st.session_state.history:
        if sender == "You":
            st.markdown(f'<div style="background-color:#4f5b62;color:white;padding:10px;border-radius:10px;margin-bottom:10px;">**{sender}:** {message}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div style="background-color:#2f3136;color:white;padding:10px;border-radius:10px;margin-bottom:10px;">**{sender}:** {message}</div>', unsafe_allow_html=True)

# Input area at the bottom
st.markdown(
    """
    <style>
    .stTextInput>div>div>input {
        padding: 10px;
        font-size: 16px;
        border-radius: 10px;
        border: none;
        background-color: #2f3136;
        color: white;
    }
    .stButton>button {
        background-color: #4f5b62;
        color: white;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

input_container = st.empty()

# Get user input and send button (aligned at the bottom)
with input_container.container():
    user_input = st.text_input("Ask me anything, and I will clear your doubts or questions right away!!", "")
    if st.button("Send") and user_input:
        st.session_state.full_conversation += f"User: {user_input}\nBot:"
        output = query({"inputs": st.session_state.full_conversation})

        if output and isinstance(output, list) and "generated_text" in output[0]:
            full_reply = output[0]["generated_text"]
            # Extract only bot's response
            bot_reply = full_reply.split("Bot:")[-1].strip()
            st.session_state.history.append(("You", user_input))
            st.session_state.history.append(("Bot", bot_reply))
            st.session_state.full_conversation += f" {bot_reply}\n"
        else:
            st.session_state.history.append(("Bot", "Sorry, something went wrong."))

# Display chat history
for sender, message in st.session_state.history:
    if sender == "You":
        st.markdown(f'<div style="background-color:#4f5b62;color:white;padding:10px;border-radius:10px;margin-bottom:10px;">**{sender}:** {message}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div style="background-color:#2f3136;color:white;padding:10px;border-radius:10px;margin-bottom:10px;">**{sender}:** {message}</div>', unsafe_allow_html=True)

st.sidebar.success("Select a page from the sidebar.")