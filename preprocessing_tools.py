import pandas as pd

def preprocess_input(data):
    # Crear un DataFrame a partir de los datos de entrada
    input_df = pd.DataFrame(data, index=[0])



    # Unir las columnas numéricas y las codificadas en un único DataFrame
    numeric_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
    # Convertir la columna 'TotalCharges' a tipo de datos numérico
    input_df['TotalCharges'] = pd.to_numeric(input_df['TotalCharges'], errors='coerce')
    input_df['MonthlyCharges'] = pd.to_numeric(input_df['MonthlyCharges'], errors='coerce')
    input_df['tenure'] = pd.to_numeric(input_df['tenure'], errors='coerce')

    # preprocessed_data = pd.concat([input_df[numeric_cols], input_df_encoded], axis=1)

    encoded_data = pd.DataFrame(columns=['tenure', 'MonthlyCharges', 'TotalCharges',
        'gender_Female', 'gender_Male',
        'SeniorCitizen_No', 'SeniorCitizen_Yes',
        'Partner_No', 'Partner_Yes',
        'Dependents_No', 'Dependents_Yes',
        'PhoneService_No', 'PhoneService_Yes',
        'MultipleLines_No', 'MultipleLines_No phone service', 'MultipleLines_Yes',
        'InternetService_DSL', 'InternetService_Fiber optic', 'InternetService_No',
        'OnlineSecurity_No', 'OnlineSecurity_No internet service', 'OnlineSecurity_Yes',
        'OnlineBackup_No', 'OnlineBackup_No internet service', 'OnlineBackup_Yes',
        'DeviceProtection_No', 'DeviceProtection_No internet service', 'DeviceProtection_Yes',
        'TechSupport_No', 'TechSupport_No internet service', 'TechSupport_Yes',
        'StreamingTV_No', 'StreamingTV_No internet service', 'StreamingTV_Yes',
        'StreamingMovies_No', 'StreamingMovies_No internet service', 'StreamingMovies_Yes',
        'Contract_Month-to-month', 'Contract_One year', 'Contract_Two year',
        'PaperlessBilling_No', 'PaperlessBilling_Yes',
        'PaymentMethod_Bank transfer (automatic)', 'PaymentMethod_Credit card (automatic)','PaymentMethod_Electronic check', 'PaymentMethod_Mailed check'])

    encoded_data['tenure'] = input_df['tenure']
    encoded_data['MonthlyCharges'] = input_df['MonthlyCharges']
    encoded_data['TotalCharges'] = input_df['TotalCharges']

    if input_df['gender'].item() == 'Female':
        encoded_data['gender_Female'] = 1
        encoded_data['gender_Male'] = 0
    elif input_df['gender'].item() == 'Male':
        encoded_data['gender_Female'] = 0
        encoded_data['gender_Male'] = 1

    if input_df['SeniorCitizen'].item() == 'No':
        encoded_data['SeniorCitizen_No'] = 1
        encoded_data['SeniorCitizen_Yes'] = 0
    elif input_df['SeniorCitizen'].item() == 'Yes':
        encoded_data['SeniorCitizen_No'] = 0
        encoded_data['SeniorCitizen_Yes'] = 1

    if input_df['Partner'].item() == 'No':
        encoded_data['Partner_No'] = 1
        encoded_data['Partner_Yes'] = 0
    elif input_df['Partner'].item() == 'Yes':
        encoded_data['Partner_No'] = 0
        encoded_data['Partner_Yes'] = 1

    if input_df['Dependents'].item() == 'No':
        encoded_data['Dependents_No'] = 1
        encoded_data['Dependents_Yes'] = 0
    elif input_df['Dependents'].item() == 'Yes':
        encoded_data['Dependents_No'] = 0
        encoded_data['Dependents_Yes'] = 1

    if input_df['PhoneService'].item() == 'No':
        encoded_data['PhoneService_No'] = 1
        encoded_data['PhoneService_Yes'] = 0
    elif input_df['PhoneService'].item() == 'Yes':
        encoded_data['PhoneService_No'] = 0
        encoded_data['PhoneService_Yes'] = 1

    if input_df['MultipleLines'].item() == 'No':
        encoded_data['MultipleLines_No'] = 1
        encoded_data['MultipleLines_No phone service'] = 0
        encoded_data['MultipleLines_Yes'] = 0
    elif input_df['MultipleLines'].item() == 'No phone service':
        encoded_data['MultipleLines_No'] = 0
        encoded_data['MultipleLines_No phone service'] = 1
        encoded_data['MultipleLines_Yes'] = 0
    elif input_df['MultipleLines'].item() == 'Yes':
        encoded_data['MultipleLines_No'] = 0
        encoded_data['MultipleLines_No phone service'] = 0
        encoded_data['MultipleLines_Yes'] = 1

    if input_df['InternetService'].item() == 'DSL':
        encoded_data['InternetService_DSL'] = 1
        encoded_data['InternetService_Fiber optic'] = 0
        encoded_data['InternetService_No'] = 0
    elif input_df['InternetService'].item() == 'Fiber optic':
        encoded_data['InternetService_DSL'] = 0
        encoded_data['InternetService_Fiber optic'] = 1
        encoded_data['InternetService_No'] = 0
    elif input_df['InternetService'].item() == 'No':
        encoded_data['InternetService_DSL'] = 0
        encoded_data['InternetService_Fiber optic'] = 0
        encoded_data['InternetService_No'] = 1

    if input_df['OnlineSecurity'].item() == 'No':
        encoded_data['OnlineSecurity_No'] = 1
        encoded_data['OnlineSecurity_No internet service'] = 0
        encoded_data['OnlineSecurity_Yes'] = 0
    elif input_df['OnlineSecurity'].item() == 'No internet service':
        encoded_data['OnlineSecurity_No'] = 0
        encoded_data['OnlineSecurity_No internet service'] = 1
        encoded_data['OnlineSecurity_Yes'] = 0
    elif input_df['OnlineSecurity'].item() == 'Yes':
        encoded_data['OnlineSecurity_No'] = 0
        encoded_data['OnlineSecurity_No internet service'] = 0
        encoded_data['OnlineSecurity_Yes'] = 1

    if input_df['OnlineBackup'].item() == 'No':
        encoded_data['OnlineBackup_No'] = 1
        encoded_data['OnlineBackup_No internet service'] = 0
        encoded_data['OnlineBackup_Yes'] = 0
    elif input_df['OnlineBackup'].item() == 'No internet service':
        encoded_data['OnlineBackup_No'] = 0
        encoded_data['OnlineBackup_No internet service'] = 1
        encoded_data['OnlineBackup_Yes'] = 0
    elif input_df['OnlineBackup'].item() == 'Yes':
        encoded_data['OnlineBackup_No'] = 0
        encoded_data['OnlineBackup_No internet service'] = 0
        encoded_data['OnlineBackup_Yes'] = 1

    if input_df['DeviceProtection'].item() == 'No':
        encoded_data['DeviceProtection_No'] = 1
        encoded_data['DeviceProtection_No internet service'] = 0
        encoded_data['DeviceProtection_Yes'] = 0
    elif input_df['DeviceProtection'].item() == 'No internet service':
        encoded_data['DeviceProtection_No'] = 0
        encoded_data['DeviceProtection_No internet service'] = 1
        encoded_data['DeviceProtection_Yes'] = 0
    elif input_df['DeviceProtection'].item() == 'Yes':
        encoded_data['DeviceProtection_No'] = 0
        encoded_data['DeviceProtection_No internet service'] = 0
        encoded_data['DeviceProtection_Yes'] = 1

    if input_df['TechSupport'].item() == 'No':
        encoded_data['TechSupport_No'] = 1
        encoded_data['TechSupport_No internet service'] = 0
        encoded_data['TechSupport_Yes'] = 0
    elif input_df['TechSupport'].item() == 'No internet service':
        encoded_data['TechSupport_No'] = 0
        encoded_data['TechSupport_No internet service'] = 1
        encoded_data['TechSupport_Yes'] = 0
    elif input_df['TechSupport'].item() == 'Yes':
        encoded_data['TechSupport_No'] = 0
        encoded_data['TechSupport_No internet service'] = 0
        encoded_data['TechSupport_Yes'] = 1

    if input_df['StreamingTV'].item() == 'No':
        encoded_data['StreamingTV_No'] = 1
        encoded_data['StreamingTV_No internet service'] = 0
        encoded_data['StreamingTV_Yes'] = 0
    elif input_df['StreamingTV'].item() == 'No internet service':
        encoded_data['StreamingTV_No'] = 0
        encoded_data['StreamingTV_No internet service'] = 1
        encoded_data['StreamingTV_Yes'] = 0
    elif input_df['StreamingTV'].item() == 'Yes':
        encoded_data['StreamingTV_No'] = 0
        encoded_data['StreamingTV_No internet service'] = 0
        encoded_data['StreamingTV_Yes'] = 1

    if input_df['StreamingMovies'].item() == 'No':
        encoded_data['StreamingMovies_No'] = 1
        encoded_data['StreamingMovies_No internet service'] = 0
        encoded_data['StreamingMovies_Yes'] = 0
    elif input_df['StreamingMovies'].item() == 'No internet service':
        encoded_data['StreamingMovies_No'] = 0
        encoded_data['StreamingMovies_No internet service'] = 1
        encoded_data['StreamingMovies_Yes'] = 0
    elif input_df['StreamingMovies'].item() == 'Yes':
        encoded_data['StreamingMovies_No'] = 0
        encoded_data['StreamingMovies_No internet service'] = 0
        encoded_data['StreamingMovies_Yes'] = 1

    if input_df['Contract'].item() == 'Month-to-month':
        encoded_data['Contract_Month-to-month'] = 1
        encoded_data['Contract_One year'] = 0
        encoded_data['Contract_Two year'] = 0
    elif input_df['Contract'].item() == 'One year':
        encoded_data['Contract_Month-to-month'] = 0
        encoded_data['Contract_One year'] = 1
        encoded_data['Contract_Two year'] = 0
    elif input_df['Contract'].item() == 'Two year':
        encoded_data['Contract_Month-to-month'] = 0
        encoded_data['Contract_One year'] = 0
        encoded_data['Contract_Two year'] = 1

    if input_df['PaperlessBilling'].item() == 'No':
        encoded_data['PaperlessBilling_No'] = 1
        encoded_data['PaperlessBilling_Yes'] = 0
    elif input_df['PaperlessBilling'].item() == 'Yes':
        encoded_data['PaperlessBilling_No'] = 0
        encoded_data['PaperlessBilling_Yes'] = 1

    if input_df['PaymentMethod'].item() == 'Bank transfer (automatic)':
        encoded_data['PaymentMethod_Bank transfer (automatic)'] = 1
        encoded_data['PaymentMethod_Credit card (automatic)'] = 0
        encoded_data['PaymentMethod_Electronic check'] = 0
        encoded_data['PaymentMethod_Mailed check'] = 0
    elif input_df['PaymentMethod'].item() == 'Credit card (automatic)':
        encoded_data['PaymentMethod_Bank transfer (automatic)'] = 0
        encoded_data['PaymentMethod_Credit card (automatic)'] = 1
        encoded_data['PaymentMethod_Electronic check'] = 0
        encoded_data['PaymentMethod_Mailed check'] = 0
    elif input_df['PaymentMethod'].item() == 'Electronic check':
        encoded_data['PaymentMethod_Bank transfer (automatic)'] = 0
        encoded_data['PaymentMethod_Credit card (automatic)'] = 0
        encoded_data['PaymentMethod_Electronic check'] = 1
        encoded_data['PaymentMethod_Mailed check'] = 0
    elif input_df['PaymentMethod'].item() == 'Mailed check':
        encoded_data['PaymentMethod_Bank transfer (automatic)'] = 0
        encoded_data['PaymentMethod_Credit card (automatic)'] = 0
        encoded_data['PaymentMethod_Electronic check'] = 0
        encoded_data['PaymentMethod_Mailed check'] = 1

    # Devolver los datos preprocesados
    return encoded_data