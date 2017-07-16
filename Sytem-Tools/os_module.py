import os
## Admininstrative Tools

# calling process's process ID
os.getpid()

# current working directory
os.getcwd()

# change to new directory
os.chdir()

# if filename is a directory or a simple file, return True or False
os.path.isdir()
os.path.isfile()

# split and join directory path string
os.path.split()  # return directory path and filename
os.path.join()  # put file in a directory

# portably returns the full directory pathname of a file;
# it accounts for adding the current directory as a path prefix, .. parent syntax, and more
os.path.abspath('temp') # expand to full pathname in cwd
os.path.abspath('.') # relative path syntax expanded
os.path.abspath('..')








