'''Python Types'''

#Everything in python is an object
#Everythig in python has a type

MYLIST = ['a', 'b', 'c']
MYBOOL = True
MYNONE = None

def myfunc():
    '''prints hello'''
    print 'hello'

print type(MYLIST)
print type(MYBOOL)
print type(MYNONE)
print type(myfunc)

THISTYPE = type(MYLIST)
print type(THISTYPE)

VAR = 5

print dir(VAR) #prints the attributes of type int
