import sys
from robust_division_calculator import safe_divide

def main():
    # Must have exactly 3 parts: python main.py 10 5
    if len(sys.argv) != 3:
        print("Usage: python main.py <number1> <number2>")
        print("Example: python main.py 10 5")
        return

    numerator = sys.argv[1]      # first number you typed
    denominator = sys.argv[2]    # second number

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()