"""
System-level actions like typing, toggling settings, etc.
"""
import pyautogui
import time

def type_text(text: str):
    print(f"[ACTION] Typing: {text}")
    time.sleep(1)
    pyautogui.typewrite(text, interval=0.05)

def toggle_setting(setting: str, value=None):
    print(f"[ACTION] Toggling setting: {setting} -> {value}")
    # For now, simulate — real toggles will be added later
    if setting.lower() == "wifi":
        print("Pretend toggled Wi-Fi.")
    elif setting.lower() == "bluetooth":
        print("Pretend toggled Bluetooth.")
    else:
        print("Unsupported setting.")
