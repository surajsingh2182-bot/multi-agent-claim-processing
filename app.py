import streamlit as st

st.set_page_config(page_title="AI Claim Processing", layout="wide")

st.title("Multi-Agent Claim Processing System")

uploaded_files = st.file_uploader(
    "Upload claim documents",
    accept_multiple_files=True
)

if uploaded_files:
    st.success(f"{len(uploaded_files)} files uploaded successfully")

    if st.button("Process Claim"):
        st.write("Running agents...")
