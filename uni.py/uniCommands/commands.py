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
        print('Google Speech Recognition could not detect this audio')
    except sr.RequestError as e:
        print('Request results from Google Speech Recognition service error' + e)

    return data

#recognizeAudio()

def uniResponse(text):

    print(text)

    myObject = gTTS(text=text, lang='en', slow=False)
    myObject.save('uni_response.mp3')
    os.system('open uni_response.mp3')

#text = 'This is just a test'
#uniResponse(text)

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

def getDate():
    now = datetime.datetime.now()
    todaysDate = datetime.datetime.today()
    weekday = calendar.day_name[todaysDate.weekday()] 
    monthNumber = now.month
    dayNumber = now.day

    #a list of months 
    calendarMonths = ['January', 'February', 'March', 'April', 'May', 
    'June', 'July', 'August', 'September', 'October', 'November', 'December']

    #a list of ordinal numbers
    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th','10th', '11th', '12th', 
    '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th'
    '26th', '27th', '28th','29th', '30th', '31st']

    return 'Today is '+weekday+' '+ calendarMonths[monthNumber - 1] + ' the '+ ordinalNumbers[dayNumber - 1]+ '. '

#print (getDate())