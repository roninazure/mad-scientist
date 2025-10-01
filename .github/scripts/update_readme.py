
import os
from dotenv import load_dotenv
load_dotenv()
import datetime
from openai import OpenAI

# === Setup Clients ===
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# === Generate AI Log Entry ===
ai_log = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You're a mad scientist AI generating daily absurd research logs."},
        {"role": "user", "content": "Give me today's log entry."},
    ],
)
ai_entry = ai_log.choices[0].message.content.strip()

# === Sample Live Feeds ===
suspicious_ip = "86.140.121.31"
bitcoin_price = "$114,319.00"
ufo_sighting = "Teardrop-shaped craft spotted over rural Oregon; chased by two F-16s, disappeared into low cloud cover."

# === Build New README ===
now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
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
👁️‍🗨️ Exposed Webcam: ⚠️ Shodan API key missing or unauthorized
💀 Port 22 (SSH) exposed: ⚠️ Shodan API key missing or unauthorized
🧩 Exposed MongoDB: ⚠️ Shodan API key missing or unauthorized
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
