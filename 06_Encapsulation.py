'''Encapsulation'''

# by using Encapsulation through setval and getval we can ensure the integrity of the data

class MyClass(object):
    '''My Class'''
    def __init__(self):
        self.val = 0

    def set_val(self, val):
        '''set the val'''
        if val > 0:
            self.val = 0
        else:
            return

    def get_val(self):
        '''returns the val'''
        return self.val

MYINST1 = MyClass()
MYINST2 = MyClass()

MYINST1.set_val(10)
MYINST2.set_val(100)

print MYINST1.get_val()
print MYINST2.get_val()


