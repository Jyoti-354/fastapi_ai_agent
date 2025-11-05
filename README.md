# FastAPI AI Agent

A backend service built with **FastAPI** that demonstrates integration of AI reasoning with external API tools like **weather** and **Wikipedia lookups**. 


## How the Solution Works

1. The backend exposes a single endpoint:
   

**Request Example:**
```json
{
  "question": "What is the weather in mumbai today?"
}

**Response Example:**
{
"reasoning": "Detected a weather-related question?",
"answer": "the weather in mumbai is haze with 27.99 degree celcius temperature."
}

**APIs Used**

| API                         | Purpose                                   |
| --------------------------- | ----------------------------------------- |
| OpenWeatherMap API          | Get real-time weather data                |
| Wikipedia API               | Get factual summaries for questions       |


**How to Run**

Clone the repository
git clone https://github.com/Jyoti-354/fastapi_ai_agent.git
cd fastapi_ai_agent

**Create a virtual environment**
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows

**Install dependencies**
pip install -r requirements.txt

**main.py**
OPENWEATHER_API_KEY=your_openweathermap_api_key

**Run the FastAPI server**
uvicorn main:app --reload

**Test the API**
POST a request to http://127.0.0.1:8000/docs

click on ask/ endpoint
click on try it now
write your question
click on excute you will see your answer


**Example**:
{
  "question": "What's the weather in Mumbai today?"
}
Response Example:
{
"reasoning": "Detected a weather-related question?",
"answer": "the weather in mumbai is haze with 27.99 degree celcius temperature."
}

