# AI Agent Backend (FastAPI)

### 🚀 Overview
This project demonstrates an intelligent backend that integrates **LLM reasoning (GPT)** with **external APIs (OpenWeatherMap)** to simulate a decision-making AI agent.

### 🧠 How It Works
- The `/ask` endpoint receives a user query.
- The system decides whether to:
  - Use GPT directly, or
  - Fetch real data from OpenWeatherMap.
- The agent then combines reasoning and factual data to respond.

### 🛠️ Tech Stack
- FastAPI
- OpenAI GPT API
- OpenWeatherMap API
- Python-dotenv for environment variables

### ▶️ Run Locally
```bash
pip install -r requirements.txt
uvicorn main:app --reload
