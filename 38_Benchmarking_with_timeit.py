import timeit

#memory and time is not often a concern for python developers
#time tests should run multiple times
#the tests should consider the context in which they will run
#in the real env we might have 10000 values in the dict so we should simulate that to get good idea


print 'by index:    ', timeit.timeit(stmt="mydict['c']", setup="mydict = {'a': 5, 'b': 6, 'c': 6}", number=1000000) 
print 'by get:    ', timeit.timeit(stmt="mydict.get('c')", setup="mydict = {'a': 5, 'b': 6, 'c': 6}", number=1000000) 

def testtime(this_dict, key):
    return this_dict[key]

print 'testime time :    ', timeit.timeit(stmt="testtime(mydict, 'c')", setup="from __main__ import testtime; mydict = {'a': 5, 'b': 6, 'c': 6}", number=1000000) 
