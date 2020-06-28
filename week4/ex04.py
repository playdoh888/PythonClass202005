tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"

print(tup1)
print(tup2)
print(tup3)

tup1 = ()

tup2 = (1, 2, 3, 4, 5, 6, 7 )
# print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

coral = ('blue coral', 'staghorn coral', 'pillar coral', 'elkhorn coral')

print(coral)
print(coral[-4])

print('This reef is made up of ' + coral[1])
print(coral[1:3])

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
print(numbers[1:11:2])

print(numbers[::3])


coral = ('blue coral', 'staghorn coral', 'pillar coral', 'elkhorn coral')
kelp = ('wakame', 'alaria', 'deep-sea tangle', 'macrocystis')

coral_kelp = (coral + kelp)

print(coral_kelp)

more_numbers = (11.13, 34.87, 95.59, 82.49, 42.73, 11.12, 95.57)
print(max(more_numbers))
print(min(more_numbers))

# coral[0] = 'black coral'

newcoral= list(coral)

print(newcoral)

newcoral[0] = 'red coral'
print(newcoral)