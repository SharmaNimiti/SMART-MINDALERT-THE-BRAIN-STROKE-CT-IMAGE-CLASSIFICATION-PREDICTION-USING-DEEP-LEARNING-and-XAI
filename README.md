# SMART-MINDALERT-THE-BRAIN-STROKE-CT-IMAGE-CLASSIFICATION-PREDICTION-USING-DEEP-LEARNING-and-XAI
This web application predicts brain strokes in real-time using CT scans and deep learning, achieving 97.21% accuracy, with features like emergency alerts, chatbot, treatment guidance, and video consultations.

### 📸 Application Modules
🏠 Home
ℹ️ About (Symptoms & Causes)
📊 Insights
💉 Treatment
🤖 Chatbot
📹 Video Consultation
🧠 Stroke Prediction Dashboard

# 🧠 SMART MINDALERT APP – Brain Stroke Prediction System

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Framework](https://img.shields.io/badge/Framework-Streamlit-red)
![Deep Learning](https://img.shields.io/badge/DeepLearning-TensorFlow%20%7C%20Keras-orange)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)

An **AI-powered healthcare application** that predicts **brain stroke risk** from CT scan images using deep learning models.  
The system provides **real-time predictions**, **treatment recommendations**, **chatbot assistance**, and **emergency alerts**.

---

## 🚀 Features

### 🧠 AI-Based Stroke Detection
- Upload Brain CT scan images
- Predict stroke risk using:
  - CNN Model
  - Xception Model
  - Inception Model
- Displays **stroke probability (%)**

---

### 🚨 Emergency Alert System
- Automatically detects **high-risk cases**
- Sends **email alerts** to emergency contacts
- Provides **instant treatment recommendations**

---

### 💬 Smart Chatbot
- Answers questions about:
  - Stroke symptoms
  - Prevention
  - Treatment
- Includes **suggested queries** for user guidance

---

### 📊 Insights & Awareness
- Stroke statistics and trends
- Risk factors and prevention strategies
- Educational content for awareness

---

### 🩺 Treatment Guidance
- Emergency treatment steps
- Post-stroke rehabilitation
- Lifestyle recommendations

---

### 📹 Video Consultation (Simulation)
- Connects users to healthcare professionals via video call
- Uses Google Meet integration

---

### 🎨 Interactive UI
- Built using **Streamlit**
- Custom CSS styling
- Sidebar navigation dashboard

---

## 🛠️ Tech Stack

- **Frontend/UI:** Streamlit  
- **Backend:** Python  
- **Deep Learning:** TensorFlow, Keras  
- **Image Processing:** OpenCV, PIL  
- **Visualization:** Matplotlib  
- **Speech (optional):** gTTS  
- **Email Alerts:** SMTP  

---

## ⚙️ How It Works

```text
1. User uploads Brain CT Scan image
2. Image is preprocessed (resize + normalization)
3. Selected model predicts stroke probability
4. If risk > 75%:
   → Emergency alert triggered
   → Email sent to contact
   → Treatment recommendations displayed
5. If risk is low:
   → Healthy lifestyle tips shown. 


