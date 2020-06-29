"""
Filtering - The function

    filter(function, sequence)

offers an elegant way to filter out all the elements of a sequence "sequence",
for which the function function returns True.
i.e. an item will be produced by the iterator result of filter(function, sequence)
if item is included in the sequence "sequence" and if function(item) returns True.

In other words: The function filter(f,l) needs a function f as its first argument.
f has to return a Boolean value, i.e. either True or False.
This function will be applied to every element of the list l.
Only if f returns True will the element be produced by the iterator,
which is the return value of filter(function, sequence).
"""

fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
odd_numbers = list(filter(lambda x: x % 2, fibonacci))
print(odd_numbers)
# [1, 1, 3, 5, 13, 21, 55]

even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
print(even_numbers)
# [0, 2, 8, 34]

even_numbers = list(filter(lambda x: x % 2 -1, fibonacci))
print(even_numbers)
# [0, 2, 8, 34]


# list of letters
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filterVowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(letter in vowels):
        return True
    else:
        return False

filteredVowels = filter(filterVowels, letters)

print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)