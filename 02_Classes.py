'''Classes example'''

#an instance of a class knows what class it's format
#var defined in the class are available to the instance

# class : a blueprint for an isinstance
# instance : a constructed object of the class
# type : indicates the class the instance belongs to
# attribute : any object value: object.Attribute
# method : a 'callable attribute ' defined in the class

class MyClass(object):
    '''My Class'''
    var = 10

THISOBJ = MyClass()
THATOBJ = MyClass()

print THISOBJ
print THATOBJ

print THISOBJ.var
print THATOBJ.var

