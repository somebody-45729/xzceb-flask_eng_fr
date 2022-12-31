from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation # Imported

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_To_French():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    french_text = translator.english_to_french(textToTranslate)
    return french_text

@app.route("/frenchToEnglish")
def french_To_English():
    textToTranslate2 = request.args.get('textToTranslate2')
    # Write your code here
    english_text = translator.french_to_english(textToTranslate2)
    return english_text

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
