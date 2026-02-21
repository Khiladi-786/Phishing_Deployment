from flask import Flask, request, render_template
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load Model
model = joblib.load('model/best_phishing_model.pkl')

def extract_features(url_string):
    # NOTE: In a real production scenario, you must extract ALL 80+ features 
    # from the live URL string exactly as done in the training dataset.
    # For this demo, we will simulate feature extraction or expect pre-calculated input.
    # 
    # Placeholder: Returning random values to match model input shape (87 features)
    # REPLACE THIS with your actual URL feature extraction logic function.
    return np.random.rand(1, 87) 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']
    
    # 1. Preprocess Input
    # (Here we assume the user might input raw features or a URL)
    # For the sake of this template, we assume features are passed or extracted
    features = extract_features(url)
    
    # 2. Predict
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]
    
    result = "PHISHING" if prediction == 1 else "LEGITIMATE"
    color = "red" if prediction == 1 else "green"
    
    return render_template('index.html', 
                           prediction_text=f'Result: {result}', 
                           prob_text=f'Confidence: {probability*100:.2f}%',
                           result_color=color)

if __name__ == "__main__":
    app.run()
