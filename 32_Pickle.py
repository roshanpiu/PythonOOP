'''Pickle'''
import pickle

mylist = ['a', 'b', 'c', 'd']

with open('datafile.txt', 'w') as fh:
    pickle.dump(mylist, fh)

with open('datafile.txt') as fh:
    unpickledlist = pickle.load(fh)

print unpickledlist

this_int = 555
this_string = 'oh my goodness'
mydict_of_lists = {
    'a': [1, 2, 3],
    'b': [4, 5, 6]
}

query_results = [('joe', 22, 'clerk'), ('pete', 34, 'salesman')]

with open('datafile.txt', 'w') as fh:
    pickle.dump((this_int, this_string, mydict_of_lists, query_results), fh)

with open('datafile.txt') as fh:
    tup = pickle.load(fh)
    print tup


#when pickling object the file doesn't store the class it stors the reference 
#when unpickling them the class definition must be available
class MyNum(object):
    '''My Num'''
    def __init__(self, val):
        try:
            val = int(val)
        except ValueError:
            val = 0
        self.val = val

    def increment(self):
        '''Increments the value'''
        self.val = self.val + 1

MYNUM1 = MyNum(10)
MYNUM1.increment()
MYNUM1.increment()

with open('datafile.txt', 'w') as fh:
    pickle.dump(MYNUM1, fh)

with open('datafile.txt') as fh:
    result = pickle.load(fh)

print result

