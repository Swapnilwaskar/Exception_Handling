# Task 1 Safe Division utility

try:
    numerator = float(input("enter the numberator"))
    denominator = float(input("Enter the denominator")) 
    result = numerator/denominator

except ValueError:
    print("Error: Please enter valid number")
except ZeroDivisionError:
    print("Error: Denomitor cannot be zero")

else:
    print("Result: ", result)

finally:
    print("Operation Complete")