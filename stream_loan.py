import streamlit as st
import pandas as pd
import pickle

st.title("Loan Status Prediction App")

# Load the trained model
model = pickle.load(open('loan_status_model.pkl', 'rb'))

# Function to predict loan status
def predict_loan_status(data):
    prediction = model.predict(data)
    return prediction

# User input
col1, col2 = st.columns(2)

with col1 :
    gender = st.selectbox("Gender", ['Male', 'Female'])

with col2 :
    married = st.selectbox("Marital Status", ['Yes', 'No'])

with col1 :
    dependents = st.selectbox("Dependents", ['0', '1', '2', '3+'])

with col2 :
    education = st.selectbox("Education", ['Graduate', 'Not Graduate'])

with col1 :
    self_employed = st.selectbox("Self Employed", ['Yes', 'No'])

with col2 :
    applicant_income = st.number_input("Applicant Income", value=0)

with col1 :
    coapplicant_income = st.number_input("Coapplicant Income", value=0)

with col2 :
    loan_amount = st.number_input("Loan Amount", value=0)

with col1 :
    loan_amount_term = st.number_input("Loan Amount Term", value=0)

with col2 :
    credit_history = st.selectbox("Credit History", [0, 1])

with col1 :
    property_area = st.selectbox("Property Area", ['Rural', 'Semiurban', 'Urban'])

# Create a dictionary to hold the user input
data = {
    'Gender': gender,
    'Married': married,
    'Dependents': dependents,
    'Education': education,
    'Self_Employed': self_employed,
    'ApplicantIncome': applicant_income,
    'CoapplicantIncome': coapplicant_income,
    'LoanAmount': loan_amount,
    'Loan_Amount_Term': loan_amount_term,
    'Credit_History': credit_history,
    'property_Area' : property_area
}

# Convert the dictionary to a DataFrame
data_df = pd.DataFrame([data])

predict = ''

# Make predictions
if st.button("Predict Loan Status"):
    prediction = predict_loan_status(data_df)
    if prediction[0] == 'Y':
        predict = 'Congratulations! Your loan is approved.'
    else:
        predict = 'Sorry, your loan is not approved.'

    st.success(predict)