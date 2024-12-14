import sys
import openai
import os

def main():
    if len(sys.argv) < 2:
        print("No diff provided.")
        sys.exit(1)

    diff = sys.argv[1]

    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompt = f"""
    Generate a detailed and well-formatted changelog entry based on the following Git diff. The changelog should include a summary of changes, affected areas, and any relevant details. Format the output in Markdown.
    
    {diff}
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system",
                 "content": "You are a helpful assistant that generates changelog entries based on Git diffs."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=500
        )

        changelog_entry = response.choices[0].message['content'].strip()
        print(changelog_entry)

    except Exception as e:
        print(f"Error generating changelog: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
