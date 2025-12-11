from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory

# 1. LLM
model = ChatOllama(model="llama3.2:3b")

# 2. Prompt expecting history
prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder(variable_name="history"),
    ("human","{input}")
])

runnable = prompt | model

# 3. Memory
history_store = {}

def get_session_history(session_id):
    if session_id not in history_store:
        history_store[session_id] = InMemoryChatMessageHistory()
    return history_store[session_id]

# 4. Attach memory
chain = RunnableWithMessageHistory(
    runnable,
    get_session_history,
    history_messages_key="history",
    #input_messages_key="input"
)

# -------------------------
# FIRST MESSAGE
# -------------------------
chain.invoke(
    {"input": "Hi, my name is Raj"},
    config={"configurable": {"session_id": "1"}}
)

# -------------------------
# SECOND MESSAGE
# -------------------------
response = chain.invoke(
    {"input": "What is my name?"},
    config={"configurable": {"session_id": "1"}}
)

print("\nModel Response:", response.content)


response1 = chain.invoke(
    {"input": "Who is Rohit Sharma?"},
    config={"configurable": {"session_id": "1"}}
)

print("\nModel Response:", response1.content)


response2 = chain.invoke(
    {"input": "What is his age currently,you help me with age only ?"},
    config={"configurable": {"session_id": "1"}}
)

print("\nModel Response:", response2.content)


