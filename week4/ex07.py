f = open("demofile2", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2", "r")
print(f.read())

#/media/sf_SharedProjects/PythonClassProjects/PythonClass202005/week4