# Simple Calculator

# Get numbers from the user
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

# Ask the user which operation to perform
print(
    "Choose an operation: + for addition, - for subtraction, * for multiplication, / for division"
)
operation = input("Enter the operation: ")

# Perform the calculation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Cannot divide by zero."
else:
    result = "Invalid operation! Please choose +, -, *, or /"

# Show the result
print("Result:", result)
