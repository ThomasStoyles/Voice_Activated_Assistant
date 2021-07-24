import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import secrets
import random
import numpy as np

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say('Hi Thomas, How can i assist you')
engine.runAndWait()


# code if wanted to change voice ATM will change to female
# Voices = engine.getProperty('voices')
# engine.setProperty('voice', Voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def taking_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            # listen to the microphone as a source
            voice = listener.listen(source)
            # uses google API to listen
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                # removes the need to say jarvis
                command = command.replace('jarvis', '')
                print(command)

    except:
        pass
    return command


def run():
    command = taking_command()
    if 'play' in command:
        song = command.replace('play', '')
        song = command.replace('jarvis', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song, use_api=True)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'tell me about' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'vision' in command:
        PO = ['what is a vision ?', 'Where is the soul stone ?', 'Am i alive ?']
        talk(secrets.choice(PO))

    else:
        talk('Please say that again.')


while True:
    run()
