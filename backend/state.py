from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage
from typing import (
    TypedDict,
    Annotated
)

# Create the state which will be provided to our graph
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]