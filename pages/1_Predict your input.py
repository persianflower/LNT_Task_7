import streamlit as st
from utils import predict_model

st.title("This is prediction page")
st.sidebar.success("Give input and see the magic!")

predict_model()
