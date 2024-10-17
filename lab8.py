import streamlit as st
import pandas as pd
st.title("Rail Transport Infrastructure")
db_file=r"C:\Users\user\Downloads\data_RailTransport.csv"
df= pd.read_csv(db_file)
st.write("Натисніть кнопку нижче, щоб побачити повний датафрейм:")
if st.button('Показати дані'):
    st.write(df)