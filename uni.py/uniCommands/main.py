from commands import getDate, greetingType, recognizeAudio, setReminder, takeCommand
#getPerson, greeting, greetingType, recognizeAudio, takeCommand, uniResponse, wakeCommand
import wikipedia
import datetime
import pyttsx3 



if __name__ =="__main__":
    greetingType()
    #text = recognizeAudio("how can I help you?")
    while True:
        data = takeCommand().lower()

        if 'who is' in data:
            recognizeAudio('Searching wikipedia')
            data = data.replace('wikipedia', '')
            results = wikipedia.summary(data, sentences=2)
            recognizeAudio('According to Wikipedia')
            print(results)
            recognizeAudio(results)

        elif 'date' in data:
            getDate = datetime.datetime.today().strftime('%b, %d %Y')
            print(getDate)
            recognizeAudio(getDate)

        elif 'time' in data:
            getTime = datetime.datetime.now().strftime('%I:%M' '%p')
            print(getTime)
            recognizeAudio(getTime)

        elif 'reminder' in data:
            remindMe = setReminder
            print(remindMe)
            recognizeAudio(remindMe)



           

       

'''
while True:

    #Record audio
    #text = recognizeAudio()
    #response = ''

    #check for wake phrase
    if(wakeCommand(text) == True):
        #check for greeting
        response = response + greeting(text)

    #check if person mentions date
    if('date' in text):
        getDate = getDate()
        response = response + ' ' + getDate

    #check if person mentions time
    if('time' in text):
        currently = datetime.datetime.currently()
        midDay = ''
        if currently.hour >= 12:
            postMidDay = 'p.m'
            hour = currently.hour - 12
        else:
            currently = 'a.m'
            hour = currently.hour
    
        #convert minute to string
        if currently.minute < 10:
            minute = '0' + str(currently.minute)
        else:
            minute = str(currently.minute)
        response = response + ' ' + 'It is ' + str(hour) + ':' + minute + ' ' + postMidDay + ' .'

    #check if 'who is' is mentioned
    if('who is' in text):
        user = getPerson(text)
        wiki = wikipedia.summary (user, sentences=2)
        response = response + ' ' + wiki 

    #have uni respond back using audio and text 
    uniResponse(response)
'''


        
        

