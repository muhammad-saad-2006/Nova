
# Nova — AI Chatbot

Nova is an AI-powered chatbot project built with Python, Streamlit, LangChain, and LangGraph.

The project was started to explore how modern AI chat applications work, including language model integration, conversational workflows, chat history, and persistent conversation storage.

Nova currently provides a simple interactive chatbot that accepts user messages and generates AI-powered responses using Google's Gemini 2.5 Flash model.

The project is currently a work in progress. Development was paused due to time constraints, but I plan to return to it and expand its functionality in the future.

---

## Project Overview

Nova is designed as a lightweight conversational AI application.

The current implementation allows users to:

- Interact with an AI chatbot through a Streamlit interface.
- Ask questions and receive AI-generated responses.
- Create new conversations.
- Maintain multiple conversation threads.
- View previously created conversations through the sidebar.
- Restore conversation history when reopening a saved chat.
- Generate conversation titles automatically from the first user message.
- Store conversation information using SQLite.
- Maintain chatbot conversation state through LangGraph.

The main goal of this project is to understand the architecture behind AI-powered conversational applications and gradually develop Nova into a more capable chatbot.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.13 | Main programming language |
| Streamlit | Chat interface and application UI |
| LangChain | Language model integration |
| LangGraph | Conversational workflow and state management |
| Google Gemini 2.5 Flash | AI language model |
| LangChain Google GenAI | Integration with Google's Gemini models |
| SQLite | Persistent conversation storage |
| LangGraph Checkpoint SQLite | Conversation state persistence |
| python-dotenv | Environment variable management |
| LangSmith | LangChain ecosystem tooling |

---

## Current Features

### 1. AI-Powered Conversations

Nova uses Google's Gemini 2.5 Flash model to process user messages and generate responses.

The chatbot receives messages through LangChain and sends them to the configured language model.

### 2. Interactive Chat Interface

The frontend is developed using Streamlit.

It provides:

- A chat input field.
- Separate user and assistant message displays.
- Streaming AI responses.
- A sidebar for conversation navigation.
- A button to start a new conversation.

### 3. Multiple Conversations

Users can create separate chat sessions instead of keeping every message in a single conversation.

Each conversation is assigned a unique UUID-based thread ID.

### 4. Conversation History

Nova uses LangGraph's SQLite checkpointing functionality to preserve conversational state.

Previously created conversations can be selected from the sidebar and their messages can be restored.

### 5. Automatic Conversation Titles

When a new conversation begins, Nova generates a simple title using the first user message.

For longer messages, the title is created from the first six words.

### 6. Conversation Persistence

SQLite is used to store conversation metadata, including:

- Conversation thread ID.
- Conversation title.
- Persisted chatbot state through LangGraph checkpoints.

---

## Project Structure

```text
Nova/
│
├── backend/
│   ├── __init__.py
│   ├── database.py
│   ├── graph.py
│   └── state.py
│
├── frontend/
│   ├── __init__.py
│   └── chat_interface.py
│
├── main.py
├── pyproject.toml
├── uv.lock
├── .python-version
├── .gitignore
└── README.md
```

### Backend

The backend contains the chatbot's logic, workflow, conversation state, and database functionality.

**`backend/graph.py`**

- Initializes the Google Gemini language model.
- Creates a LangGraph state graph.
- Defines the chatbot node.
- Processes incoming messages.
- Connects the workflow's starting and ending points.
- Compiles the graph with SQLite checkpointing.

**`backend/state.py`**

Defines the chatbot's conversation state using Python's `TypedDict`.

It uses LangGraph's `add_messages` function to manage message updates.

**`backend/database.py`**

Handles SQLite database operations.

It provides functionality to:

- Initialize the SQLite connection.
- Create the conversations table.
- Register new conversation threads.
- Update conversation titles.
- Retrieve existing conversations.
- Configure LangGraph's SQLite checkpoint saver.

### Frontend

**`frontend/chat_interface.py`**

Contains the Streamlit chatbot interface.

It handles:

- Session state initialization.
- Creating new conversations.
- Loading existing conversations.
- Displaying chat history.
- Sending user messages to the chatbot.
- Streaming AI-generated responses.
- Updating conversation titles.
- Navigating between conversation threads.

### Main Entry Point

**`main.py`**

Contains a basic Python entry point.

The Streamlit chat interface is currently located in `frontend/chat_interface.py`.

---

## Getting Started

Follow these steps to run Nova locally.

