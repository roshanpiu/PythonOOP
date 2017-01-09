'''With context'''

#with is a context manager
#with provides a block that cleans up after exit

with open('test.txt') as fh:
    for line in fh:
        line = line.strip()
        print(line)

#filehandle will be close after we leave the with block
print 'done'
 
fh = open('test.txt')
for line in fh:
    print(line)
fh.close()

class MyClass(object):
    def __enter__(self):
        print 'we have entered "with"'
        return self

    def __exit__(self, type, value, traceback):
        print 'error type: {0}.'.format(type) 
        print 'error value: {0}'.format(value)
        print 'error traceback: {0}'.format(traceback)
        print 'we are leaving "with"'

    def sayhi(self):
        print 'hi, instance {0}'.format(id(self))

#if somewhere in with block an exception occurs you can use the __exit__ to capture the error
with MyClass() as cc:
    cc.sayhi()

print('after  the "With" block')