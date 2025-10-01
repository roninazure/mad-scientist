import os
import datetime
import requests
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
SHODAN_API_KEY = os.environ.get("SHODAN_API_KEY")

# === AI Log Entry ===
ai_log = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You're a mad scientist AI generating daily absurd research logs."},
        {"role": "user", "content": "Give me today's log entry."}
    ]
)
ai_entry = ai_log.choices[0].message.content.strip()

# === Live Feeds (fun placeholders) ===
suspicious_ip = "86.140.121.31"
bitcoin_price = "$114,319.00"
ufo_sighting = "Teardrop-shaped craft spotted over rural Oregon; chased by two F-16s, disappeared into low cloud cover."

# === Shodan Live API Feeds ===
def shodan_search(query):
    try:
        r = requests.get(f"https://api.shodan.io/shodan/host/search", params={
            "key": SHODAN_API_KEY,
            "query": query
        })
        data = r.json()
        if data.get("matches"):
            ip_str = data["matches"][0].get("ip_str", "N/A")
            return ip_str
        return "No result"
    except Exception as e:
        return f"⚠️ Error: {e}"

exposed_webcam = shodan_search("has_screenshot:true")
exposed_mongodb = shodan_search("product:MongoDB")
exposed_port22 = shodan_search("port:22")

# === Timestamp ===
now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

# === Final README Content ===
new_readme = f"""
🧠 **AI Log Entry:** {ai_entry}

📡 **Live Feeds:**
- 🕵️ Suspicious IP of the day: `{suspicious_ip}`
- 💰 Bitcoin price: {bitcoin_price}
- 🛸 UFO Sighting of the Day: {ufo_sighting}

# 🧪 Welcome to Mad Scientist Mode

> This README is alive. Check back tomorrow.

<!--START_SHODAN-->
### 🛰️ Shodan Recon Feed
👁️‍🗨️ Exposed Webcam: `{exposed_webcam}`
💀 Port 22 (SSH) exposed: `{exposed_port22}`
🧩 Exposed MongoDB: `{exposed_mongodb}`
🗺️ Global Threat Map Snapshot: [![ThreatMap](https://shodan.io/images/worldmap.png)](https://www.shodan.io/search?query=map)
<!--END_SHODAN-->

🕒 **Last updated:** {now}

### 🧠 Current Focus
- ScottGPT: AI that pitches me
- Secure RAG Playground
- AutoJob Pipeline
- Prompt Injection Showcase
- BlackOps Labs site
- VC-Style One-Pager PDF

🔁 _This README updates daily. Madness never sleeps._
"""

# === Write to README.md ===
with open("README.md", "w") as f:
    f.write(new_readme)

print("✅ README updated successfully.")
