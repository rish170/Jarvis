"""
Routes intents to proper execution modules.
"""
from app_control import open_app
from system_actions import type_text, toggle_setting

def execute_command(parsed):
    intent = parsed.get("intent")
    params = parsed.get("params", {})

    if intent == "open_app":
        return open_app(params.get("app_name"))
    elif intent == "type_text":
        return type_text(params.get("text"))
    elif intent == "toggle_setting":
        return toggle_setting(params.get("setting"), params.get("value"))
    else:
        print("[ROUTER] Unknown intent, no action performed.")
        return False
