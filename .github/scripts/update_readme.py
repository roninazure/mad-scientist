import os
import datetime
import random
import openai
import requests
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

QUOTES = [
    "I’m not here to compete. I’m here to rewire the entire arena.",
    "This README is alive. Check back tomorrow.",
    "Madness is doing the same thing twice and getting better results.",
    "I don’t chase opportunity. I auto-generate it.",
    "All systems nominal. Creativity abnormal.",
    "This README rewrites itself. So do I.",
    "Science is just magic with a command line.",
]

PROJECTS = [
    "ScottGPT: AI that pitches me",
    "Secure RAG Playground",
    "AutoJob Pipeline",
    "Prompt Injection Showcase",
    "Calgentik Labs site",
    "VC-Style One-Pager PDF",
]

def fetch_threat_domain():
    try:
        response = requests.get("https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt")
        domains = response.text.strip().splitlines()
        suspicious_ip = random.choice(domains[10:])  # skip header
        return f"Suspicious IP of the day: `{suspicious_ip}`"
    except Exception as e:
        return f"Could not fetch suspicious IP: {e}"

def fetch_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        price = data['bpi']['USD']['rate']
        return f"Bitcoin price: ${price}"
    except Exception as e:
        return f"Could not fetch BTC price: {e}"

def generate_blurb():
    try:
        client = openai.OpenAI(api_key=openai.api_key)
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You're ScottGPT, a slightly unhinged AI researcher who logs bizarre daily experiments."},
                {"role": "user", "content": "Generate a one-sentence log of today’s most unhinged AI experiment, worthy of a mad scientist."},
            ],
            temperature=0.9,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Experiment log failed: {e}"

def generate_readme():
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    quote = random.choice(QUOTES)
    blurb = generate_blurb()
    threat = fetch_threat_domain()
    btc = fetch_bitcoin_price()
    project_list = "\n".join(f"- {p}" for p in PROJECTS)

    return f"""# 🧪 Welcome to Mad Scientist Mode

> {quote}

🧠 **AI Log Entry:** _{blurb}_

📡 **Live Feeds:**
- {threat}
- {btc}

---

**🗓 Last updated:** {now}  
**🧠 Current Focus:**  
{project_list}

**🔁 This README updates daily. Madness never sleeps.**

---
"""

if __name__ == "__main__":
    with open("README.md", "w") as f:
        f.write(generate_readme())
