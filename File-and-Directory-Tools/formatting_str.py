"""
Formating string
%d	integers
%f  float
%s	string

"""
print('Hi %s, you have balance $%d.' % ('Mike', 1000))

# determine the digits and fill in when not enough input digits
print('%2d - %02d' % (3, 1))

# determine the digits for float
print('%.2f' % 3.1415926)

"""
REMARK:
    Always use %s if not sure the type of input
    if percentage is required, use %% to present percent %
"""

