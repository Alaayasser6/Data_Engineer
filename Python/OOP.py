#---------------------------Module--------------------------
#module -> a file containing code you want to include in your program use 'import' to include a module

#To creat your own module   1) click on your project  
                         #  2) new
                         #  3)python file
                         #  4) write code  (functions) you want 

print (help("modules"))  #Built-in modules
#import math 
import math as m
print(m.pi)

from math import pi
print(pi)

#------------------------------------------------------------------
#object =  bundle of related attribures (variables ) and Methods
#  Ex. phone ,cup ,book
#  you nedd a class to crate many objects
#-------------------------------------------------------------------

class car :
    def __init__(self,model,year,color,for_sale):
     self.model=model
     self.year=year
     self.color=color
     self.for_sale=for_sale  

    def drive(self):
       print(f"You drive {self.model}") 
    def stop(self): 
       print(f"You Stop {self.model}") 

car1=car("Mustang",2025,"red",False)
print(car1.color) 
print(car1.year)
car1.drive()
car1.stop()
#-------------------------------------------------------------------
# Class Variable : shared among all instances of the class
# Class Variable :Defined outside  the constructor
# Class Variable : Allow you to share data among all objects created from that class
#-------------------------------------------------------------------

class student :
  
  class_year=2025   #class Variable 
  num_students=0
  def __init__(self,name,age):  #Instance method
    self.name=name              # instance variable
    self.age =age 
    student.num_students +=1

student_1=student("Alaa",21)          
student_2=student("sara",22) 
print(student_1.name)
print(student_1.age)
print(student.class_year)  
print(student.num_students)

#---------------------------Inheritance---------------------------
#Inheritance -> Allows a class to inherit attribtes ND METHODS FROM ANOTHER CLASS 
# Helps with code reusability and extensibility

class Animal:
   def __init__(self,name):
    self.name=name
    self.is_alive=True
   def eat(self):
     print(f"{self.name}is eating") 
   def sleep(self):
      print(f"{self.name}is sleeping")   
class Dog(Animal):
    pass

class Cat(Animal):
   pass 

class Mouse(Animal):
   pass 

dog=Dog("Scooby")
cat=Cat("Garfield")
mouse=Mouse("Mickey")

print(dog.name)
print(dog.is_alive)
print(cat.name)
mouse.sleep()

#---------------------------Supper()---------------------------
#super(): used in a child class to call methods from a parent class 

class shape:   #parent class
   def __init__(self,color,is_filled):
      self.color=color
      self.is_filled=is_filled
   def describe(self):
      print(f"the shape color ={self.color} and {"filled"if self.is_filled==True else "not filled"}")   


class circle(shape):
   def __init__(self,color,is_filled,radius):
     super().__init__(color,is_filled)
     self.radius=radius
   
   def describe(self):      # describe method in each subclass has the shared describtion  + the unique describtion
      super().describe()   
      print(f"the area of circle = {3.14*self.radius*self.radius}cm^2")
      

class square(shape):
   def __init__(self, color, is_filled,width):
      super().__init__(color, is_filled)
      self.width=width

class triangle(shape):
   def __init__(self, color, is_filled,width,height):
      super().__init__(color, is_filled)      
      self.width=width
      self.height=height

cir=circle(color="red",is_filled=True,radius=5)
sqr=square(color="blue",is_filled=False,width=6)
tri=triangle(color="yellow",is_filled=True,width=5,height=7)

print(cir.color)
print(cir.is_filled)
print(cir.radius)

cir.describe()
tri.describe()
sqr.describe()
#---------------------------polymorphism---------------------------
#polymorphism = Greek word that means to have many forms or faces:
# The same function make different functions

            # Two ways to achieve polymorphism :
            # 1) Inheritance :
            # 2) "Duck Typing "  


from abc import ABC,abstractmethod
class shape :
   @abstractmethod   #An abstract method in Python is a method that is declared in a base class
                     #but does not contain any implementation.
                     # Abstract methods are meant to be overridden in derived classes, ensuring that certain methods are implemented in all subclasses of the base class
   def area(self):
      pass


   pass 
class Circle(shape):
    def __init__(self,radius):
       self.radius=radius
    def area(self):          # area method must be implemented in each sub class , it is  abstractmethod in the base class
       return 3.14*self.radius**2   
       
    
class Square(shape) :
   def __init__(self,side):
      self.side=side
   def area(self):
      return self.side**2
   
class pizza(Circle):
   def __init__(self,topping, radius):
      super().__init__(radius) 
      self.topping=topping

     
shapes=[Circle(4),Square(5),pizza("pepperoni",15)]   # pizza considered a circle ,shape , pizza     
for shape in shapes :
   print(shape.area())

#---------------------------Duck Typing--------------------------- 
#Duck typing : Another way to achieve polymorphism besides Inheritance
#object must have the minimum necessary attributes/ methods


class Animal :
   alive =True

class Dog (Animal):
   def speak(self):
      print("WOOF!")
