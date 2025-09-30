import requests
import random
import datetime
import feedparser

README_PATH = "README.md"

def get_ai_log_entry():
    prompts = [
        "trained an AI to compose symphonies using only the electromagnetic waves emitted by a microwave reheating leftover lasagna",
        "taught an AI to detect sarcasm in legal contracts with 97% accuracy",
        "developed a neural net that dreams about solving quantum physics with crayons",
        "trained a transformer to simulate the behavior of a squirrel during a caffeine overdose",
        "trained an AI to write obituaries for obsolete technology in iambic pentameter",
        "developed a GAN that hallucinates future startup ideas based on pizza toppings",
    ]
    return random.choice(prompts)

def get_suspicious_ip():
    octets = [str(random.randint(1, 255)) for _ in range(4)]
    return ".".join(octets)

def get_bitcoin_price():
    try:
        response = requests.get(
            "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd",
            timeout=5
        )
        data = response.json()
        return f"${data['bitcoin']['usd']:,}"
    except Exception as e:
        return f"Could not fetch BTC price: {e}"

def get_ufo_sighting():
    try:
        feed = feedparser.parse("https://nuforc.org/webreports/rss.xml")
        if feed.entries:
            entry = random.choice(feed.entries[:5])  # Take from most recent 5
            title = entry.title
            date = entry.published
            return f"🛸 UFO sighting: *{title}* ({date})"
        return "🛸 No recent UFO sightings found."
    except Exception as e:
        return f"🛸 Error fetching UFO feed: {e}"

def build_readme():
    ai_log = get_ai_log_entry()
    suspicious_ip = get_suspicious_ip()
    btc_price = get_bitcoin_price()
    ufo_entry = get_ufo_sighting()
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    content = f"""# 🧪 Welcome to Mad Scientist Mode

> This README is alive. Check back tomorrow.

🧠 **AI Log Entry**: Today, I {ai_log}, resulting in a hauntingly delicious sonata I call *The Mozzarella Crescendo.*

🛰️ **Live Feeds**:
- Suspicious IP of the day: `{suspicious_ip}`
- 💰 Bitcoin price: {btc_price}
- {ufo_entry}

📅 **Last updated**: {now}

🧪 **Current Focus**:
- ScottGPT: AI that pitches me
- Secure RAG Playground
- AutoJob Pipeline
- Prompt Injection Showcase
- Calgentik Labs site
- VC-Style One-Pager PDF

> _This README updates daily. Madness never sleeps._
"""

    with open(README_PATH, "w") as f:
        f.write(content)

if __name__ == "__main__":
    build_readme()
