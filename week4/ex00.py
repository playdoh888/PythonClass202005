mylist = ["apple", "banana", "cherry"]
x = len(mylist)

testList = []
print(testList, 'length is', len(testList))

testList = [1, 2, 3]
print(testList, 'length is', len(testList))

testTuple = (1, 2, 3)
print(testTuple, 'length is', len(testTuple))

testRange = range(1, 10)
print('Length of', testRange, 'is', len(testRange))


class Session:
    def __init__(self, number=0):
        self.number = number

    def __len__(self):
        return self.number


# default length is 0
s1 = Session()
print(len(s1))

# giving custom length
s2 = Session(6)
print(len(s2))
