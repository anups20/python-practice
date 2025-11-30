#List of numbers divisible by 5
number_list =[]
divisible = []
# Take 9 numbers as input from the user
for i in range(1,10):
    if i == 9:
        number = int(input("Enter last number: "))
    else:
        number = int(input("Enter number: "))
    number_list.append(number)
# Check for numbers divisible by 5 and store them in a new list    
    if number % 5 == 0:
        divisible.append(number)
# Print the original list and the list of numbers divisible by 5
print(f"Given list is {number_list}")
print(f"Numbers divisible by 5 are:\n")
for j in divisible:
    print(f"{j}")