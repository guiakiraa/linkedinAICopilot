# LinkedIn AI Copilot 🤖

AI-powered assistant to help you create posts, analyze your profile, 
repurpose content, and plan your LinkedIn content strategy.

## Features
- Post generator with web research
- Profile analyzer
- README → LinkedIn post converter
- 30-day content calendar

## Tech Stack
- CrewAI · LangChain · OpenAI GPT-4o · Serper API · FastAPI · Streamlit

## Setup
```bash
cp .env.example .env
# Add your API keys to .env
pip install -r requirements.txt
streamlit run app.py
```