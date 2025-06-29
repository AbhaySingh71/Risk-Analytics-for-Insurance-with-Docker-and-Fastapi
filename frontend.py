import streamlit as st
import requests

# ------------------------ Configuration ------------------------ #
API_URL = "http://34.205.23.88:8000/predict"

# ------------------------ App Header ------------------------ #
st.set_page_config(page_title="Insurance Premium Predictor", page_icon="💰")
st.title("💰 Insurance Premium Category Predictor")
st.markdown("Fill in the details below to predict your **insurance premium category** based on your profile.")

# ------------------------ User Inputs ------------------------ #
st.header(" User Information")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input(" Age", min_value=1, max_value=119, value=30)
    weight = st.number_input(" Weight (kg)", min_value=1.0, value=65.0)
    income_lpa = st.number_input(" Annual Income (LPA)", min_value=0.1, value=10.0)

with col2:
    height = st.number_input(" Height (m)", min_value=0.5, max_value=2.5, value=1.7)
    smoker = st.selectbox(" Are you a smoker?", options=[True, False])
    occupation = st.selectbox(
        " Occupation",
        ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job']
    )

city = st.text_input("🌆 City", value="Mumbai")

# ------------------------ Prediction ------------------------ #
if st.button("🔍 Predict Premium Category"):
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    with st.spinner("⏳ Sending data to prediction server..."):
        try:
            response = requests.post(API_URL, json=input_data)
            result = response.json()

            if response.status_code == 200 and "response" in result:
                prediction = result["response"]
                st.success(f"✅ Predicted Premium Category: **{prediction['predicted_category']}**")

                st.metric(" Confidence Score", f"{prediction['confidence']:.2f}")
                st.subheader("📊 Class Probabilities")
                st.json(prediction["class_probabilities"])

            else:
                st.error(" Received an unexpected response from the API.")
                st.json(result)

        except requests.exceptions.ConnectionError:
            st.error("❌ Could not connect to the Aws ec2 server. Please make sure it’s running and accessible.")
        except Exception as e:
            st.error("🚫 An error occurred during prediction.")
            st.exception(e)
