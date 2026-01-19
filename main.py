import os
import argparse
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from config import MAX_ITERS
from prompts import system_prompt
from call_function import available_functions, call_function

def main():
    parser = argparse.ArgumentParser(description = "AI Code Assistant")
    parser.add_argument("user_prompt", type = str, help = "Prompt to send to Gemni")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")
    
    for _ in range(MAX_ITERS):
        try:
            done = generate_content(client, messages, args.verbose)
            if done:
                return
        except Exception as e:
            print(f"Error in generate_content: {e}")
    print(f"Error: Agent reached maximum iteration limit ({MAX_ITERS}).")
    sys.exit(1)


def generate_content(client, messages, verbose):
    g_model = "gemini-2.5-flash"
    response = client.models.generate_content(
            model = g_model,
            contents = messages,
            config = types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt,
                ),
            )
    # Verify usage_metadata is not None
    if not response.usage_metadata:
        raise RuntimeError("Gemini API response appears to be malformed")
    # Extract token counts
    prompt_tokens = response.usage_metadata.prompt_token_count
    candidate_tokens = response.usage_metadata.candidates_token_count

    if verbose:
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {candidate_tokens}")
    
    # Add the model's response to history immediately
    if response.candidates:
        for candidate in response.candidates:
            if candidate.content:
                messages.append(candidate.content)
    # Check if the model is finished
    if not response.function_calls:
        print("\nFinal Response:")
        print(response.text)
        return True
    
    function_results = []
    for function_call in response.function_calls:
        result = call_function(function_call, verbose)
        if (
            not result.parts
            or not result.parts[0].function_response
            or not result.parts[0].function_response.response
        ):
            raise RuntimeError(f"Empty function response for {function_call.name}")
        if verbose:
            print(f"-> {result.parts[0].function_response.response}")
        function_results.append(result.parts[0])

    messages.append(types.Content(role="user", parts=function_results))
    return False


if __name__ == "__main__":
    main()
