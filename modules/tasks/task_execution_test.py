"""
End-to-end Phase 3 test:
 - Simulate parsed command dicts.
 - Verify router triggers correct actions.
"""
from router import execute_command

# Simulate parsed results
commands = [
    {"intent": "open_app", "params": {"app_name": "notepad"}},
    {"intent": "type_text", "params": {"text": "Jarvis is active!"}},
    {"intent": "toggle_setting", "params": {"setting": "wifi", "value": "off"}},
]

for cmd in commands:
    print("\nExecuting:", cmd)
    execute_command(cmd)
