# Variable Parameter#
# if number of parameters are not certain
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# input parameters as list or tuple
calc([1,2,3])
calc((1,2,3,4))

# change parameters as *parameters i.e. variable parameters
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# input any form
calc(1,2,3)

# if input is alreay a list
num = [1,2,3]
calc(*num) # change element in num as variable parameters


# Keyword  Parameter#
# **kw allows any input including none
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

# if input is already a dict
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra) # input keys of extra into person


# Key Parameter #
# paratmers after * are the key parameter
def person(name, age, *, city, job):
    print(name, age, city, job)

# person('Jack', 24, 'Beijing', 'Engineer') # wrong !
person('Jack', 24, city='Beijing', job='Engineer') # must indicate key parameter

# if key parameter city is pre-defined, no need to input city again
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

person('Jack', 24, job='Engineer')

# combination of all types of parameters
"""
REMARK:
    在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
    但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
"""
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)







