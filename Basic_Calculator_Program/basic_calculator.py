def calculator():
    # Get user input
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operator = input("Enter an operation (+, -, *, /): ")
    
    # Perform calculation based on the operation
    if operator == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operator == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operator == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operator. Please run again and enter +, -, *, or / . ")

# Run the calculator
calculator()
