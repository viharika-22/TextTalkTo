option= input(" Select the option:\n 1. Speech to text \n 2. Text to Speech\n")
import speech_recognition as sr
from gtts import gTTS
import os
if option =="1":
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('speak now:')
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            print('text:{}'.format(text))
        except:
            print("could not understand")
elif option=="2":
    f=open('ex.txt')
    x=f.read()
    language='en'
    audio=gTTS(text=x,lang=language,slow=False)
    audio.save('ex.wav')
    os.system('ex.wav')

