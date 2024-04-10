from ctypes import *

so_file = "./my_functions.so"

my_functions = CDLL(so_file)


print(type(my_functions))
print((my_functions.square(10)))
print(type(my_functions.square(1000)))


my_int = 5 
print(type(my_int))