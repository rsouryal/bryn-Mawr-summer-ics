nums = []

operations = ["addition", "subtraction", "multiplication", "division", "modular division"]

option = input("Enter the operation you would like to perform: ").strip().lower()

if option == "addition":
    num1 = int(input("1: "))
    num2 = int(input("2: "))
    nums.append(num1)
    nums.append(num2)
    
    result = nums[0] + nums[1]
    print(f"The sum of {num1} and {num2} is {result}")

elif option == "subtraction":
    num3 = int(input("3: "))
    num4 = int(input("4: "))
    nums.append(num3)
    nums.append(num4)
    result = nums[0] - nums[1]
    print(f"The difference between {nums[0]} and {nums[1]} is {result}")

elif option == "multiplication":
    num5 = int(input("5: "))
    num6 = int(input("6: "))
    nums.append(num5)
    nums.append(num6)
    result = nums[0] * num[1]
    print(f"The product of {nums[0]} and {nums[1]} is {result}")
 
elif option == "division":
    num7 = int(input("7: "))
    num8 = int(input("8: "))
    nums.append(num7)
    nums.append(num8)
    result = nums[0] / nums[1]
    print(f"The quotient of {nums[0]} and {nums[1]} is {result}")

elif option == "modular division":
    num9 = int(input("9: "))
    num10 = int(input("10: "))
    nums.append(num9)
    nums.append(num10)
    result = nums[0] % nums[1]
    print(f"The remainder of {nums[0]} and {nums[1]} is {result}")
    
