import requests
from collections import defaultdict

owner = "amzn"
repo = "selling-partner-api-models"
branch = "main"
directory = "models/"

# 1. Get the latest commit tree SHA
commit = requests.get(
    f"https://api.github.com/repos/{owner}/{repo}/commits/{branch}"
).json()
tree_sha = commit["commit"]["tree"]["sha"]

# 2. Get the full recursive tree
tree = requests.get(
    f"https://api.github.com/repos/{owner}/{repo}/git/trees/{tree_sha}?recursive=1"
).json()

# 3. Filter for your subdirectory
entries = [item for item in tree["tree"] if item["path"].startswith(directory)]

grouped = defaultdict(list)
base_url = f"https://raw.githubusercontent.com/{owner}/{repo}/refs/heads/{branch}/"

for entry in entries:
    if entry["type"] == "blob" and entry["path"].endswith((".json", ".md")):
        parts = entry["path"].split("/")
        if len(parts) >= 2:
            model = parts[1].replace('-model', '').replace('-api', '').replace('-', '_')
            file_name = parts[-1]
            raw_link = base_url + entry["path"]
            if raw_link.endswith(".json"):
                grouped[model].append({"file_name": file_name, "raw_link": raw_link})

