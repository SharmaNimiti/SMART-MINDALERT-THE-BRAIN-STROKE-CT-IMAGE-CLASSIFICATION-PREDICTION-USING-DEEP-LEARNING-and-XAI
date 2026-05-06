import streamlit as st
import tensorflow as tf
import numpy as np
from keras.models import load_model
from PIL import Image
import cv2
import webbrowser
from gtts import gTTS
import os
import base64
import matplotlib.pyplot as plt
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


with open ("style.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)
    
# Load trained models
cnn_model = tf.keras.models.load_model("C:\\Brain Stroke image dataset\\Brain_Data_Organised\\cnn_brain_stroke_model.h5")
xception_model = tf.keras.models.load_model("C:\\Brain Stroke image dataset\\Brain_Data_Organised\\ xception_brain_stroke_model.h5")
inception_model = tf.keras.models.load_model("C:\\Brain Stroke image dataset\\Brain_Data_Organised\\inception_brain_stroke_model.h5")

# 📌 Email Alert Credentials (Use App Passwords for security)
SENDER_EMAIL = "pallavi.diligence@gmail.com"
SENDER_PASSWORD = "mgop fbvs opdp lgve"
EMERGENCY_CONTACT_EMAIL = "nimitisharma1605@gmail.com"

# Function to preprocess image
def preprocess_image(image):
    image = image.convert("RGB")
    image = image.resize((224, 224))
    image = np.array(image) / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)
    return image  

# ---- 📌 Function to send emergency email alert ----
def send_email_alert(patient_name, risk_level):
    subject = "🚨 Emergency Alert: High Stroke Risk Detected!"
    body = f"""
    ALERT: Patient **{patient_name}** has been detected with a HIGH stroke risk ({risk_level}). 🚨   
    Immediate medical attention is recommended. Please take the necessary action.
    
    Regards,  
    SMART MINDALERT SYSTEM 🧠✨
    """

    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = EMERGENCY_CONTACT_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain', 'utf-8'))  # Ensure UTF-8 encoding

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, EMERGENCY_CONTACT_EMAIL, msg.as_string())
        server.quit()
        st.success("✅ Emergency email sent successfully!")
    except Exception as e:
        st.error(f"❌ Email Alert Failed: {e}")


#Sidebar
st.sidebar.title("Dashboard ✨")
app_mode = st.sidebar.selectbox("Select Page",["Home","About","Insights","Treatment","Chatbot","Video Consultation"])

#Main Page
if(app_mode=="Home"):
    st.header("SMART MINDALERT APP 🧠✨")
    image_path= "https://t3.ftcdn.net/jpg/08/07/02/52/360_F_807025205_WdvDE7fKkMfKelrQmc36PuCXTDxnrfIN.jpg"
    st.image(image_path,use_column_width=True)
    st.markdown("""
   Welcome to the Brain Stroke Prediction System!🧠🩺🔍
    
   Brain Stroke Prediction is a machine learning project that analyzes brain CT images using deep learning to assess stroke risk. This tool supports healthcare providers in early diagnosis, enabling timely intervention to reduce stroke severity and improve patient outcomes.
   
   Our goal is to effectively assist in the identification of Brain Stroke. Our technology can identify any indications of stroke by analysing a brain CT image that you upload. Let’s work together to protect brain health and ensure a better quality of life.


    ### How It Works 🧑‍⚕️
    1. **Upload Image:** Go to the **Stroke Detection** page and upload a brain CT scan image.
    2. **Analysis:** Our system analyzes the image using advanced algorithms to detect signs of stroke.
    3. **Results:** View the detection results and recommendations for further action.

    ### Why Choose Us❓
    - **Accuracy:** Our system employs cutting-edge machine learning techniques for precise stroke detection.
    - **User-Friendly:** Intuitive interface designed for seamless user experience.
    - **Fast and Efficient:** Get results in seconds, facilitating prompt medical response.
    - **Early Detection.** Identifies stroke symptoms early, aiding in quicker intervention to prevent further damage.
    - **Resource Optimization.** Helps healthcare professionals prioritize patients needing urgent attention.
    - **Cost Effective.** Reduces costs by minimizing unnecessary tests and focusing on timely treatment.

    ### Get Started 🚀
    Visit the Stroke Detection page in the sidebar to upload a CT scan and see our Brain Stroke Prediction System in action!


    ### About Us ✨
    Discover more about our mission, dataset, team, and goals on the **About** page.
    """)

