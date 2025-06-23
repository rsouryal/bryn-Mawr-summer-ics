nums = [
    "addition", 
    "subtraction", 
    "multiplication", 
    "division", 
    "modular division",
    "list addition",
    "list multiplication"
]

option = input("Enter the operation you would like to perform: ").strip().lower()

if option == "addition":
    num1 = int(input("1: "))
    num2 = int(input("2: "))
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}")

elif option == "subtraction":
    num3 = int(input("3: "))
    num4 = int(input("4: "))
    result = num3 - num4
    print(f"The difference between {num3} and {num4} is {result}")

elif option == "multiplication":
    num5 = int(input("5: "))
    num6 = int(input("6: "))
    result = num5 * num6
    print(f"The product of {num5} and {num6} is {result}")
 
elif option == "division":
    num7 = int(input("7: "))
    num8 = int(input("8: "))
    if num8 == 0:
        print("Error: Division by zero.")
    else:
        result = num7 / num8
        print(f"The quotient of {num7} and {num8} is {result}")

elif option == "modular division":
    num9 = int(input("9: ")
    num10 = int(input("10: "))
    if num10 == 0:
        print("Error: Division by zero.")
    else:
        result = num9 % num10
        print(f"The remainder of {num9} and {num10} is {result}")

