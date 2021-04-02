# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 10:39:09 2020

@author: Ankur
"""

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os 
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good Morning Sir !")

      
    elif hour >=12 and hour <18:
        speak("Good Afternoon Sir ")
        
    else: 
        speak("Good Evening")
 
    speak(" I am Pinn , An Artificial Neural Network , How May I Help You")

def takeCommand():
    
          
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening to your beautiful voice ")
        r.pause_threshold = 1
        audio = r.listen(source)
         
         
    try:
         print("Recognizing ....")
         query = r.recognize_google(audio, language='en-in')
         print(f"User Said : {query}\n")
         
    except Exception as e :
         print("Say that again please ...  ")
         return "None"
    return query
 

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("youremailaddress@example.com",'your_password')
    server.sendmail("youremailaddress@example.com",to,content)
    


if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query =  takeCommand().lower()
   #logic for executing  command 
        if 'wikipedia' in query :
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
         
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open youtube' in query:
            webbrowser.open("google.com")
            
        elif 'open youtube' in query:
            webbrowser.open("stackoverflow.com")   
            
        elif 'play music' in query:
            music_dir = 'E:\\Total Songs\\new song' 
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
            
        elif 'the time ' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , the time is {strTime}")
            
        
        elif 'open code' in query :
            codePath = "C:\Program Files\Microsoft VS Code\Code.exe"
            os.startfile(codePath)
            
        elif 'email to name' in query :
            try:
                speak("What should iI say ?")
                content = takeCommand()
                to ="recevieremailaddress@example.com"
                sendEmail(to,content)
                speak("Email has been sent !")
            
            except  Exception as e:
                print(e)
                speak("Sorry my friend Luv , I am not able to send this email")
                        
    
  
   
    
    
    