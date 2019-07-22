import pyautogui
import speech_recognition as sr
import pyttsx3
from time import sleep

def play_rickandmorty():
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
    r = sr.Recognizer()
    with sr.Microphone() as source:             
        audio = r.listen(source)                

    try:
        text = r.recognize_google(audio)    
    except LookupError:                          
        print("Could not understand audio")
    return text
