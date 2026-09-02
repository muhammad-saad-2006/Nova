from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import (
    StateGraph,
    START,
    END
)
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv
from state import ChatState


load_dotenv()

# Create llm going to use for the chatbot
llm = ChatGoogleGenerativeAI(model="gemini-flash-2.5")

def chat_node(state: ChatState):
    # extract the message
    messages = state['messages']

    # send the message to llm
    response = llm.invoke(messages)

    # now return the response
    return {'messgaes': [response]} 

# Now create a graph for the workflow
graph = StateGraph(ChatState)

graph.add_node("chat_node", chat_node)

graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

# create checkpoints
"""
Currently the memory is stored in RAM which will work for a session which once closed lead to loss of all memory.
Will add the database integration later.
"""
checkpointer = InMemorySaver()  

# Now compile the graph
chatbot = graph.compile(checkpointer=checkpointer)
