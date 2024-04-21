GEMINI_API_KEY="AIzaSyAmIckBZH2xuGlJgBaZngLl1xSUdc6sHu0"
OPENAI_API_KEY="sk-proj-PLG55GEuPsGW3glPBGOjT3BlbkFJskR5GPeaFTxvOVj5Ub6v"

model='gemini-1.0-pro'

unkownValueError_Sound="Söylediğiniz Anlaşılmadı Tekrar Deneyiniz"
timeoutError_Sound = "ZamanAşımı Hatası Tekrar Deneyiniz"

helloSound = "Merhaba Size Nasıl Yardımcı Olabilirim ?"

generation_config={
     "temperature":0.5,
     "top_p":1,
     "top_k":1,
     "max_output_tokens":2000,
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



def setModel(model_name):
    global model
    
    if model_name =='gemini-1.0-pro':
          model = 'gemini-pro-vision'
    else:
         model='gemini-1.0-pro'
    
def getModel():
     return model

def getConfig():
     return generation_config

  