"""
We don't have to re-import Person class to fetch its instance
When instances are shelved or pickled, the underlying pickling system records to locate their class automatically
"""

import shelve

db = shelve.open('class-shelve')
for key in db:
    print(key, '=>\n', db[key].name, db[key].pay)


bob = db['bob']
print(bob.lastName())
print(db['tom'].lastName())