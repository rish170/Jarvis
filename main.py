from modules.voice_input import listen

def jarvis_main():
    while True:
        command = listen()
        if command and "hey jarvis" in command:
            print("Jarvis activated. How can I help?")
            break

if __name__ == "__main__":
    jarvis_main()
