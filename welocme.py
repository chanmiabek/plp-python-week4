# Week 4 Assignment: Functions
# File: welcome.py

def welcome_user(name="Student"):
    """Return a welcome message for the user."""
    return f"Welcome, {name}! Let's practice Python functions."


if __name__ == "__main__":
    student_name = input("Enter your name (or press Enter): ").strip()

    if student_name:
        print(welcome_user(student_name))
    else:
        print(welcome_user())