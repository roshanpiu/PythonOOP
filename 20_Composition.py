'''Composition'''

#Decoupled code is classes, functions, etc that work independantly and don't depend on one another
#As long as the interface is maitained interactions betweem classes will work
#Not checking or requiring patticular types is ploymorphic and Pythonic
#Inheritance can be brittle a change may require changes elsewhere

import StringIO

class WriteMyStuff(object):
    '''WriteMyStuff Class'''
    def __init__(self, writer):
        self.writer = writer

    def write(self):
        '''write function'''
        write_text = 'this is a silly message'
        self.writer.write(write_text)

FH = open('test.txt', 'w')
W1 = WriteMyStuff(FH)

SIOH = StringIO.StringIO()
W2 = WriteMyStuff(SIOH)
W2.write()

print 'file object: ', open('test.txt', 'r').read()
print 'StringIO object: ', SIOH.getvalue()

