import json, sys

# File handling
'''
File open modes:
- Read (r)
- Read Binary (rb)
- Write (w)
- Write Binary (wb)
format > open(filename, mode)
'''
ifile = open('car_sales_data.csv','r')

# line1 = ifile.readline()
# line2 = ifile.readline()
# print(line1)
# print(line2)

# all_lines = ifile.readlines()
# print(all_lines)
#
# for i in all_lines:
#     print(i)

# ifile.close()
#
# ifile2 = open('car_sales_data.csv','r')
# var1 = ifile2.readline()
# print(var1)

# with open('inputfile.json','r') as input:
#     for i in input:
#         print(i)
#         var_list = json.loads(i)
#         print(var_list['product_make'], var_list['quantity_sold'])

# Serialization and Deserialization (SerDe)
'''
pickle module is used in SerDe 
- pickle.dump for serialization
- pickle.load for deserialization

while reading multiple lines of data using "pickle.load" a generator has to be used along with file handler.
'''
var_dict = dict()
var_list = list()
var_tuple = ('check','pickle','working')

var_dict['name'] = "Deep"
var_dict['address'] = {
    "addr1" : "India",
    "addr2" : "Bangalore",
    "addr3" : "Karnataka"
}

var_list.append("aws")
var_list.append("gcp")
var_list.append("spark")
var_list.append("python")
var_list.append("scala")
var_list.append("mongodb")

#-------------------------------------------------------------
# using Pickle >> pickle.dump and pickle.load
#-------------------------------------------------------------
import pickle
ofile = open('pickle1.obj','wb')

pickle.dump(var_dict, ofile)
pickle.dump(var_tuple, ofile)
pickle.dump(var_list, ofile)

ofile.close()
print('                   ')

# infile = open('pickle1.obj','rb')
# var1 = pickle.load(infile)
# var2 = pickle.load(infile)
# var3 = pickle.load(infile)

# print(var2)

def unpickle_file(infile):
    try:
        while True:
            yield pickle.load(infile)
    except EOFError:
        pass

with open('pickle1.obj','rb') as infile:
    for i in unpickle_file(infile):
        print(i)









