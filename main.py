from fastapi import FastAPI
from pydantic import BaseModel
import requests
import wikipedia
import re  # 👈 Added for flexible city name extraction
import os

app = FastAPI()

class QueryRequest(BaseModel):
    question: str


# def get_weather(city: str):
#     api_key = os.getenv("OPENWEATHER_API_KEY")
    
def extract_city(query: str):
    # Try to extract city name from query using regex patterns
    match = re.search(r"in\s+([a-zA-Z\s]+)", query)
    if match:
        city = match.group(1).strip().replace("today", "").replace("weather", "").strip()
        return city
    return query.strip()
    
# ✅ WEATHER FUNCTION
def get_weather(query: str):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    city = extract_city(query) 
    if not api_key:
        return "API key not found. Please set it in environment variables."

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        return f"The weather in {city.title()} is {desc} with {temp}°C temperature."
    elif response.status_code == 404:
        return f"Sorry, I couldn’t find weather information for '{city}'."
    else:
        return f"Weather API error: {response.status_code}"


# ✅ WIKIPEDIA FUNCTION
def get_wikipedia_summary(query: str):
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Multiple possible results found: {e.options[:3]}"
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn’t find any information on that topic."
    except Exception as e:
        return f"Wikipedia lookup failed: {str(e)}"


@app.post("/ask")
async def ask_question(request: QueryRequest):
    question = request.question.lower().strip()
    reasoning = ""
    answer = ""

    # ✅ Detect if it's a weather question
    if "weather" in question or "temperature" in question:
        reasoning = "Detected a weather-related question."

        # Try to extract city name (using regex and keywords)
        match = re.search(r"weather\s+(in|of)?\s*([a-zA-Z\s]+)", question)
        if match:
            city = match.group(2).strip()
        else:
            # fallback: take last word if no "in" found
            words = question.split()
            city = words[-1] if len(words) > 1 else ""

        if city:
            answer = get_weather(question)
        else:
            answer = "Please specify a city name to get weather information."

    # ✅ Detect factual questions
    elif any(word in question for word in ["who", "when", "where", "capital", "what is", "founded", "invented"]):
        reasoning = "Detected a factual question. Fetching summary from Wikipedia."
        answer = get_wikipedia_summary(question)

    # ✅ Unsupported question
    else:
        reasoning = "Question type not recognized. Please ask about weather or facts."
        answer = "I can currently answer questions about the weather or general facts."

    return {"reasoning": reasoning, "answer": answer}


