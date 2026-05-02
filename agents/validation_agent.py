from utils.simulation_engine import simulate_missing

def validate_claim(data):
    simulated_fields = {}

    for field in data["missing_fields"]:
        simulated_fields[field] = simulate_missing(field)

    return {
        "status": "validated",
        "simulated_fields": simulated_fields
    }
