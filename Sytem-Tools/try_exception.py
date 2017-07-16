import traceback

try:
    fh = open('testfile','w')
    fh.write('this file is used to test error !')
except FileNotFoundError:
    print('>>> traceback <<<')
    traceback.print_exc()
    print('>>> traceback <<<')