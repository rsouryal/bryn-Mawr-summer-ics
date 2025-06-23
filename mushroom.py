mushrooms = []
check = True

while check:
    option = input("Enter mushroom weight or 'STOP': ")
    if option == "STOP":
        check = False
    elif int(option) < 1:
        print("Weight must be bigger than zero!")
    else:
        mushrooms.append(int(option))

# Count each size
counts = {}
for m in mushrooms:   
     if m in counts:
        counts[m] += 1
else:
        counts[m] = 1

print(f"Your mushrooms: {mushrooms}")
for size, count in counts.items():
    print(f"Weight {size}: {count} mushroom(s)")