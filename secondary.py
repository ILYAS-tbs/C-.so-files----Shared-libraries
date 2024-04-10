from ctypes import *

so_file = "./my_functions_second.so"

my_functions = CDLL(so_file)


""" def heavy(n):
    j = 0 
    while(j<n): 
         j =j+1
	

    print(f"value :{j}")
    return 0

heavy(1000000000) """

my_functions.heavy(1000000000)