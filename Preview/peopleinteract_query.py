"""
interactive queries
"""

import shelve
fieldnames = ('name', 'age', 'job', 'pay')
maxfield = max(len(f) for f in fieldnames) # max() list comprehension, recall list comprehension at chapter 1 / step 1
# print(maxfield)
db = shelve.open('class-shelve')

while True:
    key = input('\nkey ? =>')
    if not key: break
    try:
        record = db[key]
    except:
        print('No such key "%s" !' %key)
    else:
        for field in fieldnames:
            # getattr : fetch an object's attribute when given its name string
            # ljust : left-justify method of strings to align outputs
            print(field.ljust(maxfield) , '=>', getattr(record, field))