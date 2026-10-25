# Task 3: Custom exception: age validator

class AgeError(ValueError):
    pass


def check_age(age):
    if age < 1 or age > 120:
        raise AgeError("Age must be between 1 and 120")


try:
    age = int(input("Enter your age: "))
    check_age(age)
    print(f"Your age is {age}")
except ValueError as e:
    print(f"Error: {e}")
