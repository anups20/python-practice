#Accept string from user
input_text = input("Enter a string: ")
#Output characters at even index positions
size = len(input_text)
print(f"Original String is {input_text}")
print(f"Printing only even index chars:")
for i in range(0,size-1,2):
    print(f"\n{input_text[i]}")