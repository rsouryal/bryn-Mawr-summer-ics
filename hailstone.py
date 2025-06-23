num = int(input("Enter an integer: "))

while num >= 2:
    if num % 2 == 0:
        num = num // 2
    else:
        num = num * 3 + 1
    print(f"The hailstone's current height is {num}")