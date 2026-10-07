
import pickle
import numpy as np
import pandas as pd
from tensorflow import keras, float16
import requests
from PIL import Image
import streamlit as st
import cv2
import joblib


@st.cache_resource
def load_model():
    return joblib.load("model.gz")

def predict_model():
    model = load_model()
    st.write('Predict the cloth shown')
    image = st.file_uploader("Choose a file")
    if image:
        image = Image.open(image)
        if st.button('Predict cloth'):
            max_size = (51, 73)
            image.thumbnail(max_size)
                    # creating thumbnail
            image.save('thumb.png')
            new_img = np.array(image)
            new_img = cv2.resize(new_img, (28, 28))
            new_img = np.dot(new_img[..., :3], [0.2989, 0.5870, 0.1140])
            new_img = 255 - new_img
                                    # data = request.get_json()
            data = np.array(new_img, dtype=np.float32)
            data = data.reshape(1, 28, 28, 1)
            data = data / 255.0
                                    # Perform prediction
            prediction = model.predict(data)
            predicted_class = int(np.argmax(prediction[0]))
            confidence = prediction.flatten()
            labels=[
                                        "Tshirt/Top",
                                        "Trouser",
                                        "Pullover",
                                        "Dress",
                                        "Coat",
                                        "Sandal",
                                        "Shirt",
                                        "Sneaker",
                                        "Bag",
                                        "Ankle Boot"
                                    ]
            label = labels[predicted_class]
            st.success(f'Estimated category: {label}')
            with open('confidence.pkl','wb') as f:
                pickle.dump(confidence,f)









