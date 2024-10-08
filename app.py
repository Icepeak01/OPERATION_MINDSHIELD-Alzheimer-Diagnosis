from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib
import pandas as pd


def validate_input(data):
    required_fields = ['MMSE', 'FunctionalAssessment', 'MemoryComplaints', 'BehavioralProblems', 'ADL']

    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return False, f"Missing fields: {', '.join(missing_fields)}"

    # Ensure numeric fields are actually numbers
    numeric_fields = ['MMSE', 'FunctionalAssessment', 'MemoryComplaints', 'BehavioralProblems', 'ADL']
    for field in numeric_fields:
        if not isinstance(data[field], (int, float)):
            return False, f"Invalid type for {field}, expected a number"

    return True, None


def return_prediction(model, scaler, data):
    # Convert input data to a DataFrame for scaling and prediction
    input_data = pd.DataFrame([data])

    # Apply the scaler to the input data
    scaled_data = scaler.transform(input_data)

    # Make the prediction using the model
    prediction = model.predict(scaled_data)[0]

    # Interpret the prediction result
    if prediction == 1:
        return "Positive diagnosis for Alzheimer's"
    else:
        return "Negative diagnosis for Alzheimer's"


# Initialize the Flask app
alz = Flask(__name__)

# Load the model and scaler
model = joblib.load('Alzhiemer_model.pkl')
scaler = joblib.load("Alzhiemer_scaler.pkl")


# Route for the homepage
@alz.route('/')
def home():
    return render_template('index.html')


# Route for the diagnosis page (HTML form for input)
@alz.route('/diagnosis')
def diagnosis_page():
    return render_template('diagnosis.html')


# API route to handle the form submission and make predictions
@alz.route('/diagnos', methods=['POST'])
def Alzhiemer():
    content = request.json
    is_valid, message = validate_input(content)
    if not is_valid:
        return jsonify({'error': message}), 400
    
    # Get prediction result
    result = return_prediction(model, scaler, content)

    # Placeholder for ChatGPT integration (to be added later)
    recommendations = "Coming soon!."

    return jsonify({'diagnosis': result, 'recommendations': recommendations})


if __name__ == '__main__':
    alz.run(debug=True)
