# 🤖 LinkedIn AI Copilot

> Multi-agent AI system to generate posts, analyze profiles and repurpose content for LinkedIn.

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat&logo=python)
![CrewAI](https://img.shields.io/badge/CrewAI-multi--agent-purple?style=flat)
![LangChain](https://img.shields.io/badge/LangChain-chains-green?style=flat)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-black?style=flat&logo=openai)
![FastAPI](https://img.shields.io/badge/FastAPI-API-teal?style=flat&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?style=flat&logo=streamlit)

---

## 📽️ Demo

![demo](assets/demo.gif)

---

## ✨ Features

- **✍️ Post generator** — Describe a topic, the agents research the web and write an engaging post
- **🔍 Profile analyzer** — Paste your profile text and get concrete improvement suggestions  
- **♻️ README → Post** — Transform a GitHub README into a LinkedIn-ready post

---

## 🏗️ Architecture
```
User Input
    │
    ▼
┌─────────────────────┐
│   Researcher Agent  │ → Searches the web (Serper API) for trends and references
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    Writer Agent     │ → Writes the post based on research
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Reviewer Agent    │ → Reviews tone, hook and CTA
└──────────┬──────────┘
           │
           ▼
      Final Output

── Profile Analyzer and Repurpose use LangChain Chains (single LLM call)
── Post Generator uses CrewAI (3 agents in sequence)
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Multi-agent orchestration | CrewAI |
| Chains & prompt templates | LangChain |
| LLM | OpenAI GPT-4o-mini |
| Web search | Serper API |
| Backend | FastAPI |
| Interface | Streamlit |

---

## ⚙️ Setup

### 1. Clone the repository
```bash
git clone https://github.com/seu-usuario/linkedin-ai-copilot.git
cd linkedin-ai-copilot
```

### 2. Create virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
```bash
cp .env.example .env
```

Edit `.env` with your API keys:
```
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key
```

> Get your Serper API key at [serper.dev](https://serper.dev) — free tier available.

---

## 🚀 Running

### Streamlit interface
```bash
streamlit run app.py
```
Access: `http://localhost:8501`

### FastAPI
```bash
uvicorn api:app --reload
```
Access: `http://localhost:8000/docs`

---

## 📁 Project Structure
```
linkedin-ai-copilot/
│
├── src/
│   ├── agents/
│   │   ├── researcher.py    # searches web for references
│   │   ├── writer.py        # writes the post
│   │   └── reviewer.py      # reviews and refines
│   │
│   ├── chains/
│   │   ├── profile_chain.py    # profile analysis
│   │   └── repurpose_chain.py  # README → post
│   │
│   ├── tools/
│   │   └── search_tool.py   # Serper API wrapper
│   │
│   └── crew.py              # agent orchestration
│
├── app.py                   # Streamlit interface
├── api.py                   # FastAPI
├── assets/
│   └── demo.gif             # demo recording
└── README.md
```

---

## 💡 Technical Decisions

**Why CrewAI for post generation?**  
The task involves research + writing + review — three distinct responsibilities that benefit from specialized agents with different goals and backstories.

**Why LangChain Chains for profile and repurpose?**  
These are direct input → output transformations. A single LLM call with a well-structured prompt is enough — no need for multi-agent overhead.

**Why Serper API instead of a static dataset?**  
Real-time web search ensures the content is always based on current trends, not outdated references.