'''Instance methods'''

#every method inside a class gets passed the instance it self as the first implicit parameter
#instance methods are called bound methods

class Joe(object):
    '''Joe class'''
    def callme(self):
        '''call me function'''
        print 'call me'
        print self #prints the instance

THISJOE = Joe()

THISJOE.callme()
print THISJOE #prints the instance
