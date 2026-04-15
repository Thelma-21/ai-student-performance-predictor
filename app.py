import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import streamlit as st

df = pd.read_csv("student_data.csv")
df['Pass_Fail'] = (df['math score'] >= 50).astype(int)

X = df[['reading score', 'writing score']]
y = df['Pass_Fail']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
acc = accuracy_score(y_test, predictions)

st.title("🎓 Student Performance Predictor")

st.metric(label="Model Accuracy", value=f"{acc * 100:.1f}%")

st.divider()

st.subheader("📊 Training Data Overview")
chart_data = df[['reading score', 'writing score', 'Pass_Fail']].copy()
st.scatter_chart(chart_data, x='reading score', y='writing score', color='Pass_Fail')

st.divider()

st.subheader("🔍 Make a Prediction")
reading = st.slider("Reading Score", 0, 100)
writing = st.slider("Writing Score", 0, 100)

if st.button("Predict"):
    input_df = pd.DataFrame([[reading, writing]], columns=['reading score', 'writing score'])
    result = model.predict(input_df)
    confidence = model.predict_proba(input_df)[0]
    pass_conf = confidence[1] * 100
    fail_conf = confidence[0] * 100

    if result[0] == 1:
        st.success("✅ Student will PASS")
    else:
        st.error("❌ Student will FAIL")

    st.write(f"**Confidence:** {pass_conf:.1f}% Pass / {fail_conf:.1f}% Fail")
    st.progress(int(pass_conf))
