
import os
import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

today = datetime.date.today()
hour = int(datetime.datetime.now().hour)
print()

if hour>=0 and hour <12:
    speak("Good Morning")
    print("Good Morning.")

elif hour>=12 and hour <17:
    speak("Good Afternoon.")
    print("Good Afternoon.")

else:
    speak("Good Evening")
    print("Good Evening.")    

print("I am Alfred and I am an AI Assitant and can perform a few tasks for you !")
speak("I am Alfred")
speak("I am an AI Assistant and can perform a few tasks for you !")
print()
print("Today's Date is :")
speak("Today's Date is :")
speak(today)
print(today)


speak("I will help you to, open Chrome, Windows Media Player, Calculator, Notepad, Control Panel, Settings. If you want, I can also open Lightroom , Spotify or Zoom App for you")
speak("So, tell me, what can I do for you ? ")
print()
print()

def takeCommand():
     r = sr.Recognizer()
     with sr.Microphone() as source:
          print("I'm listening")
          r.pause_threshold = 1
          audio = r.listen(source)

     try:
          print("Recognizing..")
          p = r.recognize_google(audio, language='en-in')
          print("User said : ",p) 
     except Exception as e:
          print("I did not get you.")
          pyttsx3.speak("I did not get you.")
     
       
     return p
 
 
if __name__ =="__main__":
     while True:
          p = takeCommand().lower()
          if(("do not" not in p) and ("dont" not in p) and ("don't" not in p)) and ((("run" in p) or ("execute" in p) or ("open" in p)) and (("chrome" in p) or ("browser" in p) or ("search engine" in p) or ("google" in p))):
               pyttsx3.speak("Opening Google Chrome")
               os.system("chrome")

 

          elif(("do not" not in p) and ("dont" not in p) and ("don't" not in p)) and ((("run" in p) or ("execute" in p) or ("open" in p)) and (("player" in p) or ("media player" in p) or ("audio player" in p) or ("video player" in p))):
               pyttsx3.speak("Opening Windows Media Player")
               os.system("wmplayer")



          elif(("do not" not in p) and ("dont" not in p) and ("don't" not in p)) and ((("run" in p) or ("execute" in p) or ("open" in p)) and (("editor" in p) or ("notepad" in p) or ("text editor" in p) or ("writer" in p))):
               pyttsx3.speak("Opening Notepad")
               os.system("notepad")


          elif(("do not" not in p) and ("dont" not in p) and ("don't" not in p)) and ((("open" in p) or ("run" in p) or ("execute" in p)) and (("control panel" in p) or ("hardware settings" in p) or ("software settings" in p) or ("user control settings" in p) or ("controlpanel" in p))):
               pyttsx3.speak("Opening Control Panel")
               os.system("control panel")


          elif(("do not" not in p) and ("dont" not in p) and ("don't" not in p)) and ((("open" in p) or ("run" in p) or ("want" in p)) and (("lightroom" in p) or ("edit" in p) or ("picture" in p))):
               pyttsx3.speak("Opening Adobe Lightroom")
               os.system("lightroom")


          elif(("do not" not in p) and ("dont" not in p) and ("don't" not in p)) and ((("open" in p) or ("run" in p) or ("execute" in p)) and (("computer settings" in p) or ("settings" in p) or ("pc settings" in p))):
               pyttsx3.speak("Opening System Settings")
               os.system("start ms-settings:")



          elif(("do not" not in p) and ("dont" not in p) and ("don't" not in p)) and ((("open" in p) or ("play" in p) or ("want" in p)) and (("spotify" in p) or ("music" in p) or ("song" in p))):
               pyttsx3.speak("Opening Spotify")
               os.system("spotify")



          elif(("do not" not in p) and ("dont" not in p) and ("don't" not in p)) and ((("open" in p) or ("play" in p) or ("want" in p)) and (("calculator" in p) or ("add" in p) or ("subtract" in p) or ("multiply" in p) or ("divide" in p) or ("numbers" in p))):
               pyttsx3.speak("Opening Calculator")
               os.system("calc")



          elif(("do not" not in p) and ("dont" not in p) and ("don't" not in p)) and ((("run" in p) or ("execute" in p) or ("open" in p)) and (("video call" in p) or ("zoom app" in p) or ("zoom" in p) or ("video conference" in p))):
               pyttsx3.speak("Opening Zoom App")
               os.system("zoom")

          
          elif(("wikipedia" in p) or ("who"in p) or ("tell" in p)):
               speak("Searching Wikipedia")
               p = p.replace("wikipedia", "")
               result = wikipedia.summary(p, sentences = 2)
               speak("According to Wikipedia")
               print(result)
               speak(result)

     


          elif("exit" in p) or ("close" in p) or ("quit" in p):
               pyttsx3.speak("Thank you Sir, goodbye, have a nice day ahead")
               print("Thank you Sir, goodbye, have a nice day ahead.")
               break
                
          elif("shutdown" in p):
               pyttsx3.speak("All Shutting down sequence starrting sir;process killing complete sir , Have a nice day")
                os.system('shutdown -s')


          else:
               pyttsx3.speak("I don't know how to do this")
               print("Try again !")
