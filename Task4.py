# Task 4: File reader with exception handling

filename = input("Enter a filename: ")

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines[:3]:
            print(line.rstrip())
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("File operation attempted.")