#About Project
elif(app_mode=="About"):
    st.markdown("### Symptoms of Stroke🤕")
    image_path = "https://www.fcneurology.net/wp-content/uploads/2024/02/stroke-symptoms.jpg"
    st.image(image_path,use_column_width=True)
    st.write("""
        Early recognition of stroke symptoms is crucial for effective treatment. Key symptoms include:
        - **Sudden numbness or weakness** in the face, arm, or leg, particularly on one side of the body.
        - **Confusion** or difficulty speaking and understanding.
        - **Vision disturbances** in one or both eyes.
        - **Trouble walking**, dizziness, loss of balance, or lack of coordination.
        - **Severe headache** with no known cause.
""")

# Causes Section
    st.markdown("### Causes of Stroke")
    image_path = "https://blog.uvahealth.com/wp-content/uploads/2022/10/stroke-causes-graphic.jpg"
    st.image(image_path,use_column_width=True)
    st.write("""
      Strokes typically stem from two main causes:
      - **Ischemic Stroke**: Due to a blood clot or artery blockage, which prevents blood flow to the brain.
      - **Hemorrhagic Stroke**: Caused by a blood vessel rupture, leading to bleeding within the brain.

      Other risk factors include high cholesterol, hypertension, diabetes, smoking, excessive alcohol intake, and genetic predisposition.
""")

    
# Insights Section
elif app_mode == "Insights":
    st.title("Insights on Brain Stroke🧠📈")
    st.write("Explore key insights, trends, and statistics related to brain stroke.")

# Placeholder for data visualization
    st.markdown("""
        - **Global Stroke Statistics**: Around 15 million people suffer from stroke each year.
        - **Risk Factors**: Hypertension, diabetes, smoking, and sedentary lifestyle are significant risk factors.
        - **Prevention**: Regular exercise, a balanced diet, and regular check-ups can reduce stroke risk.
    """)
    st.image("https://www.world-stroke.org/assets/CVs/Screenshot_2023-09-06_at_12.57.18.png", caption="Stroke Data Insights", use_column_width=True)  
    

#Treatment
elif(app_mode=="Treatment"):
    st.header("Treatment🩺💉")
    image_path = "https://chaitanyastemcell.com/wp-content/uploads/2023/05/BEst-brain-stroke.png"
    st.image(image_path,use_column_width=True)
    st.markdown("""
                 ### Stroke Treatment
                  **Meaning**:
                   A stroke occurs when there is an interruption in blood flow to the brain, leading to the death of brain cells. It is a medical emergency, and timely treatment can significantly improve outcomes for stroke patients.

                  **Types of Strokes**:
                     - **Ischemic Stroke**: Caused by a blockage in a blood vessel supplying blood to the brain.
                     - **Hemorrhagic Stroke**: Occurs when a blood vessel ruptures, causing bleeding in the brain.

                  ### Treatment Approaches
                   **Emergency Treatment**:
                     - **For Ischemic Stroke**: Thrombolytic drugs (like tPA) may be administered to dissolve blood clots if the patient arrives within a critical time window (typically within 4.5 hours of the stroke).
                     - **For Hemorrhagic Stroke**: Surgery may be required to stop the bleeding and relieve pressure on the brain.

                  **Post-Stroke Care**:
                     - **Rehabilitation**: A multidisciplinary approach involving physical, speech, and occupational therapy is crucial for stroke recovery. The goal is to restore function and improve the quality of life.
                     - **Medications**: Anticoagulants, blood pressure medications, and cholesterol-lowering drugs may be prescribed to prevent future strokes.

                  **Lifestyle Modifications**:
                     - **Diet and Exercise**: A balanced diet, regular exercise, and maintaining a healthy weight can reduce the risk of stroke recurrence.
                     - **Controlling Risk Factors**: Managing risk factors like hypertension, diabetes, and high cholesterol is key to preventing strokes.

                 ### Preventing Stroke
                    **Meaning**:
                     Preventive care and lifestyle changes can significantly reduce the risk of having a stroke. Early detection of risk factors like hypertension or heart disease can help in managing stroke risks.

                    **Prevention Strategies**:
                     1. **Control Hypertension**: Regular monitoring of blood pressure and medication adherence.
                     2. **Healthy Diet**: Diet rich in fruits, vegetables, whole grains, and low in sodium and fats.
                     3. **Exercise Regularly**: Aim for at least 30 minutes of physical activity on most days.
                     4. **Quit Smoking and Limit Alcohol**: Smoking and excessive alcohol intake are major risk factors for stroke.
                     5. **Control Diabetes**: Proper management of blood sugar levels reduces stroke risks.

                 ### Stroke Rehabilitation
                    **Meaning**:
                     Stroke rehabilitation focuses on helping individuals regain skills and function lost due to the stroke. Rehabilitation begins as soon as the patient's condition is stable.

                    **Key Components**:
                     - **Physical Therapy**: Helps patients regain strength, mobility, and coordination.
                     - **Speech Therapy**: Aims to improve communication and swallowing abilities.
                     - **Occupational Therapy**: Assists patients in regaining the ability to perform daily activities and live independently.

                    **Important Note**:
                     Timely treatment is crucial to improving outcomes after a stroke. The faster the intervention, the better the chance of reducing brain damage and improving the chances of recovery.
    """)
    
    
    # Chatbot Section
