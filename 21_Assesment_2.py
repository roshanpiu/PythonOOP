'''Assesment 2'''

import abc
from datetime import datetime

class WriteFile(object):
    '''WriteFile'''
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def write(self):
        '''write'''
        return

    def __init__(self, filename):
        self.filename = filename

    def write_line(self, text):
        '''write_line'''
        file_handle = open(self.filename, 'a')
        file_handle.write(text + '\n')
        file_handle.close()

class DelimFile(WriteFile):
    '''DelimFile'''
    def __init__(self, filename, delim):
        super(DelimFile, self).__init__(filename)
        self.delim = delim

    def write(self, this_list):
        '''write'''
        line = self.delim.join(this_list)
        self.write_line(line)

class LogFile(WriteFile):
    '''LogFile'''
    def write(self, this_line):
        '''write'''
        date = datetime.now()
        date_str = date.strftime('%Y-%m-%d %H:%M')
        self.write_line('{0}   {1}'.format(date_str, this_line))
        