import speech_recognition as sr
import pywhatkit
from playsound import playsound
from gtts import gTTS
from datetime import datetime
import time


def speech(text):
    print(text)
    language = "en"
    output = gTTS(text=text, lang=language, slow=False)
    output.save("./sounds/output.mp3")
    playsound("./sounds/output.mp3")


def check():
    recorder = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.... ")
        audio = recorder.listen(source)

    text = recorder.recognize_google(audio)
    print(f" You Said: {text}")

    if "youtube" in text.lower():
        speech("Okay, Searching For That On YouTube")
        pywhatkit.playonyt(text)

    elif "what is your name" in text.lower():
        speech("My Name is Siri.")

    elif "tell me a joke" in text.lower():
        speech("See Your Self in the Mirror")

    elif "date" in text.lower() or "time" in text.lower():
        now = datetime.now()
        current_date = now.strftime("%d-%m-%Y")
        current_time = now.strftime("%H:%M:%S")
        speech(f"The current date is {current_date} and current time is {current_time}")

    else:  # search on Google
        speech("Okay, Searching For That On Google")
        pywhatkit.search(text)


def assistant():
    recorder = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.... ")
        audio = recorder.listen(source)

    text = recorder.recognize_google(audio)
    print(f" You Said: {text}")

    if "hey siri" in text.lower() or "hello" in text.lower():
        speech("Hello There, How May I Help You?")
        #playsound("./sounds/siri.mp3")
        check()
    else:
        return


assistant()
