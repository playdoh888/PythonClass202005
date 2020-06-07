from sys import argv

script, first, second, third = argv

print("script name: {}".format(script))
a = first
b = second
c = int(a) + int(b)
print(f"{third}")

print("Sum of first and second parameter is {}".format(c))
