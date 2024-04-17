import speech_recognition as sr
import pyttsx3
import os
from gtts import gTTS
from playsound import playsound
from pydub import AudioSegment
from pathlib import Path
from openai import OpenAI

r = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('voice','turkish')


while True:
    
    with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source=source)
            audio = r.listen(source)  
    data = ""
    try :
            data = r.recognize_google(audio,language="tr-TR")
            print("Sonuc:",data)
            tts =gTTS(text=data,lang="tr")
            file_path = "answer.mp3"
            tts.save(file_path)
            playsound('answer.mp3')
            os.remove("answer.mp3")
             
    except sr.UnknownValueError:
            print(" Error")
    except sr.WaitTimeoutError:
            print("Timeout Error") 
    except sr.RequestError as e:
            print("Request Error")
   

                        

   