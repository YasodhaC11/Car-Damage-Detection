# Car-Damage-Prediction

## Project Overview
This project is an AI-based **Car Damage Classification** System built using PyTorch, ResNet50, Optuna, Streamlit, and FastAPI.
It detects the type of car damage from an uploaded image.

## Dataset
- **Images:** 2300  
- **Class labels:** "Front Breakage",'Front Crushed','Front Normal','Rear Breakage','Rear Crushed','Rear Normal'

## Features / Preprocessing

✅ Deep Learning model (ResNet50 pretrained on ImageNet)

✅ Fine-tuned last layers + hyperparameter tuning using Optuna

✅ Image augmentations for better generalization

✅ Streamlit Web App for easy image upload & prediction

✅ FastAPI endpoint for programmatic inference

✅ Supports 6 classes of car damage

✅ Achieved ~80% accuracy

## Project Structure

**Car-Damage-Prediction/
│
├── streamlit_app/
│   ├── app.py              # Streamlit UI
│   ├── helper.py           # Model loading + prediction logic
│   ├── model/
│   │   └── saved_model.pth # Trained model file
│
├── requirements.txt
├── README.md
└── .gitignore
**

## Modeling
- **Models:** Base: ResNet50 (pretrained)
              Frozen: All layers except layer4 
- **Hyperparameter Tuning:** Using Optuna, tuned:Learning rate (1e−5 to 1e−2) and Dropout rate (0.2 to 0.7)

## Streamlit App
- Built an **interactive frontend** using Streamlit  
- **Live Demo:** [Streamlit Cloud]https://dl-car-damage-detection-project.streamlit.app/
- it varies much from running it locally. Need further improvement.

## Installation
1. Clone the repository:  
2. pip install -r requirements.txt
3. streamlit run app.py

