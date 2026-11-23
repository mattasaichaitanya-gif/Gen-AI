import os
from dotenv import load_dotenv
from google import genai

# 1. Load settings from the .env file
load_dotenv()

# 2. Read the API key
api_key = os.getenv("GEMINI_API_KEY")

# 3. Check that the key exists
if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found. Check your .env file."
    )

# 4. Create the Google GenAI API client
client = genai.Client(api_key=api_key)

# 5. Write a prompt for the model
prompt = """Explain Artificial Intelligence in simple words.
Give five real-world examples suitable for a
first-year engineering student."""

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)

# 7. Print the generated response
print("\n========== LLM RESPONSE ==========\n")
print(response.text)
print("\n==================================")