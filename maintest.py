import google.generativeai as genai
import os
import credentials
import PIL.Image
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from pydub import AudioSegment
from openai import OpenAI
import credentials
import requests
from io import BytesIO
from PIL import Image

GOOGLE_API_KEY = credentials.GEMINI_API_KEY
OPENAI_API_KEY=credentials.OPENAI_API_KEY
genai.configure(api_key=GOOGLE_API_KEY)
client_OpenAI = OpenAI(api_key=OPENAI_API_KEY)

r = sr.Recognizer()

model=genai.GenerativeModel(model_name=credentials.getModel(),
                            generation_config=credentials.generation_config,
                            safety_settings=credentials.safety_settings ) 

history = model.start_chat(history=[])

def SpeechErrorSound(e):
         errorSound = e
         print(f">> {errorSound}")
         tts=gTTS(text=errorSound,lang="tr")
         file_path="answer.mp3"
         tts.save(file_path)
         playsound('answer.mp3')
         os.remove("answer.mp3")
         
def inputPrompt(choice):
    file_path=""
    errorSound = ""
    helloSound = credentials.helloSound
    while True:
        with sr.Microphone() as source:

            print(f"Hamilton : >> {helloSound}")
            audio=r.listen(source,timeout=10)
            os.remove
            data=""
            try:
                data = r.recognize_google(audio,language="tr-TR")
            except sr.UnknownValueError:
                errorSound = credentials.unkownValueError_Sound
                print(f">> {errorSound}")
                SpeechErrorSound(errorSound)
            except sr.WaitTimeoutError:
                errorSound = credentials.timeoutError_Sound
                print(f">> {errorSound}")
                SpeechErrorSound(errorSound)
        if data:
             break 
    if choice =="asistan":
            print("Siz : >>",data)
            response=model.generate_content(data)
            print("Hamilton : >>",response.text)

    if choice =="resim":   
            print("Siz : >>",data)
            image_url = client_OpenAI.images.generate(
            model=credentials.dallE_model,
            prompt=data,
            size=credentials.dallE_size,
            quality="standard",
            n=1, )
            response = image_url.data[0].url
    return response

def requestImage(response):
      r=requests.get(response)
      if r.status_code==200:
        image_data = BytesIO(r.content)
        img = Image.open(image_data)
        img.show()
      else:
        print("Resim indirilemedi. Hata kodu:", response.status_code)
                 
def speechPrompt(response):
        tts=gTTS(text=response,lang="tr")
        file_path="answer.mp3"
        tts.save(file_path)
        playsound('answer.mp3')

def filterResponse(response):
     print(type(response))
     r =""
     for i in response:
          if i =="*":
               continue
          r+=i
     return r

def setChoice():
    choice =""
    while True: 
        with sr.Microphone() as source:
            print("Hamilton : >> Merhaba Ben Hamilton , 'Asistan' Veya 'Resim' Diyerek Seçim Yapınız ")
            audio=r.listen(source,timeout=5)
            try:
                print("Hamilton : >> Dinliyorum")
                choice = r.recognize_google(audio,language="tr-TR")
            except sr.UnknownValueError:
                        errorSound = credentials.unkownValueError_Sound
                        SpeechErrorSound(errorSound)
            except sr.WaitTimeoutError:
                        errorSound = credentials.timeoutError_Sound
                        SpeechErrorSound(errorSound)
            if choice =="asistan" or choice =="resim": 
                  choice.lower()                  
                  break 
    return choice
    
            
while True:
      choice = setChoice()
      if choice =="asistan":
            response=inputPrompt(choice)
            speechPrompt(filterResponse(response.text))
            os.remove("answer.mp3")
      if choice =="resim":
            response=inputPrompt(choice)
            requestImage(response)
            
    

          
          


    
   
    
     