### Prerequisites

Make sure you have the following installed:

- Python 3.13 or later.
- Git.
- An API key for Google Gemini.

### 1. Clone the Repository

```bash
git clone https://github.com/muhammad-saad-2006/Nova.git
```

### 2. Navigate to the Project

```bash
cd Nova
```

### 3. Create a Virtual Environment

**Windows:**

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

The project uses `pyproject.toml` and includes a `uv.lock` file.

Using pip:

```bash
pip install -e .
```

Alternatively, install and use UV:

```bash
pip install uv
uv sync
```

### 5. Configure Environment Variables

Create a `.env` file in the project's root directory.

Add your Google Gemini API key:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

Replace the placeholder with your actual API key.

Keep your `.env` file private. Do not commit API keys or other secrets to GitHub.

### 6. Run the Application

Start the Streamlit application using:

```bash
streamlit run frontend/chat_interface.py
```

Streamlit will start the application and provide a local URL in the terminal.

Open that URL in your browser to interact with Nova.

---

## How Nova Works

Nova uses a simple conversational workflow built with LangGraph.

The general request flow is:

```text
       User
         |
         v
   Streamlit UI
         |
         v
   User Message
         |
         v
   LangGraph Workflow
         |
         v
      Chat Node
         |
         v
   Google Gemini API
         |
         v
   AI Generated Response
         |
         v
    Streamlit UI
         |
         v
       User
```

### Conversation Persistence

Each conversation receives a unique thread ID.

LangGraph uses this thread ID in its configurable checkpointing system to identify and restore the corresponding conversation state.

SQLite stores the conversation metadata and LangGraph checkpoints.

This allows the application to maintain separate conversation sessions.

---

## Environment and Configuration

| File | Description |
|---|---|
| `pyproject.toml` | Project metadata, Python requirements, and dependencies. |
| `uv.lock` | Locked dependency versions. |
| `.python-version` | Specifies Python 3.13. |
| `.env` | Stores private environment variables and API credentials. |
| `.gitignore` | Excludes virtual environments, generated files, environment variables, and SQLite database files. |
| `nova.db` | Local SQLite database generated when the application runs. |

---

## Development Status

<badge color="warning">Work in Progress</badge>

Nova is currently an early-stage chatbot project.

The basic conversational functionality has been implemented, and the project already includes a foundation for conversation management and persistence.

Development was paused because of time constraints. I intend to continue working on it when I have more time.

### Implemented

- [x] Streamlit-based chatbot interface.
- [x] Google Gemini model integration.
- [x] LangChain integration.
- [x] LangGraph conversational workflow.
- [x] User message processing.
- [x] AI-generated responses.
- [x] Streaming responses.
- [x] Multiple conversation threads.
- [x] SQLite conversation metadata.
- [x] LangGraph SQLite checkpointing.
- [x] Conversation history restoration.
- [x] Automatic basic conversation titles.

### Planned Improvements

These are future development goals, not features currently implemented.

- [ ] Improve the chatbot's interface and overall user experience.
- [ ] Add message editing and deletion.
- [ ] Add conversation deletion and renaming.
- [ ] Improve conversation title generation.
- [ ] Add chat export functionality.
- [ ] Support additional language models.
- [ ] Add configurable chatbot behavior and system instructions.
- [ ] Improve error handling and API failure management.
- [ ] Add more robust conversation management.
- [ ] Expand testing and project documentation.

---

## Why I Started This Project

I started Nova to explore the development of AI-powered chatbot applications and gain practical experience with tools such as LangChain, LangGraph, Google Gemini, and Streamlit.

The project has helped me understand:

- How to integrate a large language model into a Python application.
- How to process conversational messages.
- How to build workflows using LangGraph.
- How to manage conversation state.
- How to persist chat history using SQLite.
- How to build an interactive chatbot interface with Streamlit.

Although the project is not complete yet, it serves as a foundation for further experimentation and development.

---

## Future Vision

My goal is to continue developing Nova into a more capable conversational AI application.

Future development will focus on improving its interface, expanding conversational capabilities, introducing additional functionality, and making the application more flexible and reliable.

For now, Nova remains a simple working chatbot and an ongoing personal development project.

---

## Author

**Muhammad Saad**

GitHub: [@muhammad-saad-2006](https://github.com/muhammad-saad-2006)

Project Repository: [Nova](https://github.com/muhammad-saad-2006/Nova)

---

**Nova — A small step towards building a smarter conversational AI.**
