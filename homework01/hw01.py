"""
Question 1.
What is the output of the following
snippet?
"""

l1 = [1, 2]
for v in range(2):
    l1.insert(-1, l1[v])
print(l1)


#Question 3.


nums = [1, 2, 3]
vals = nums


def func1(a):
    return None


def func2(a):
    return func1(a) * func1(a)


print(func2(2))

#Question 6.


1 // 2

# Question 7.


def func(a, b):
    return b ** a


print(func(2, b=2))

# Question 8.

z = 0
y = 10
x = y < z and z > y or y > z and z < y

# Question 10.


list = [x * x for x in range(5)]


def fun(L):
    del L[L[2]]
    return L


print(fun(list))

# Question 11.

x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z
print(x, y, z)

# Question 12.

a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)

#Question 13.


def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2


print(fun(fun(2)))

#Question 14.

nums = [1, 2, 3]
vals = nums
del vals[:]

#Question 15.


x = int(input())
y = int(input())
x = x % y
x = x % y
y = y % x
print(y)

#Question 16.

y = input()
x = input()
print(x + y)

#Question 17.


print("a", "b", "c", sep="sep")

#Question 18.

X = 1 // 5 + 1 / 5
print(X)

#Question 19.


tuple[1] = tuple[1] + tuple[0]

