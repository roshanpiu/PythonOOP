#if the same class in a method resoluton order
#the earlier occurances of the class are removed
#normaly when the depth first is applied to ClassD mro - D-B-A-object-C-A-object
#after the rule applied mro - D-B-C-A-object

class ClassA(object):
    '''A'''
    def dothis(self):
        '''Do this'''
        print 'doing this in A'

class ClassB(ClassA):
    '''A'''
    pass

class ClassC(ClassA):
    '''C'''
    def dothis(self):
        '''Do this'''
        print 'doing this in C'

class ClassD(ClassB, ClassC):
    '''D'''
    pass

DINST = ClassD()
DINST.dothis()      #mro - D-B-C-A-object

print ClassD.mro()
