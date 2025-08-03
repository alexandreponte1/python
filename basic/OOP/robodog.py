class Robot_dog:
   def __init__(self, name, breed):
      self.name = name
      self.breed = breed
   def bark(self):
      print('woof woof!')

# main program
my_dog = Robot_dog('Spot','viraLata')
print(my_dog.name + ' is a ' + my_dog.breed)
my_dog.bark()
