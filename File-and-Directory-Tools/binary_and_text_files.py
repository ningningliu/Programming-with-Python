
# open binary files
"""

file = open('data.txt', 'wb') # open binary output file
file = open('data.txt','rb') # open binary input file

open('data.txt').read() # text mode: str
open('data.txt','rb').read() # binary mode: bytes

file = open('data.txt','rb')
for line in file: print(line)

"""
open('data.bin','wb').write(b'Spam\n')
open('data.bin','rb').read()

# Unicode encodings for text files #
data = 'sp\xe4m'
print(data)

"""
# manually encode
data.encode('latin1')   # 8-bit characters: ascii + extras
data.encode('utf8')     # 2 bytes for special characters only
data.encode('ascii')    # does not encode per ascii
data.encode('utf16')    # 2 bytes per character plus preamble
data.encode('cp500')    # an ebcdic encoding : very different
"""

# open with encoding
open('test.txt','w',encoding='latin1').write(data)
open('test.txt','rb').read() # return binary bytes

"""
REMARK:
    If text is ASCII, we can ignore encoding altogether. Data in files maps directly to characters in string, 
    beacuse ACII is a subset of most platforms' default encodings.
"""
