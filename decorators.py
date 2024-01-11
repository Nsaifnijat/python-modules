# -*- coding: utf-8 -*-
#Assigning Functions to Variables

def plus_one(number):
    return number + 1

add_one = plus_one
add_one(5)


#Defining Functions Inside other Functions

def plus_one(number):
    def add_one(number):
        return number + 1


    result = add_one(number)
    return result
plus_one(4)

#Passing Functions as Arguments to other Functions
#Functions can also be passed as parameters to other functions. Let's illustrate that below.

def plus_one(number):
    return number + 1

def function_call(function):
    number_to_add = 5
    return function(number_to_add)

function_call(plus_one)