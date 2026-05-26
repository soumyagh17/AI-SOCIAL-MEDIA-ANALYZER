from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():

    text = request.form['text']

    analysis = TextBlob(text)

    if analysis.sentiment.polarity > 0:
        result = "Positive 😊"

    elif analysis.sentiment.polarity < 0:
        result = "Negative 😔"

    else:
        result = "Neutral 😐"

    return render_template('index.html', sentiment=result)

if __name__ == '__main__':
    app.run(debug=True)