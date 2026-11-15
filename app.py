
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained machine learning model
model = pickle.load(open("spam_model.pkl", "rb"))

# Load TF-IDF vectorizer
tfidf = pickle.load(open("tfidf_vectorizer.pkl", "rb"))


# Home page
@app.route('/')
def home():
    return render_template('index.html')


# Predict spam or genuine message
@app.route('/predict', methods=['POST'])
def predict():

    # Get message entered by user
    message = request.form.get('message', '').strip()

    # Check empty message
    if not message:
        return render_template(
            'index.html',
            message=message,
            result="Please enter a message!",
            result_type="error"
        )

    # Convert message into TF-IDF numerical features
    message_tfidf = tfidf.transform([message])

    # Check whether message contains known vocabulary
    if message_tfidf.nnz == 0:
        return render_template(
            'index.html',
            message=message,
            result="Unable to classify. Please enter meaningful text.",
            result_type="error"
        )

    # Predict message category
    prediction = model.predict(message_tfidf)[0]

    # Calculate spam probability
    spam_index = list(model.classes_).index('spam')

    spam_score = model.predict_proba(message_tfidf)[0][spam_index] * 100

    # Display prediction
    if prediction == 'spam':

        result = "SPAM MESSAGE DETECTED!"

        result_type = "spam"

    else:

        result = "THIS IS NOT SPAM!"

        result_type = "ham"

    # Send prediction to website
    return render_template(
        'index.html',
        message=message,
        result=result,
        result_type=result_type,
        spam_score=round(spam_score, 2)
    )


# Run Flask application
if __name__ == '__main__':

    app.run(
        host='127.0.0.1',
        port=5007,
        debug=False
    )
