import streamlit as st

st.title("Model performance metrics")
st.sidebar.success("You are viewing metrics page")

st.markdown('''
:red[DISCLAIMER: The graphs shown on this page contains metrics of two models namely: Basic CNN and Deeper CNN 
as the model training was carried out for both. The predictions however are only performed on the basis of 
the higher accuracy and lower loss model i.e. Basic CNN]
''')

st.subheader("Accuracy and loss curve",divider=True)
st.image('images/acc & loss curve.png')
st.subheader("Confusion matrix of models",divider=True)
st.image('images/cnn predictions.png')
st.subheader("Model comparision",divider=True)
st.image('images/confusion matric.png')
st.subheader("Basic CNN predictions of validation dataset",divider=True)
st.image('images/model comparision.png')