"""
******************************************************
(1) The \n digraph forces the print() function to:

    * output exactly two characters: \ and n
    * duplicate the character next to the digraph
    * stop its execution
    * break the output line
******************************************************
"""

print("Python wants to say:\nHello World!")

"""
******************************************************
(2) The meaning of the keyword parameter is determined by:

    * its position within the argument list
    * its value
    * its connection with existing variables
    * the argument’s name specified along with its value 

******************************************************
"""

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't" + action, )
    print("if you put" + str(voltage) + "volts through it.")
    print("-- Lovely plumage, the" + type)
    print("-- It's " + state + "!")


parrot(1000)  # 1 positional argument
parrot(voltage=1000)  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')  # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)  # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')  # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

"""
******************************************************
(3) The value twenty point twelve times ten raised to the power of eight should be written as:

    * 20E12.8
    * 20.12E8
    * 20.12*10^8
    * 20.12E8.0

******************************************************
"""

"""
******************************************************

(4) The 0o prefix means that the number after it is denoted as:
print(f"{oct(98)}")

    * decimal
    * binary
    * octal
    * hexadecimal

******************************************************
"""

"""
******************************************************

(5) Only one of the following statements is false – which one?
print(f"{1 / 1}")

    * multiplication precedes addition
    * the result of the / operator is always an integer value
    * the right argument of the % operator cannot be zero
    * the ** operator uses right sided binding

******************************************************
"""

"""
******************************************************
(6) One of the following variables’ names is illegal – which one?

    * true
    * tRUE
    * True
    * TRUE
******************************************************
"""

"""
******************************************************
(7) The print() function can output values of:

    * any number of arguments (excluding zero)
    * just one argument
    * any number of arguments (including zero)
    * not more than five arguments
******************************************************
"""

"""
******************************************************
(8) What is the output of the following snippet?
x=1
y=2
z=x
x=y
y=z
print(x,y)

    1 2
    2 1
    1 1
    2 2
******************************************************
"""

"""
******************************************************
(9)  What is the output of the following snippet if the user enters two lines containing 2 and 4 respectively?
x=input()
y=input()
print(x+y)

    * 6
    * 24
    * 4
    * 2
******************************************************
"""

"""
******************************************************
(10) What is the output of the following snippet if the user enters two lines containing 2 and 4 respectively?
x=int(input())
y=int(input())
x=x//y
y=y//x
print(y)

    ? 2.0
    ? the code will cause a runtime error
    ? 4.0
    ? 8.0
******************************************************
"""

# Floor division - division that results into whole number adjusted to the left in the number line

"""
******************************************************
(11) What is the output of the following snippet if the user enters two lines containing 2 and 4 respectively?

x=int(input())
y=int(input())
x=x/y
y=y/x
print(y)

    ? the code will cause a runtime error
    ? 8.0
    ? 4.0
    ? 2.0

******************************************************
"""

"""
******************************************************
(12) What is the output of the following snippet if the user enters two lines containing 11 and 4 respectively?
x=int(input())
y=int(input())
x = x % y
x = x % y
y = y % x
print(y)

    3
    2
    1
    4

******************************************************
"""

"""
******************************************************
(13) What is the output of the following snippet if the user enters two lines containing 3 and 6 respectively?
x=input()
y=int(input())
print(x*y)

    36
    18
    333333
    666

******************************************************
"""

"""
******************************************************
(14) What is the output of the following snippet?
z = y = x = 1
print(x,y,z,sep=’*’)

    1 1 1
    x y z
    1*1*1
    x*y*z

******************************************************
"""

"""
******************************************************

(15) What is the output of the following snippet?
x = 2 + 3 * 5.
print(X)

    the snippet will cause an execution error
    17
    17.0
    25.0

******************************************************
"""

"""
******************************************************
(16) What is the output of the following snippet?
x = 1 / 2 + 3 // 3 + 4 ** 2
print(x)

    17
    17.5
    8.5
    8
******************************************************
"""

"""
******************************************************
(17) 
    What is the output of the following snippet if the user enters two lines containing 2 and 4 respectively?
    x=int(input())
    y=int(input())
    print(x+y)

        4
        2
        24
        6

******************************************************
"""

