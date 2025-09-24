import datetime
import random

QUOTES = [
    "I’m not here to compete. I’m here to rewire the entire arena.",
    "This README is alive. Check back tomorrow.",
    "Madness is doing the same thing twice and getting better results.",
    "I don’t chase opportunity. I auto-generate it.",
    "All systems nominal. Creativity abnormal.",
    "This README rewrites itself. So do I.",
    "Science is just magic with a command line.",
]

def generate_readme():
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    quote = random.choice(QUOTES)

    return f"""# 🧪 Welcome to Mad Scientist Mode

> {quote}

---

**🗓 Last updated:** {now}  
**🧠 Current Focus:**  
- ScottGPT: AI that pitches me  
- Secure RAG Playground  
- AutoJob Pipeline  
- Prompt Injection Showcase  
- Calgentik Labs site  
- VC-Style One-Pager PDF  

**🔁 This README updates daily. Madness never sleeps.**

---
"""

if __name__ == "__main__":
    with open("README.md", "w") as f:
        f.write(generate_readme())
