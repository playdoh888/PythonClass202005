f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3", "r")
print(f.read())

"""
"x" - Create - will create a file, returns an error if the file exist

"a" - Append - will create a file if the specified file does not exist

"w" - Write - will create a file if the specified file does not exist

"""

# Result: a new empty file is created!
f = open("myfile.txt", "x")

# Create a new file if it does not exist:
f = open("myfile2.txt", "w")
f.write("Woops! I have deleted the content!")