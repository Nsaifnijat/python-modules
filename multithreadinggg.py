# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import threading
from threading import *

import time

start=time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')
    
#pass the function without parenthesis

p1=threading.Thread(target=do_something)
p2=threading.Thread(target=do_something)

#we have created multiprocessing in the above code, we have not started it, so we do the following

p1.start()
p2.start()

#the  following prints out the result in the order they are
p1.join()
p2.join()

finish=time.perf_counter()

print(f'Finished in {round(finish-start,2)} second(s)')



#using a loop to run as many threads as we neeed

start=time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done Sleeping...')
    
threads=[]
# - in the loop is used when we dont use the variable,
# the followin also shows how to pass the argument for your function,args is the argument of do_something
for _ in range(10):
    p=threading.Thread(target=do_something, args=[1.5])
    p.start()
    threads.append(p)
    
for thread in threads:
    thread.join()

finish=time.perf_counter()

print(f'Finished in {round(finish-start,2)} second(s)')


#using thread pool executer, it makes the thread, run on multiple threads

#doing the above work using threadpool

import concurrent.futures


start=time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return 'Done Sleeping...'

with concurrent.futures.ProcessPoolExecutor() as executer:
    #the submit method schedules a func to be executed, and return a future object to check if its done or running
    f1=executer.submit(do_something, 1)
    print(f1.result())


finish=time.perf_counter()

print(f'Finished in {round(finish-start,2)} second(s)')

print(current_thread().getName())


#to use it for a number of funcs do the following

start=time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return 'Done Sleeping...'

with concurrent.futures.ProcessPoolExecutor() as executer:
    results=[executer.submit(do_something, 1) for _ in range(10)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())
    
    #to pass different secs to our do_someting func
    '''
    secs=[5,4,3,2,1]
    results=[executer.submit(do_something, sec) for sec in secs]
    for f in concurrent.futures.as_completed(results):
        print(f.result())
    '''
    #the above submitted func returns the future object as they complete
    
# map returns results instead of future objects and returns results in the order that they started
'''
with concurrent.futures.ProcessPoolExecutor() as executer:
    secs=[5,4,3,2,1]
    results=executer.map(do_something, secs)
    for result in results:
        print(result)
#to switch from process to thread using concurrentfutures its just ThreadPoolExecutor()

with concurrent.futures.ThreadPoolExecutor() as executer:
    secs=[5,4,3,2,1]
    results=executer.map(do_something, secs)
    for result in results:
        print(result)
  '''      
        
finish=time.perf_counter()

print(f'Finished in {round(finish-start,2)} second(s)')




























