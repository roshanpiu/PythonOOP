'''Exceptions'''

MYDICT = {'a': 1, 'b': 2, 'c': 3}

key = raw_input('please input a key: ')

try:
    print 'testing for error'
    print 'the value for {0} is {1}'.format(key, MYDICT[key])
except KeyError:
    print 'trap error'
    print 'the key {0} does not exist'.format(key)

print 'program continues'


#custom Exceptions

def make_delim_line(list_to_join, delim):

    try:
        formatted_line = delim.join(list_to_join)
    except TypeError:
        raise TypeError('make_delim_line(): arg 1 must be a tuple for a list')
    return formatted_line

fline make_delim_line(100, ',')

mydict = {'a': 1, 'b': 2}

try:
    print 5/0
except ZeroDivisionError, e:
    print e.message
    print e.args