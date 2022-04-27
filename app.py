import sys
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
from flask import Flask
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    """text to speech function"""
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takeCommand():
    """function to convert voice into text"""
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said :  {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

def wish():
    """function to wish the user according to time"""
    _hour = datetime.datetime.now().hour
    if _hour>=0 and _hour<=12:
        speak("Good Morning")
    elif _hour>12 and _hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis Sir, How can i help you?")


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail,com', 587)
    server.ehlo()
    server.starttls()
    server.login('demoxxxxxxx@gmail.com','v@84xxxxx')
    server.sendmail('demoxxxxxx@gmail.com',to, content)
    server.close()




if __name__== "__main__":
    wish()

    while True:
        query = takeCommand().lower()

        if "open notepad" in query:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
                cap.release()
                cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "D:\\personal\\music"
            songs = os.listdir(music_dir)
            # rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir,song))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open google" in query:
            speak("Sir, what should i search on google")
            cm= takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            kit.sendwhatmsg("+9190125xxxxx", "This is test message",16,30)

        elif "play songs on youtube" in query:
            kit.playonyt("Beliya")

        elif "email to chandan" in query:
            try:
                speak("what should i say")
                content = takeCommand().lower()
                to = "mecxxxxxxxx@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent to chandan")

            except Exception as e:
                print(e)

        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day")
            sys.exit()
        speak("Sir, do you have any other work")