
var_string = "Hi, my name is Deep"
var_int = 12345
var_bool = True


class Vehicle:
    wheels = 5
    windows = 6
    indicator = 4
    type = "Personal Ride"

    def __init__(self, engine, cc, speed, height, length):
        self.engine = engine
        self.cc = cc
        self.speed = speed
        self.height = height
        self.length = length

    def changeSpeed(self,speed):
        self.speed = speed

    def __add__(self, other):
        self.length = self.length/1000
        other.length = other.length/100
        return (self.length + other.length)

    @staticmethod
    def func():
        pass

'''
Abstract Class
'''
from abc import ABCMeta, abstractmethod

class Transportation():

    __metaclass__ = ABCMeta

    @abstractmethod
    def mode(self):
        pass

    @abstractmethod
    def wheels(self):
        pass


# class Truck(Vehicle, Transportation):
#     def __init__(self,engine, cc, speed, height, length, design):
#         super.__init__(engine, cc, speed, height, length)
#         self.design = design
#
#     def mode(self,mode):
#         self.mode = mode


# tesla_cyber_truck = Truck("Electric", "NA", "300km/h", 100,200,"rigid")

bmw = Vehicle("V10",4000, "400Km/h",2000,80000)
city = Vehicle("kjsdhs",4000, "400Km/h",200,8000)

var = bmw.__add__(city.length)

print(var)

