# use add modules
# use div_module
# use mul_module
# sub_module
# pow_module
'''
modules.py
add_module.py
dm
├── div_module.py
├── extra
│   ├── pow_module.py
│   └── sub_module.py
└── mul_module.py
'''
import sys
sys.path.append('/Users/deep.cloud2208/HDD/Training/temp/')

import add_module
from dm.div_module import div
from dm.extra import sub_module as sm
import dm.extra.sub_module
x = add_module.add(10,100)
y = div(31,7)
z = sm.sub(100,10)

# print(sys.path)
# print("            ")
# print("x ---> ",x)

import pymongo

# print(dir(pymongo))
# print(globals())
# print(id(x))
# print(hash(x))
# print(max([10,100,1000,2000,400]))
# print(min([10,100,1000,2000,400]))
# print(pow(2,4))
# for i in range(1,10):
#     print(i)
#
# import math
# print(math.random(1,100))

var_string = "THis is Python Class"
print(var_string.swapcase())

var_num = 123
var_num


