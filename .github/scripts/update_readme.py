import os
import requests
from dotenv import load_dotenv

load_dotenv()

SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")
README_PATH = "README.md"

def get_shodan_results(query, tag, limit=1):
    try:
        url = f"https://api.shodan.io/shodan/host/search?key={SHODAN_API_KEY}&query={query}"
        response = requests.get(url, timeout=5)
        results = response.json().get("matches", [])
        lines = []
        for match in results[:limit]:
            ip = match.get("ip_str", "unknown")
            port = match.get("port", "???")
            org = match.get("org", "unknown")
            lines.append(f"{tag} `{ip}:{port}` _({org})_")
        return lines
    except Exception as e:
        return [f"{tag} ⚠️ Shodan error: {e}"]

def generate_shodan_section():
    lines = [
        "### 🛰️ Shodan Recon Feed",
    ]
    lines += get_shodan_results("port:554 has_screenshot:true", "👁️‍🗨️ Exposed Webcam:")
    lines += get_shodan_results("port:22 country:US", "💀 Port 22 (SSH) exposed:")
    lines += get_shodan_results("port:27017 _mongo", "🧩 Exposed MongoDB:")
    lines += [
        "🗺️ Global Threat Map Snapshot: [![ThreatMap](https://shodan.io/images/worldmap.png)](https://shodan.io)",
    ]
    return "\n".join(lines)

def update_readme():
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = "<!--START_SHODAN-->"
    end_marker = "<!--END_SHODAN-->"
    start = content.find(start_marker)
    end = content.find(end_marker)

    if start == -1 or end == -1:
        print("⚠️ Markers not found. Make sure <!--START_SHODAN--> and <!--END_SHODAN--> exist in README.md")
        return

    pre = content[:start + len(start_marker)]
    post = content[end:]

    injected = generate_shodan_section()
    updated = f"{pre}\n{injected}\n{post}"

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(updated)

    print("✅ README.md updated with Shodan data.")

if __name__ == "__main__":
    update_readme()
