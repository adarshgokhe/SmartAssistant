# SmartAssistant

A Python-based Desktop Voice Assistant capable of taking voice commands to automate daily tasks, control your computer, type text, and interact with applications.

## Features

- **Voice Recognition**: Listens to commands via microphone using `SpeechRecognition`.
- **Text-to-Speech**: Responds back with voice using `pyttsx3`.
- **App Automation**: Can open common applications (Chrome, YouTube, Notepad, Excel, Calculator) and system folders (Desktop, Downloads) via voice.
- **Keyboard & Typing Automation**: Uses `pyautogui` and `pyperclip` to automatically type or paste dictated text into any open window.

## Installation

1. Clone the repository.
2. Ensure you have Python installed.
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: You may also need to install `PyAudio` depending on your operating system for microphone support).*

## Usage

Run the main script to start the assistant:
```bash
python assistant.py
```
The assistant will listen for keywords and execute desktop automations automatically.
