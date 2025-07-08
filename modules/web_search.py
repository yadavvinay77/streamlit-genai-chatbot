import requests
import streamlit as st


@st.cache_data(show_spinner=False)
def search_web(keywords, api_key, num_results=5):
    """
    Query SerpAPI Google engine and return list of snippets.
    """
    query = " ".join(keywords)
    params = {"q": query, "api_key": api_key, "engine": "google", "num": num_results}
    res = requests.get("https://serpapi.com/search", params=params, timeout=10)
    if res.status_code != 200:
        return [f"Search failed: {res.status_code}"]
    data = res.json().get("organic_results", [])
    return [item.get("snippet", "") for item in data]
