""" Demonstrating inheritence """

class Vehicle:  # Parent Vehicle class
    def __init__(self, color, manuf):
        self.color = color
        self.manuf = manuf
        self.gas = 4  # full tank
        
    def drive(self):  # drive method
        if self.gas > 0:
            self.gas -= 1
            print("The {} {} goes BROOM".format(self.color, self.manuf))
        else:
            print("The {} {} is out of gas.".format(self.color, self.manuf))

class car(Vehicle):  # sub-calss of vehicles

    # radio method
    def radio(self):
        print("Great music")
        
    # window method
    def window(self):
        print("I like the breeze")
        
class motorcycle(Vehicle):
    # safety comes first
    def helmet(self):
        print('Safety comes first')    
        
class ecar(car):        # Inherits from Car class
    def drive(self):    # overrides the parent's drive method
        print("The {} {} goes hhmmmmmmm.".format(self.color, self.manuf))

# # create car & motorcycle objects        
# my_car = Car('red', 'BMW')
# my_mc = Motorcycle('blue', 'Honda')

# # take them out for a test drive
# my_car.drive()
# my_mc.drive()
# my_mc.drive()
# my_mc.drive()
# my_mc.drive()
# my_mc.drive() # out of gas
# my_car.drive()

# # play around with accessories
# my_car.radio()
# my_car.window()
# my_mc.helmet()
# # my_mc.window() # windows do not exist on motorcycles

# create and use an electric car
# my_ecar = ecar('white','Leaf')
# my_ecar.window()
# my_ecar.radio()
# my_ecar.drive()

# access the lingering gas tank
# print(my_ecar.gas)