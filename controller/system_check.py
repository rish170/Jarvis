import platform, os
print("OS:", platform.system(), platform.release())
print("Python:", platform.python_version())
print("Mic connected:", "Yes" if "Microphone" in os.popen('powershell Get-PnpDevice -Class AudioEndpoint').read() else "Check manually")
