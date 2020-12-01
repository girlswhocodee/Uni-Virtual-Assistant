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
import shutil



#SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


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




























'''
def takeABreak():
    pwd = os.getcwd()
    name = getpass.getuser()
    message = 'Hello'
    notify2.init(message)
    n = notify2.Notification(message+'Take a break')
    task="recognizeAudio "+"'"+message +"I think you need to take a break"+"'" +" -s 150"
    os.system(task)
    n.setUrgency(notify2.URGENCY_NORMAL)
    n.setTimeout(100)
    n.show()
'''

'''
def authenticateGoogleCalendar():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    return service 

def getEvents(day, service):
    # Call the Calendar API
    date = datetime.datetime.combine(day, datetime.datetime.min.time())
    endDate = datetime.datetime.combine(day, datetime.datetime.max.time())
    utc = pytz.UTC
    date = date.astimezone(utc)
    endDate = endDate.astimezone(utc)

    print('Getting the upcoming {n} events')
    events_result = service.events().list(calendarId='primary', timeMin=date.isoformat, timeMax=date.isoformat, singleEvents=True,
    orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        recognizeAudio('No upcoming events found.')
    else:
        recognizeAudio(f'You have {len(events)} events on this day.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        recognizeAudio(start, event['summary'])
        startTime = str(start.split('T')[1].split('-')[0])
        if int(startTime.split(':')[0]) < 12:
            startTime = startTime + 'am'
        else:
            startTime = str(int(startTime.split(':')[0]) -12)
            startTime = startTime + 'pm'

        takeCommand(event['summary'] + 'at' + startTime)


def getDate(text):

    text = text.lower()
    now = datetime.datetime.now()
    todaysDate = datetime.date.today()
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
    #ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th','10th', '11th', '12th', 
    #'13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th'
    #'26th', '27th', '28th','29th', '30th', '31st']

    if text.count('todaysDate') > 0:
        return todaysDate

    day = -1
    dayOfTheWeek = -1
    month = -1
    year = todaysDate.year 

    for word in text.split():
        if word in calendarMonths:
            month = calendarMonths.index(word) + 1
        elif word in calendarDays:
            dayOfTheWeek = calendarDays.index(word)
        elif word.isdigit():
            day = int(word)
        else:
            for ext in dayExtensions:
                found = word.find(ext)
                if found > 0:
                    try:
                        day = int(word[:found])
                    except:
                        pass

    if month < todaysDate.month and month != -1:
        year = year + 1

    if day < todaysDate.day and month == -1 and day != -1:
        month = month + 1

    if month == -1 and day == -1 and dayOfTheWeek != -1:
        currentDayOfWeek = todaysDate.weekday()
        dif = dayOfTheWeek - currentDayOfWeek 

        if dif < 0:
            dif += 7
            if text.count('next') >= 1:
                dif += 7

        return todaysDate + datetime.timedelta(dif)
    if month == -1 or day == -1:
        return None
    return datetime.date(month=month, day=day, year=year)
    

service = authenticateGoogleCalendar()
text = takeCommand()
calendarStrs = ['what do i have', 'do i have plans', 'am i busy']
for phrase in calendarStrs:
    if phrase in text.lower():
        date = getDate(text)
        if date:
            getEvents(date, service)
        else:
            recognizeAudio('Please try again')
'''