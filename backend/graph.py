from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import (
    StateGraph,
    START,
    END
)
from dotenv import load_dotenv
from .state import ChatState
from .database import checkpointer


load_dotenv()

# Create llm going to use for the chatbot
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

def chat_node(state: ChatState):
    # extract the message
    messages = state['messages']

    # send the message to llm
    response = llm.invoke(messages)

    # now return the response
    return {'messages': [response]} 

# Now create a graph for the workflow
graph = StateGraph(ChatState)

graph.add_node("chat_node", chat_node)

graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)


# Now compile the graph
"""
Now we have added sqlite3 a small database to maintain our chat history.
Rather then maintaing in RAM
"""
chatbot = graph.compile(checkpointer=checkpointer)
