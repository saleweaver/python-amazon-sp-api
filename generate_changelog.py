import sys
import os
import openai
from sp_api.__version__ import __version__


openai.api_key = os.getenv("OPENAI_API_KEY")

if len(sys.argv) < 2:
    print("No diff file provided.")
    sys.exit(1)

diff_file = sys.argv[1]
with open(diff_file, 'r') as f:
    diff = f.read()

prompt = f"""
You are a helpful assistant who generates changelog entries for the python-amazon-sp-api, a wrapper to access Amazon's Selling Partner API with an easy-to-use interface. This tool helps developers and businesses connect seamlessly with Amazon's vast marketplace, enabling powerful automations and data management.
This is a growing changelog entry for the project. Only add changes that are relevant to the end-users, such as new features, changes to existing features, and bug fixes. Categorize and group changes between internal and relevant to the project..
The current version is {__version__}. Add this to the Changelog header. Never include dates or release status in the changelog entry.

Given the following git diff, generate a concise, well-formatted Markdown changelog entry. Add mermaid diagrams to showcase changes. Do not enclose the resulting markdown in backticks.:

```diff
{diff}
```
"""

response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that generates changelog entries."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.3,
    max_tokens=750
)

changelog_entry = response.choices[0].message.content.strip()
print(changelog_entry)
with open('changelog_entry.md', 'w') as out_file:
    out_file.write(changelog_entry.strip('`') + "\n")
