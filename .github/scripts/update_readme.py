import os
import datetime
import requests
import json
import random
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

# === Load API keys ===
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

# === Live CoinGecko BTC Price ===
def get_bitcoin_price():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {"ids": "bitcoin", "vs_currencies": "usd"}
        response = requests.get(url, params=params)
        response.raise_for_status()
        price = response.json()["bitcoin"]["usd"]
        return f"${price:,.2f}"
    except Exception as e:
        print(f"[WARN] Could not fetch BTC price: {e}")
        return "$???"

bitcoin_price = get_bitcoin_price()
suspicious_ip = "86.140.121.31"

# === Load UFO Sighting ===
UFO_FEED_FILE = os.path.join(os.path.dirname(__file__), "../data/ufo_sightings.json")
ufo_sighting = "No recent UFO sightings found."
try:
    with open(UFO_FEED_FILE, "r") as f:
        sightings = json.load(f)
        if sightings:
            ufo_sighting = random.choice(sightings).strip()
except Exception as e:
    print(f"[WARN] Could not load UFO sightings: {e}")

# === Shodan Queries ===
def shodan_search(query):
    try:
        r = requests.get("https://api.shodan.io/shodan/host/search", params={
            "key": SHODAN_API_KEY,
            "query": query
        })
        data = r.json()
        if data.get("matches"):
            return data["matches"][0].get("ip_str", "N/A")
        return "No result"
    except Exception as e:
        return f"⚠️ Error: {e}"

exposed_camera = shodan_search("product:Hikvision")
exposed_ssh = shodan_search("port:22")
exposed_mongo = shodan_search("product:MongoDB")
exposed_rdp = shodan_search("port:3389")
exposed_scada = shodan_search("port:502 OR product:Modbus")
exposed_alarm = shodan_search("product:Hikvision OR port:34567")
exposed_lpr = shodan_search("ANPR OR LPR OR plate reader")

# === AI Recon Lore ===
recon_blurb = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a black-ops AI analyst creating threat blurbs using live cyber recon IPs."},
        {"role": "user", "content": f"""Write a dramatic 3-4 sentence blurb summarizing today's threat intelligence from Shodan:
- Hikvision cam at {exposed_camera}
- SSH exposed on {exposed_ssh}
- MongoDB exposed at {exposed_mongo}
- RDP open at {exposed_rdp}
- SCADA system at {exposed_scada}
- Alarm system at {exposed_alarm}
- License Plate Reader at {exposed_lpr}
Be vivid, concise, and theatrical."""}
    ]
).choices[0].message.content.strip()

# === Timestamp ===
now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

# === Final README Content ===
new_readme = f"""# 💪 Welcome to Mad Scientist Mode

> This README is alive. Check back tomorrow.

🧠 **AI Log Entry:**  
{ai_entry}

---

📡 **Live Feeds:**
- 🕵️ Suspicious IP of the day: `{suspicious_ip}`
- 💰 Bitcoin price: {bitcoin_price}
- 🛸 UFO Sighting of the Day: {ufo_sighting}

<!--START_SHODAN-->
### 🚁 Shodan Recon Feed
- 🔒 Security Camera Leak: `{exposed_camera}`
- 💠 Port 22 (SSH) exposed: `{exposed_ssh}`
- 🧬 Exposed MongoDB: `{exposed_mongo}`
- 🌍 Global Threat Map Snapshot: [🌍 Threat Map](https://www.shodan.io/search?query=map)

### 🔥 High-Risk Exposure of the Day (DEFCON ZONE)
- 🪟 RDP Exposure: `{exposed_rdp}`
- ⚡ SCADA/ICS System: `{exposed_scada}`
- 🚨 Security Alarm / Smart Home: `{exposed_alarm}`
- 🚱 License Plate Reader: `{exposed_lpr}`

---

🧠 **AI Threat Recon Lore:**  
{recon_blurb}
<!--END_SHODAN-->

🕒 **Last updated:** {now}

---

### 🧠 Current Focus
- ScottGPT: AI that pitches me  
- Secure RAG Playground  
- AutoJob Pipeline  
- Prompt Injection Showcase  
- BlackOps Labs site  
- VC-Style One-Pager PDF

🔁 _This README updates daily. Madness never sleeps._
"""

# === Write to top-level README.md ===
readme_path = Path(__file__).resolve().parents[2] / "README.md"
readme_path.write_text(new_readme, encoding="utf-8")
print(f"✅ README updated successfully at {readme_path}")
