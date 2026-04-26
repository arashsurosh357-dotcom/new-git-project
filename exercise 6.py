# Bonus function
def add_bonus(scores):
    return [score + 5 for score in scores]


# Main analyzer function
def analyze_student(name, *scores):
    if len(scores) == 0:
        return {"error": "No scores provided"}

    # Apply bonus
    scores = add_bonus(scores)

    avg = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)
    status = "Pass" if avg >= 50 else "Fail"

    return {
        "name": name,
        "scores": scores,
        "average": avg,
        "highest": highest,
        "lowest": lowest,
        "status": status
    }


# Report printer function
def print_report(report):
    if "error" in report:
        print(report["error"])
    else:
        for key, value in report.items():
            print(f"{key}: {value}")


# Example usage
student = analyze_student("Ali", 60, 70, 80, 40)
print_report(student)