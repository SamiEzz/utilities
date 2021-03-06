import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
r = sr.Recognizer()

with sr.Microphone() as source:                # use the default microphone as the audio source
    audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

try:
    engine.say(r.recognize_google(audio, language="fr-FR"))
    engine.runAndWait()
except LookupError:                            # speech is unintelligible
    print("Could not understand audio")