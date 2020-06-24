# def myfunc(add1, add2):
#     print("I am myfunc")
#     c = add1 + add2
#     return c
#
# c = myfunc(134,768)
# print(c)
import pprint

def list_func(dict_arg, p, q):
    # global x
    a_collection = dict_arg
    b = p
    c = q
    print("Inside the func: ",a_collection,b,c)

    b = 100
    a_collection["name"] = "Keerthi"
    a_collection["addr"]["zipcode"] = 560068
    # x = b
    print("Inside the func (after modification): ",a_collection,b,c)


var_set = {"aws", "gcp", "spark"}
x = 10
y = 20

var_dict = {
    "name" : "vasu",
    "exp" : "manager",
    "addr" :
        {
            "country" : "USA",
            "state" : "CA"
        },
    "technologies": ["mgr", "python", "spark"]
}

# print(var_dict["addr"]["country"], var_dict["name"])

pprint.pprint(var_dict)
list_func(var_dict,x,y)
pprint.pprint(var_dict)


