import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained model
model = joblib.load('random_forest_model.pkl')  # Replace with your model file

# Define a function to make predictions
def predict_thyroid_disease(data):
    prediction = model.predict(data)
    return prediction[0]

# Create the Streamlit app
def main():
    st.title("Thyroid Disease Prediction")

    st.write("Please input the following details:")

    # Input fields for user data
    age = st.number_input("Age", min_value=0, max_value=120, value=30)
    gender = st.selectbox("Gender", ["Male", "Female"])
    smoking = st.selectbox("Smoking Status", ["Yes", "No"])
    hx_smoking = st.selectbox("History of Smoking", ["Yes", "No"])
    hx_radiotherapy = st.selectbox("History of Radiotherapy", ["Yes", "No"])
    thyroid_function = st.selectbox("Thyroid Function", ["Normal", "Abnormal"])
    physical_examination = st.selectbox("Physical Examination", ["Normal", "Abnormal"])
    adenopathy = st.selectbox("Adenopathy", ["Yes", "No"])
    pathology = st.selectbox("Pathology", ["Benign", "Malignant"])
    focality = st.selectbox("Focality", ["Unifocal", "Multifocal"])
    risk = st.selectbox("Risk", ["Low", "High"])
    t_category = st.selectbox("T Category", ["T1", "T2", "T3", "T4"])
    n_category = st.selectbox("N Category", ["N0", "N1", "N2", "N3"])
    m_category = st.selectbox("M Category", ["M0", "M1"])
    stage = st.selectbox("Stage", ["Stage I", "Stage II", "Stage III", "Stage IV"])
    response = st.selectbox("Response", ["Complete", "Partial", "No Response"])

    # Prepare the input data
    input_data = pd.DataFrame({
        'Age': [age],
        'Gender': [gender],
        'Smoking': [smoking],
        'Hx Smoking': [hx_smoking],
        'Hx Radiothreapy': [hx_radiotherapy],
        'Thyroid Function': [thyroid_function],
        'Physical Examination': [physical_examination],
        'Adenopathy': [adenopathy],
        'Pathology': [pathology],
        'Focality': [focality],
        'Risk': [risk],
        'T': [t_category],
        'N': [n_category],
        'M': [m_category],
        'Stage': [stage],
        'Response': [response]
    })

    # Button to make prediction
    if st.button("Predict"):
        prediction = predict_thyroid_disease(input_data)
        st.write(f"The model predicts: {'Recurred' if prediction == 1 else 'Not Recurred'}")

# Run the app
if __name__ == "__main__":
    main()
