import sys
print(sys.platform)

# search path
print(sys.path)

# add path
# sys.append(path)

# Exception details
import traceback, sys
def grail(x):
    raise TypeError('already got one')

try:
    grail('arthur')
except:
    exc_info = sys.exc_info()
    print(exc_info[0])
    print(exc_info[1])
    traceback.print_tb(exc_info[2])
