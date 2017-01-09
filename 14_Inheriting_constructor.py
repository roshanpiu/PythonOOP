
import random

class Animal(object):
    '''Animal class'''
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    '''Dog class'''
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.breed = random.choice(['Shih Tzu', 'Beagle', 'Mutt'])

    def fetch(self, thing):
        '''fetch method'''
        print '%s goes after the %s!' % (self.name, thing)

D = Dog('dogname')

print D.name
print D.breed
