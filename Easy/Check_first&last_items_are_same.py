# Initialize an empty list to store the numbers
number_list = []
# Take 6 numbers as input from the user
for i in range(0,6):
    if i == 5:
        number = int(input("Enter last number: "))
    else:
        number = int(input("Enter a number: "))
    number_list.append(number)
if number_list[0] == number_list[-1]:
    print("True. First and last items are the same.")
else:
    print("False. First and last items are different.")
