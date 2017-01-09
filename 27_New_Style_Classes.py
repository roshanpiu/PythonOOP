'''New Style Classes'''

#in old style classes the concept of class and type are not related
#in new style classes the concept of class and type are directly related
#one of the motivation of the new style classes is to unify the idea of class with type


#new type classes can be constructed with default attributes from "metaclass" constructors
#new style classes allows subclassing of built-ins
#allows the use of "slots" to define instance attributes
#new style classes supports descriptors
#new style classes uses the M3 method resolution order

#additional readings - metaclasses and descriptors

#old style "Classic" class 
class OldClass():
    pass

#new style class

class NewClass(object):
    pass

OC = OldClass()
NC = NewClass()

print type(OC)
print type(NC)

print OC.__class__