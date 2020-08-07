# You are writing a Python program to automate inventory.
# Your first task is to read a file of inventory transactions.
# The file contains sales from the previous day, including the item id, price, and quantity.
# The following shows a sample of data from the file:

# The code must meet the following requirements:
#
# -> Each line of the file must be read and printed
# -> If a blank line is encountered, it must be ignored
# -> When all lines have been read, the file must be closed

inventory = open("inventory.txt", "r")
eof = False
while eof == False:
    line = inventory.readline()
    # if line != '\n':       #A
    #     if line != "":
    #         print(line)
    # if line != '\n':       #B
    #     if line != None:
    #         print(line)
    # if line != '':       #C
    #     if line != "":
    #         print(line)
    if line != '':       #D
        if line != "\n":
            print(line)
    else:
        print("End of file")
        eof = True
        inventory.close()

# Method	Argument
# read([n])	    Reads and returns n bytes or less (if there aren't enough characters to read)
#               from the file as a string. If n not specified, it reads the entire file as a string and returns it.
# readline()	Reads and returns the characters until the end of the line is reached as a string.
# readlines()	Reads and returns all the lines as a list of strings.
#
# When the end of the file (EOF) is reached the read() and readline() methods returns an empty string,
# while readlines() returns an empty list ([]).