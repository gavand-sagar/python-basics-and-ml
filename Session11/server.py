"""
Session 11: MCP (Model Context Protocol) — Your First MCP Server
=================================================================

WHAT IS MCP?
------------
MCP = A standard "plug" that lets AI talk to your tools and data.

Real-life analogy:
  Imagine you hired a super-smart assistant (Claude/AI).
  Without MCP → assistant sits in a room with no tools, only their memory.
  With MCP    → assistant has a desk with a notepad, calculator, phone, files.
               Now they can DO things, not just THINK things.

HOW IT WORKS (3 steps):
  1. You build an MCP Server  →  defines what tools the AI can use
  2. AI connects to it        →  Claude Desktop reads your server
  3. AI calls your tools      →  Claude says "add a note" → your Python runs

TODAY'S DEMO: Personal Notes Manager
-------------------------------------
Use case: Everyone takes notes daily.
We give Claude the ability to manage your notes — add, view, search, delete.

INSTALL:
  pip install mcp
"""

import json
import os
from datetime import datetime
from mcp.server.fastmcp import FastMCP

# =============================================================
# A. CREATE THE MCP SERVER
# Think of this as "opening your tool shop" and giving it a name.
# =============================================================
mcp = FastMCP("Personal Notes Manager")

NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.json")


# =============================================================
# B. HELPER FUNCTIONS (internal — NOT tools, AI can't call these)
# =============================================================

def load_notes():
    """Read notes from file. Returns empty list if file doesn't exist."""
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "r") as f:
        return json.load(f)


def save_notes(notes):
    """Write notes list back to file."""
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)


# =============================================================
# C. DEFINE TOOLS
#
# @mcp.tool() = "Hey Claude, you are ALLOWED to call this function."
#
# Rules for tools:
#   - Must have type hints (str, int, etc.)
#   - Must have a docstring (Claude reads it to know WHEN to use the tool)
#   - Must return a string (the result Claude gets back)
# =============================================================

@mcp.tool()
def add_note(title: str, content: str) -> str:
    """
    Add a new note. Use this when user wants to save or remember something.
    Example: 'Remember to call the dentist' or 'Meeting notes from today'.
    """
    notes = load_notes()

    note = {
        "id": len(notes) + 1,
        "title": title,
        "content": content,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    notes.append(note)
    save_notes(notes)

    return f"Note saved! ID=#{note['id']}, Title='{title}'. Total notes: {len(notes)}"


@mcp.tool()
def get_all_notes() -> str:
    """
    Get and display all saved notes.
    Use this when user asks to see, list, or show all notes.
    """
    notes = load_notes()

    if not notes:
        return "No notes yet. Ask me to add your first note!"

    lines = [f"You have {len(notes)} note(s):\n"]
    for note in notes:
        lines.append(f"  #{note['id']} | {note['created_at']} | {note['title']}")
        lines.append(f"       {note['content']}\n")

    return "\n".join(lines)


@mcp.tool()
def search_notes(keyword: str) -> str:
    """
    Search notes by a keyword. Looks in both title and content.
    Use this when user wants to find a specific note or topic.
    """
    notes = load_notes()

    matches = [
        n for n in notes
        if keyword.lower() in n["title"].lower()
        or keyword.lower() in n["content"].lower()
    ]

    if not matches:
        return f"No notes found containing '{keyword}'."

    lines = [f"Found {len(matches)} match(es) for '{keyword}':\n"]
    for note in matches:
        lines.append(f"  #{note['id']} | {note['title']}: {note['content']}")

    return "\n".join(lines)


@mcp.tool()
def delete_note(note_id: int) -> str:
    """
    Delete a note by its ID number.
    Use this when user wants to remove or discard a specific note.
    """
    notes = load_notes()
    updated = [n for n in notes if n["id"] != note_id]

    if len(updated) == len(notes):
        return f"Note #{note_id} not found. Use get_all_notes to see valid IDs."

    save_notes(updated)
    return f"Note #{note_id} deleted. Remaining notes: {len(updated)}"


# =============================================================
# D. RUN THE SERVER
#
# mcp.run() starts the server using stdio transport.
# Claude Desktop will launch this script and talk to it via stdin/stdout.
# =============================================================
if __name__ == "__main__":
    print("Notes MCP Server starting...")
    mcp.run(transport="streamable-http")
    print("server started ...")
    
