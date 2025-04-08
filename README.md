# Disease Prediction Using Machine Learning

This is a web application that predicts the most probable disease based on user-input symptoms using a trained Machine Learning model. It also provides the recommended precautions for the predicted disease.

## Features

- User-friendly web interface to select symptoms
- Predicts disease using a trained ML model
- Suggests three key precautions for the predicted disease
- Validates input: requires at least 3 symptoms for prediction

---

## Tech Stack

- **Backend**: Python, Flask  
- **Frontend**: HTML (via Flask templates)  
- **Machine Learning**: Trained model (loaded from `model_and_symptoms.py`)  
- **Data Handling**: pandas  
- **Model Inputs**: 5 user-selected symptoms  
- **Precautions Source**: `precaution.csv` file  

---
