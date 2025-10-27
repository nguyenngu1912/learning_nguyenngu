# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
    
#     def printname(self):
#         print(self.fname,self.lname)

# class Student(Person):
#     def __init__(self, fname, lname, graduationyear):
#         super().__init__(fname,lname)
#         self.graduationyear = graduationyear
#     def helle(self):
#         print("Congrats",self.fname,self.lname,self.graduationyear)    

# x1 = Student("Adam","Smith",2016)
# # x1.printname()
# x1.helle()

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()