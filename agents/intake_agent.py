def process_documents(uploaded_files):
    extracted_data = {
        "claim_id": "CLM001",
        "documents_uploaded": [file.name for file in uploaded_files],
        "missing_fields": ["policy_number"]
    }

    return extracted_data
