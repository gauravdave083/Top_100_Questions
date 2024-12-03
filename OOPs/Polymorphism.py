# POLYMORPHISM ALLOWS METHODS IN DIFFERENT CLASSES TO HAVE THE SAME NAME BUT BEHAVE DIFFERENLY BASED ON THE CLASS OBJECT


class Dog:
     def make_sound(self):
          return "Woof Woof!"

class Cat:
     def make_sound(self):
          return "Meow Meow!"

def animal_sound(animal):
     print(animal.make_sound())

# USAGE
dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat)