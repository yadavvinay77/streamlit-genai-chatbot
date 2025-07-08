# 🌐 Universal NLP + Web Search + LLM Chatbot

A modular Streamlit-based GenAI chatbot that blends lightweight NLP, real-time web search, and local LLaMA model inference to generate up-to-date, context-aware responses in a conversational UI.

---

## 🎯 Project Overview

This repository is a GenAI Lab sandbox, ideal for freelance demonstrations or AI prototyping. It integrates:

- **Natural Language Understanding**: Entity & keyword extraction via spaCy.
- **Real-Time Web Search**: Dynamic internet search using SerpAPI (Google).
- **Local LLM Chat**: Quantized LLaMA-2 model running offline via `llama-cpp-python`.
- **Interactive UI**: Built using Streamlit's native `st.chat_message` API.
- **Session Memory & Caching**: Retains conversation context and caches responses.

Use this project to explore AI chatbots, NLP pipelines, open-source LLM integration, or build client-ready GenAI demos.

---

## 🚀 Features

✅ Keyword & Intent Extraction (spaCy)  
✅ Dynamic Google Search (via SerpAPI)  
✅ Text Summarization of Web Contexts  
✅ Local LLaMA Chat (no OpenAI or cloud calls)  
✅ Session-Aware Chat Memory  
✅ Interactive Streamlit Chat UI  
✅ Fast Repeat Queries (using `st.cache_data`)  
✅ Modular Python Architecture  

---

## 📁 Project Structure

```
genai_lab/
├── app.py                  # Main Streamlit app
├── requirements.txt        # Python dependencies
├── serpapi.txt             # SerpAPI key (excluded from Git)
├── .gitignore              # Ignore secrets and model files
├── README.md               # Documentation
├── llama_model/            # Local quantized LLaMA model
│   └── llama-2-7b.Q4_K_M.gguf
├── modules/                # All backend components
│   ├── nlp_utils.py        # spaCy keyword/entity extractor
│   ├── web_search.py       # Google search via SerpAPI
│   ├── summarizer.py       # Web result summarizer
│   ├── llm_utils.py        # LLaMA-based chat wrapper
│   ├── memory.py           # In-session memory functions
│   ├── translator.py       # Translation helper (optional)
│   └── open_source_data.py # Optional open datasets
└── .github/
    └── workflows/
        └── ci.yml          # GitHub Actions CI pipeline
```

---

## 🛠️ Installation

### 1. Clone the repo
```bash
git clone https://github.com/yadavvinay77/streamlit-genai-chatbot.git
cd streamlit-genai-chatbot
```

### 2. Create & activate virtual environment

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 4. Add SerpAPI Key
Save your key to a file:
```bash
echo "YOUR_SERPAPI_KEY" > serpapi.txt
```

### 5. Add Quantized LLaMA Model
Download `llama-2-7b.Q4_K_M.gguf` into:
```
llama_model/llama-2-7b.Q4_K_M.gguf
```

---

## ▶️ Usage

Start the app:
```bash
streamlit run app.py
```

Visit: [http://localhost:8501](http://localhost:8501)

Type a natural question. The bot will:
- Extract keywords
- Search online
- Summarize context
- Answer with the LLaMA model

---

## ⚙️ Configuration

You can customize the following in `app.py`:

| Parameter         | Purpose                          |
|------------------|----------------------------------|
| `num_results`     | Number of web snippets to fetch |
| `max_tokens`      | Max tokens in LLaMA response     |
| `cache_ttl`       | Time-to-live for search cache    |
| `llama_model_path`| Model file path on disk          |

---

## 🧪 CI/CD Pipeline

GitHub Actions runs automated checks on push/PR:

✅ Python Linting with `flake8`  
✅ Imports & syntax test for all modules  
✅ Dependency setup and spaCy model download  
🔄 Optional deployment to Streamlit Cloud  

---

## 🚫 Security Best Practices

- ✅ `serpapi.txt` and `llama_model/` are **excluded** via `.gitignore`
- ❌ Never commit API keys to GitHub
- 🔒 Use environment variables or secrets for cloud deployment

---

## 🤝 Contributing

1. Fork this repo  
2. Create a branch: `git checkout -b feature/your-feature`  
3. Commit your changes  
4. Push and open a pull request 🎉  

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).  
Use, modify, and share freely with attribution.

---

## 🌍 How to Enable CI/CD

1. Push your code to GitHub (public or private)
2. Go to the **Actions** tab and enable workflows
3. CI will now trigger on each `git push` or PR
4. (Optional) Connect to [Streamlit Cloud](https://streamlit.io/cloud) for free hosting

---

**Need Help?** Raise an issue or start a discussion in the repo.
