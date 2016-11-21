#encoding=utf-8
"""
>>> import module1
>>> import module1  # the first time import is different

>>> dir(module1)
>>> module1.name
>>> module1.sys
>>> module1.get_name
>>> module1.someClass

"""


print 'starting to load the module ...'
import sys

name = 'John'

age = 18

def get_name():
    pass

class someClass:
    pass

print sys.path
print 'finish to load the module ...'
