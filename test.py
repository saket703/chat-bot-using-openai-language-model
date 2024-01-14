import speech_recognition as sr
import pyttsx3
import openai
import os

# Set your API keys for ChatGPT
os.system('cls')
openai.api_key = "Your Api"

BOT_NAME = "Spark"  # Set the bot's name here

def get_audio_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, show_all=False)
            os.system('cls')
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            os.system('cls')
            return ""
        except sr.RequestError as e:
            print("Could not request results from speech recognition service; {0}".format(e))
            return ""

def get_response_from_chatgpt(text):
    prompt = f"You are {BOT_NAME}, an intelligent assistant, created by Saket, Pranav, Shushank for The science exhibition in nandi international school using Python and including the openai model. you are currently a robot in Nandi International school at a science and arts exhibition. you know about nandi school and nandi international school which are very good schools in bellary.  try to give answers in very short way, not huge{text}"
    chat = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}]
    )
    response = chat.choices[0].message.content
    return response

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak_response(response):
    engine.say(response)
    engine.runAndWait()

def main():
    while True:
        user_input = get_audio_input()
        if user_input:
            response = get_response_from_chatgpt(user_input)
            print(f"{BOT_NAME}: {response}")
            speak_response(response)

if __name__ == "__main__":
    main()