elif app_mode == "Chatbot":
    st.title("SMART MINDALERT CHATBOT🗣️")
    st.write("Ask any questions about strokes, prevention, symptoms, or treatments.")
# Define a function for chatbot response
    def chatbot_response(user_query):
        responses = {
            "What is a brain stroke?": "A brain stroke occurs when blood flow to a part of the brain is interrupted, causing brain cell damage.",
            "What are the symptoms of a stroke?": "Symptoms include sudden numbness, confusion, trouble speaking, and difficulty walking.",
            "How can I prevent a stroke?": "Maintain a healthy lifestyle: control blood pressure, stay active, eat healthy, and avoid smoking.",
            "What should I do if I think someone is having a stroke?": "Call emergency services immediately. Time is critical in treating a stroke.",
            "Can strokes be treated?": "Yes, treatment options depend on the type and severity of the stroke.",
            "What increases the risk of a stroke?": "High blood pressure, smoking, diabetes, and a sedentary lifestyle are key risk factors.",
            "Tell me more about strokes.": "There are two main types of strokes: ischemic (caused by clots) and hemorrhagic (caused by bleeding in the brain).",
        }
 # Default response for unrecognized questions
        default_response = "I'm here to help! Please ask about stroke symptoms, prevention, or treatment."
        return responses.get(user_query, default_response)
    

# Suggested questions
    suggested_questions = [
        "What is a brain stroke?",
        "What are the symptoms of a stroke?",
        "How can I prevent a stroke?",
        "What should I do if I think someone is having a stroke?",
        "Can strokes be treated?",
        "What increases the risk of a stroke?",
        "Tell me more about strokes."
    ]

# Display suggested questions for user convenience
    st.write("### Suggested Questions:")
    for question in suggested_questions:
        st.write(f"- {question}")
        
    
        
 # Chat container
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("Ask a question about brain strokes:")

# Show chatbot response
    if user_input:
        response = chatbot_response(user_input)
        st.write("Response:", response)
        
