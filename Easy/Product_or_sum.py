# This program takes two numbers as input and either multiplies them or adds them based on the product value.
number1 = input("Emter first number: ")
number2 = input("Enter second number: ")
product = int(number1) * int(number2)
# Check if the product is less than or equal to 1000
if product <= 1000:
    print("The result is:", product)
else:
    sum = int(number1) + int(number2)
    print("The result is:", sum)