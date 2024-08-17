# Function for adding two numbers
def add(a, b):
    return a + b

# Function for subtracting two numbers
def subtract(a, b):
    return a - b

# Function for multiplying two numbers
def multiply(a, b):
    return a * b

# Function for dividing two numbers
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# Get user input
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

if choice in ['1', '2', '3', '4']:
    if choice == '1':
        print("Result=", add(number1, number2))
    elif choice == '2':
        print("Result=", subtract(number1, number2))
    elif choice == '3':
        print("Result=", multiply(number1, number2))
    elif choice == '4':
        print("Result=", divide(number1, number2))
else:
    print("Invalid input")
    