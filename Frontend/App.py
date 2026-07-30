import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Resume & Content Analyzer", layout="wide")

st.title("🤖 AI Resume & Content Analyzer SaaS")

# Load AI model cached so it loads fast
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

try:
    nlp_pipeline = load_model()
except Exception as e:
    st.error(f"Error loading AI model: {e}")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

menu = st.sidebar.selectbox("Navigation", ["Home", "Login / Signup", "Analyzer Dashboard"])

if menu == "Home":
    st.subheader("Welcome to your AI-powered SaaS Product!")
    st.write("This platform analyzes text and resumes using natural language processing.")

elif menu == "Login / Signup":
    st.subheader("🔑 User Authentication")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if email and password:
            st.session_state["logged_in"] = True
            st.success("Successfully logged in!")
        else:
            st.error("Please enter credentials.")

elif menu == "Analyzer Dashboard":
    if not st.session_state["logged_in"]:
        st.warning("Please log in first from the sidebar!")
    else:
        st.subheader("📄 Paste Resume / Text for Analysis")
        user_input = st.text_area("Paste text here:", height=200)
        
        if st.button("Analyze with AI"):
            if user_input:
                with st.spinner("AI is analyzing..."):
                    # Run AI model prediction directly
                    result = nlp_pipeline(user_input)
                    word_count = len(user_input.split())
                    skills_found = [word for word in ["python", "machine learning", "sql", "api", "chemistry", "research"] if word in user_input.lower()]
                    score = min(100, len(skills_found) * 20 + (10 if word_count > 50 else 5))
                    
                    st.success("Analysis Complete!")
                    
                    col1, col2 = st.columns(2)
                    col1.metric("Match Score", f"{score}%")
                    col1.write(f"**Detected Keywords/Skills:** {', '.join(skills_found) if skills_found else 'General text'}")
                    
                    col2.write(f"**AI Sentiment:** {result[0]['label']}")
                    col2.info(f"**Recommendation:** Strong profile match detected!" if score >= 40 else "Consider adding more technical keywords.")
            else:
                st.warning("Please provide text input.")
