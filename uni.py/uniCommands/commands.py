# Import the libraries
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia
import pyaudio
import webbrowser
#import pyttsx3
#from pyttsx3 import voice


#engine = pyttsx3.init('pyaudio')
#voices = engine.getProperty('voices') #getting details of the current voice
#engine.setProperty('voice', voice[0].id)

#def speak(audio):
    #pass

#pyaudio.get_portaudio_version()
#p = pyaudio.PyAudio() 

#Record audio and return it as a string
def recognizeAudio():
    rec = sr.Recognizer()

    #open microphone and record
    with sr.Microphone() as source:
        rec.adjust_for_ambient_noise(source,duration=1) #adjust audio to account for ambient noise
        print('Hi, how can I help you?')
        audio = rec.listen(source, timeout=10) #timeout if no speech is detected after 10 seconds

    #Use Google Speech Recognition
    data = ''
    try:
        data = rec.recognize_google(audio)
        print('You said: ' + data)

    #check for unknown errors
    except sr.UnknownValueError:
        print('Could not detect this audio')
    except sr.RequestError as e:
        print('Could not request results' + e)

    return data

#recognizeAudio()

#function to get Uni response
def uniResponse(text):

    print(text)

    #convert text to speech
    myObject = gTTS(text=text, lang='en', slow=False)

    #saves the converted audio to a file
    myObject.save('uni_response.mp3')

    #plays converted file
    os.system('open uni_response.mp3') #use "start" for windows operating system

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

#function to get current date
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

#Function to make Uni greet according to the time
def greetingType():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        return('Good Morning!')
    elif hour>=12 and hour<18:
        return('Good Afternoon!')   
    else:
        return('Good Evening!')

#print (greetingType())