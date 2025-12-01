from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

response = ChatOpenAI(model="gpt-5-nano").invoke("What is the capital of France?")

print(response.content)