import streamlit as st
import pandas as pd
import numpy as np
import joblib
from preprocessing_tools import preprocess_input
import os

# Carga el modelo entrenado

current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, '..', 'models', 'random_forest_model.pkl')
model = joblib.load(model_path)



def predict_churn(data):
    # Preprocesa los datos ingresados por el usuario
    preprocessed_data = preprocess_input(data)

    # Realiza la predicción utilizando el modelo cargado
    prediction = model.predict(preprocessed_data)[0]

    # Retorna la predicción
    return prediction

def main():
    # Título de la aplicación
    st.title('Predicción de Churn en Telco')

    # Descripción de la aplicación
    st.markdown('Este es un ejemplo de una aplicación web para predecir la churn en una empresa de telecomunicaciones.')

    # Campos de entrada para los datos del usuario
    gender = st.selectbox('Género', ['Female', 'Male'])
    senior_citizen = st.selectbox('Senior Citizen', ['No', 'Yes'])
    partner = st.selectbox('Partner', ['No', 'Yes'])
    dependents = st.selectbox('Dependents', ['No', 'Yes'])
    tenure = st.number_input('Tenure', min_value=0, max_value=100, step=1)
    phone_service = st.selectbox('Phone Service', ['No', 'Yes'])
    multiple_lines = st.selectbox('Multiple Lines', ['No', 'No phone service', 'Yes'])
    internet_service = st.selectbox('Internet Service', ['DSL', 'Fiber optic', 'No'])
    online_security = st.selectbox('Online Security', ['No', 'No internet service', 'Yes'])
    online_backup = st.selectbox('Online Backup', ['No', 'No internet service', 'Yes'])
    device_protection = st.selectbox('Device Protection', ['No', 'No internet service', 'Yes'])
    tech_support = st.selectbox('Tech Support', ['No', 'No internet service', 'Yes'])
    streaming_tv = st.selectbox('Streaming TV', ['No', 'No internet service', 'Yes'])
    streaming_movies = st.selectbox('Streaming Movies', ['No', 'No internet service', 'Yes'])
    contract = st.selectbox('Contract', ['Month-to-month', 'One year', 'Two year'])
    paperless_billing = st.selectbox('Paperless Billing', ['No', 'Yes'])
    payment_method = st.selectbox('Payment Method', ['Bank transfer (automatic)', 'Credit card (automatic)', 'Electronic check', 'Mailed check'])
    monthly_charges = st.number_input('Monthly Charges', min_value=0, max_value=200, step=1)
    total_charges = st.number_input('Total Charges', min_value=0, max_value=10000, step=1)

    # Agrega los demás campos de entrada...

    # Botón para realizar la predicción
    if st.button('Predecir'):
        # Crea un DataFrame con los datos ingresados por el usuario
        input_data = pd.DataFrame({
            'gender': [gender],
            'SeniorCitizen': [senior_citizen],
            'Partner': [partner],
            'Dependents': [dependents],
            'tenure': [tenure],
            'PhoneService': [phone_service],
            'MultipleLines': [multiple_lines],
            'InternetService': [internet_service],
            'OnlineSecurity': [online_security],
            'OnlineBackup': [online_backup],
            'DeviceProtection': [device_protection],
            'TechSupport': [tech_support],
            'StreamingTV': [streaming_tv],
            'StreamingMovies': [streaming_movies],
            'Contract': [contract],
            'PaperlessBilling': [paperless_billing],
            'PaymentMethod': [payment_method],
            'MonthlyCharges': [monthly_charges],
            'TotalCharges': [total_charges]

        })

        # Realiza la predicción de churn
        prediction = predict_churn(input_data)

        if prediction == 0:
            prediction = 'No'
        else:
            prediction = 'Si'

        # Muestra el resultado de la predicción
        st.success('La predicción de churn es: {}'.format(prediction))

main()