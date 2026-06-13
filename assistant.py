import os
import time
import webbrowser
import pyautogui
import pyttsx3
import speech_recognition as sr
import keyboard
import pyperclip


pyautogui.FAILSAFE = True

engine = pyttsx3.init()
engine.setProperty("rate", 160)
engine.setProperty("volume", 1.0)


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            recognizer.pause_threshold = 2
            recognizer.energy_threshold = 300
            audio = recognizer.listen(source, timeout=12, phrase_time_limit=15)

        command = recognizer.recognize_google(audio)
        command = command.lower().strip()
        print("You:", command)
        return command

    except sr.WaitTimeoutError:
        return ""

    except sr.UnknownValueError:
        return ""

    except Exception as e:
        print("Mic error:", e)
        return ""


def paste_text(text):
    pyperclip.copy(text)
    time.sleep(0.2)
    pyautogui.hotkey("ctrl", "v")


def open_app(command):
    if "chrome" in command:
        speak("Opening Chrome.")
        os.system("start chrome")
        return True

    if "google" in command and "search" not in command and "write" not in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")
        return True

    if "youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
        return True

    if "notepad" in command:
        speak("Opening Notepad.")
        os.system("notepad")
        return True

    if "excel" in command:
        speak("Opening Excel.")
        os.system("start excel")
        return True

    if "calculator" in command:
        speak("Opening Calculator.")
        os.system("calc")
        return True

    if "desktop" in command:
        speak("Opening Desktop.")
        os.system(r"explorer %USERPROFILE%\Desktop")
        return True

    if "download" in command or "downloads" in command:
        speak("Opening Downloads.")
        os.system(r"explorer %USERPROFILE%\Downloads")
        return True

    if "folder" in command or "file explorer" in command:
        speak("Opening File Explorer.")
        os.system("explorer")
        return True

    if "whatsapp" in command:
        speak("Opening WhatsApp.")
        webbrowser.open("https://web.whatsapp.com")
        return True

    return False


def search_google(command):
    query = command

    remove_words = [
        "search google for",
        "search on google for",
        "search for",
        "search",
        "google",
        "find",
        "open"
    ]

    for word in remove_words:
        query = query.replace(word, "")

    query = query.strip()

    if query == "":
        speak("Tell me what to search.")
        query = listen()

    if query:
        speak("Searching Google for " + query)
        webbrowser.open("https://www.google.com/search?q=" + query.replace(" ", "+"))
        return True

    return False


def write_in_google(command):
    text = command

    remove_words = [
        "write in google",
        "type in google",
        "write on google",
        "type on google",
        "google write",
        "google type"
    ]

    for word in remove_words:
        text = text.replace(word, "")

    text = text.strip()

    if text == "":
        speak("What should I write in Google?")
        text = listen()

    if text:
        speak("Opening Google and typing " + text)
        webbrowser.open("https://www.google.com")
        time.sleep(4)
        paste_text(text)
        pyautogui.press("enter")
        return True

    return False


def type_anywhere(command):
    text = command

    remove_words = [
        "type",
        "write",
        "please type",
        "please write"
    ]

    for word in remove_words:
        text = text.replace(word, "", 1)

    text = text.strip()

    if text == "":
        speak("Tell me what to type.")
        text = listen()

    if text:
        speak("Typing now.")
        paste_text(text)
        return True

    return False


def write_code():
    speak("Opening Notepad and writing Python code.")
    os.system("notepad")
    time.sleep(2)

    code = """print("Hello User")

name = input("Enter your name: ")
print("Welcome", name)
"""

    paste_text(code)
    speak("Code written.")
    return True


