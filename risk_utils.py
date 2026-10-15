def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)


def risk_level(age, cholesterol, bmi):
    score = 0
    if age > 50:
        score += 2
    if cholesterol > 240:
        score += 3
    if bmi > 30:
        score += 2
    if score >= 5:
        return "high"
    elif score >= 3:
        return "medium"
    return "low"


def average_risk(patients):
    total = sum(p["score"] for p in patients)
    return total / len(patients)
