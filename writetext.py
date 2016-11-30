from os.path import exists

filename = raw_input("Input name of file: ")

have = exists(filename)
print "So does the file exist? %s" % have

print "Please input new content below"
raw_input("...")
contents = raw_input("Insert Here: ")

openfile = open(filename, 'w')
openfile.write(contents)

openfile.close()

raw_input("Now I will read it back...")

readback = open (filename)
print readback.read()

print "Now we will close the files."
readback.close()
