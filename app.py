# importing Flask and other modules
from flask import Flask, request, render_template

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from googletrans import Translator
 
# Flask constructor
app = Flask(__name__)  
 
@app.route('/')
def home():
    return render_template('form.html')

# A decorator used to tell the application
# which URL is associated function
@app.route('/predict', methods =["GET", "POST"])
def predict():
    if request.method == "POST":
       # getting input with input in HTML form
      #  words = request.form.get("input")
       words = request.form
       for k, v in words.items():
          val = v

       tokenizer = AutoTokenizer.from_pretrained("roberta-base-openai-detector")
       model = AutoModelForSequenceClassification.from_pretrained("roberta-base-openai-detector")

       translator = Translator()
       translated_text = translator.translate(val, dest='en')
         
       inputs = tokenizer(translated_text.text, return_tensors="pt")
       with torch.no_grad():
          logits = model(**inputs).logits
         
       predicted_class_id = logits.argmax().item()
       results = model.config.id2label[predicted_class_id]

      #  return "Hasilnya adalah "+results
    return render_template("form.html", val=translated_text, results=results)
#      return render_template("form.html", results=results)
 
if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=3000)
