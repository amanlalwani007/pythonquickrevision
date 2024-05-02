from  functools import  reduce

reduce(lambda x,y:x*y,[1,2,3,4])
# returns 24 

# is used  to apply function  over  and over on an iterable 
# to  reduce it to one  single value


def my_add(a,b):
    return  a+b 

numbers = [0,1,2,3,4]
reduce(my_add , numbers  , 100)
# output  110

