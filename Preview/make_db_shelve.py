import  shelve
from initdata import bob, sue, tom
db= shelve.open('people-shelve')
db['bob']= bob
db['sue'] = sue
db['tom']= tom
suefile = db['sue']
suefile['pay'] *=1.5
db['sue']= suefile
for key in db:
    print(key, "====", db[key])
db.close()