import streamlit as st

st.set_page_config(page_title = "This is a Multipage WebApp for Deep Learning Prediction")
st.title("Welcome to Fashion MNIST Prediction Hub")

st.subheader("This website aims to provide a centralised place to predict images of clothing and "
             "provide metrics for the same",divider=True)

st.markdown(":green[Please follow the given sequence of pages to get the perfect experience]")

st.markdown("1. Go to page: Predict your input -> Here you can provide any piece of clothing as an input and see what the model predicts")
st.markdown("2. Go to page: Visualize your results -> Here you can see the confidence level of the various categories of data. :red[Please click on the button 'visualize results' to view the same]")
st.markdown("3. Go to page: Model metrics -> Here you can see the various metrics of the trained model. This can be used to understand the accuracy and reliability of the model used in production")


