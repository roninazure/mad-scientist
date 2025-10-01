import os, requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()  # LOAD ENV

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")
README_PATH = os.path.join(os.path.dirname(__file__), "../../README.md")

# === AI Log Entry ===
def get_openai_log_entry():
    try:
        resp = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-4",
                "messages": [
                    {"role": "system", "content": "You are an AI log generator for a Mad Scientist GitHub profile. Write a 1–2 sentence log entry that’s brilliant, absurd, and creative."},
                    {"role": "user", "content": "Generate today’s AI log entry."}
                ],
                "temperature": 1.2,
            },
            timeout=8,
        )
        return f"🧠 **AI Log Entry:** {resp.json()['choices'][0]['message']['content'].strip()}"
    except Exception as e:
        return f"🧠 **AI Log Entry:** ⚠️ Failed to fetch: {e}"

def get_bitcoin_price():
    try:
        r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd", timeout=5)
        price = r.json()["bitcoin"]["usd"]
        return f"💰 Bitcoin price: ${price:,.2f}"
    except Exception as e:
        return f"💰 Bitcoin error: {e}"

def get_ufo_sighting():
    return "🛸 UFO Sighting of the Day: Teardrop-shaped craft spotted over rural Oregon; chased by two F-16s, disappeared into low cloud cover."

def get_suspicious_ip():
    return "🕵️ Suspicious IP of the day: `86.140.121.31`"

def get_shodan_results(query, tag, limit=1):
    try:
        url = f"https://api.shodan.io/shodan/host/search?key={SHODAN_API_KEY}&query={query}"
        r = requests.get(url, timeout=6)
        if r.status_code != 200:
            return [f"{tag} ⚠️ Shodan API error: {r.status_code} {r.reason}"]
        results = r.json().get("matches", [])
        if not results:
            return [f"{tag} 💤 No results found."]
        lines = []
        for m in results[:limit]:
            ip = m.get("ip_str", "unknown")
            port = m.get("port", "???")
            org = m.get("org", "unknown")
            lines.append(f"{tag} `{ip}:{port}` _({org})_")
        return lines
    except Exception as e:
        return [f"{tag} ⚠️ Shodan exception: {e}"]

def generate_shodan_section():
    lines = ["### 🛰️ Shodan Recon Feed"]
    lines += get_shodan_results("port:554 has_screenshot:true", "👁️‍🗨️ Exposed Webcam:")
    lines += get_shodan_results("port:22 country:US", "💀 Port 22 (SSH) exposed:")
    lines += get_shodan_results("port:27017 _mongo", "🧩 Exposed MongoDB:")
    lines.append("🗺️ Global Threat Map: [View on Shodan](https://www.shodan.io/explore/map)")
    return "\n".join(lines)

def update_readme():
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = "<!--START_SHODAN-->"
    end_marker = "<!--END_SHODAN-->"
    start = content.find(start_marker)
    end = content.find(end_marker)
    if start == -1 or end == -1:
        print("⚠️ Markers not found.")
        return

    pre = content[:start + len(start_marker)]
    post = content[end:]

    # Build sections
    ai_log = get_openai_log_entry()
    btc = get_bitcoin_price()
    ufo = get_ufo_sighting()
    sus_ip = get_suspicious_ip()
    shodan = generate_shodan_section()
    timestamp = f"🕒 **Last updated:** {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC"

    live_feeds_block = f"""
{ai_log}

📡 **Live Feeds:**
- {sus_ip}
- {btc}
- {ufo}
"""

    updated = f"{live_feeds_block}\n{pre}\n{shodan}\n{post}\n\n{timestamp}"

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(updated)

    print("✅ README.md updated with live OpenAI + Bitcoin + Shodan intel.")

if __name__ == "__main__":
    update_readme()
