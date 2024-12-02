# SINGLE LEVEL INHERITANCE


class Sample1:
     def display1(self):
          print("I am in parent class")

class Sample2(Sample1):   # (Sample1) - this builds relationships 
     def display2(self):
          print("I am in child class")

s2 = Sample2()
s2.display2()

s2.display1() 
# - This will give an error if Sample2(Sample1) 





# MULTI-LEVEL INHERITANCE


class Sample1:
     def display1(self):
          print("im in parent class")

class Sample2(Sample1):
     def display2(self):
          print("im in child class 1")

class Sample3(Sample2):
     def display3(self):
          print("im in child class 2")

s2 = Sample3()
s2.display2()
s2.display1()
s2.display3()



# HIERARCHIAL INHERITANCE


class Sample1:
     def display1(self):
          print("im in parent class")

class Sample2(Sample1):
     def display2(self):
          print("im in child class 1")

class Sample3(Sample1):
     def display3(self):
          print("im in child class 2")

s2 = Sample3()
s2.display1()
s2.display3()

s=Sample2()
s.display1()
s.display2()



# MULTIPLE INHERITANCE


class Sample1:
     def display1(self):
          print("im in parent class")

class Sample2:
     def display2(self):
          print("im in child class 1")

class Sample3(Sample1, Sample2):
     def display3(self):
          print("im in child class 2")

s2 = Sample3()
s2.display1()
s2.display3()