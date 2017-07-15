# find(), return str index
mystr = 'xxxSPAMxxx'
mystr.find('SPAM')

# global replacement
mystr = 'xxaaxxaa'
mystr.replace('aa','SPAM')
print(mystr.replace('aa','SPAM'))

# in statement, return True or False
mystr = 'xxxSPAMxxx'
print('SPAM' in mystr)

# remove whitespace
mystr = '\t Ni\n'
print(mystr)
mystr.strip()

# remove right side whitespace
mystr.rstrip()

# case converter
mystr.lower()

# content test
mystr.isalpha()
mystr.isdigit()

import string
print(string.ascii_lowercase)
print(string.whitespace) # whitespaces characters

# splitting up strings
mystr ='aaa,bbb,ccc'
mystr.split(',')

mystr ='a b\nc\nd'
print(mystr.split()) # default delimiter: whitespace

# join substring list
delim = 'NI'
delim.join(['aaa','bbb','ccc'])
' '.join(['A','dead','parrot'])

# convert to charchar list
chars = list('Lorreta')
print(chars)
chars.append('!')
''.join(chars)
print(''.join(chars))

# string replace hard way
mystr = 'xxaaxxaa'
'SPAM'.join(mystr.split('aa'))






