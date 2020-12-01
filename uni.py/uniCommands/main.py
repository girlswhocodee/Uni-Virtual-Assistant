from commands import getCurrentDate, greetingType, recognizeAudio, takeCommand, wakeCommand
import wikipedia
import datetime
import pyttsx3 
import commands
from time import sleep
from datetime import date
import time
import pyjokes
import webbrowser



if __name__ =="__main__":
    #this is the first method that is executed before taking any commands
    greetingType()
    
    while True:
        #converting user data into lowercase
        data = takeCommand().lower()

        #if who is is found in the data, Uni will search wikipedia
        if 'who is' in data:
            recognizeAudio('Searching wikipedia')
            data = data.replace('wikipedia', '')
            results = wikipedia.summary(data, sentences=2)
            recognizeAudio('According to Wikipedia')
            print(results)
            recognizeAudio(results)

        #if date is found in data, Uni will tell us the date
        elif 'date' in data:
            getCurrentDate = datetime.datetime.today().strftime('%b, %d %Y')
            print(getCurrentDate)
            recognizeAudio(getCurrentDate)

        #if time is found in data, Uni will tell us the time
        elif 'time' in data:
            getTime = datetime.datetime.now().strftime('%I:%M' '%p')
            print(getTime)
            recognizeAudio(getTime)

        #if write is found in data, Uni will take notes
        elif "write" in data:
            recognizeAudio("What should i write Mariam?")
            note = takeCommand()
            file = open('uni.txt', 'w')
            recognizeAudio("Should i include the date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%I:%M")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        #if show note is found in data, Uni will open up the text file 
        elif "show note" in data:
            recognizeAudio("Showing Notes")
            file = open("uni.txt", "r") 
            print(file.read())
            recognizeAudio(file.read(10))

        #if joke is found in data, Uni will tell jokes
        elif 'joke' in data:
            recognizeAudio(pyjokes.get_joke())

        #if where is is found in data, Uni will do a google search
        elif "where is" in data:
            data = data.replace('where is', '')
            location = data
            recognizeAudio('Let me look that up for you')
            recognizeAudio(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + '')

        #if youtube is found in data, Uni will open YouTube
        elif 'youtube' in data:
            recognizeAudio('Opening Youtube\n')
            webbrowser.open('youtube.com')

        #if blackboard is found in data, Uni will open the UMBC Blackboard website
        elif 'blackboard' in data:
            recognizeAudio('Opening Blackboard\n')
            webbrowser.open('https://blackboard.umbc.edu/')

        #if who are you is found, Uni will introduce herself
        elif "who are you" in data:
            recognizeAudio("My name is Uni and I am your virtual assistant")
 