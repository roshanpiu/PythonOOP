'''Inheritance'''

#when we call a method ,property on an instance python will follow the lookup order
#Object.attribute lookup hierachy
#1 The instance
#2 The class
#3 The class from which this class inherits

class Date(object):             #the paren/super/base class
    '''Date class'''
    def get_date(self):
        '''get date'''
        return '2014-10-13'

class Time(Date):               #inherits from Date class /  child/derived/sub class
    '''Time class'''
    def get_time(self):
        '''get time'''
        return '08:13:07'

DT = Date()
print DT.get_date()

TM = Time()
print TM.get_time()
print TM.get_date()

