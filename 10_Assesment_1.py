'''Assesment 1'''

class MaxSizeList(object):
    '''MaxSizeList'''
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = []

    def push(self, item):
        '''adds item to list'''
        if len(self.items) < self.max_size:
            self.items.append(item)
        else:
            self.items.pop(0)
            self.items.append(item)

    def get_list(self):
        '''returns the list'''
        return self.items

LIST1 = MaxSizeList(3)
LIST2 = MaxSizeList(1)

LIST1.push("hey")
LIST1.push("hi")
LIST1.push("let's")
LIST1.push("go")

LIST2.push("hey")
LIST2.push("hi")
LIST2.push("let's")
LIST2.push("go")

print LIST1.get_list()
print LIST2.get_list()


