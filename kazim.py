import math

def display_menu():
    print("\n================ SCIENTIFIC CALCULATOR ================")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Square Root (√x)")
    print("7. Factorial (n!)")
    print("8. Logarithm (log10)")
    print("9. Natural Logarithm (ln)")
    print("10. Sine (sin) [Degrees]")
    print("11. Cosine (cos) [Degrees]")
    print("12. Tangent (tan) [Degrees]")
    print("13. Exit")
    print("======================================================")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("Enter choice (1-13): ").strip()

        if choice == '13':
            print("\nExiting calculator. Goodbye!")
            break

        # Operations requiring two inputs
        if choice in ['1', '2', '3', '4', '5']:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == '1':
                print(f"\nResult: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"\nResult: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"\nResult: {num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("\nError: Division by zero is undefined.")
                else:
                    print(f"\nResult: {num1} / {num2} = {num1 / num2}")
            elif choice == '5':
                print(f"\nResult: {num1} ^ {num2} = {math.pow(num1, num2)}")

        # Operations requiring one input
        elif choice in ['6', '7', '8', '9', '10', '11', '12']:
            num = get_number("Enter number: ")

            if choice == '6':
                if num < 0:
                    print("\nError: Cannot compute square root of a negative number.")
                else:
                    print(f"\nResult: √{num} = {math.sqrt(num)}")

            elif choice == '7':
                if num < 0 or not num.is_integer():
                    print("\nError: Factorial requires a non-negative integer.")
                else:
                    print(f"\nResult: {int(num)}! = {math.factorial(int(num))}")

            elif choice == '8':
                if num <= 0:
                    print("\nError: Logarithm undefined for zero or negative values.")
                else:
                    print(f"\nResult: log10({num}) = {math.log10(num)}")

            elif choice == '9':
                if num <= 0:
                    print("\nError: Natural logarithm undefined for zero or negative values.")
                else:
                    print(f"\nResult: ln({num}) = {math.log(num)}")

            elif choice == '10':
                rad = math.radians(num)
                print(f"\nResult: sin({num}°) = {math.sin(rad)}")

            elif choice == '11':
                rad = math.radians(num)
                print(f"\nResult: cos({num}°) = {math.cos(rad)}")

            elif choice == '12':
                # Check for undefined points (90, 270, etc.)
                if (num - 90) % 180 == 0:
                    print(f"\nError: tan({num}°) is undefined.")
                else:
                    rad = math.radians(num)
                    print(f"\nResult: tan({num}°) = {math.tan(rad)}")

        else:
            print("\nInvalid selection! Please choose a number between 1 and 13.")

if __name__ == "__main__":
    main()