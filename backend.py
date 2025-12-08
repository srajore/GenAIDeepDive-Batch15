#from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()


def get_available_models():
    """Return list of available models."""
    return ["gpt-5-nano", "gpt-4o-mini"]


def find_achievements(model_name, person_name, person_role):
    """
    Find achievements for a given person and role.
    
    Args:
        model_name: The Ollama model to use
        person_name: Name of the person
        person_role: Role of the person
        
    Returns:
        dict with 'success', 'message', and 'content' keys
    """
    try:
        #---------langchain login ---------
        llm= ChatOpenAI(model=model_name)
        
        # Dynamic ChatPrompt Template : we pass BOTH variables into the template
        
        prompt = ChatPromptTemplate.from_messages([
            ("system",'''
              You are an expert research assistant.
              Format the response strictly as follows:
              - Start with a 1- sentance summery of who they are
              - Provide 5 bullet points of specific achievements in their role
              - Keep the tone professional and factual
             '''),
            ("human"," Identify the top 5 key professional achievements of {name} specifically in their role as {role}.If you don't know the answer, just say that you don't know.")
        ])
        
        # Create the chain
        
        chain = prompt | llm  # LCEL
        
        # Invoke the chain with dictionary containing both variables
        
        response = chain.invoke({
            'name': person_name,
            'role': person_role
        })
        
        return {
            'success': True,
            'message': 'Data Retrieved Successfully!',
            'content': response.content
        }
        
    except Exception as e:
        return {
            'success': False,
            'message': f' Error: Could not connect to Ollama.{e}',
            'content': None
        }
