import os
import random
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

README_PATH = "README.md"
AI_LOG_FILE = ".github/mad-log/ai_memory_log.md"

# === 🔮 EXPERIMENT LOGIC ===
EXPERIMENT_TEMPLATES = [
    "Today, I successfully trained an AI to compose symphonies using only the electromagnetic waves emitted by a microwave reheating leftover lasagna, resulting in a hauntingly delicious sonata I call \"The Mozzarella Crescendo.\"",
    "Today's most unhinged AI experiment involved training an algorithm to compose operatic arias by sampling the electromagnetic frequencies emitted from the synchronized opening of a thousand pickle jars under a full moon.",
    "I taught an AI to detect sarcasm in government press releases. It exploded.",
    "I trained an LLM exclusively on conspiracy theory forums and now it thinks *I'm* the simulation.",
    "Built a neural network that only responds to questions asked while holding a rubber duck. Accuracy shot up 400%."
]

def generate_ai_log():
    return random.choice(EXPERIMENT_TEMPLATES)

# === 🌐 LIVE FEED LOGIC ===
def get_suspicious_ip():
    return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"

def get_bitcoin_price():
    try:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd", timeout=5)
        data = response.json()
        return f"${data['bitcoin']['usd']:,}"
    except Exception as e:
        return f"Could not fetch BTC price: {e}"

def get_ufo_sighting():
    try:
        # Placeholder for actual UFO API or data source
        cities = ["Roswell, NM", "Rendlesham Forest, UK", "Phoenix, AZ", "Kecksburg, PA", "Shag Harbor, NS"]
        shapes = ["disc", "triangle", "cylinder", "orb", "boomerang"]
        return f"Reported {random.choice(shapes)} sighting near {random.choice(cities)}"
    except:
        return "No UFO data available today. The truth is out there."

# === 🧠 MEMORY SYSTEM ===
def write_memory_log(entry):
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    with open(AI_LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {entry}\n")

# === 📝 README UPDATER ===
def update_readme():
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    ai_entry = generate_ai_log()
    suspicious_ip = get_suspicious_ip()
    btc_price = get_bitcoin_price()
    ufo_sighting = get_ufo_sighting()

    write_memory_log(ai_entry)

    with open(README_PATH, "r") as f:
        lines = f.readlines()

    new_lines = []
    in_ai_log = False
    in_live_feed = False

    for line in lines:
        if line.strip().startswith("🧠 AI Log Entry"):
            in_ai_log = True
            new_lines.append(f"🧠 AI Log Entry: *{ai_entry}*\n")
        elif in_ai_log and line.strip() == "":
            in_ai_log = False
            new_lines.append(line)
        elif line.strip().startswith("🐍 Live Feeds"):
            in_live_feed = True
            new_lines.append("🐍 Live Feeds:\n")
            new_lines.append(f"- Suspicious IP of the day: `{suspicious_ip}`\n")
            new_lines.append(f"- Current BTC price: {btc_price}\n")
            new_lines.append(f"- 🛸 UFO Sighting of the Day: {ufo_sighting}\n")
        elif in_live_feed and line.strip() == "":
            in_live_feed = False
            new_lines.append(line)
        elif line.strip().startswith("🕒 Last updated"):
            new_lines.append(f"🕒 Last updated: {timestamp}\n")
        else:
            new_lines.append(line)

    with open(README_PATH, "w") as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    update_readme()
