import pandas as pd
from sklearn.linear_model import LogisticRegression
import streamlit as st

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(page_title="Student Predictor", page_icon="🎓")

# ---------------------------
# DATASET
# ---------------------------
data = {
    'hours': [1,2,3,4,5,6,7,8,2,3,6,7],
    'sleep': [8,7,6,6,5,5,4,4,7,6,5,4],
    'pass':  [0,0,0,1,1,1,1,1,0,0,1,1]
}

df = pd.DataFrame(data)

# ---------------------------
# MODEL TRAINING
# ---------------------------
X = df[['hours','sleep']]
y = df['pass']

model = LogisticRegression()
model.fit(X, y)

# ---------------------------
# UI
# ---------------------------
st.title("🎓 Student Performance Predictor")
st.write("Enter study hours and sleep hours to predict result")
st.write("---")

# User input
hours = st.number_input("📚 Hours Studied", min_value=0.0, max_value=12.0, step=0.5)
sleep = st.number_input("😴 Sleep Hours", min_value=0.0, max_value=12.0, step=0.5)

# ---------------------------
# PREDICTION
# ---------------------------
if st.button("Predict"):

    # Validation
    if hours == 0 and sleep == 0:
        st.warning("⚠️ Please enter valid values")

    else:
        result = model.predict([[hours, sleep]])
        prob = model.predict_proba([[hours, sleep]])

        if result[0] == 1:
            st.success(f"✅ PASS (Confidence: {prob[0][1]*100:.2f}%)")
        else:
            st.error(f"❌ FAIL (Confidence: {prob[0][0]*100:.2f}%)")

        st.write("---")

        # ---------------------------
        # SMART SUGGESTIONS (AGENT STYLE)
        # ---------------------------
        if hours < 3:
            st.warning("⚠️ Study hours are too low. Try increasing study time.")

        elif hours >= 5:
            st.success("👍 Good study effort!")

        if sleep > 8:
            st.info("💡 Too much sleep may reduce study efficiency.")

        elif sleep < 4:
            st.warning("⚠️ Very low sleep can affect performance.")
               

































