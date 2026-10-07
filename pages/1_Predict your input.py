import streamlit as st
from utils import predict_model

st.title("This is PageOne Geeks.")
st.sidebar.success("Give input and see the magic!")

predict_model()
