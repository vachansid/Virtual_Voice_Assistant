import pyttsx3
import speech_recognition as sr
from speech import *
from funcs import *
import pyautogui
import time
import random as rand
pyautogui.FAILSAFE = False

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 180)
engine.setProperty('volume', 1)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
with open('data.json', 'r') as fp:
    qdb=json.load(fp)
all_ques=list(qdb.keys())

while True:
    query=take_user_input().lower()
    if 'hello luna' in query or 'hey luna' in query:
        greet_user("Sir")
        while True:
            query_1=take_user_input().lower()
            if query_1 in all_ques:
                qlen=len(qdb[query_1])
                r_index=rand.randrange(qlen)
                print(qdb[query_1][r_index])
                speak(qdb[query_1][r_index])
                continue
            if 'luna' == query_1:
                speak("Sir")
                continue
            if 'search' in query_1 and 'google' in query_1 :
                idx1 = query_1.index('search')
                idx2 = query_1.index('on')
                res = query_1[idx1 + len('search') + 1: idx2]
                search_on_google(res)
            if 'play' in query_1 and 'on' in query_1 :
                idx1 = query_1.index('play')
                idx2 = query_1.index('on')
                res = query_1[idx1 + len('play') + 1: idx2]
                play_on_youtube(res)
            
            elif 'play' in query_1:
                play_on_youtube(query_1.split('play')[1])
            if 'show desktop' in query_1:
                show_desktop()
            if 'when i say' in query_1:
                if q_and_a_train(query_1):
                    with open('data.json', 'r') as fp:
                        qdb=json.load(fp)
                    all_ques=list(qdb.keys())
                    speak("added to my database Sir")
            if 'close tab' in query_1:
                close_tab()    
            if 'hotspot' in query_1:
                action_centre(2)
            if 'bluetooth' in query_1:
                action_centre(1)
            if 'night light' in query_1:
                action_centre(3)                 
            if 'take rest'==query_1:
                speak('thank you sir but I am always glad to speak to you')
                break    
            if 'full screen' in query_1 :
                pyautogui.press('f')
                
            elif 'pause' in query_1:
                pyautogui.press('space')
            elif 'resume' in query_1:
                pyautogui.press('space')
             

    if 'go home' in query:
        speak('Thanks for letting me sleep Sir')
        speak('Bye Sir, but I am always ready to serve you sir')
        break
   

