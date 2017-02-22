import pickle
import pprint
dbfile = open('people-pickle','rb') # read binary mode
db= pickle.load(dbfile)

# for key in db:
#     print(key, "=====", db[key])

print(pprint.pprint(db))