def laptop_control(command):
    if "increase volume" in command or "volume up" in command:
        for _ in range(5):
            pyautogui.press("volumeup")
        speak("Volume increased.")
        return True

    if "decrease volume" in command or "volume down" in command:
        for _ in range(5):
            pyautogui.press("volumedown")
        speak("Volume decreased.")
        return True

    if "mute" in command:
        pyautogui.press("volumemute")
        speak("Muted.")
        return True

    if "screenshot" in command or "screen shot" in command:
        file_name = "screenshot.png"
        img = pyautogui.screenshot()
        img.save(file_name)
        speak("Screenshot saved.")
        return True

    if "lock laptop" in command or "lock screen" in command:
        speak("Locking laptop.")
        os.system("rundll32.exe user32.dll,LockWorkStation")
        return True

    if "close window" in command or "close this" in command or "close file" in command:
        speak("Closing current window.")
        pyautogui.hotkey("alt", "f4")
        return True

    if "close all" in command:
        speak("Closing current window. Say close all again to close another window.")
        pyautogui.hotkey("alt", "f4")
        return True

    return False


def whatsapp_message(command):
    if "message" not in command and "send" not in command:
        return False

    if "whatsapp" not in command:
        return False

    speak("Opening WhatsApp Web.")
    webbrowser.open("https://web.whatsapp.com")
    time.sleep(8)

    speak("Click the WhatsApp search box, then press Enter.")
    keyboard.wait("enter")

    speak("Tell me contact name.")
    contact = listen()

    if not contact:
        speak("I did not hear contact name.")
        return True

    paste_text(contact)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)

    speak("Tell me message.")
    message = listen()

    if not message:
        speak("I did not hear message.")
        return True

    paste_text(message)
    pyautogui.press("enter")
    speak("Message sent.")
    return True


def whatsapp_call(command):
    if "call" not in command:
        return False

    if "whatsapp" not in command and "piyush" not in command:
        return False

    speak("Opening WhatsApp Web.")
    webbrowser.open("https://web.whatsapp.com")
    time.sleep(8)

    name = command.replace("call", "").replace("on whatsapp", "").replace("in whatsapp", "").replace("whatsapp", "").strip()

    if name == "":
        speak("Whom should I call?")
        name = listen()

    if not name:
        speak("I did not hear contact name.")
        return True

    speak("I will search contact " + name)
    speak("Click WhatsApp search box, then press Enter.")
    keyboard.wait("enter")

    paste_text(name)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(2)

    speak("Contact opened. I cannot safely press the call button automatically on every screen.")
    speak("Please click the call button manually.")
    return True


def chat(command):
    if "hello" in command or "hi" in command:
        speak("Hello User. I am listening.")

    elif "what are you doing" in command:
        speak("I am waiting for your command and ready to control your laptop.")

    elif "talk with me" in command or "can you talk" in command:
        speak("Yes, I can talk with you. Tell me what you want me to do.")

    elif "what can you do" in command:
        speak("I can open apps, search Google, write in Google, type text, control volume, take screenshots, close windows, open WhatsApp, and help with simple automation.")

    elif "handle my data" in command or "data entry" in command:
        speak("I can help with data entry, but first you need to open your form and tell me exact fields.")

    elif "thank you" in command or "thanks" in command:
        speak("Welcome User.")

    else:
        speak("I heard you, but I do not know this action yet.")


def main():
    speak("Smart Assistant started.")
    speak("Now I will only listen. I will not force you to type.")
    speak("Say stop assistant to close me.")

    while True:
        command = listen()

        if command == "":
            continue

        if "stop assistant" in command or "exit" in command or "quit" in command:
            speak("Closing assistant. Goodbye.")
            break

        if whatsapp_message(command):
            continue

        if whatsapp_call(command):
            continue

        if "write code" in command or "write one code" in command:
            write_code()
            continue

        if "write in google" in command or "type in google" in command:
            write_in_google(command)
            continue

        if "search" in command or "search google" in command or "open python tutorial" in command:
            search_google(command)
            continue

        if "type" in command or "write" in command:
            type_anywhere(command)
            continue

        if laptop_control(command):
            continue

        if open_app(command):
            continue

        chat(command)


if __name__ == "__main__":
    main()