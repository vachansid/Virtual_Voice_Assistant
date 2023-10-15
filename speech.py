import speech_recognition as sr
import pyttsx3
import time
from datetime import datetime
engine_d = pyttsx3.init('sapi5')
engine_d.setProperty('rate', 180)
engine_d.setProperty('volume', 1)
voices_d = engine_d.getProperty('voices')
engine_d.setProperty('voice', voices_d[1].id)

def speak(text,engine=engine_d):
    engine.say(text)
    engine.runAndWait()

def greet_user(USERNAME,engine=engine_d):
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}",engine)
        speak("I am very happy to see you Sir")
        time.sleep(0.5)
        speak("Oh Wait, Actually I cannot see you Sir as you didn't give me access to your webcam Sir")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
        speak("Did you have your Lunch Sir")
        time.sleep(0.5)
        speak("Sometimes I feel like eating real food Sir")
    elif (hour >= 16) :
        speak(f"Good Evening {USERNAME}")
        speak("Hope your day went as planned Sir")
    else :
        speak("good to see you awake Sir")
        time.sleep(0.5)
        speak("I thought I am the only one awake")
        
def take_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
    except Exception:
        # speak('Sorry Sir, I could not understand. Could you please say that again?')
        query = 'None'
    return query    


