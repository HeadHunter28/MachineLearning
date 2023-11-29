import openai
from gtts import gTTS
import os
import tkinter as tk
from tkinter import simpledialog
import urllib.request 

ROOT = tk.Tk()
#ROOT.wm_state('iconic')

# the input dialog
USER_INP = simpledialog.askstring(title="CHAT GPT AUDIO CHATBOT",
                                  prompt="Enter your question? \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t:")





openai.api_key = "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"
language="en"

model_engine = "text-davinci-003"

prompt = USER_INP
            
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
mytext=str(response)
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("youranswer.mp3")
#os.wait(2)
ROOT.withdraw()


os.system("youranswer.mp3") 



print(response)