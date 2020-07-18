# You are creating a function that reads a data file and prints each line of the file.
# You write the following code. Line numbers are included for reference only

import os

def read_file(file):
    line = None
    if os.path.isfile(file):
        data = open(file, 'r')
    while line != '':
        line = data.readline()
        print()

# The code attempts to read the file even if the file does not exist.
# You need to correct the code.
# Which three lines have indentation problems? Each correct answer presents part of the solution. (Choose three.)

# A. Line 04
# B. Line 06
# C. Line 07
# D. Line 08
# E. Line 09
# F. Line 10
# G. Line 11
# H. Line 12

