# -*- coding: utf-8 -*-


#functools are higher order functions which take function as an argument, manipulate and may return a functions

#reduce was built in python but later it was added to functools
from functools import reduce

#suppose we have the following 
1 2 3 4 5  #we add first two elements and put the rest as they are until we get the final result, 1+2
3 3 4 5     #3+3
6 4 5 
10 5
15

#or we can write the above like this
1+2+3+4+5 = 15
#for mulitplication we write this
1*2*3*4*5 =120
#so the final result is 15 which we can do using the reduce in the following way

reduce(lambda x,y: x+y, [1,2,3,4,5])
#you find multiplications and max
reduce(lambda x,y: x*y, [1,2,3,4,5])
reduce(lambda x,y: max(x,y), [1,2,3,4,5])

#we can also give a initial to start from
reduce(lambda x,y: x+y, [1,2,3,4,5],10)
#the above is like this
10+1+2+3+4+5 = 25



#magic functions for comparison

__eq__ (==)
__lt__ (<)
__le__ (<=)
__gt__ (>)
__ge__ (>=)

class car:
    
    def __init__(self, model, mileage):
        
        self.model = model
        self.mileage = mileage
        
    def __eq__(self, other):
        return self.mileage == other.mileage
    def __lt__(self, other):
        return self.mileage < other.mileage


c1 = car('Aud', 700)
c2 = car('Benz',800)

c1 == c2
c2 < c1

#now if we use other comparisons that we have not defined in the class we get error but we can solve it functools
c2 >= c1



#we can solve the above error with total ordering, for total ordering to work, we have to have at least 
#two magic funcs already define in our class, any of them with __eq__ func can work, one of them must be __eq__

from functools import total_ordering

@total_ordering
class car:
    
    def __init__(self, model, mileage):
        
        self.model = model
        self.mileage = mileage
        
    def __eq__(self, other):
        return self.mileage == other.mileage
    def __lt__(self, other):
        return self.mileage < other.mileage


c1 = car('Aud', 700)
c2 = car('Benz',800)

c2 >= c1

c2 <= c1

#using caching for functions, once a functions is run after that it gets cached, and when we call it again it returns its value from the cache memory
from functools import cached_property


class Marksheet:
    
    def __init__(self, *grades):
        
        self.grades = grades
    @cached_property
    def total(self):
       print('calculating total')
       return sum(self.grades)
   
    @cached_property
    def average(self):
       print('calculating average')
       return self.total/len(self.grades)
        

m = Marksheet(100,90, 95)

m.average
m.total


#now we have the following func on which we use lru_cache to see the difference

def fib(n):
    if n < 2:
        return n
    print(f'calculating fib {n}')
    return fib(n-1)+fib(n-2)

[fib(x) for x in range(10)]


#we can use lru_cache to avoid repeating the repetitive values as follow
from functools import lru_cache

 #128 is default which means it can remember upto 128 call results, if you put maxsize=None,it will make it unlimited
#you can also give type=True param which means it will treat 3 and 3.0 differently,
#you can also remove the parameters and just put ( lru_cache) , it will run with defaults
@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    print(f'calculating fib {n}')
    return fib(n-1)+fib(n-2)

[fib(x) for x in range(10)]


#the following gives us info,hits means maches, misses means different, maxsize is the size, currsize  is our current size 
fib.cache_info()



#lets suppose we have the following

def add(a,b):
    return a+b

def add_one(a):
    return add(a,1)

add_one(4)

#we can do the above in a single line using partial

from functools import partial

add_one = partial(add, 1) 
#1 is the b argument, you can also assign a=1 like, partial(add, a=1)
#if assigned like above then do, add_one(b=4)
add_one(4) #now a is 4




#if you remove that wraps decorator before the wrapper func you get wrapper return by my_timer, 
#but if you put it this way you get display info as return func
from functools import wraps

def my_timer(orig_func):
    import time  
    
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
       
        print('running {}'.format(orig_func.__name__))
        return orig_func(*args, **kwargs)
    return wrapper

@my_timer
def add(a,b):
    """add a and b """
    return a+b
print(add.__name__)
add(3,4)













