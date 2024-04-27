from dotenv import load_dotenv
import os

def configure():
     load_dotenv()
  

configure()
#GEMINI_API_KEY=os.getenv('GEMINI_API_KEY')
#OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')

gemini_model='gemini-1.0-pro'

unkownValueError_Sound="Söylediğiniz Anlaşılmadı Tekrar Deneyiniz"
timeoutError_Sound = "ZamanAşımı Hatası Tekrar Deneyiniz"


text_helloSound = "Size Nasıl Yardımcı Olabilirim ?"
image_helloSound = "Merhaba Size Nasıl Bir Görsel Üreteyim ?"

choice_helloSound ="Merhaba Ben Hamilton , 'Asistan' Veya 'Resim' Diyerek Seçim Yapınız "

generation_config={
     "temperature":0.5,
     "top_p":1,
     "top_k":1,
     "max_output_tokens":2020
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

dallE_model="dall-e-3"
dallE_size="1024x1024"

choice =""

special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
def setChoice(c):
     global choice
     choice = c
     
def getChoice():
      return choice
def getModel():
     return gemini_model
def getConfig():
     return generation_config

  
