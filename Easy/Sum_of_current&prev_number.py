#For numbers from 0 to 10, print the sum of the current number and the previous number
for i in range(0, 11):
    if i == 1 or i == 0:
        prev_number = 0
    else:
        prev_number = i - 1
    sum = i + prev_number
    print(f"Current Number: {i}, Previous Number: {prev_number}, Sum: {sum}")