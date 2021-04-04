import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour < 12:
       speak("good morning owais")
    elif hour>=12 and hour<18:
        speak("good afternoon owais")
    else:
        speak("good evening owais")

    speak("iam jarvis sir. please tell me how may i help you")

def takecommand():
    #it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
       print("Recognizing...")
       query = r.recognize_google(audio,language='en-in')
       print(f"user said: {query}\n")

    except Exception as e:
           print(e)
           print("say that again plz")
           return "none"
    return query          
if __name__ == "__main__":
   wishme()
   while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")   

        elif 'open google' in query:
            webbrowser.open("google.com")   
       
        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir='D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[3]))   


#welcome to jarvis

            