# Handle user input
    if user_input:
        response = chatbot_response(user_input)
        st.session_state.chat_history.append(("user", user_input))
        st.session_state.chat_history.append(("bot", response))

    # Display chat history
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for sender, message in st.session_state.chat_history:
        if sender == "user":
            st.markdown(f'<div class="user-message">{message}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-message">{message}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    
       
# Load custom CSS for styling
    st.markdown("""
    <style>
        .chat-container {
            max-height: 400px;
            overflow-y: auto;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 10px;
            background-color: #f9f9f9;
        }
        .user-message {
            background-color: #dcf8c6;
            padding: 10px;
            border-radius: 10px;
            margin: 10px 0;
            width: fit-content;
            align-self: flex-end;
        }
        .bot-message {
            background-color: #ffffff;
            padding: 10px;
            border-radius: 10px;
            margin: 10px 0;
            width: fit-content;
            align-self: flex-start;
        }
        .user-message::before {
            content: "👤";
            margin-right: 5px;
        }
        .bot-message::before {
            content: "🤖";
            margin-right: 5px;
        }
    </style>
""", unsafe_allow_html=True)
    

# Video Consultation
elif app_mode == "Video Consultation":
    st.title("VIDEO CONSULTATION 📸")
    st.write("Consult a health professional via video call.")
    if st.button("Start Video Consultation"):
        st.info("Launching video consultation...")
        st.info("Connecting to a health professional... (Simulation)")
        webbrowser.open("https://meet.google.com/tvq-ywjo-wvx")

# Styling
st.markdown("""
<style>
.stButton>button {background-color: #4CAF50; color: white;}
.stTextInput input {border: 2px solid #ccc; padding: 10px;}
</style>
""", unsafe_allow_html=True)


# Custom styling
st.markdown(
    """
    <style>
    .stButton>button {background-color: #4CAF50; color: Red;}
    .stTextInput input {border: 2px solid #ccc; padding: 10px; font-size: 20px;}
    </style>
    """,
    unsafe_allow_html=True
)
       

# ---- Main Navigation (Dashboard Sidebar) ----
st.sidebar.title("Navigation 📌")
navigation_option = st.sidebar.radio("Select Section:", ["Navigation", "Home", "Brain Stroke Prediction"])


if navigation_option == "Home":
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTX-Q9uEiUN1NS9jPSNoyM0mDcw_3nIUJ7wMw&s", use_column_width=True) 
    st.markdown("""
        ## 🧠 Welcome to the Brain Stroke Prediction App
        This application allows you to predict the risk of stroke using AI models trained on **Brain CT Scan images**.
        
        - **CNN Model**: A convolutional neural network-based stroke classifier.
        - **Xception Model**: A deeper CNN architecture for better accuracy.
        - **Real-time Predictions** based on uploaded medical images.
    """)

elif navigation_option == "Brain Stroke Prediction":
    st.markdown("<h2 style='text-align: center;'>🧠 Brain Stroke Detection </h4>", unsafe_allow_html=True)
    
    # Upload Image
    uploaded_file = st.file_uploader("📤 Upload a Brain CT Scan image...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Brain CT Scan", use_column_width=True)

        # Model Selection
        model_choice = st.selectbox("Select AI Model:", ["CNN", "Xception", "Inception"])
        selected_model = cnn_model if model_choice == "CNN" else xception_model
        if model_choice == "CNN":
         selected_model = cnn_model
        elif model_choice == "Xception":
         selected_model = xception_model
        elif model_choice == "InceptionV3":
         selected_model = inception_model
         
        # Preprocess Image
        processed_image = preprocess_image(image)

        # Make Prediction
        prediction = selected_model.predict(processed_image)
        stroke_probability = prediction[0][0] * 100
        
        # Display the Prediction
        st.subheader("🩺 Prediction Result:")
        st.write(f"**Stroke Risk Probability:** {stroke_probability:.2f}%")

        if stroke_probability > 75: 
            st.error("🚨 High Risk of Stroke Detected! Emergency Alert Required⚠️!")
            patient_name = st.text_input("Enter Patient Name", "John Doe")
            st.markdown("## 🏥 Treatment Recommendation:")
            treatment_text = """
            - **Emergency Care:** Seek immediate medical attention.
            - **Medication:** Antiplatelet drugs (aspirin), anticoagulants, or clot-busting drugs like tPA.
            - **Surgery:** In severe cases, thrombectomy or carotid artery surgery may be required.
            - **Rehabilitation:** Speech therapy, physical therapy, and lifestyle modifications.
            - **Lifestyle Changes:** Quit smoking, control blood pressure, and maintain a healthy diet.
            """
            st.info(treatment_text)
            email_status = send_email_alert(patient_name, stroke_probability)
            st.success(email_status)
            
        else:
          st.success("✅ No Stroke Detected! 😍 Stay Healthy!")
          st.markdown("## 🌿 Healthy Lifestyle Tips:")
          healthy_tips = """
            - **Exercise Regularly:** Aim for 30 minutes of physical activity daily.
            - **Eat a Balanced Diet:** Include fruits, vegetables, and whole grains.
            - **Stay Hydrated:** Drink at least 8 glasses of water per day.
            - **Quit Smoking & Limit Alcohol:** Avoid tobacco and excessive alcohol.
            - **Manage Stress:** Practice meditation, yoga, or deep breathing exercises.
            - **Regular Check-Ups:** Monitor blood pressure, cholesterol, and glucose levels.
            """
          st.success(healthy_tips)
            
