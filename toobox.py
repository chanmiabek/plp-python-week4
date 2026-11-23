# Week 4 Assignment: Grades, Eligibility & Smart Decisions
# File: toolbox.py


def calculate_grade(score):
    """Return a letter grade based on the score."""

    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def check_eligibility(age, minimum_age=18):
    """Check whether a person meets the minimum age."""

    if age >= minimum_age:
        return "Eligible"
    else:
        return "Not eligible"


def make_decision(score, attendance: float = 75.0):
    """Determine the outcome based on score and attendance."""

    if score >= 70 and attendance >= 75:
        return "Pass: requirements met"

    elif score >= 70 and attendance < 75:
        return "Review: attendance requirement not met"

    else:
        return "Not passed: score requirement not met"


if __name__ == "__main__":

    score = float(input("Enter your score (0-100): "))
    age = int(input("Enter your age: "))
    attendance = float(input("Enter attendance percentage: "))

    print("\n--- Results ---")
    print("Grade:", calculate_grade(score))
    print("Eligibility:", check_eligibility(age))
    print("Decision:", make_decision(score, attendance))