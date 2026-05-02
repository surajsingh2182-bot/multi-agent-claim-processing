def process_documents(uploaded_files):
    extracted_data = {
        "claim_id": "CLM001",
        "documents_uploaded": [file.name for file in uploaded_files],
        "missing_fields": ["policy_number"],
        "claim_amount": 150000,
        "policy_age_days": 15,
        "previous_claims": 4
    }

    return extracted_data
