# Import the libraries
import speech_recognition as sr
import os
import datetime
import warnings
import calendar
import random
import wikipedia
import webbrowser
import pyttsx3 
from pyttsx3 import voice
import pyttsx3.voice
import time



engine = pyttsx3.init('sapi5')


def recognizeAudio(audio):

    en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0"

    # Use female English voice
    engine.setProperty('voice', en_voice_id)
    engine.say(audio)
    engine.runAndWait()
    engine.stop()


def takeCommand():
    rec = sr.Recognizer()

    #open microphone and record
    with sr.Microphone() as source:
        rec.adjust_for_ambient_noise(source,duration=1) #adjust audio to account for ambient noise
        print('Hi, how can I help you Mariam?')
        audio = rec.listen(source, timeout=10) #timeout if no speech is detected after 10 seconds

    #data = ''
    try:
        data = rec.recognize_google(audio, language='en-in')
        print('You said: ' + data)

    except Exception as e:
        recognizeAudio('Could you say that again please...')
        return 'None'
        
    return data


#function for wake phrases
def wakeCommand(text):
    WAKE_PHRASES = ['hey Uni', 'okay Uni']

    #convert text to all lower case words 
    text = text.lower()

    #check to see if command is a wake phrase
    for phrase in WAKE_PHRASES:
        if phrase in text:
            return True
    #executed if wake phrase isn't found in the text
    return False


def getCurrentDate():

    text = text.lower()
    now = datetime.datetime.now()
    todaysDate = datetime.datetime.today()
    weekday = calendar.day_name[todaysDate.weekday()] 
    monthNumber = now.month
    dayNumber = now.day

    #a list of months 
    calendarMonths = ['january', 'february', 'march', 'april', 'may', 
    'june', 'july', 'august', 'september', 'october', 'november', 'december']

    #list of days
    calendarDays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    #day extensions 
    dayExtensions = ['rd', 'th', 'st']

    #a list of ordinal numbers
    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th','10th', '11th', '12th', 
    '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th'
    '26th', '27th', '28th','29th', '30th', '31st']

    return 'Today is '+weekday+' '+ calendarMonths[monthNumber - 1] + ' the '+ ordinalNumbers[dayNumber - 1]+ '. '


#Function to make Uni greet according to the time
def greetingType():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        recognizeAudio('Good Morning!')
    elif hour>=12 and hour<18:
        recognizeAudio('Good Afternoon!')   
    else:
        recognizeAudio('Good Evening!')

    recognizeAudio("How can I help you Mariam?")



def getPerson(text):
    wordList = text.split()
    for i in range (0, len(wordList)):
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'who' and wordList[i+1].lower() == 'is':
            return wordList[i+2] + ' ' + wordList[i+3] 

