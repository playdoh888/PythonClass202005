def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))

for i in x:
    print(i)

print("Another way to get the length of each word in the list")
for word in ('apple', 'banana', 'cherry'):
    print(len(word))