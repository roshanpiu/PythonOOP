var1 = 'hello'
var2 = ' world!'

print var1 + var2

#the above line gets converted to this
print var1.__add__(var2)

var3 = 10
var4 = 20

print var3 + var4
#the above line gets converted to this
print var3.__add__(var4)

class SumList(object):
    def __init__(self, this_list):
        self.mylist = this_list

    def  __add__(self, other):

        new_list = [ x + y for x, y in zip(self.mylist, other.mylist)]

        #following 4 lines same as line above
        #new_list = []
        #zipped_list = zip(self.mylist, other.mylist)
        #for tup in zipped_list:
        #new_list.append(tup[0] + tup[1])

        return SumList(new_list)

    #when certain operation like print is called __repr__ is called
    def __repr__(self):
        return str(self.mylist)

cc = SumList([1, 2, 3, 4, 5])
dd = SumList([100, 200, 300, 400, 500])

ee = cc + dd
print ee

var = 'abcd'

#same
'abc' in var 
var.__contains__('abc')

#same
var == 'abcd'
var.__eq__('abcd')

#same
var[1]
var.__getitem__(1)

#same
var[1:3]
var.__getslice__(1, 3)

#same
len(var)
var.__len__()

#same
print var
var.__repr__()