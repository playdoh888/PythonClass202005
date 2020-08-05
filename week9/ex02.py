def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


# For loop to reverse the string
word = input("Please enter a word: ")
for char in rev_str(word):
    print(char)
