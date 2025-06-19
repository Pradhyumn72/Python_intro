#jitni bhi real world entites contectecd he
#class-dummy model/design/blueprint  of an object,ek class se n num of object bana sakte he
#classs me atehe======> behavior-methods , or properties-variables
#clas ka name capital letter se hota he hmesa


#OBject======= physical existence of class ,

#class syntax
#class Class_name:
#   "doc string"
#  varible are three category--class variable,instance variable , local variable


#constructor 
#method=instnace method,class method ,static method



# class Demo:
#     "this is the class "
#     pass
# print(id(Demo))
# print(dir(Demo))   #yeh sareee inbuilt method dikhata heeeee 
# print(Demo.__doc__)



# class Demo:
#     "this is the class "
#     x=10
#     y=20
#     def new(self):
#         pass
# print(Demo.__dict__)
#isme jo main he wo file ki enetrry point hoti he




# class Demo:
#     "this is the class "
#     x=10
#     y=20
#     def new(self):
#         pass
# print(id(Demo))
# obj=Demo
# print(id(obj))
#yeh same address dega because abi hamne kisi ko assign nahi kiya he




# class Demo:
#     "this is the class "
#     x=10
#     y=20
#     def new(self):
#         pass
# print(id(Demo))
# obj=Demo() #yaha per jo paranthersis he wo external constructor ko call kr rh he
# print(id(obj))



# class Student:
#     def __init__(self,name,gread):
#         self.n=name
#         self.g =gread
#         print(id(self))
# #obj=Student
# obj=Student('pradhyumn','btech')
# print(id(obj))
#self ek referece variable he jo cufrrent obj ka adresss hold krta he 
#current class ka current obj hold krta he

# Day 2 OOPS
# we can create n number of const but the recent one will be executed
# constructor overload is not supported in py, const can be called explicitly
# class Student:
#     def __init__(self):
#         print("const called")
#     def __init_(self,x):
#         print("2nd const called")
#     def __init__(self,x,y,z):
#         print("3rd const called ")
#     def __init__(self):
#         print("4th const called")
# obj=Student()

# class Student:
#     # variable with self is instance variable
#     # method with first parameter as self is known as instance method
#     # n,a,r,c is instance variable
#     def __init__(self,name,age,roll_no,city):
#         self.n=name
#         self.a=age
#         self.r=roll_no
#         self.c=city
#     def show(self):
#         print(self.n)
#         print(self.a)
#         print(self.r)
#         print(self.c)
#         print(self.school)
#         # another method to variable
#     def  add (self,principal):
#         self.p=principal
# x=str(input("enter your name "))
# y=int(input("enter your age "))
# z=int(input("enter your roll no "))
# w=str(input("enter your city "))
# stu1=Student(x,y,z,w)
# accessing instance variable outside class
# print(stu1.n)
# print(stu1.a)
# print(stu1.r)
# print(stu1.c)
# obj=Student('pradhyumn',19,100,'idr')
# # obj.show()
# # we can define an instance variable outside the const as the add is same of obj and self 
# obj.school='SPS'
# obj.show()
# obj.add('mac')
# print(obj.p)


# Day 3 OOPS

# class variable and static variable

# class Student ():
#     school="SPSSN" # declaration of class variable
#     def __init__(self,name,grade,roll):
#         self.name=name
#         self.grade=grade
#         self.roll=roll
#         Student.principal="Python" ## this variable can only be accessed when we will call the const 
#         print(Student.city) # accessing class variable declared outside class
#     def show(self):
#         print(self.name)
#         print(self.grade)
#         print(self.roll)
#         print(Student.school) #accessing of class variable

# Student.city="Bhopal" # declaring class variable outside class and 
# obj=Student("pradhyumn","A+",101)
# print(Student.school)
# print(Student.principal) ##
# obj.show()
# obj1=Student("bunny","B+",102)
# obj1.show()


# class method
# class Student:
#     grade="1st"
#     def __init__(self,name,roll):
#         self.n=name
#         self.r=roll 
#     def show(self):
#         print(self.n)
#         print(self.r)
#         print(Student.grade)
#     @classmethod
#     def update(cls,x):
#         cls.grade=x
# obj=Student("action",40)
# obj.update("2nd")
# obj.show()
    



#local variable
# class student:
#   def new(self):
#     x=10
#     print(x)
#   def new1(self):
#     print(x)
# obj1=student()
# obj1.new()



# class student:
#   def first(self):
#     print("from first method")
    
#   @staticmethod
#   def wel_great():
#     print("welcome this webspage")
    
#   @staticmethod
#   def thankx_great():
#     print("thankx for visit")
# obj=student()
# obj.wel_great()


''' ABSTRACTION: taking useful info only 

'''
from abc import ABC,abstractmethod
class Senior(ABC):
    def add(self,x,y):
        return x+y
    def sub(self,x,y):
        return x-y
    @abstractmethod
    def multi(self):
        pass
class Junior(Senior):
    def multi(self,x,y): #in child we are bound to use abstract of parent class
        return x*y
obj=Junior()