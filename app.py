import os
import streamlit as st
from langchain_openai import OpenAI

st.set_page_config(
    page_title="AI Homework Solver",
    page_icon="🦜",
    layout="centered"
)

# Sidebar
with st.sidebar:
    st.header("About")
    st.write("AI-powered Homework Assistant built with Streamlit and LangChain.")
    if os.path.exists("cutie-cat.gif"):
        st.image("cutie-cat.gif")

# Check for API key from environment variable or user input
env_api_key = os.environ.get("OPENAI_API_KEY", "")
if not env_api_key:
    apikey = st.text_input("Enter your OpenAI API key:", type="password", key="api_key_input")
    if apikey:
        os.environ['OPENAI_API_KEY'] = apikey
else:
    apikey = env_api_key
    st.info("API Key loaded from environment.", icon="🔑")

# Display media files if present
if os.path.exists("Lofi hiphop.mp3"):
    st.audio("Lofi hiphop.mp3")
if os.path.exists("girl.gif"):
    st.image("girl.gif")

st.title("🦜️🔗 Ask your Homework problem 🧟‍♂️")
prompt = st.text_input("Type your homework question below", key="homework_prompt_input")

# LLM Execution
if apikey and prompt:
    try:
        with st.spinner("Analyzing and solving your problem..."):
            llm = OpenAI(temperature=0.7)
            # Use modern LangChain .invoke() instead of deprecated __call__
            response = llm.invoke(prompt)
            st.success("Solution:")
            st.write(response)
    except Exception as e:
        st.error(f"Error communicating with AI: {e}")
elif not apikey:
    st.warning("Please enter your OpenAI API key to proceed.")
