from langgraph.checkpoint.sqlite import SqliteSaver
from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent.parent
DB_Path = BASE_DIR/"nova.db"

conn = sqlite3.connect(
    DB_Path,
    check_same_thread=False
)

checkpointer = SqliteSaver(conn=conn)


conn.execute("""
    CREATE TABLE IF NOT EXISTS conversations(
        thread_id TEXT PRIMARY KEY,
        title TEXT NOT NULL
    )
""")

conn.commit()

def add_thread(thread_id, title="New Conversation"):
    conn.execute(
        """
        INSERT OR IGNORE INTO conversations (thread_id, title)
        VALUES(?, ?)
        """,
        (str(thread_id), title)
    )

    conn.commit()

def update_title(thread_id, title):

    conn.execute(
        """
        UPDATE conversations
        SET title = ?
        WHERE thread_id = ?
        """,
        (title, str(thread_id))
    )

    conn.commit()

def retrieve_all_threads():

    cursor = conn.execute(
        """
        SELECT thread_id, title FROM conversations
        """
    )

    return dict(cursor.fetchall())
