'''class and instance data'''

class InstanceCounter(object):
    '''InstanceCounter'''
    count = 0

    def __init__(self, value):
        self.val = value
        InstanceCounter.count += 1

    def set_val(self, newval):
        '''sets val'''
        self.val = newval

    def get_val(self):
        '''returns val'''
        return self.val

    def get_count(self):
        '''returns num of instances created'''
        return InstanceCounter.count


INS1 = InstanceCounter(5)
INS2 = InstanceCounter(10)
INS3 = InstanceCounter(15)

for obj in (INS1, INS2, INS3):
    print "val of obj: %s" % (obj.get_val())
    print "count: %s" % (obj.get_count())
