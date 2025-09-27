#!/usr/bin/env python3
import datetime
import random
import os
import base64

# -----------------------
# Content buckets
# -----------------------
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

# Temporary fallback while OpenAI is offline
def generate_blurb():
    return "Stole electricity from a thunderstorm to power today’s idea."

# -----------------------
# ARG / clue payloads
# -----------------------
# Human-readable clue (harmless): "scottsteele:hire_me_for_ai_infra"
PLAIN_CLUE = "scottsteele:hire_me_for_ai_infra"

# Base64-encoded payload (hidden in HTML comment)
B64_CLUE = base64.b64encode(PLAIN_CLUE.encode("utf-8")).decode("ascii")

# Rot13 version (also hidden)
ROT13_CLUE = "".join(
    chr(((ord(c) - 97 + 13) % 26) + 97) if "a" <= c <= "z"
    else chr(((ord(c) - 65 + 13) % 26) + 65) if "A" <= c <= "Z"
    else c
    for c in PLAIN_CLUE
)

# Invisible zero-width joiner trick (optional; here we keep it as a visible comment)
VIRUS_COMMENT = (
    "<!-- scott-arg-begin\n"
    f"base64:{B64_CLUE}\n"
    f"rot13:{ROT13_CLUE}\n"
    "<!-- decode-instructions: base64 -> utf-8 OR rot13 -> ascii -->\n"
    "scott-arg-end -->"
)

# -----------------------
# README generator
# -----------------------
def generate_readme():
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    quote = random.choice(QUOTES)
    blurb = generate_blurb()
    project_list = "\n".join(f"- {p}" for p in PROJECTS)

    # A small visible hint for curious humans (optional)
    curious_hint = "_Tip for the curious: some lines contain encoded breadcrumbs. Decode wisely._"

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

## 🎚️ ScottGPT Personality Tuning Sliders
- 🔊 Boldness: **{random.randint(70,100)}/100**
- 🌀 Creativity: **{random.randint(75,100)}/100**
- 🕵️ Obscurity: **{random.randint(40,95)}/100**
- ⚙️ Hackiness: **{random.randint(60,100)}/100**
- 📡 Broadcast Level: **{random.randint(30,90)}/100**

{curious_hint}

{VIRUS_COMMENT}

**🔁 This README updates daily. Madness never sleeps.**
"""

# -----------------------
# Main: write README + daily snapshot
# -----------------------
if __name__ == "__main__":
    content = generate_readme()

    # Write main README
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

    # Ensure mad-log exists and save snapshot
    today_str = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    os.makedirs(".github/mad-log", exist_ok=True)
    snapshot_path = f".github/mad-log/{today_str}.md"
    with open(snapshot_path, "w", encoding="utf-8") as log_file:
        log_file.write(content)

    # Print info for CI logs / local testing
    print(f"Wrote README.md and snapshot -> {snapshot_path}")
