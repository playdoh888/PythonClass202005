def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))

for i in x:
    print(i)