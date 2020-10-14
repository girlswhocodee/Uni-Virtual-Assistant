# Import the libraries
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia


def recognizeAudio():
    rec = sr.Recognizer()

    with sr.Microphone() as source:
        rec.adjust_for_ambient_noise(source,duration=1)
        print('Hi, how can I help you?')
        audio = rec.listen(source, timeout=10)


    data = ''
    try:
        data = rec.recognize_google(audio)
        print('You said: ' + data)

    except sr.UnknownValueError:
        print('Google Speech Recgonition could not understand the audio')
    except sr.RequestError as e:
        print('Request results from Google Speech Recognition service error' + e)

    return data

#recognizeAudio()

def uniResponse(text):

    print(text)

    myObject = gTTS(text=text, lang='en', slow=False)

