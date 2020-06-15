# A class to order custom made jeans
# Programming with objects enables attributes and methods to be implemented
# automatically. The user only needs to know that methods exist to use them
# User can focus on completing tasks rather than operation details
# Difference between functions and objects: Objects contain state and behaviour
# while a function only defines a behaviour

class jeans:
    # the _init_ method is a python constructor method for creating new objects.
    # it defines unique parameters for a new object.
     def __init__(self, waist, length, color):
        self.waist = waist
        self.length = length
        self.color = color
        self.wearing = False
    
     def put_on(self):
        print('Putting on {}x{} {} jeans'.format(self.waist, self.length, self.color))
        self.wearing = True


     def take_off(self):
        print('Taking off {}x{} {} jeans'.format(self.waist, self.length, self.color))
        self.wearing = False
        
# create and examine a pair of jeans
my_jeans = jeans(31, 32, 'blue') # creating a jeans object
print(type(my_jeans))
print(dir(my_jeans))

# put on the jeans
my_jeans.put_on()
print(my_jeans.wearing)

my_jeans.take_off()
print(my_jeans.wearing)


## Properties of objects ################################################

class shirt:

    def __init__(self):
        self.clean = True

    def make_dirty(self):
        self.clean = False

    def make_clean(self):
        self.clean = True

# create one shirt with two names
red = shirt()
crimson = red

# examine the red/crimson shirt
print(id(red))
print(id(crimson))
print(red.clean)
print(crimson.clean)

# spill juice on the red/crimson shirt
red.make_dirty()
print(red.clean)
print(crimson.clean)

# check that red and crimson are the same shirt
print(red is crimson)

# create a second shirt to be named crimson
crimson = shirt()

# examine both shirts
print(id(red))
print(id(crimson))
print(crimson.clean)
print(red.clean)

# clean the red shirt
red.make_clean()
print(red.clean)
print(crimson.clean)

# check that red and crimson are different shirts
print(red is crimson)

## Mutable vs. immutable ################################################

# A mutable object can be modified after creation
# Immutable objects can not be modified.

closet = ['shirt', 'hat', 'pants', 'jacket', 'socks'] # Mutable variable (list)
print(closet)
print(id(closet))
closet.remove('hat')
print(closet)
print(id(closet))

words = "You're wearing that " # Immutable variable (string)
print(id(words))

# We can only modify it if we assign a new value to the variable
words = words + 'beutiful dress'  
print(words)
print(id(words)) # it is now a different id
