# 🌐 Universal NLP + Web Search + LLM Chatbot

A **Streamlit**‑based chat application that combines lightweight NLP, real‑time internet search, and a local open‑source LLM to deliver up‑to‑date answers in a friendly chat UI.

---

## 🎯 Project Overview

This repository implements a modular “GenAI Lab” toolkit featuring:

1. **Natural Language Understanding**  
   – Extracts keywords/entities from your question using **spaCy**.  
2. **Real‑Time Web Search**  
   – Queries Google via **SerpAPI** to fetch fresh snippets.  
3. **Local LLM Inference**  
   – Runs a quantized **LLaMA** model (`llama-cpp-python`) on‑device.  
4. **Chat UI & Memory**  
   – Persistent chat history with Streamlit’s built‑in `st.chat_message` & `st.chat_input`.  
5. **Caching & Performance**  
   – Caches search results and model outputs to minimize waiting.  

Use this as your **freelance GenAI playground**, demoing everything from AI chatbots to analytics dashboards and more.

---

## 🚀 Features

- **Keyword / Intent Extraction**  
- **Dynamic Google Search** (via SerpAPI)  
- **Context Summarization** (simple truncation + optional pipeline)  
- **Local LLaMA Chat** (no external LLM calls)  
- **Conversation Memory** (in‑session)  
- **Streamlit Chat UI** for interactive Q&A  
- **Result & Model Caching** for instant repeat queries  
- **Modular Structure**—easily swap in new data sources or LLMs  

---

## 📁 Repository Structure

genai_lab/
├── app.py
├── requirements.txt
├── serpapi.txt # Your SerpAPI key (do NOT commit)
├── .gitignore
├── README.md
├── llama_model/
│ └── llama-2-7b.Q4_K_M.gguf
├── modules/
│ ├── nlp_utils.py
│ ├── web_search.py
│ ├── llm_utils.py
│ |── summarizer.py
│ ├── memory.py
│ |── open_source_data.py
│ └── translator.py
└── .github/
└── workflows/
└── ci.yml

---

## 🛠️ Installation

1. **Clone** this repo:
   ```bash
   git clone https://github.com/yourusername/genai_lab.git
   cd genai_lab
Create & activate a Python virtual environment:

python -m venv venv
. venv/Scripts/activate    # Windows
# source venv/bin/activate # macOS/Linux
Install dependencies:

pip install -r requirements.txt
python -m spacy download en_core_web_sm
Add your SerpAPI key:

echo "YOUR_SERPAPI_KEY" > serpapi.txt
Download a quantized LLaMA model (Q4_K_M) to: llama_model/llama-2-7b.Q4_K_M.gguf

---


## ▶️ Usage

streamlit run app.py
Open your browser at http://localhost:8501

Chat naturally: the bot will extract keywords, search online, and answer via LLaMA.

---


## ⚙️ Configuration
Edit top of app.py to adjust:

Number of web snippets (num_results)

LLaMA model path & max_tokens

Cache TTLs in @st.cache_data decorators

---


## 🧪 CI/CD Pipeline
We use GitHub Actions to:

-Run flake8 lint

-Install dependencies & spaCy model

-Smoke‑test import of each module

-(Optional) Deploy to Streamlit Cloud

---


## 🚫 Security & Best Practices
-Do not commit your serpapi.txt or any API keys.

-Add serpapi.txt and llama_model/ to .gitignore.

---


## 🤝 Contributing
-Fork the repo

-Create a feature branch (git checkout -b feature/foo)

-Commit your changes & push

-Open a Pull Request

---


## 📄 License
-This project is licensed under the MIT License. See LICENSE for details.

---


### How to Enable CI/CD

1. Push this repo to GitHub in a public or private repo.  
2. Enable **Actions** tab—you’ll see the “CI” workflow run on each push/PR.  
3. (Optional) Link your Streamlit Cloud account in the `deploy` step.

---

That should give you a **self‑documented repo** with **automated testing** and optional **deployment**. Let me know if you’d like to customize further!







