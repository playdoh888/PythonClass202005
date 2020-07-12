def calculateSquare(n):
    return n*n


numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)

def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry', 'apple'), ('orange', 'lemon', 'pineapple', 'orange'))
sum_of_two = list(x)
print(sum_of_two)
