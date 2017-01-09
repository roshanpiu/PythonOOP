'''class and static methods'''

#class and static methods are not bound to the instance
#class method works with the class
#static methods works independantly with either the class or instance
#@classmethod when applied to a function it modifies the function and passes the class as 1st arg

#class methods takes the class as the first argument and works with the class
#static methods doesn't require any arguments and does not work with class or instance
#@classmethod and @instancemethod modifies the default binding the that instance method provide

class InstanceCounter(object):
    '''InstanceCounter'''
    count = 0

    def __init__(self, value):
        self.val = self.filterint(value)
        InstanceCounter.count += 1

    def set_val(self, newval):
        '''sets val'''
        self.val = newval

    def get_val(self):
        '''returns val'''
        return self.val

    @classmethod
    def get_count(cls):
        '''get_count receives the class as first argument.'''
        return cls.count

    @staticmethod
    def filterint(value):
        '''filters the value to verify it's an int'''
        if not isinstance(value, int):
            return 0
        else:
            return value


INS1 = InstanceCounter(5)
INS2 = InstanceCounter(10)
INS3 = InstanceCounter('hello') #gets filtered to 0

for obj in (INS1, INS2, INS3):
    print "val of obj: %s" % (obj.get_val())

print 'instance count : {0}'.format(InstanceCounter.get_count())

print 'filtered result of "hello" to int is {0}'.format(InstanceCounter.filterint('hello'))

