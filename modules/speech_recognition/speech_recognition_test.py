"""
speech_recognition_test.py
- Purpose: end-to-end test that:
    1) waits for activation phrase using the Phase-1 activation module
    2) records a short command (listener)
    3) parses it into intent (command_parser)
    4) prints the detected intent/parameters
- Run this from the repository root:
    python modules/speech_recognition/speech_recognition_test.py
"""

import time

# Import activation listener from Phase 1.
# Make sure your modules.activation.voice_input has a function that listens for
# the wakeword and returns True (or returns the transcribed phrase).
try:
    from modules.activation.voice_input import listen as activation_listen
except Exception as e:
    # If import fails, give a helpful error. In early phases, you may not have activation structured yet.
    print("Warning: couldn't import activation listener. Make sure Phase 1 file exists at modules/activation/voice_input.py")
    activation_listen = None

from listener import listen_once
from command_parser import parse_command

WAKE_KEYWORDS = ["hey jarvis", "ok jarvis", "jarvis"]

def wait_for_wakeword(timeout=30):
    """
    Very simple wakeword loop:
    - If you have a Phase1 `listen` that returns full transcribed text repeatedly,
      adapt this to check for wakewords in that text.
    - If the Phase1 module already does keyword detection and returns a boolean, use that.
    This implementation tries to call `activation_listen()` and checks for keywords.
    """
    if activation_listen is None:
        # If activation module missing, fall back to a simple prompt to continue testing
        input("Activation module not found. Press Enter to simulate wakeword and continue...")
        return True

    print("Waiting for wakeword (say 'Hey Jarvis')...")
    start = time.time()
    while time.time() - start < timeout:
        try:
            transcribed = activation_listen()  # reuse your Phase1 function
        except TypeError:
            # some Phase1 implementations may require different args; catch gracefully
            transcribed = activation_listen()  # attempt anyway
        if not transcribed:
            # nothing heard; loop again
            continue
        # check for any of the keywords inside transcribed phrase
        for kw in WAKE_KEYWORDS:
            if kw in transcribed.lower():
                print("Wakeword detected.")
                return True
    print("Wakeword not detected within timeout.")
    return False


def main():
    # 1) Wait for wakeword (Phase 1)
    ok = wait_for_wakeword(timeout=30)
    if not ok:
        print("Exiting test - wakeword not detected.")
        return

    # 2) Listen for actual command (Phase 2 listener)
    command_text = listen_once(timeout=3, phrase_time_limit=6)
    if command_text is None:
        print("No command captured.")
        return

    # 3) Parse the command into intent + params
    parsed = parse_command(command_text)
    print("Parsed command result:")
    print(parsed)

    # 4) Simulate action (for testing only)
    intent = parsed.get("intent")
    params = parsed.get("params")
    if intent == "open_app":
        print(f"[SIMULATED ACTION] Would open app: {params.get('app_name')}")
    elif intent == "search_web":
        print(f"[SIMULATED ACTION] Would search web for: {params.get('query')}")
    elif intent == "type_text":
        print(f"[SIMULATED ACTION] Would type text: {params.get('text')}")
    elif intent == "toggle_setting":
        print(f"[SIMULATED ACTION] Would toggle {params.get('setting')} -> {params.get('value')}")
    else:
        print("[SIMULATED ACTION] Unknown or unsupported intent. No action taken.")


if __name__ == "__main__":
    main()