class Cat(Animal):
   def speak(self):
      print("MEOW!")

class car:  
   alive=True
   def speak(self):
      print("ksks")      

Animals=[Dog(),Cat(),car()]  # car isn't the animal but has the same properties  like the car in cartoon

for animal in Animals:
   print(animal.speak())
   print(animal.alive)


#---------------------------static methods---------------------------
# static Method : belongs to a class rather then any object from that class (intsttance) 
# static method :best utility funcrios that do not need access to class data  
#insttance Method: best for operations on instance of the class (object)



class Empolyee :
   def __init__(self,name,position):
      self.name=name
      self.position= position
   def get_info (self):
      return f"{self.name}={self.position}"
   
   @staticmethod
   def is_valid_position (position):
       valid_positions=["Manager","Cashier","Cook","Janitor"]
       return position in valid_positions
   
print(Empolyee.is_valid_position("Manager"))


empolyee1=Empolyee("Alaa","Student")
employee2=Empolyee("Sara","Engineer")
print(Empolyee.is_valid_position(empolyee1.position))
print(empolyee1.get_info())

#---------------------------Class Method---------------------------
#  take (cls) as the first parameter , which represents the class it self

#class method    :best for class-level data or require access to the class itself
#static method   :best utility functios that do not need access to class data  
#instance Method :best for operations on instance of the class (object)

class Student :
   count = 0
   total_gpa=0
   def __init__(self,name,gpa):
      self.name=name
      self.gpa=gpa
      Student.count +=1
      Student.total_gpa+=gpa

   @classmethod
   def get_count(cls):   #class method
      return f"Total of students:{cls.count}"
   @classmethod
   def get_average_gpa(cls):
      if cls.count==0:
       return 0
      else:
       return f"average={cls.total_gpa / cls.count :.2f}"
      
student_1=Student("Alaa",3)
student_2=Student("sara",4)
print(Student.get_count())
print(Student.get_average_gpa())# class methods : Allow operations related to the class itself

#---------------------------Magic Method---------------------------
#Magic Method : Dunder methods __inti__ ,___str___,__eq__
#They are automatically called by many of python's built-in operations
#They allow developers to define or customize the behavior od the object 
#2)self.__class The class  return the class which the class instance belong
#3)__str__ :gives a human -readable output of the object
#4)__len__ : return the length of the container  , called when we use built-in len() on the object

class Book:
   def __init__(self,title,author,num_pages):
      self.title=title
      self.author=author
      self.num_pages=num_pages

   def __str__(self):
      return f"{self.title} by {self.author}"   
   
   def __eq__(self,other):
      return self.title==other.title  and self.author==other.author
   def __lt__(self,other):
      return self.num_pages < other.num_pages
   

book1=Book("the Hobbit","J.R.R",310)  #__init__ called automatically and i customize this function with some variables (title,author,num_pages)
print(book1)  # without customize  __str__ :          <__main__.Book object at 0x000001F15256C560>
print(book1)  # with define and customize __str__ :   the Hobbit by J.R.R
book2=Book("the Hobbit","J.R.R",309)
print(book1==book2)  # without customize  __str__ : False
print(book1==book2)  # with customize  __str__ :  True
print(book2 <book1)  # without customize  __lt__ : '<' not supported between instances of 'Book' and 'Book'
print(book2 <book1)  #True


#---------------------------@property---------------------------
#@property : Decorator used to define a method as a property (it can be accessed like an attribute)
#            add  aditional logic when read ,write ,or delete attributes
#            gives you getter ,setter , and deleter method



class Rectangle:
   def __init__ (self,width,height):
      self._width=width       # _width: meant to be used internally (inter the class) (private)
      self._height=height




   @property                         #getter
   def width(self):
      return f"{self._width:.1f}"    # aditional logic when read
   
   @property
   def height(self):
      return f"{self._height:.1f}"
   
   @width.setter                    #setter (write)
   def width(self,new_width):       
       if new_width>0:
          self._width=new_width
       else :
          print("Width must be greater than 0")   
   @height.setter
   def height(self,new_height):
       if new_height>0:
          self._width=new_height
       else :
          print("Height must be greater than 0")

   @width.deleter
   def width(self):
      del self._width
      print ("Width has been deleted")    

   @height.deleter                      #deleter
   def height(self):
      del self._height
      print ("Hight has been deleted") 

  

   
   
rectangle=Rectangle(3,4)   
# print(rectangle._width)   #warning
# print(rectangle._height)  #warning 
#print(rectangle.height()) # Error 
print(rectangle.height)   # 4
print(rectangle.width)  # 3

rectangle.width=0     #Width must be greater than 0
print(rectangle.height)   # 4
print(rectangle.width)  # 3

rectangle.width=5
rectangle.height=6
print(rectangle.height)   # 6
print(rectangle.width)  # 5

del rectangle.width
del rectangle.height

#-----------------------------------------------------------------------------------------------------------------