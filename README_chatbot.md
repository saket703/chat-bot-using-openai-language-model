# Spark: a voice chatbot using the OpenAI API

Spark is a talking chatbot written in Python. You speak to it through your microphone, it sends what you said to OpenAI's `gpt-3.5-turbo` model, and it reads the answer back to you out loud. It is set up as a small robot guide for a school science and arts exhibition, and it is told to keep its answers short.

## How it works

1. `speech_recognition` listens on the default microphone and converts your speech to text (Google speech recognition).
2. The text is sent to the OpenAI Chat Completions API (`gpt-3.5-turbo`) along with Spark's persona prompt.
3. The reply is printed in the console as `Spark: ...` and spoken aloud with `pyttsx3` (works offline).
4. This repeats in a loop until you stop the program.

## Requirements

- Python 3.8 or newer
- A working microphone and speakers
- An OpenAI API key
- Windows (the script clears the screen with `cls`)

Install the libraries:

```bash
pip install openai SpeechRecognition pyttsx3 pyaudio
```

If `pyaudio` fails to install on Windows, try `pip install pipwin` and then `pipwin install pyaudio`.

## Setup and run

1. Clone the repo:
   ```bash
   git clone https://github.com/saket703/chat-bot-using-openai-language-model
   cd chat-bot-using-openai-language-model
   ```
2. Open `test.py` and replace the `Your Api Key` placeholder with your own OpenAI API key.
3. Run it:
   ```bash
   python test.py
   ```
4. Speak when the console says it is listening. Press `Ctrl+C` to quit.

> **Do not commit your real API key.** Keep it only on your own machine, or load it from an environment variable instead of writing it into the file.

## Limitations

- Voice input only; there is no typed-text mode.
- No exit command, so you stop it with `Ctrl+C`.
- Needs an internet connection for speech recognition and for the OpenAI API.

## Built with

Python, OpenAI API, SpeechRecognition, pyttsx3
