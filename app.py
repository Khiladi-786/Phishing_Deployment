from flask import Flask, request, render_template
import joblib
import numpy as np
import os

app = Flask(__name__)

# ----------------------------
# Load model safely (Render compatible)
# ----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "best_phishing_model.pkl")

model = joblib.load(MODEL_PATH)


# ----------------------------
# Feature Extraction (TEMP placeholder)
# ----------------------------
def extract_features(url_string):
    n_features = model.n_features_in_
    return np.random.rand(1, n_features)


# ----------------------------
# Routes
# ----------------------------
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        url = request.form['url']

        features = extract_features(url)

        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1]

        result = "PHISHING" if prediction == 1 else "LEGITIMATE"
        color = "red" if prediction == 1 else "green"

        return render_template(
            'index.html',
            prediction_text=f'Result: {result}',
            prob_text=f'Confidence: {probability*100:.2f}%',
            result_color=color
        )

    except Exception as e:
        return render_template(
            'index.html',
            prediction_text="Error occurred",
            prob_text=str(e),
            result_color="black"
        )


# ----------------------------
# Render requires this
# ----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
