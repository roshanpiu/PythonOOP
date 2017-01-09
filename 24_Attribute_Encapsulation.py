'''Attribute Encapsulation'''

#@property should not encapsulate expensive operations
#@property controls attributes that are expected but can't control attributes that are unexpected

class GetSet(object):
    
    def __init__(self, value):
        self.attrval = value

    @property
    def var(self):
        print 'getting the "var" attribute'
        return self.attrval

    @var.setter
    def var(self, value):
        print 'setting the "var" attribute'
        self.attrval = value

    @var.deleter
    def var(self):
        print 'deleting the "var" attribute'
        self.attrval = None

ME = GetSet(5)

ME.var = 100
print ME.var
del ME.var
print ME.var