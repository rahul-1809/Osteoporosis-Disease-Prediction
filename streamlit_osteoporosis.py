import streamlit as st
import joblib
import pandas as pd

# Load the trained model
def load_model():
    return joblib.load("osteoporosis_model.joblib")

# Predict function
def predict(model, input_data):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)[:, 1]
    return prediction[0], probability[0]

# Streamlit UI
st.title("Osteoporosis Prediction App")
st.write("Enter patient data to predict osteoporosis risk.")

# Input fields
age = st.number_input("Age", min_value=18, max_value=100, value=50)
gender = st.selectbox("Gender", ["Male", "Female"])
hormonal_changes = st.selectbox("Hormonal Changes", ["Normal", "Postmenopausal"])
family_history = st.selectbox("Family History", ["Yes", "No"])
race_ethnicity = st.selectbox("Race/Ethnicity", ["Asian", "Caucasian", "African American", "Other"])
body_weight = st.selectbox("Body Weight", ["Underweight", "Normal", "Overweight", "Obese"])
calcium_intake = st.selectbox("Calcium Intake", ["Low", "Adequate", "High"])
vitamin_d_intake = st.selectbox("Vitamin D Intake", ["Insufficient", "Sufficient"])
physical_activity = st.selectbox("Physical Activity", ["Sedentary", "Active"])
smoking = st.selectbox("Smoking", ["Yes", "No"])
alcohol_consumption = st.selectbox("Alcohol Consumption", ["None", "Moderate", "High"])
medical_conditions = st.selectbox("Medical Conditions", ["None", "Rheumatoid Arthritis", "Hyperthyroidism"])
medications = st.selectbox("Medications", ["None", "Corticosteroids"])
prior_fractures = st.selectbox("Prior Fractures", ["Yes", "No"])

# Convert categorical inputs to numerical
input_data = {
    "Age": age,
    "Gender": 1 if gender == "Male" else 0,
    "Hormonal Changes": 1 if hormonal_changes == "Postmenopausal" else 0,
    "Family History": 1 if family_history == "Yes" else 0,
    "Race/Ethnicity": ["Asian", "Caucasian", "African American", "Other"].index(race_ethnicity),
    "Body Weight": ["Underweight", "Normal", "Overweight", "Obese"].index(body_weight),
    "Calcium Intake": ["Low", "Adequate", "High"].index(calcium_intake),
    "Vitamin D Intake": 1 if vitamin_d_intake == "Sufficient" else 0,
    "Physical Activity": 1 if physical_activity == "Active" else 0,
    "Smoking": 1 if smoking == "Yes" else 0,
    "Alcohol Consumption": ["None", "Moderate", "High"].index(alcohol_consumption),
    "Medical Conditions": ["None", "Rheumatoid Arthritis", "Hyperthyroidism"].index(medical_conditions),
    "Medications": 1 if medications == "Corticosteroids" else 0,
    "Prior Fractures": 1 if prior_fractures == "Yes" else 0
}

# Prediction button
if st.button("Predict Osteoporosis Risk"):
    model = load_model()
    prediction, probability = predict(model, input_data)
    
    st.subheader("Prediction Result")
    if prediction == 1:
        st.error(f"High risk of osteoporosis (Probability: {probability:.2f})")
    else:
        st.success(f"Low risk of osteoporosis (Probability: {probability:.2f})")
