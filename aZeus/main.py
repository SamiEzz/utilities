import pyautogui
import speech_recognition as sr
import pyttsx3
import functions
import json
from time import sleep


engine = pyttsx3.init()

def task_run(id):
    with open('d:/CODE/git/utilities/aZeus/ressources/tasks.json') as json_tasks:
        data = json.load(json_tasks)
        
        for task in data['tasks']:
            for i in task:
                print(i+" : "+str(task[i]))


def play_youtube_pl_rap():    
    print("play_rickandmorty")
    k=2
    pyautogui.hotkey('win','r')
    pyautogui.typewrite("chrome www.youtube.com/watch?v=t7lM7Bn16Zg&list=PLfAtJsXDs3i7uCqZLGZKNklmoUqrIvyt7\n")
    sleep(k*2)
    pyautogui.hotkey('win','up')


def play_rickandmorty():
    print("play_rickandmorty")
    k=2
    pyautogui.hotkey('win','r')
    pyautogui.typewrite("chrome www.netflix.com\n")
    sleep(k*2)
    pyautogui.hotkey('win','up')

    pyautogui.click(358,534)
    sleep(k*1)
    pyautogui.click(1083,136)
    pyautogui.typewrite("Rick and morty")
    sleep(k*2)
    pyautogui.click(217,270)
    sleep(k*1)
    pyautogui.click(217,270)
    sleep(k*2)
    pyautogui.press("f11")

def record_cmd():
    #engine.say("Que puis-je faire pour vous sidi Sami")
    #engine.runAndWait()
    print("record_cmd")

    r = sr.Recognizer()
    with sr.Microphone() as source:             
        audio = r.listen(source,timeout=3)   

    try:
        text = r.recognize_google(audio,language='FR-fr')
        #text = r.recognize_google(audio)
            
        print(text)
    except LookupError:                          
        print("Could not understand audio")
    print("end recording !")
    return text



def main():
    print("main")
    command = record_cmd()
    print(command)
    
    if(command=="Rick et Morty"):
        engine.say("Prépare toi Sami à regarder ta série préférer : Rick et morty !")
        engine.runAndWait()
        play_rickandmorty()
    elif(command=="ma playlist rap"):
        engine.say("Prépare toi sidi Sami à écouter du lourd wesh ! ")
        engine.runAndWait()
        play_youtube_pl_rap()
        
# while(1):
#     main()
#     sleep(1)

task_run(0)