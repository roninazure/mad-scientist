import os
import openai
import requests
import random
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_ai_log():
    prompt = (
        "Give me a fictional AI experiment of the day, written like a mad scientist log entry. "
        "Be bizarre, creative, and short enough for a README."
    )
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a mad AI scientist."},
            {"role": "user", "content": prompt},
        ],
        temperature=1.1,
        max_tokens=100,
    )
    return response.choices[0].message.content.strip()

def get_suspicious_ip():
    # Dummy suspicious IP generator
    return f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

def get_bitcoin_price():
    try:
        response = requests.get(
            "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd", timeout=5
        )
        data = response.json()
        return f"${data['bitcoin']['usd']:,}"
    except Exception as e:
        return f"Could not fetch BTC price: {e}"

def get_ufo_sighting():
    # Simulated UFO feed (or eventually hook to real UFO sightings API)
    fake_sightings = [
        "3 glowing orbs over Nevada desert",
        "Disc-shaped object seen over Tokyo Tower",
        "Fast-moving lights zigzagging above the Atlantic Ocean",
        "Silent triangle over rural Iowa farm",
        "Hovering saucer with blinking lights in São Paulo"
    ]
    return random.choice(fake_sightings)

def update_readme():
    ai_log = get_ai_log()
    suspicious_ip = get_suspicious_ip()
    btc_price = get_bitcoin_price()
    ufo = get_ufo_sighting()
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    readme = f"""# 🧪 Welcome to Mad Scientist Mode

This README is alive. Check back tomorrow.

🧠 **AI Log Entry**: {ai_log}

🦴 **Live Feeds**:
- Suspicious IP of the day: `{suspicious_ip}`
- 🟠 Bitcoin price (via CoinGecko): **{btc_price}**
- 🛸 UFO Sighting of the Day: *{ufo}*

🗓️ **Last updated**: {timestamp}

📡 **Current Focus:**
- ScottGPT: AI that pitches me
- Secure RAG Playground
- AutoJob Pipeline
- Prompt Injection Showcase
- Calgentik Labs site
- VC-Style One-Pager PDF

> This README updates daily. Madness never sleeps.
"""

    with open("README.md", "w") as f:
        f.write(readme)

if __name__ == "__main__":
    update_readme()
