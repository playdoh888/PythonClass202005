f = open("demofile", "r")
print(f.readline())
f.close()

"""
Often, it is hard to remember to close the file once we are done with the file. 
Python offers an easy solution for this. 
We can use with statement in Python such that we don’t have to close the file handler. 
The with statement creates a context manager and it will automatically close the file handler for you when you are done with it. 
Here is an example using with statement to read all lines of a file.
"""
filename = "demofile"
with open(filename, 'r') as fh:
    all_lines = fh.readlines()


in_filename = "demofile"
out_filename = "out_demofile.txt"
with open(in_filename) as in_file, open(out_filename, 'w') as out_file:
   for line in in_file:
        parsed_line = line.replace('e', 'E')
        out_file.write(parsed_line)