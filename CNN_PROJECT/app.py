import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load Model
model = tf.keras.models.load_model("cnn_model.h5")

# Class Names
class_names = [
    "chair",
    "mobile",
    "pen"
]

# Title
st.title("CNN Real World Object Detection")

st.write("Upload an image for prediction")

# Upload Image
uploaded_file = st.file_uploader(
    "Choose an Image",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file is not None:

    # Open Image
    image = Image.open(uploaded_file)

    # Convert RGB
    image = image.convert("RGB")

    # Show Image
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Resize Image
    image = image.resize((224,224))

    # Convert to Array
    img_array = np.array(image)

    # Normalize
    img_array = img_array / 255.0

    # Expand Dimensions
    img_array = np.expand_dims(img_array, axis=0)

    # Prediction
    prediction = model.predict(img_array)

    predicted_index = np.argmax(prediction)

    predicted_class = class_names[predicted_index]

    confidence = np.max(prediction) * 100

    # Result
    st.success(f"Prediction: {predicted_class}")

    st.write(f"Confidence: {confidence:.2f}%")