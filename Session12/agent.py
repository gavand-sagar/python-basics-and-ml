import asyncio
import requests
import json
from mcp.client.streamable_http import streamable_http_client
from mcp import ClientSession
import mcp

# =========================
# CONFIG
# =========================

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma3:1b"

MCP_URL = "http://localhost:8000/mcp"

# =========================
# OLLAMA CALL
# =========================

def ask_llm(prompt):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()

    return data["response"].strip()

# =========================
# MCP TOOL CALLS
# =========================

async def _call_tool(tool_name, arguments):
    async with streamable_http_client(MCP_URL) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool(tool_name, arguments)
            return result

def save_note(note):
    result = asyncio.run(_call_tool("add_note", {"title": "Note", "content": note}))
    # result.content is a list of TextContent objects
    return result.content[0].text if result.content else "Done"

def get_notes():
    result = asyncio.run(_call_tool("get_all_notes", {}))
    return result.content[0].text if result.content else "No notes"

# =========================
# SYSTEM PROMPT
# =========================

SYSTEM_PROMPT = """
You are a simple AI Agent.

TOOLS AVAILABLE:

1. save_note
Use when user wants to remember/store/save something.

Response format:
{
  "tool": "save_note",
  "note": "text to save"
}

2. get_notes
Use when user wants to read/show/list notes.

Response format:
{
  "tool": "get_notes"
}

IMPORTANT:
- Respond ONLY with valid JSON.
- No markdown.
- No explanation.
"""

# =========================
# AGENT LOOP
# =========================

print("=" * 50)
print("LOCAL AI AGENT USING OLLAMA + MCP")
print("=" * 50)

while True:

    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    full_prompt = f"""
{SYSTEM_PROMPT}

USER:
{user_input}
"""

    llm_response = ask_llm(full_prompt)

    print("\n[LLM RAW RESPONSE]")
    print(llm_response)

    # =========================
    # PARSE JSON RESPONSE
    # =========================

    # Strip markdown code fences if the model wraps JSON in ```json ... ```
    clean_response = llm_response.strip()
    if clean_response.startswith("```"):
        clean_response = clean_response.split("\n", 1)[-1]
        clean_response = clean_response.rsplit("```", 1)[0].strip()

    try:
        parsed = json.loads(clean_response)

    except Exception:
        print("\nAgent:")
        print(llm_response)
        continue

    # =========================
    # TOOL: SAVE NOTE
    # =========================

    if parsed.get("tool") == "save_note":

        note_content = parsed.get("note")

        try:
            result = save_note(note_content)

            print("\nAgent:")
            print("Note saved successfully.")
            print(json.dumps(result, indent=2))

        except Exception as e:
            print("\nError calling MCP save_note")
            print(e)

    # =========================
    # TOOL: GET NOTES
    # =========================

    elif parsed.get("tool") == "get_notes":

        try:
            result = get_notes()

            print("\nAgent:")
            print(json.dumps(result, indent=2))

        except Exception as e:
            print("\nError calling MCP get_notes")
            print(e)

    # =========================
    # NORMAL RESPONSE
    # =========================

    else:

        print("\nAgent:")
        print(parsed)