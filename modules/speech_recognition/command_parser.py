"""
command_parser.py
- Purpose: convert a transcribed text string into a canonical "intent" + "params" dict.
- This is a lightweight, deterministic parser (regex / keyword based).
- It is intentionally simple so it is predictable and safe for automation-critical tasks.
- Later phases will replace or augment this with an ML-based NLU or LLM canonicalizer.
"""

import re

def parse_command(text):
    """
    Parse `text` and return a dictionary: {"intent": <str>, "params": {...}}
    Known intents in this starter:
        - open_app: open a named application (param: app_name)
        - search_web: search query in browser (param: query)
        - type_text: type some text into focused input (param: text)
        - unknown: fallback intent when nothing matches
    """
    if not text:
        return {"intent": "unknown", "params": {}, "raw": text}

    text = text.strip().lower()

    # 1) open application: "open notepad", "open chrome", "launch calculator"
    m = re.match(r'^(open|launch|start)\s+(?P<app>.+)$', text)
    if m:
        app_name = m.group("app").strip()
        return {"intent": "open_app", "params": {"app_name": app_name}, "raw": text}

    # 2) search web: "search for cats", "google latest ai news"
    m = re.match(r'^(search for|search|google|find)\s+(?P<query>.+)$', text)
    if m:
        query = m.group("query").strip()
        return {"intent": "search_web", "params": {"query": query}, "raw": text}

    # 3) type text: "type hello world", "write hello"
    m = re.match(r'^(type|write|say)\s+(?P<text>.+)$', text)
    if m:
        t = m.group("text").strip()
        return {"intent": "type_text", "params": {"text": t}, "raw": text}

    # 4) simple toggle-like commands (e.g., "turn on bluetooth", "turn off wifi")
    m = re.match(r'^(turn|switch)\s+(on|off)\s+(?P<setting>.+)$', text)
    if m:
        action = m.group(2)  # 'on' or 'off'
        setting = m.group("setting").strip()
        return {"intent": "toggle_setting", "params": {"setting": setting, "value": action}, "raw": text}

    # 5) fallback: if nothing matched, return unknown intent
    return {"intent": "unknown", "params": {}, "raw": text}


# Quick interactive test helper
if __name__ == "__main__":
    print("Interactive command parser test. Type text (or 'exit').")
    while True:
        s = input(">>> ").strip()
        if s in ("exit", "quit"):
            break
        print(parse_command(s))
