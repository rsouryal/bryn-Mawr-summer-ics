# Palindrome Lab
# This program lets you enter a word or phrase and checks if it is a palindrome.
check= True
while check == True:

    text = input("Enter a word or phrase (or type 'quit' to exit): ")
    if text.lower() == "quit":
        print("Goodbye!")
        check = False
    chars = ""
    for char in text:
        chars = char + chars
    if chars == text:
        print("Palindrome!")
    else:
        print("Not a palindrome.")