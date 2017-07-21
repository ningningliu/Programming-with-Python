# Text File #
# text files contain Unicode text and their content is always a str string - a sequence of characters.

# Binary File #
# binary files contain raw 8-bit bytes. Their content is always a byte string - a sequence of samll integers.
# which support most str operations and displays ASCII characters.
# open( 'rb'/'wb') means file containing a binary data.


# Output Files #
file = open('data.txt','w')
file.write('Hello file word! \n')
file.write('Bye file world ! \n')
file.close() # colsed on gc and exit too

# alternatively use writelines
# it isn't commonly used but can be emulated with for loop or other iteration tools.
# it convenient to save output in a list to be written later.
file.writelines(['Hello file world! \n','Bye file world. \n'])







