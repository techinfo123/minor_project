from flask import Flask, render_template, request
from SentimentAnalyzerEngine import predict_sentiment

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        review = request.form["review"]
        sentiment, emoji = predict_sentiment(review)
        return render_template("predict.html", pred=emoji, sent=sentiment)

if __name__ == "__main__":
    app.run(debug=True)
