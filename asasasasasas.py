text = input("Enter a string: \r")

if(text[::-1] == text[::]):
    print("palindrome!")
else:
    print("No palindrome...")
