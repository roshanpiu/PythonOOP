'''class attributes'''

#attributes in a class is holds the state of the instance
#when an attribute is requested in an instance it will look
#first in instance attributes then in class attributes

class MyClass(object):
    '''My Class'''
    classy = 'class value'

INST = MyClass()
print INST.classy

INST.classy = 'inst value'
print INST.classy

del INST.classy
print INST.classy

