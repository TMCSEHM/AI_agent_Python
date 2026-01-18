import os
import argparse

from dotenv import load_dotenv
from google import genai

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    client = genai.Client(api_key=api_key)
    
    parser = argparse.ArgumentParser(description = "AI_agent")
    parser.add_argument("user_prompt", type = str, help = "User prompt")
    args = parser.parse_args()

    model = "gemini-2.5-flash"

    response = client.models.generate_content(
            model = model,
            contents = args.user_prompt,
            )
    
    # Verify usage_metadata is not None
    if not response.usage_metadata:
        raise RuntimeError("Failed API request: usage_metadata is missing")
    # Extract token counts
    prompt_tokens = response.usage_metadata.prompt_token_count
    candidate_tokens = response.usage_metadata.candidates_token_count

    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {candidate_tokens}")
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
