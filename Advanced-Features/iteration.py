# Iteration for dictionary #

# keys
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

# values
for value in d.values():
    print(value)

# keys and values
for k, v in d.items():
    print(k)
    print(v)

# Check if iterable
from collections import Iterable
isinstance('abc', Iterable)

#enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# for two variables
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


