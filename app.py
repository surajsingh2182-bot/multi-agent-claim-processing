import streamlit as st
from agents.intake_agent import process_documents
from agents.validation_agent import validate_claim
from agents.fraud_agent import detect_fraud

st.set_page_config(page_title="AI Claim Processing", layout="wide")

st.title("Multi-Agent Claim Processing System")

uploaded_files = st.file_uploader(
    "Upload claim documents",
    accept_multiple_files=True
)

if uploaded_files:
    st.success(f"{len(uploaded_files)} files uploaded successfully")

    if st.button("Process Claim"):

        intake_result = process_documents(uploaded_files)
        validation_result = validate_claim(intake_result)
        fraud_result = detect_fraud(intake_result)

        st.subheader("Intake Agent Output")
        st.json(intake_result)

        st.subheader("Validation Agent Output")
        st.json(validation_result)

        st.subheader("Fraud Detection Output")
        st.json(fraud_result)
