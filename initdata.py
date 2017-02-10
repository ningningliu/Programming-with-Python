# initialize data to be stored i files, pickles, shelves

# records
bob ={'name':'Bob Smith', 'age':42, 'pay':30000,'job':'dev'}
sue = {'name':'Sue Jones', 'age':45, 'pay':40000,'job':'hdw'}
tom ={'name':'Tom', 'age':50, 'pay':0,'job':None}

# database
db ={}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

if __name__ == ' __main__': # when run as a script
    # __name__ test is true only when this file is run, not when it is imported
    for key in db:
        print(key, '=> \n ', db[key])

