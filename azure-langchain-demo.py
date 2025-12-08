from langchain_openai import AzureChatOpenAI

from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv

load_dotenv()

# Initialize the Azure Chat OpenAI client

llm = AzureChatOpenAI(
    deployment_name="gpt-5-nano",
    model_name="gpt-5-nano",
    #azure_api_version="2024-12-01-preview",
)

prompt = PromptTemplate.from_template("What is the capital of {country}?")

chain = prompt | llm 

response = chain.invoke({'country': 'India'})

print(response.content)