# importing Flask and other modules
from flask import Flask, request, render_template

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from googletrans import Translator
 
# Flask constructor
app = Flask(__name__)  
 
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with input in HTML form
       words = request.form.get("input")

       tokenizer = AutoTokenizer.from_pretrained("roberta-base-openai-detector")
       model = AutoModelForSequenceClassification.from_pretrained("roberta-base-openai-detector")

       translator = Translator()
       translated_text = translator.translate(words, dest='en')
       
       inputs = tokenizer(translated_text.text, return_tensors="pt")
       with torch.no_grad():
            logits = model(**inputs).logits
       
       predicted_class_id = logits.argmax().item()
       results = model.config.id2label[predicted_class_id]

       return "The result is "+results
    return render_template("form.html")
 
if __name__=='__main__':
   app.run()