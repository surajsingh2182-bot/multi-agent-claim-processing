def simulate_missing(field):
    defaults = {
        "hospital_name": "Apollo Hospital",
        "claim_amount": 50000,
        "policy_type": "Gold Health Plan",
        "policy_number": "POL123456"
    }

    return defaults.get(field, "Unknown")
