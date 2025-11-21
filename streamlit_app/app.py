import os
import streamlit as st
from helper import predict
from PIL import Image

st.title("Vehicle Damage Detection")

# Use /tmp in cloud
UPLOAD_DIR = "/tmp/Uploaded_images"
os.makedirs(UPLOAD_DIR, exist_ok=True)

uploaded_file = st.file_uploader("Upload an image", type=["jpg","jpeg","png"],accept_multiple_files=True)

if uploaded_file:
    # Save image safely
    for image_file in uploaded_file:
        image_path = os.path.join(UPLOAD_DIR, image_file.name)
    with open(image_path, "wb") as f:
        f.write(image_file.getbuffer())

    with st.container():
        # Show image
        st.image(image_file, caption="Uploaded Image", use_container_width=True)

        # Predict
        try:
            prediction = predict(image_path)
            st.success(f"Predicted Class: {prediction}")
        except Exception as e:
            st.error(f"Prediction Error: {e}")

st.caption("⚠ Model may make mistakes — verify with multiple images.")
