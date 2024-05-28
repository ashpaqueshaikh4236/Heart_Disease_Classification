import streamlit as st
import pickle
import pandas as pd
import numpy as np

df = pd.read_csv('Clean_data')
model = pickle.load(open('model.pkl','rb'))


sex = [''] + sorted(df['sex'].unique().tolist())
cp = [''] + sorted(df['cp'].unique().tolist())
fbs = [''] + sorted(df['fbs'].unique().tolist())
restecg = [''] + sorted(df['restecg'].unique().tolist())
exang = [''] + sorted(df['exang'].unique().tolist())
slope = [''] + sorted(df['slope'].unique().tolist())
ca = [''] + sorted(df['ca'].unique().tolist())
thal = [''] + sorted(df['thal'].unique().tolist())

st.title('Heart Deissis Classification')


Age= st.text_input('Age')
Sex = st.selectbox('Sex',sex)
Cp = st.selectbox('Cp',cp)
Trestbs = st.text_input('Trestbps')
Chol= st.text_input('Chol')
Fbs = st.selectbox('Fbs',fbs)
Restecg = st.selectbox('Restecg',restecg)
Thalach = st.text_input('Thalach')
Exang = st.selectbox('Exang',exang)
Oldpeak = st.text_input('Oldpeak')
Slope = st.selectbox('Slope',slope)
Ca = st.selectbox('Ca',ca)
Thal = st.selectbox('Thal',thal)

Selected_data = (Age,Sex,Cp,Trestbs,Chol,Fbs,Restecg,Thalach,Exang,Oldpeak,Slope,Ca,Thal)

try:
    if st.button('Predict'):
        rehasped_data = np.asarray(Selected_data).reshape(1,-1)
        if 'select' in reshaped_data or '' in reshaped_data:
            st.warning('Please fill all values')
        else:
            prediction = model.predict(rehasped_data)
            if prediction[0] == 0:
                st.success("Person has no Deissis")
            else:
                st.warning("Person has Deissis")
                
except Exception as e:
    st.warning(f'An error occurred: {e}')
