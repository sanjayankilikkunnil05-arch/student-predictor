# 🎓 Student Performance Predictor

A machine learning web application that predicts whether a student will pass or fail based on study hours and sleep patterns.

---

## 🚀 Overview
This project uses a Logistic Regression model to analyze student behavior and predict academic performance. It provides real-time predictions along with confidence scores and smart suggestions.

---

## ⚙️ Features
- Predicts PASS/FAIL based on input data  
- Displays prediction confidence using probability scores  
- Provides smart suggestions to improve performance  
- Simple and interactive UI using Streamlit  

---

## 🧠 Machine Learning Model
- Algorithm: Logistic Regression  
- Input Features:
  - Study Hours  
  - Sleep Hours  
- Output:
  - 1 → Pass  
  - 0 → Fail  

---

## 🛠️ Tech Stack
- Python  
- Pandas  
- Scikit-learn  
- Streamlit  

---

## 📂 Dataset
A small sample dataset is used within the code for training:
- Includes study hours, sleep hours, and pass/fail labels  
- Used for demonstration and learning purposes  

---

## ▶️ How to Run

```bash
git clone https://github.com/sanjayankilikkunnil05-arch/student-predictor
cd student-predictor
pip install -r requirements.txt
streamlit run app.py
