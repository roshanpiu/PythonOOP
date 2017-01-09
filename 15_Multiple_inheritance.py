#by default python will use depth first to resolve attribute lookups

class ClassA(object):
    '''A'''
    def dothis(self):
        '''Do this'''
        pass

class ClassB(ClassA):
    '''A'''
    pass

class ClassC(object):
    '''C'''
    def dothis(self):
        '''Do this'''
        pass

class ClassD(ClassB, ClassC):
    '''D'''
    pass

DINST = ClassD()
DINST.dothis()      #mro D-B-A-C #depth first

print ClassD.mro()  #prints the method resolution order
