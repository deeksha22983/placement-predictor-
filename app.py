# app.py
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Securely load the saved Random Forest classification model
with open('placement_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Extract form inputs strictly as numerical values
            cgpa = float(request.form['cgpa'])
            placement_exam_marks = float(request.form['placement_exam_marks'])

            # Align inputs into a 2D array for the scikit-learn model
            features = np.array([[cgpa, placement_exam_marks]])
            
            # Predict status (0 = Not Placed, 1 = Placed)
            prediction = model.predict(features)[0]
            
            if prediction == 1:
                result_text = "Placed 🎉"
            else:
                result_text = "Not Placed 😔"

            return render_template('index.html', prediction_text=f'Placement Status: {result_text}')
        except Exception as e:
            return render_template('index.html', prediction_text="Error: Please verify your input parameters.")

if __name__ == '__main__':
    app.run(debug=True)