'''Method Overloading'''

#inherit : use parent class definition classmethod
#overide/overload: provide child's own version of a method
#extend: do work in addtion to that in parent's method
#provide: implement abstract method that parent requires

import abc

class GetSetParent(object):
    '''GetSetParent'''
    __metaclass__ = abc.ABCMeta
    def __init__(self, value):
        self.val = 0

    def set_val(self, value):
        '''set_val'''
        self.val = value

    def get_val(self):
        '''get_val'''
        return self.val

    @abc.abstractmethod
    def showdoc(self):
        '''showdoc'''
        return

class GetSetInt(GetSetParent):
    '''GetSetInt'''
    def set_val(self, value):
        if not isinstance(value, int):
            value = 0
        super(GetSetInt, self).set_val(value)

    def showdoc(self):
        print 'GetSetInt object ({0}), only accepts integer values'.format(id(self))

class GetSetList(GetSetParent):
    '''GetSetList'''
    def __init__(self, value = 0):
        self.vallist = [value]
    def get_val(self):
        return self.vallist[-1]

    def get_vals(self):
        '''get_vals'''
        return self.vallist

    def set_val(self, value):
        self.vallist.append(value)

    def showdoc(self):
        print 'GetSetList object, len {0}, store history of values set'.format(len(self.vallist))


X = GetSetInt(3)
X.set_val(5)
print X.get_val()
X.showdoc()


GSL = GetSetList(5)
GSL.set_val(10)
GSL.set_val(20)
print GSL.get_val()
print GSL.get_vals()
GSL.showdoc()
