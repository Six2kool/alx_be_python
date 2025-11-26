def perform_operation(num1, num2, operation):
    """
    This function does add, subtract, multiply, or divide
    It takes two numbers and what operation to do
    """

    if operation == "add":
        return num1 + num2

    elif operation == "subtract":
        return num1 - num2

    elif operation == "multiply":
        return num1 * num2

    elif operation == "divide":
        if num2 == 0:
            return "Error: Cannot divide by zero!"  # Special message for zero
        else:
            return num1 / num2

    else:
        return "Error: Invalid operation! Use add, subtract, multiply, or divide."