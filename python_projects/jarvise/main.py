import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import time

print("Jarvis Initialising ...")
wish = "Have a Good day mam"

# engine initialised for understaning the text
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# function for speak the text passes to it
def speak_assistance(text):
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    global wish
    if hour >= 0 and hour <= 10:
        wish = "Good Morning miss beautiful"
    elif hour > 10 and hour <=5:
        wish = "Good Evening Katlic"
    else:
        wish = "Good Night Katlic.." 

# Introduction Jarvis
# wish_me()
# speak_assistance(wish)
# speak_assistance("How can I help you ?")


# main program starts from here
def take_command():
    r = sr.Recognizer()
    print("something")
    with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source)
        try:
            print("Recognosation..")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said {query}\n")
        except Exception as e:
            print("Say that again please")
            speak_assistance("Say that again please")


take_command()