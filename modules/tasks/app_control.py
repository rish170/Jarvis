import os
import subprocess
import pygetwindow as gw
import time

def open_app(app_name: str):
    print(f"[ACTION] Opening app: {app_name}")
    known_apps = {
        "notepad": "notepad.exe",
        "chrome": "chrome.exe",
        "calculator": "calc.exe",
        "word": "winword.exe",
    }

    # Start app
    process = None
    if app_name in known_apps:
        process = subprocess.Popen(known_apps[app_name])
    else:
        os.system(f'start {app_name}')

    # Wait a bit for window to appear
    time.sleep(2)

    # Try to focus window
    focus_app(app_name)
    return True


def focus_app(app_name: str):
    """Bring an existing app window to the front."""
    time.sleep(1)
    windows = gw.getWindowsWithTitle(app_name)
    if windows:
        win = windows[0]
        win.activate()
        print(f"[ACTION] Focused window: {win.title}")
        return True
    else:
        print(f"[WARN] No window found for {app_name}")
        return False
