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

def inputPrompt():
    while True:
        with sr.Microphone() as source:
            print("Birşey Söyleyin")
            audio=r.listen(source)
            data = ""
            try:
                data = r.recognize_google(audio,language="tr-TR")
            except sr.UnknownValueError:
                print(">> Söylediğiniz Anlaşılmadı")
            except sr.WaitTimeoutError:
                print(">> ZamanAşımı Hatası")
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

while True:
     response = inputPrompt()
     speechPrompt(response)
     os.remove("answer.mp3")
     




