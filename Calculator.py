print("Welcome to our calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Remainder")

option = input("Enter the operation you would like me to do: ").lower()

if option == "addition":
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    sum_result = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum_result}")

elif option == "subtraction":
    num3 = int(input("Enter num3: "))
    num4 = int(input("Enter num4: "))
    subtraction = num3 - num4
    print(f"The subtraction of {num3} and {num4} is {subtraction}")

elif option == "multiplication":
    num5 = int(input("Enter num5: "))
    num6 = int(input("Enter num6: "))
    product = num5 * num6
    print(f"The product of {num5} and {num6} is {product}")

elif option == "division":
    num7 = int(input("Enter num7: "))
    num8 = int(input("Enter num8: "))
    if num8 != 0:
        quotient = num7 / num8
        print(f"The quotient of {num7} and {num8} is {quotient}")
    else:
        print("Error: Division by zero is not allowed.")

elif option == "remainder":
    num9 = int(input("Enter num9: "))
    num10 = int(input("Enter num10: "))
