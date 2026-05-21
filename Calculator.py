# Function for addition
def addition(a, b):
    return a + b


# Function for subtraction
def subtraction(a, b):
    return a - b


# Function for multiplication
def multiplication(a, b):
    return a * b


# Function for division
def division(a, b):

    if b == 0:
        return "Division by zero is not possible"

    return a / b


# Main program using while loop
while True:

    print("\n===== SIMPLE CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Exit option
    if choice == "5":
        print("Calculator Closed")
        break

    # Invalid choice
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice")
        continue

    # Input numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform operation
    if choice == "1":
        result = addition(num1, num2)
        print("Result:", result)

    elif choice == "2":
        result = subtraction(num1, num2)
        print("Result:", result)

    elif choice == "3":
        result = multiplication(num1, num2)
        print("Result:", result)

    elif choice == "4":
        result = division(num1, num2)
        print("Result:", result)