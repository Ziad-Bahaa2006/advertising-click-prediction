import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
    page_title="Advertising Click Prediction",
    page_icon="📈",
    layout="centered"
)

# -----------------------
# Load Models
# -----------------------
knn = joblib.load("knn_model.pkl")
nb = joblib.load("nb_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("📈 Advertising Click Prediction")
st.write("Predict whether a customer will click on an advertisement.")

st.divider()

# -----------------------
# Choose Model
# -----------------------
model_name = st.selectbox(
    "Choose Machine Learning Model",
    ["KNN", "Naive Bayes"]
)

if model_name == "KNN":
    model = knn
else:
    model = nb

# -----------------------
# User Input
# -----------------------

col1, col2 = st.columns(2)

with col1:
    daily_time = st.number_input(
        "Daily Time Spent on Site",
        min_value=0.0
    )

    age = st.number_input(
        "Age",
        min_value=1
    )

    income = st.number_input(
        "Area Income",
        min_value=0.0
    )

with col2:

    internet = st.number_input(
        "Daily Internet Usage",
        min_value=0.0
    )

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

male = 1 if gender == "Male" else 0

st.divider()

# -----------------------
# Prediction
# -----------------------

if st.button("Predict", use_container_width=True):

    data = pd.DataFrame({
        "Daily Time Spent on Site":[daily_time],
        "Age":[age],
        "Area Income":[income],
        "Daily Internet Usage":[internet],
        "Male":[male]
    })

    data = scaler.transform(data)

    prediction = model.predict(data)[0]

    probability = model.predict_proba(data)[0]

    confidence = max(probability) * 100

    st.subheader("Prediction Result")

    if prediction == 1:
        st.success("✅ Customer WILL click on the advertisement.")
    else:
        st.error("❌ Customer will NOT click on the advertisement.")

    st.metric(
        "Confidence",
        f"{confidence:.2f}%"
    )

    st.subheader("Input Summary")

    st.dataframe(pd.DataFrame({
        "Feature":[
            "Daily Time Spent on Site",
            "Age",
            "Area Income",
            "Daily Internet Usage",
            "Gender"
        ],
        "Value":[
            daily_time,
            age,
            income,
            internet,
            gender
        ]
    }), use_container_width=True)