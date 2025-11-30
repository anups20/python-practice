string = str(input("Enter a string: "))
string = string.lower()
rev_string = string[::-1]
if string == rev_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")