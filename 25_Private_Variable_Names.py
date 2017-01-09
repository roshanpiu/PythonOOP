'''Private Variable Names'''

#PEP - 8 the Style guide for python code

#Module name : all_lower_case
#Class and exception names: CamelCase
#Global and locals: all_lower_case
#function and methods : all_lower_case
#constants : ALL_CAPS

#public attributes: regular_lower_case (intended to be used by the importer)
#private attributes: _single_leading_underscore (internal use)
#private attributes that shouldn't be subclassed: __double_leading_underscore
#magic attributes : __double_underscores__ (use them don't create them) 

class GetSet(object):

    instance_count = 0

    __mangled_name = 'no privacy'
    
    def __init__(self, value):
        self._attrval = value

    @property
    def var(self):
        print 'getting the "var" attribute'
        return self._attrval

    @var.setter
    def var(self, value):
        print 'setting the "var" attribute'
        self._attrval = value

    @var.deleter
    def var(self):
        print 'deleting the "var" attribute'
        self._attrval = None

ME = GetSet(5)

ME.var = 100
print ME.var
del ME.var
print ME.var
