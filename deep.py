# def add(x,y):
#     return x + y
#
# x = 10
# y = 200
# z=add(x,y)
# print(z)
#
# var_lambda = lambda x,y: x+y
# z=var_lambda(x,y)
# print(z)

def get_words(line):
    a = line.split(",")[0]
    b = line.split(",")[2]
    return a,b
    # return line.split(",")[0], line.split(",")[2]

line = "AWS, GCP, Python, Spark, Hadoop"
# x = get_words(line)
# print(x)

# var_lambda = lambda line: (line.split(",")[0],line.split(",")[2] )
var_lambda = lambda line: get_words(line)
x = var_lambda(line)
print(x)

import deep