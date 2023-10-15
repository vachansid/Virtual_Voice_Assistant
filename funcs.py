import pyttsx3
import speech_recognition as sr
from speech import *
import time
from datetime import datetime
import pywhatkit as kit
import wikipedia
import pyautogui
import time
import json
pyautogui.FAILSAFE = False

bluetooth=(1661,459)
hotspot=(1548,700)
night_light=(1803,574)

def search_wiki(query):
    results = wikipedia.summary(query, sentences=2)
    return results

def play_on_youtube(video):
    kit.playonyt(video)

def search_on_google(query):
    kit.search(query)    

def show_desktop():
    x=(1919,1079)
    pyautogui.moveTo(x[0],x[1])
    pyautogui.click()

def close_tab():
    show_desktop()
    x=(836,1061)
    pyautogui.moveTo(x[0],x[1])
    pyautogui.click()
    pyautogui.hotkey('ctrl','w')

def action_centre(o):
    x=(1757,1051)
    pyautogui.moveTo(x[0],x[1])
    pyautogui.click() 
    if(o==1):
        x=bluetooth
    elif (o==2):
        x=hotspot
    else: x=night_light
    pyautogui.moveTo(x[0],x[1])
    time.sleep(0.5)
    pyautogui.click() 
    x=(1539,1042)
    pyautogui.moveTo(x[0],x[1])
    pyautogui.click() 

def q_and_a_train(query):
    try:
        idx1 = query.index('say')
        idx2 = query.index('answer')
        ques = query[idx1 + len('say') + 1: idx2-1]
        ans=query[idx2+len('answer')+1:]
        with open('data.json', 'r') as fp:
            q_dict=json.load(fp)
        all_keys=list(q_dict.keys())
        if ques in all_keys:
            q_dict[ques].append(ans)
        else:
            q_dict[ques]=[ans]
        with open('data.json', 'w') as fp:
            json.dump(q_dict, fp)
        return True    
    except:
        speak("Sorry Sir, could you please say it again")   
        return False 
    
if __name__=="__main__":
    q_and_a_train("when i say how are you answer iam fine")
    q_and_a_train("when i say how are you answer iam fine")


