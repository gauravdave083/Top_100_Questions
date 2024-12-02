class Student:
     collegeName = "qwerty"                 # --------------- Static Variable 

     def __init__(self, rno, name, age):
          self.rno = rno
          self.name = name
          self.age = age
     
     def assign(self, marks):
          self.marks = marks
     
     def display(self):                      # -------------- Instance Method
          print("rno=", self.rno)
          print("name=", self.name)
          print("age=", self.age)
          print("marks=", self.marks)

s1 = Student(1, "abc", 20)    
s2 = Student(2, "xyz", 30)  

s1.assign(70)
s2.assign(90) 

s1.display() 
s2.display()

print(id(s1))  # Shows Memory Assigned 
print(id(s2))  # Shows Memory Assigned 


