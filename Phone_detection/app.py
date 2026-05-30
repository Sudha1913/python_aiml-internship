id="ymc1mk"
# ============================================
# STREAMLIT IMAGE CLASSIFICATION APP
# ============================================

import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# ============================================
# LOAD TRAINED MODEL
# ============================================

model = tf.keras.models.load_model("cnn_model.h5")

# Class Names
class_names = [
    "chair",
    "mobile",
    "pen",
    "bottle"
]

# ============================================
# STREAMLIT UI
# ============================================

st.title("Real World Object Detection using CNN")

st.write("Upload an image to predict the object.")

# Upload Image
uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "png", "jpeg"]
)

# ============================================
# PREDICTION
# ============================================

if uploaded_file is not None:

    # Open Image
    image = Image.open(uploaded_file)

    # Display Image
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Resize Image
    image = image.resize((128, 128))

    # Convert to Array
    img_array = np.array(image)

    # Normalize
    img_array = img_array / 255.0

    # Expand Dimensions
    img_array = np.expand_dims(img_array, axis=0)

    # Prediction
    prediction = model.predict(img_array)

    predicted_class = class_names[np.argmax(prediction)]

    # Show Result
    st.success(f"Prediction: {predicted_class}")

