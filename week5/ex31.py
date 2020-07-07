"""
**********************************************************************
(1) An operator able to check whether two values are equal is coded as:

    =
    ===
    ==
    !=

**********************************************************************
"""

"""
**********************************************************************
(2) The value eventually assigned to x is equal to:
x = 1
x = x == x

    False
    1
    True
    0

**********************************************************************
"""

"""
**********************************************************************
(3) How many stars will the following snippet send to the console?
i = 0
while i <= 3 :
    i += 2
    print("*")

    two
    zero
    one
    three

**********************************************************************
"""

"""
**********************************************************************
(4) How many stars will the following snippet send to the console?
i = 0
while i <= 5 :
    i += 1
    if i % 2 == 0:
        break
    print("*")

    zero
    one
    two
    three



**********************************************************************
"""

"""
**********************************************************************
(5) How many hashes will the following snippet send to the console?
for i in range(1):
    print("#")
else:
    print("#")

    one
    two
    zero
    three

**********************************************************************
"""

"""
**********************************************************************
(6) How many hashes will the following snippet send to the console?
var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print("#")

    two
    zero
    one
    three

**********************************************************************
"""

"""
**********************************************************************
(7) How many stars will the following snippet send to the console?
var = 1
while var < 10:
    print("#")
    var = var << 1

    eight
    one
    four
    two

		    if x = 10 (0000 1010 in binary) and y = 4 (0000 0100 in binary)
			&
				Bitwise AND
				x & y = 0 (0000 0000)
		
			|
				Bitwise OR
				x | y = 14 (0000 1110)
		
			~
				Bitwise NOT
				~x = -11 (1111 0101)
		
			^
				Bitwise XOR
				x ^ y = 14 (0000 1110)
		
			>>
				Bitwise right shift
				x >> 2 = 2 (0000 0010)
		
			<<
				Bitwise left shift
				x << 2 = 40 (0010 1000)

**********************************************************************
"""

"""
**********************************************************************
(8) What value will be assigned to the x variable?
z = 10
y = 0
x = y < z and z > y or y > z and z < y

    0
    1
    True
    False

**********************************************************************
"""

"""
**********************************************************************
(9) What is the output of the following snippet?
a = 1
b = 0
c = a & b
d = a | b
e = a ^ b
print(c + d + e)

    1
    3
    2
    0


**********************************************************************
"""

"""
**********************************************************************
(10) What is the output of the following snippet?
lst = [3, 1, -2]
print(lst[lst[-1]])

    1
    -2
    3
    -1

**********************************************************************
"""

"""
**********************************************************************
(11) What is the output of the following snippet?
lst = [1,2,3,4]
print(lst[-3:-2])

    [2,3,4]
    [2]
    []
    [2,3]


**********************************************************************
"""

"""
**********************************************************************
(12) The second assignment:
vals = [0, 1, 2]
vals[0], vals[2] = vals[2], vals[0]

    doesn’t change the list
    extends the list
    shortens the list
    reverses the list

**********************************************************************
"""
"""
**********************************************************************
(13) After execution of the following snippet, the sum of all vals elements will be equal to:
vals = [0, 1, 2]
vals.insert(0,1)
del vals[1]

    2
    5
    3
    4

**********************************************************************
"""

"""
**********************************************************************
(14) Take a look at the snippet, and choose the true statement:
nums = [1,2,3]
vals = nums
del vals[1:2]

    nums is longer than vals
    vals is longer than nums
    nums and vals are of the same length
    the snippet will cause a runtime error

**********************************************************************
"""

"""
**********************************************************************
(15) Which of the following sentences is true?
nums = [1,2,3]
vals = nums[-1:-2]

    nums is longer than vals
    nums and vals are of the same length
    the snippet will cause a runtime error
    vals is longer than nums


**********************************************************************
"""

"""
**********************************************************************
(16) What is the output of the following snippet?
l1 = [1,2,3]
l2 = []
for v in l1:
    l2.insert(0,v)
print(l2)

    [3,2,1]
    [1,2,3]
    [3,3,3]
    [1,1,1]

**********************************************************************
"""
"""
**********************************************************************
(17) What is the output of the following snippet?
l1 = [1,2,3]
for v in range(len(l1)):
    l1.insert(1,l1[v])
print(l1)

    [1, 2, 3, 3, 2, 1]
    [1, 2, 3, 1, 2, 3]
    [3, 2, 1, 1, 2, 3]
    [1, 1, 1, 1, 2, 3]

**********************************************************************
"""
"""
**********************************************************************
(18) How many elements does the L list contain?
L = [i for i in range(-1,2)]

    one
    four
    three
    two

**********************************************************************
"""

"""
**********************************************************************
(19) What is the output of the following snippet?
T = [[3-i for i in range (3)] for j in range (3)]
s = 0
for i in range(3):
    s += T[i][i]
print(s)

    4
    2
    7
    6

**********************************************************************
"""

"""
**********************************************************************
(20) What is the output of the following snippet?
L = [[0, 1, 2, 3] for i in range(2)]
print(L[2][0])

    the snippet will cause a runtime error
    1
    2
    0

**********************************************************************
"""

