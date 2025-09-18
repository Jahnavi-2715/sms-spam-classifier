import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("📩 SMS Spam Classifier")

message = st.text_area("Enter an SMS message:")

if st.button("Predict"):
    if message.strip() == "":
        st.warning("Please enter a message first!")
    else:
        data = vectorizer.transform([message])
        prediction = model.predict(data)[0]
        if prediction == 1:
            st.error("🚨 This looks like SPAM!")
        else:
            st.success("✅ This looks safe (HAM).")
