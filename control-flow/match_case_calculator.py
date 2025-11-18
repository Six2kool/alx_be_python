num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
Choose_the_operation = input("Choose the operation (+, -, *, /): ")
match Choose_the_operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "divide":
        if num2 == 0:
            print("cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")    


