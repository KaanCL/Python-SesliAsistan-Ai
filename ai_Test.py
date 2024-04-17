import google.generativeai as genai
import os
import credentials
import PIL.Image

GOOGLE_API_KEY=credentials.GEMINI_API_KEY
genai.configure(api_key=GOOGLE_API_KEY)

img = PIL.Image.open('yeni-baslayanlar1.png')
modelName=credentials.getModel()
model =genai.GenerativeModel( modelName)


while True:
    print(credentials.getModel())
    prompt=(input(">>"))
    if prompt=='a':
        credentials.setModel(credentials.getModel())
        model=genai.GenerativeModel(credentials.getModel())
        response = model.generate_content(img)
        credentials.setModel(credentials.getModel())
    else:
     model=genai.GenerativeModel(credentials.getModel())
     response = model.generate_content(prompt)   
    print(response.text)


   
    
