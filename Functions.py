# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 10:39:57 2020

@author: Salim Elzwawi
"""

""" A Functional Breakfast """


# When to create a function?
# Functions should be created to do frequently used routines


############
# Example-1#
############

# Recipe generator for an omelette you eat each morning


# Funtion definition
def make_omelette():
    print('Mix the ingredients')
    print('Pour the mixture into a frying pan')
    print('Cook the first side')
    print('Flip it!')
    print('Cook the other side')
    print('Enjoy eating')
    omelette = 'a delicious omelette'     # just defining a string       
    return omelette                       # returning the string each time the function is called

# Function call
make_omelette()                           # executes the function (but it does not return the variable omelette)
print('\n')
cook_omelette = make_omelette()           # executes the function and assigns the results (omelette) to a variable
print('\n')
print(cook_omelette)                      # prints varaible containing the results of the function


############
# Example-2#
############

# Another useful purpose of functions is code reuse
# If we want to cook a pancake for breakfast we can reuse most of the code
# because the recipes are similar

# Defining the pancake function
def make_pancake():
    print('Mix the ingredients')
    print('Pour the mixture into a frying pan')
    print('Cook the first side')
    print('Flip it!')
    print('Cook the other side')
    print('Enjoy eating')
    pancake = 'a delicious pancake'      # we only changed this part       
    return pancake                       

# Function call

cook_pancake = make_pancake()            # executes the function and assigns the results (omelette) to a variable
print('\n')
print(cook_pancake)                      # prints varaible containing the results of the function


############
# Example-3#
############

# We note that there is a lot (mix and cook) common between the two recipes
# We can go a step further an write a new function that can be reused
# by both recipes 
# Another advantage is that if there is a mistake we need only to fix it at one place

# Define the common mix and cook function 
def mix_and_cook():
    print('Mix the ingredients')
    print('Grease the frying pan')                  # made it more detailed
    print('Pour the mixture into a frying pan')
    print('Cook the first side')
    print('Flip it!')
    print('Cook the other side')
    
# Notice that the function does not have a return commad. It does not have to
# It is important that this function is defined before the other functions
# that depend on it

# Now the definitions of the other two functions are much simpler
    
 # Funtion definition
def make_omelette2():
    mix_and_cook()                        # This will insert the above function here  
    omelette = 'a delicious omelette'     # just defining a string       
    return omelette   
    
def make_pancake2():
    mix_and_cook()
    pancake = 'a delicious pancake'      # we only changed this part       
    return pancake     

# Now we can have an omelette and a pancake
print(make_omelette2())
print('\n')
print(make_pancake2())                 


############
# Example-4#
############

# Another advantage is that mistakes need to be fixed at one place
# And upgrades need to to be added at one place
# Now we want to add input variables to customise the omelette
# We will reuse the same mix and cook function

# We add an ingredient option to the omelette
def make_omelette3(ingredient):                     # The ingredient is called a parameter
    mix_and_cook()
    omelette = 'a {} omelette'.format(ingredient)
    return omelette

# Now we can have the omelette with mushroom or onions by passing an argument to the function
my_omelette = make_omelette3('mushroom')            # The ingredient 'mushroom' here is called an argument
print(my_omelette)    
print('\n')
my_omelette = make_omelette3('onions')
print(my_omelette)   

############
# Example-5#
############

# What if we don't know the number of ingredients beforehand?
# We can specify a function with a variable number of paramers as input
# The asterix '*' preceeding the passed parameters tells Python that we are passing many arguments
# These parameters are stored in a data structure called tuple

def best_omelette(*ingredients):  
    mix_and_cook()
    omelette = 'the best omelette is with {} .'.format(len(ingredients))
    return omelette

best_omelette('mushroom', 'cheese', 'tomato', 'onions')



# Or naming the ingredients
def best_omelette2(*ingredients):  
    mix_and_cook()
    ing = str(ingredients)
    omelette = 'the best omelette is with ' + ing
    return omelette

best_omelette2('mushroom', 'cheese', 'tomato', 'onions')


############
# Example-6#
############

# Watch out for local variables global

cheese = 'cheddar'                  # This is a global variable that can be used anywhere inside the program

def make_omelette4():
    # global cheese                    # Tells Python that this variable can be used outside the function
    cheese = 'swiss'                 # local variable recognised only in the funtion
    mix_and_cook()
    omelette = 'a {} omelette'.format(cheese)
    return omelette

def make_pancake4():
    mix_and_cook()
    pancake = 'a {} pancake'.format(cheese)
    return pancake

# make some cheesy foods
print(cheese)           # allways prints the global variable
print('\n')
print(make_omelette4())
print('\n\n')
print(cheese)
print('\n')
print(make_pancake4())
 




