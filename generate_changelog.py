import sys
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

if len(sys.argv) < 2:
    print("No diff file provided.")
    sys.exit(1)

diff_file = sys.argv[1]
with open(diff_file, 'r') as f:
    diff = f.read()

prompt = f"""
You are a helpful assistant who generates changelog entries.
Given the following git diff, generate a concise, well-formatted Markdown changelog entry:

```diff
{diff}
```
"""

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that generates changelog entries."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.3,
    max_tokens=500
)
changelog_entry = response.choices[0].message['content'].strip()
print(changelog_entry)
with open('changelog_entry.md', 'w') as out_file:
    out_file.write(changelog_entry + "\n")