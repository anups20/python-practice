# Lists
list1 = [10,20,25,30,35]
list2 = [40,45,60,75,90]
new_list = []
# Create a new list with odd numbers from list1 and even numbers from list2
for i in list1:
    if i % 2 != 0:
        new_list.append(i)
for j in list2:
    if j % 2 == 0:
        new_list.append(j)
# Print the new list
print(new_list)