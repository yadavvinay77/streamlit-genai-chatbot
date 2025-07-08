import os
import streamlit as st
from modules import nlp_utils, web_search, llm_utils, summarizer

# --- Streamlit page config & session state ---
st.set_page_config(page_title="Universal Chatbot", layout="wide")

if "history" not in st.session_state:
    st.session_state.history = []

# Load SerpAPI key from env or file
def load_serpapi_key():
    key = os.getenv("SERPAPI_KEY")
    if key:
        return key
    try:
        with open("serpapi.txt") as f:
            return f.read().strip()
    except FileNotFoundError:
        st.error("Missing serpapi.txt with your SerpAPI key or set SERPAPI_KEY env variable.")
        st.stop()

if "serpapi_key" not in st.session_state:
    st.session_state.serpapi_key = load_serpapi_key()

# Cache keyword extraction
@st.cache_data(show_spinner=False)
def cached_extract_keywords(text):
    return nlp_utils.extract_keywords(text)

# Cache web search results
@st.cache_data(show_spinner=False)
def cached_search_web(keywords, key):
    return web_search.search_web(keywords, key)

# Cache LLM answers
@st.cache_data(show_spinner=False)
def cached_get_llm_answer(context, question):
    return llm_utils.get_llm_answer(context, question)

# --- Title ---
st.title("🧠 Universal NLP + Web Search + LLM Chatbot")

# --- Render chat history ---
for turn in st.session_state.history:
    st.chat_message("user").write(turn["user"])
    st.chat_message("assistant").write(turn["bot"])

# --- Chat input ---
user_input = st.chat_input("Your message...")

if user_input:
    # 1) Extract keywords
    keywords = cached_extract_keywords(user_input)

    # 2) Perform web search
    snippets = cached_search_web(keywords, st.session_state.serpapi_key)

    # 3) Summarize snippets
    context = summarizer.summarize_text(" ".join(snippets))

    # 4) Get answer from LLM
    answer = cached_get_llm_answer(context, user_input)
    if not answer:
        answer = snippets[0] if snippets else "Sorry, I couldn't find an answer."

    # 5) Save & display
    st.session_state.history.append({"user": user_input, "bot": answer})
    st.chat_message("assistant").write(answer)
