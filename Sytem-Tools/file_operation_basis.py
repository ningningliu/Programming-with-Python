# read entire file into string
open('file').read()

# read next N bytes into string
open('file').read(N)

# read entire file into line string list
open('file').readlines()

# read next line through '\n'
open('file').readline()

# write a file
file = open('spam.txt','w')
file.write(('spam'*5)+'\n')
file.close()
# open and read a file
file = open('spam.txt')
text = file.read()

