import os
import openai
import random
import datetime

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

def generate_blurb():
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You're ScottGPT, a slightly unhinged AI researcher who logs bizarre daily experiments.",
            },
            {
                "role": "user",
                "content": "Generate a one-sentence log of today’s most unhinged AI experiment, worthy of a mad scientist.",
            },
        ],
        temperature=0.9,
    )

    log = response.choices[0].message.content.strip()
    now = datetime.datetime.utcnow().strftime(" [%Y-%m-%d %H:%M:%S UTC]")
    return f"{log}{now}"

def generate_sliders():
    sliders = {
        "🧠 Boldness": random.randint(70, 100),
        "🎨 Creativity": random.randint(70, 100),
        "🕳️ Obscurity": random.randint(50, 100),
        "🧬 Hackiness": random.randint(60, 100),
        "📡 Broadcast Level": random.randint(60, 100),
    }

    return "\n".join(f"- {k}: {v}/100" for k, v in sliders.items())

def generate_readme():
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    quote = random.choice(QUOTES)
    blurb = generate_blurb()
    sliders = generate_sliders()

    project_list = "\n".join(f"- {p}" for p in PROJECTS)

    return f"""# 🧪 Welcome to Mad Scientist Mode

> {quote}

🧠 **AI Log Entry:** _{blurb}_

---

**🗓 Last updated:** {now}  
**🧠 Current Focus:**  
{project_list}

---

## 🧪 ScottGPT Mad Experiments Log

> {blurb}

### 🎛️ ScottGPT Personality Tuning Sliders
{sliders}

_Tip for the curious: some lines contain encoded breadcrumbs. Decode wisely._

`scott-arg-end -->`

---

**🔁 This README updates daily. Madness never sleeps.**
"""

if __name__ == "__main__":
    with open("README.md", "w") as f:
        f.write(generate_readme())
