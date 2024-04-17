import google.generativeai as genai
import os
import credentials
import PIL.Image
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from pydub import AudioSegment

GOOGLE_API_KEY = credentials.GEMINI_API_KEY
genai.configure(api_key=GOOGLE_API_KEY)

r = sr.Recognizer()

model=genai.GenerativeModel(credentials.getModel()) 

def SpeecherrorSound(e):
         errorSound = e
         print(f">> {errorSound}")
         tts=gTTS(text=errorSound,lang="tr")
         file_path="answer.mp3"
         tts.save(file_path)
         playsound('answer.mp3')
         os.remove("answer.mp3")
         
def inputPrompt():
    file_path=""
    errorSound = ""
    helloSound = credentials.helloSound
    while True:
        with sr.Microphone() as source:

            print(f"{helloSound}")
            audio=r.listen(source)
            os.remove
            data=""
            try:
                data = r.recognize_google(audio,language="tr-TR")
            except sr.UnknownValueError:
                errorSound = credentials.unkownValueError_Sound
                print(f">> {errorSound}")
                SpeecherrorSound(errorSound)
            except sr.WaitTimeoutError:
                errorSound = credentials.timeoutError_Sound
                print(f">> {errorSound}")
                SpeecherrorSound(errorSound)
        if data:
             break 
    print(">>",data)
    response=model.generate_content(data)
    print(">>",response.text)

    return response.text
def speechPrompt(response):
        tts=gTTS(text=response,lang="tr")
        file_path="answer.mp3"
        tts.save(file_path)
        playsound('answer.mp3')

def filterResponse(r):
     print(type(response))
     r =""
     for i in response:
          if i =="*":
               continue
          r+=i
     return r
               
     
while True:
     response = inputPrompt()
     speechPrompt(filterResponse(response))
     os.remove("answer.mp3")
     