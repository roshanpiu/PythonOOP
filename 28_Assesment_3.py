'''Assesment 3'''
import sys
import os

class ConfigDict(dict):

    def __init__(self, filename):
        self._filename = filename
        if os.path.isfile(self._filename):
            with open(self._filename) as fh:
                for line in fh:
                    line = line.rstrip()
                    key, value = line.split('=', 1)
                    dict.__setitem__(self, key, value)

    def __setitem__(self, key, val):
        dict.__setitem__(self, key, val)
        with open(self._filename, 'w') as fh:
                for key, val in self.items():
                    fh.write('{0}={1}\n'.format(key, val))


CD = ConfigDict('config_file.txt')

if len(sys.argv) == 3:
    key = sys.argv[1]
    value = sys.argv[2]
    print 'writing data: {0}, {1}'.format(key, value)
    CD[key] = value

else:
    print('reading data')
    for key in CD.keys():
        print '{0}  =  {1}'.format(key, CD[key])
