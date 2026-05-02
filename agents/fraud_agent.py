def detect_fraud(claim_data):
    fraud_score = 0
    flags = []

    # Rule 1: High claim amount
    claim_amount = claim_data.get("claim_amount", 50000)

    if claim_amount > 100000:
        fraud_score += 0.4
        flags.append("High claim amount")

    # Rule 2: Recently activated policy
    policy_age_days = claim_data.get("policy_age_days", 20)

    if policy_age_days < 30:
        fraud_score += 0.3
        flags.append("Recently activated policy")

    # Rule 3: Multiple previous claims
    previous_claims = claim_data.get("previous_claims", 3)

    if previous_claims > 2:
        fraud_score += 0.2
        flags.append("Multiple previous claims")

    # Determine risk
    if fraud_score >= 0.7:
        risk_level = "high"
    elif fraud_score >= 0.4:
        risk_level = "medium"
    else:
        risk_level = "low"

    return {
        "fraud_score": round(fraud_score, 2),
        "risk_level": risk_level,
        "flags": flags
    }
