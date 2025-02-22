# Osteoporosis-Disease-Prediction

## Overview
This project is a **Streamlit-based** web application that predicts the risk of **osteoporosis** based on patient input data. The model used is an **XGBoost classifier**, trained on relevant features such as **age, gender, family history, body weight, calcium intake, and medical conditions**.

## Features
- 🏥 **User-friendly interface** for data input using **Streamlit**
- 🩺 **Predicts the likelihood of osteoporosis** using a **pre-trained XGBoost model**
- ✅ Supports various patient attributes such as **age, gender, smoking habits, prior fractures, and more**
- 📊 **Displays prediction results** with probability scores

## Installation
### 1️⃣ Create a Virtual Environment
Run the following command to create and activate a virtual environment:

#### **Windows:**
```sh
python -m venv venv
venv\Scripts\activate
```

### 2️⃣ Install Dependencies
Once inside the virtual environment, install the required dependencies:
```sh
pip install streamlit pandas joblib scikit-learn xgboost
```

### 3️⃣ Run the Application
Start the **Streamlit** application using:
```sh
streamlit run streamlit_osteoporosis.py
```

## Project Files 📂
- `osteoporosis_pred.ipynb` - Model training
- `streamlit_osteoporosis.py` - Main **Streamlit** application script
- `osteoporosis_model.joblib` - Pre-trained **osteoporosis prediction model**
- `requirements.txt` - List of dependencies
- `README.md` - Documentation for the project

## Input Features 📌
The following features are required for making a prediction:
- **Age** (Numeric)
- **Gender** (Male/Female)
- **Hormonal Changes** (Normal/Postmenopausal)
- **Family History** (Yes/No)
- **Race/Ethnicity** (Asian, Caucasian, African American, Other)
- **Body Weight** (Underweight, Normal, Overweight, Obese)
- **Calcium Intake** (Low, Adequate, High)
- **Vitamin D Intake** (Insufficient/Sufficient)
- **Physical Activity** (Sedentary/Active)
- **Smoking** (Yes/No)
- **Alcohol Consumption** (None, Moderate, High)
- **Medical Conditions** (None, Rheumatoid Arthritis, Hyperthyroidism)
- **Medications** (None, Corticosteroids)
- **Prior Fractures** (Yes/No)

## Model Details 🧠
The model was trained using **XGBoost**, a powerful gradient boosting algorithm. The dataset was preprocessed to handle categorical values and missing data before training.

## License 📜
This project is **open-source** and available for **educational and research purposes**.

