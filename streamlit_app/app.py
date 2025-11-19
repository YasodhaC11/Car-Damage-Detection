import os
import streamlit as st
from helper import predict

st.title("Vehicle Damage Detection")

# Use /tmp in cloud
UPLOAD_DIR = "/tmp/Uploaded_images"
os.makedirs(UPLOAD_DIR, exist_ok=True)

uploaded_file = st.file_uploader("Upload an image", type=["jpg","jpeg","png"])

if uploaded_file:
    # Save image safely
    image_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.container():
        # Show image
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

        # Predict
        try:
            prediction = predict(image_path)
            st.success(f"Predicted Class: {prediction}")
        except Exception as e:
            st.error(f"Prediction Error: {e}")

st.caption("⚠ Model may make mistakes — verify with multiple images.")
