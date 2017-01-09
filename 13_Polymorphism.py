'''Polymorphism (Many shapes)'''

#two class which has same name

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

    def show_affection(self):
        '''show_affection method'''
        print '{0} wags tail'.format(self.name)

class Cat(Animal):
    '''Cat class'''

    def swatstring(self):
        '''swatstring method'''
        print '%s shreds the string.' % (self.name)

    def show_affection(self):
        '''show_affection method'''
        print '{0} purrs'.format(self.name)

for pet in (Dog('Rover'), Cat('Fluffy'), Dog('Shaggy')):
    pet.show_affection()
    