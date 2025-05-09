import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(page_title="IIQ Home", layout="wide")

lottie_mentor = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_jcikwtux.json")  # Education theme

st.title("📊 IIQ - The Smart Market Mentor")

st.markdown(
    """
    <div>
        Welcome to <b>IIQ - The Smart Market Mentor</b>, where we turn complexity into clarity. 
        Explore predictive models, interactive analytics, and AI-powered learning, made for every curious mind.
    </div>
    """, unsafe_allow_html=True
)

st_lottie(lottie_mentor, height=350, key="mentor", speed=1, loop=True)

st.markdown("### 🚀 Why Choose **IIQ**?")
st.markdown(
    """
- 📊 **Transforms Complex Data into Clarity**  
  Decode stock market trends through AI-powered visual insights - no finance degree needed.

- 🎓 **Built for Learning, Not Just Predicting**  
  Designed by an AI & Data Science student to teach both **financial literacy** and **AI fundamentals** interactively.

- 🌐 **Anywhere, Anytime Access**  
  Lightweight, internet-based tool - making quality finance education **accessible to Tier 2/3 cities and beyond**.

- 📚 **Bridging the 27% Financial Literacy Gap**  
  Crafted with India's alarming financial illiteracy in mind - empowering students and the general public to invest smartly, not blindly.

- 🤝 **Empowers Responsible Investing**  
  Cultivates a **scientific and ethical investing mindset**, reducing risky gambling behavior among youth.

- 🧠 **Real-Time Learning with Predictive Modeling**  
  Understand **how AI thinks** and predicts in the stock market - fostering **AI literacy** through practical use cases.

- 🏫 **Perfect for Classrooms & Self-Learning**  
  Faculties can use it to demonstrate **real-world AI + Economics applications** with live data.

- ❤️ **For the Underserved, By the Informed**  
  Not just a dashboard - it’s a **social impact tool** designed to uplift financially unaware communities.
""")

st.sidebar.success("Select a page from the sidebar.")
