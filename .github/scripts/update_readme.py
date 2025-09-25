import datetime
import random
import openai
import os

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
    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompt = (
        "You're a brilliant but unstable AI Mad Scientist. "
        "Generate a one-sentence daily status update, like a chaotic lab log entry. "
        "Keep it clever, short, and on-brand. Don't mention 'OpenAI' or GPT. "
        "Example: 'Currently destabilizing traditional job markets using a job-hunting wormhole.'"
    )

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9,
        max_tokens=40,
    )

    return response["choices"][0]["message"]["content"].strip()

def generate_readme():
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    quote = random.choice(QUOTES)
    blurb = generate_blurb()

    project_list = "\n".join(f"- {p}" for p in PROJECTS)

    return f"""# 🧪 Welcome to Mad Scientist Mode

> {quote}

🧠 **AI Log Entry:** _{blurb}_

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
