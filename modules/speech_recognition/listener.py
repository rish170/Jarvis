"""
listener.py
- Purpose: capture a short voice command from microphone and return transcribed text.
- Uses the `speech_recognition` library for audio capture and speech-to-text.
- This module is intentionally simple so you can swap STT providers later (Whisper, cloud APIs, etc.).
"""

import speech_recognition as sr
import time

# How long (seconds) we listen after activation for a one-shot command
COMMAND_LISTEN_DURATION = 5  

def listen_once(timeout=None, phrase_time_limit=COMMAND_LISTEN_DURATION):
    """
    Listen once from the default microphone and return the recognized text (lowercased).
    Parameters:
        - timeout: optional seconds to wait for phrase to start (None = block until sound)
        - phrase_time_limit: seconds of recording after phrase start
    Returns:
        - recognized_text (str) on success
        - None on failure
    Notes:
        - This uses the Google Web Speech API via SpeechRecognition by default.
          For privacy / offline, replace recognizer.recognize_google(...) with another recognizer.
    """
    recognizer = sr.Recognizer()

    # Use the default system microphone. You can pass device_index to Microphone() if needed.
    with sr.Microphone() as source:
        # optional ambient noise adjustment to improve recognition in noisy environments
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening for command...")
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        except sr.WaitTimeoutError:
            # nothing detected within timeout
            print("No speech detected (timeout).")
            return None

    # Try recognizing speech (Google Web Speech API as default)
    try:
        text = recognizer.recognize_google(audio)
        text = text.strip().lower()
        print(f"Transcribed: {text}")
        return text
    except sr.UnknownValueError:
        # speech was unintelligible
        print("Could not understand audio.")
        return None
    except sr.RequestError as e:
        # API was unreachable or unresponsive
        print(f"STT service error: {e}")
        return None


if __name__ == "__main__":
    # quick manual test
    print("Run this file directly to test microphone -> transcription.")
    print("Speak a short phrase after the prompt.")
    t = listen_once(timeout=3, phrase_time_limit=5)
    print("Result:", t)
