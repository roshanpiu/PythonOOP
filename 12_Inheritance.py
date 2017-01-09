'''Inheritance example'''

class Animal(object):
    '''Animal class'''
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        '''eat method'''
        print '%s is eating %s.' % (self.name, food)

class Dog(Animal):
    '''Dog class'''

    def fetch(self, thing):
        '''eat method'''
        print '%s goes after %s.' % (self.name, thing)

class Cat(Animal):
    '''Cat class'''

    def swatstring(self):
        '''swatstring method'''
        print '%s shreds the string.' % (self.name)

CT = Cat('Fluffy')
DG = Dog('Rover')

DG.fetch('paper')
CT.swatstring()
DG.eat('Dog food')
CT.eat('Cat food')
CT.swatstring()
