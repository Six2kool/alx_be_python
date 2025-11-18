num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))
operation = input("choose the operation(+,-,*,/): ")
match operation:
    case "for addition":
        result = num1 + num2
        print(f"the result is {result}.")
    case "subtract":
        result = num1 - num2
        print(f"the result is {result}.")
    case "multiply":
        result = num1 * num2
        print(f"the result is {result}.")
    case "divide":
        if num2 == 0:
            print("cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"the result is {result}.")    


