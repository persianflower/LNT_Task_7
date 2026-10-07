import pickle
import plotly.express as px
import streamlit as stm
stm.title("Visualization of output")
stm.sidebar.success("Ensure prediction page is visited first!")

if stm.button('Visualize prediction'):
    with open('confidence.pkl','rb') as f:
        confidence = pickle.load(f)

    conf = list(confidence)
    labels=["Tshirt/Top","Trouser","Pullover","Dress","Coat","Sandal",
           "Shirt","Sneaker","Bag","Ankle Boot"]

    fig = px.histogram(x=labels,y=conf)
    fig.update_layout(
        title="Confidence level of prediction",
        xaxis_title = "Classes",
        yaxis_title = "Confidence"
    )
    stm.plotly_chart(fig)




