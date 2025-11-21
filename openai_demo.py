#! pip install openai

from openai import OpenAI
from dotenv import load_dotenv
import os



load_dotenv()

client = OpenAI(api_key=os.getenv("TEST_API_KEY"))

response = client.responses.create(
    model="gpt-5-nano",
    input="Write a poem on GenAI?"
)

print(response.output_text)