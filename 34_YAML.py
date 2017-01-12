'''YAML'''

#just like json and pickle
#when dumping an object to yaml the file doesn't store the class it stors the reference 
#when deserializing them back from yaml the class definition must be available

import yaml
import json

mydict = {'a': 1, 'b': 2, 'c': 3}
mylist = [1, 2, 3, 4, 5, 6]
mytuple = ('x', 'y', 'z')

print yaml.dump(mydict, default_flow_style=False)
print yaml.dump(mylist, default_flow_style=False)
print yaml.dump(mytuple, default_flow_style=False)

with open('config_yaml.yaml') as fh:
    struct = yaml.load(fh)

print json.dumps(struct, indent=4, separators=(',', ': '))

