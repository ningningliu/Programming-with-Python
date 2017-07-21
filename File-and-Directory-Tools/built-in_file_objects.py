"""
#Text File #
text files contain Unicode text and their content is always a str string - a sequence of characters.

# Binary File #
binary files contain raw 8-bit bytes. Their content is always a byte string - a sequence of small integers.
which support most str operations and displays ASCII characters.
open( 'rb'/'wb') means file containing a binary data.

"""

# Output Files #

# opening
file = open('data.txt','w')

# writing
file.write('Hello file word! \n')
file.write('Bye file world ! \n')
"""
# writelines()
# it isn't commonly used but can be emulated with for loop or other iteration tools.
# it convenient to save output in a list to be written later.

file.writelines(['Hello file world! \n','Bye file world. \n'])
"""

# closing
file.close() # colsed on gc and exit too

# With statement provides more concise alternative to open, write , close files
"""
with open(filename, 'w') as myfile:
    ...process myfile , auto-closed  on a statement exit...
    
with A() as a, B() as b:
    ...statements...
    
with A() as A:
    with B() as b:
        ...statements..
"""
with open('data.txt') as fin, open('results','w') as fout:
    for line in fin:
        fout.write((line))



#  Input Files #
file = open('data.txt')
lines = file.readlines() # open input file object : 'r' default
for line in lines: # use file line iterator
    print(line, end='') # have a '\n' at end

# read
# there is many ways to read input file
"""
file.read() : 
    returns a string containing all the characters or bytes stored in a file
    
file.read(N):
    returns a string containing next N characters or bytes from the file
    
file.readline():
    reads through the next \n and return a line string
    
file.readlines():
    reads the entire file and returns a list of line strings
    
REMARK:
    read() and readlines() are not good thing to do if loading huge files.
    read(N) and readline() are safer which only call part of the file.
    
"""

# call
file.seek(0) # go back to the start of the file
file.readline()

# reading lines with file iterators
file = open('data.txt')
for line in file.readlines(): # DON'T DO THIS: now python provides more efficient way
    print(line , end='')

file = open('data.txt')
for line in file: # this methods used commonly now
    print(line, end='')

# shorter way
for line in open('data.txt'):
    print(line, end='')














