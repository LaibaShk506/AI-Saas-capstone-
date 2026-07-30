import streamlit as st
import requests

st.set_page_config(page_title="AI Content & Resume Analyzer", layout="wide")

st.title("🤖 AI Resume & Content Analyzer SaaS")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

menu = st.sidebar.selectbox("Navigation", ["Home", "Login / Signup", "Analyzer Dashboard"])

if menu == "Login / Signup":
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
        st.subheader("📄 Upload or Paste Resume / Text")
        user_input = st.text_area("Paste Resume Text Here:", height=200)
        
        if st.button("Analyze with AI"):
            if user_input:
                with st.spinner("AI is analyzing..."):
                    # Replace URL below with your Render live backend URL once deployed
                    backend_url = "http://127.0.0.1:8000/analyze"
                    try:
                        response = requests.post(backend_url, json={"text": user_input})
                        res = response.json()
                        
                        st.success("Analysis Complete!")
                        data = res["data"]
                        
                        col1, col2 = st.columns(2)
                        col1.metric("Match Score", data["score"])
                        col1.write(f"**Detected Skills:** {', '.join(data['skills'])}")
                        
                        col2.write(f"**Sentiment:** {data['sentiment']}")
                        col2.info(f"**Recommendation:** {data['recommendation']}")
                    except Exception as e:
                        st.error(f"Error connecting to API backend: {e}")
            else:
                st.warning("Please provide text input.")
                  
