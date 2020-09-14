import pyautogui
from time import sleep

# image = pyautogui.screenshot(region=(13,184,200,30),imageFilename="messages.png")
def Get_notif():
    location = pyautogui.locateOnScreen('C:/Users/sezzerouali/OneDrive - Amadeus Workplace/Documents\code/asserv/msg.png')
    #print(location)
    if (location==None):
        print("new message\n")

def chopper():
    k=0
    pyautogui.FAILSAFE = 0
    while 1:
        sleep(0.5)
        pyautogui.press("right")
        k+=1
        #Get_notif()
        if(k>1000):
            k=0
            pyautogui.press("f5")
        

chopper()
