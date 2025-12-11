from langchain_ollama import ChatOllama

#from dotenv import load_dotenv

#load_dotenv()

#llm = ChatOllama(model="llama3.2:3b")

llm = ChatOllama(model="phi3:3.8b")

response = llm.invoke("Hi, My name is Raj")

print(response.content)

response2 = llm.invoke("What is my name?")

print(response2.content)