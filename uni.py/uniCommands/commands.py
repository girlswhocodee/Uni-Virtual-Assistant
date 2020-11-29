# Import the libraries
import speech_recognition as sr
import os
from gtts import gTTS
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
        print('Hi, how can I help you?')
        audio = rec.listen(source, timeout=10) #timeout if no speech is detected after 10 seconds

    #data = ''
    try:
        data = rec.recognize_google(audio, language='en-in')
        print('You said: ' + data)

    except Exception as e:
        recognizeAudio('Could you say that again please...')
        return 'None'
        
    return data

#recognizeAudio()
'''
def uniResponse(text):

    print(text)

    #convert text to speech
    myObject = gTTS(text=text, lang='en', slow=False)

    #saves the converted audio to a file
    myObject.save('uni_response.mp3')
    os.system('start uni_response.mp3')
    #for mac operating system    os.system('open uni_response.mp3')
'''
#text = 'This is just a test'
#uniResponse(text)
'''
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
'''
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
        recognizeAudio('Good Morning!')
    elif hour>=12 and hour<18:
        recognizeAudio('Good Afternoon!')   
    else:
        recognizeAudio('Good Evening!')

    recognizeAudio("How can I help you?")

#print (greetingType())

def setReminder():
    recognizeAudio("What shall I remind you about?")
    text = str(input())
    print("In how many minutes?")
    local_time = float(input())
    local_time = local_time * 60
    time.sleep(local_time)
    print(text)


'''
#Function to return a random greeting response 
def greeting(text):
    # Greeting Inputs
    GREETING_INPUTS = ['hi', 'hey', 'hola', 'greetings', 'wassup', 'hello']
     # Greeting Response back to the user
    GREETING_RESPONSES = ['howdy', 'whats good', 'hello', 'hey there']
     # If the users input is a greeting, then return random response
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + '.'
    # If no greeting was detected then return an empty string
    return ''
'''
'''
def getPerson(text):
    wordList = text.split()
    for i in range (0, len(wordList)):
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'who' and wordList[i+1].lower() == 'is':
            return wordList[i+2] + ' ' + wordList[i+3] 
'''
'''
import sys
import string
from time import sleep
from pyttsx3 import voice, voice, voice


#sa = sys.argv
#lsa = len(sys.argv)
#if lsa != 2:
 #   print("Usage: [ python ] alarm_clock.py duration_in_minutes")
 #   print ("Example: [ python ] alarm_clock.py 10")
  #  print ("Use a value of 0 minutes for testing the alarm immediately.")
   # print ("Beeps a few times after the duration is over.")
    #print ("Press Ctrl-C to terminate the alarm clock early.")
    #sys.exit(1)

try:
    minutes = int(sa[1])
except ValueError:
    print("Invalid numeric value (%s) for minutes" % sa[1])
    print("Should be an integer >= 0")
    sys.exit(1)

if minutes < 0:
    print("Invalid value for minutes, should be >= 0")
    sys.exit(1)

seconds = minutes * 60

if minutes == 1:
    unit_word = " minute"
else:
    unit_word = " minutes"

try:
    if minutes > 0:
        print("Sleeping for " + str(minutes) + unit_word)
        sleep(seconds)
    print("Wake up")
    for i in range(5):
        print(chr(7)),
        sleep(1)
except KeyboardInterrupt:
    print("Interrupted by user")
    sys.exit(1)

'''