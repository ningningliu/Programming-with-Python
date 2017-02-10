## LIST##

bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones',45, 40000, 'hardware']
people = [bob, sue]

for person in people:
    print(person[0].split()[-1])
    person[2]*= 1.2

# Iteration tools: list comprehension, maps, generator expression
pays = [person[2] for person in people]
print(pays)

pays = map(lambda x: x[2], people)
print(list(pays))

sum(person[2] for person in people)

people.append(['Tom', 50, 0, None])
print(people[-1][0])

# Field Labels

NAME, AGE, PAY = range(3)
print(bob[NAME])
print((PAY, bob[PAY]))

# Fetcher function for positional indexing
bob= [['name','Bob Simith'],['age',42],['pay',10000]]
sue = [['name','Sue Jones'],['age',45],['pay',20000]]
people = [bob, sue]

def field (record, label):
    for (fname,fvalue) in record:
        if fname == label:
            return fvalue

print(field(bob,'age'))

## DICTIONARIES ##

bob ={'name':'Bob Smith', 'age':42, 'pay':30000,'job':'dev'}
sue = {'name':'Sue Jones', 'age':45, 'pay':40000,'job':'hdw'}

# Other ways to create dictionaries
bob = dict(name= 'Bob Smith', age =42, pay= 30000, job ='dev')

sue = {}
sue['name']= 'Sue Jones'
sue['age']= 45
sue['pay']= 40000
sue['job']= 'hdw'

# make dict from key values with optional starting value for all keys
fields = ('name','age','job','pay')
record = dict.fromkeys(fields, None)
print(record)

# Dict iteration tools
people =[ bob, sue] # create list consisting dict

names =[person['name'] for person in people] # collect the names
print(names)

names = list(map(lambda x: x['name'], people))
print(names)

print(sum( person['pay'] for person in people))

# using SQL queries
G= [rec['name'] for rec in people if rec['age'] >= 45]
print(G)
F = (rec['name'] for rec in people if rec['age'] >= 45)
print(next(F)) # run the iteration generator one by one

G =[ rec['age']**2 if rec['age'] >= 45 else rec['age'] for rec in people]
print(G)
F= ( (rec['age']**2 if rec['age'] >= 45 else rec['age']) for rec in people)
print(F.__next__())

# Nested structures
bob2 = {
    'name':{'first':'Bob','last':'Smith'},
    'age': 42,
    'job':['software','writing'],
    'pay': (40000, 50000)
}

print(bob2['name'])
print(bob2['name']['last'])

for job in bob2['job']: print(job)

bob2['job'].append('janitor') # bob get new job
print(bob2,"\n","\n")

# creating dict consisting dicts
db = {}
db['bob'] = bob
db['sue'] = sue
# print(db)

# import pprint
# pprint.pprint(db) # nice print of dict object

for key in db:
    print(db[key],db[key]['name'].split()[-1],"\n")

for record in db.values(): print(record['pay'],"\n")

x = [ db[key]['name'] for key in db]
print(x,'\n')
x= [ rec['name'] for rec in db.values()]
print(x,'\n')

# Add new record
db['Tom'] = dict(name ="Tom", age = 50, job = None,pay = 0)
print(list(db.keys()),'\n')
senior_name = [rec['name'] for rec in db.values() if rec['age'] >= 45]
print(senior_name,'\n')
