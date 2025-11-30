# Take a string and a substring as input from the user
string = input("Enter a string: ")
substring = input("Enter the substring to be counted: ")
# Count the occurrences of the substring in the string
count = string.count(substring)
# Print the count of occurrences
print(f"{substring} occurs {count} times.")