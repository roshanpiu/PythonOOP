'''Assesment 5'''

import os
import pickle

class ConfigKeyError(Exception):
    def __init__(self, this, key):
        self.key = key
        self.keys = this.keys()

    def __str__(self):
        return 'key "{0} not found. Available keys: ({1})"'.format(self.key, ', '.join(self.keys))

class ConfigPickleDict(dict):

    config_dir = './config'

    def __init__(self, picklename):
        self._filename = os.path.join(ConfigDict.config_dir, picklename + '.pickle')
        if not os.path.isfile(self._filename):
            with open(self._filename, 'w') as fh:
                pickle.dump({}, fh)
        with open(self._filename) as fh:
            pkl = pickle.load(fh)
            self.update(pkl)

    def __getitem__(self, key):
        if not key in self:
            raise ConfigKeyError(self, key)
        return dict.__getitem__(self, key)
 
    def __setitem__(self, key, val):
        dict.__setitem__(self, key, val)
        with open(self._filename, 'w') as fh:
            pickle.dump(self, fh)


CD = ConfigPickleDict('config_pickle')

if len(sys.argv) == 3:
    key = sys.argv[1]
    value = sys.argv[2]
    print 'writing data: {0}, {1}'.format(key, value)
    CD[key] = value

else:
    print('reading data')
    for key in CD.keys():
        print '{0}  =  {1}'.format(key, CD[key])