# Function to remove n characters from the beginning of a string
def remove_chars(word,n):
    print("Original String:", word)
    size = len(word)
    if n < size:
        new_word = word[n:]
        return new_word
    else:
        return "Number of characters to remove exceeds string length."
# Taking user input
index = int(input("Enter number of characters to remove from the string: "))
word = input("Enter a string: ")
# Calling the function and displaying the result
result = remove_chars(word, index)
print("String after removing characters:", result)