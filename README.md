# 📈 Advertising Click Prediction

An end-to-end Machine Learning project that predicts whether a user will click on an online advertisement based on demographic and behavioral features.

The project includes data preprocessing, model training, and deployment using Streamlit.

---

[https://your-app.streamlit.app
](https://advertising-click-prediction-fyglg89uav8pl9podqdet5.streamlit.app/)
---

## 📌 Features

- Predict whether a customer will click on an advertisement.
- Choose between **K-Nearest Neighbors (KNN)** and **Naive Bayes** models.
- Interactive Streamlit web interface.
- Displays prediction confidence.
- User-friendly input form.

---

## 📊 Dataset

The project uses the **Advertising Dataset**.

### Features

- Daily Time Spent on Site
- Age
- Area Income
- Daily Internet Usage
- Gender (Male/Female)

### Target

- Clicked on Ad
    - 1 → Clicked
    - 0 → Not Clicked

---

## 🤖 Machine Learning Models

- K-Nearest Neighbors (KNN)
- Gaussian Naive Bayes

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

---

## 📂 Project Structure

```
advertising-click-prediction/
│
├── app.py
├── advertising.csv
├── knn_model.pkl
├── nb_model.pkl
├── scaler.pkl
├── session_9.ipynb
├── requirements.txt
└── README.md
```

---

## ▶️ Run Locally

Clone the repository

```bash
git clone https://github.com/Ziad-Bahaa2006/advertising-click-prediction.git
```

Move to the project folder

```bash
cd advertising-click-prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit app

```bash
streamlit run app.py
```

```
assets/app.png
```

---

## 📈 Future Improvements

- Add more Machine Learning models.
- Hyperparameter tuning.
- Better UI/UX.
- Feature importance visualization.
- Model performance comparison.

---

## 👨‍💻 Author

**Ziad Bahaa**

- GitHub: https://github.com/Ziad-Bahaa2006
---

⭐ If you found this project useful, consider giving it a star.
