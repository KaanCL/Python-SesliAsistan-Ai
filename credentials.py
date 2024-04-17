GEMINI_API_KEY="AIzaSyAmIckBZH2xuGlJgBaZngLl1xSUdc6sHu0"

model='gemini-1.0-pro'

generation_config={
     "tempature":0.5,
     "top_p":0.3,
     "top_k":0.6,
     "max_output_tokens":1050
}

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

  