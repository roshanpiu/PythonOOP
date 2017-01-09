#An abstract class is a kind of 'modal' for other classes to be defined
#it is not designed to construct instances but can be subclassed by regular classes
#Abstract class can define an interface or methods tha must be implemented by it's subclasses
#abc module enables creation of abstract classes
#subclasses inherited from abstract class must implement all abstract methods

import abc

class GetterSetter(object):
    '''GetterSetter class'''
    __metaclass__ = abc.ABCMeta #tells that this should be defined as abstract base class

    @abc.abstractmethod
    def set_val(self, input):
        '''set a value in the instance'''
        return

    @abc.abstractmethod
    def get_val(self):
        '''returns a value in the instance'''
        return


class MyClass(GetterSetter):
    '''implements GetterSetter'''
    def __init__(self):
        self.val = 0

    def set_val(self, input):
        self.val = input

    def get_val(self):
        return self.val

X = MyClass()
print X
