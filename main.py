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
import sys
import time


GOOGLE_API_KEY = credentials.GEMINI_API_KEY
OPENAI_API_KEY=credentials.OPENAI_API_KEY


genai.configure(api_key=GOOGLE_API_KEY)


client_OpenAI = OpenAI(api_key=OPENAI_API_KEY)

r = sr.Recognizer()


model=genai.GenerativeModel(model_name=credentials.getModel(),
                            generation_config=credentials.generation_config,
                            safety_settings=credentials.safety_settings ) 


history = model.start_chat(history=[])



def _Print(s,p):
      print(f"{s}: >> {p}")


def getUserSpeech(sound):
    with sr.Microphone() as source:
        _Print("Hamilton", sound)
        speech(sound)
        _Print("Hamilton", "Dinliyorum...")
        audio = ""
        start_time = time.time() 
        while time.time()-start_time<5: 
              audio = r.listen(source)
              if audio:
                    break
              if not audio:
                errorSound = credentials.timeoutError_Sound
                _Print("Hamilton", errorSound)
                speech(errorSound)                         
    try:
        return r.recognize_google(audio, language="tr-TR")
    except sr.UnknownValueError:
        errorSound = credentials.unkownValueError_Sound
        _Print("Hamilton", errorSound)
        speech(errorSound)
        return None
                   
                  
def inputPrompt(choice):
    file_path = ""
    errorSound = ""
    helloSound = credentials.text_helloSound if choice == "asistan" else credentials.image_helloSound
    while True:
        prompt = getUserSpeech(helloSound)       
        if prompt or prompt != None:
            if prompt == "seçim değiştir":
                            _Print("Siz", prompt)
                            setChoice() 
                            inputPrompt(credentials.getChoice())
            elif prompt =="Programı kapat":
                        _Print("Hamilton","Program Kapatılıyor ...")
                        speech("Program Kapatılıyor")
                        sys.exit()
            if choice == "asistan":
                        try:
                            _Print("Siz", prompt) 
                            response = model.generate_content(prompt)  
                            _Print("Hamilton", response.text) 
                            speech(filterResponse(response.text))  
                            history.send_message(prompt)
                        except ValueError :
                            _Print("Hamilton", "Bir hata oluştu !")
                          

            elif choice == "resim":
                            _Print("Siz", prompt)
                            _Print("Hamilton", "Görsel Oluşturuluyor...")
                            try:
                                image_url = client_OpenAI.images.generate( 
                                    model=credentials.dallE_model,
                                    prompt=prompt,
                                    size=credentials.dallE_size,
                                    quality="standard",
                                    n=1
                                )
                                response = image_url.data[0].url 
                                requestImage(response)       
                            except Exception as e:
                                _Print(f"Hamilton","Hata Oluştu ! {e}")                
    return response


def requestImage(response):
      r=requests.get(response) 
      try:
        image_data = BytesIO(r.content) 
        img = Image.open(image_data) 
        _Print("Hamilton","Görsel Başarıyla Oluşturuldu !")
        img.show() 
      except Exception as e :
           _Print(f"Hamilton","Hata Oluştu ! {e}")

            
def speech(text):
        tts=gTTS(text=text,lang="tr") 
        file_path="answer.mp3" 
        tts.save(file_path) 
        playsound('answer.mp3') 
        os.remove("answer.mp3") 


def filterResponse(response):
     special_characters=credentials.special_characters
     r =""
     for i in response:
          if i in special_characters:
               continue
          r+=i
     return r


def setChoice():
    choice =""
    helloSound = credentials.choice_helloSound 
    while True:
        choice = getUserSpeech(helloSound)  
        if choice or choice != None:  
                if choice in ["asistan", "resim"]: 
                        choice.lower()
                        _Print("Siz",choice)
                        credentials.setChoice(choice)
                        inputPrompt(credentials.getChoice())
                        break
                elif choice =="Programı kapat":
                    _Print("Hamilton","Program Kapatılıyor ...")
                    speech("Program Kapatılıyor")
                    sys.exit()

setChoice()

          
          


    
   
    
     

