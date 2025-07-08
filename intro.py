#  limitation of python : it is nod good in memory management
# # a= int(input("enter radius of circle :"))
# # area= 3.14*a*a 
# # print(area)

# l=int (input(" enter val of l : "))
# b=int (input(" enter val of b : "))
# h=int (input(" enter val of h : "))
# perimeter=4*(l+b+h)


# datatypes 
#numeric => int,float,complex
#  string 
# sequence=> list[],tuple(),set{}
# key value=> dictionary{}
# boolean => true or false

# a=5.4+9j
# print(type(a))

#list[]
# a=[1,2,"jazz",10,22,True] #mutable
# print(a)
# print(type(a))

#tuple
# b=(1,2,True)  #non changable
# print(b)
# print(type(b))

# sets mutuable but do not store multiple data
# c={2,4,"hello"} 
# print(c)
# print(type(c))

# dictionary  key can't be duplicate
# d={
#     "Name":"Bunny",
#     "Age": 23,
#     "City":"Bhopal"

# }

# print(d)
# print(type(d))

#  identifiers and var difference :
# identifier - pyhton k object ka naam..name of an object
# object- container of a value....object ka reference store krta hai 

#  literals (constant values)

# list[]
# l1=["python",1,4,"look"]
# print(l1)


# tup2()
# tup2=("hello",23,"exe")
# print(tup2)
# print(type(tup2))
# print(id(tup2))

#  dictionary{} => key value pair
# d1={
#     'Name':"Bitti",
#     'Age': 19,
#     'College':"VIT"
# }
# print(d1)
# print(type(d1))
# print(id(d1))

# set{}: unordered data type or undordered collection 
# set1={10,20,30,'push',90,22,'cross','axis','cover','acis','book'}
# print(set1)
# a=frozenset(set1)
# print(type(a))

# x=10 
# y=2 
# # p,q,r,c,v,b=30,40,50,60,70,80
# # print(x,y,p,q,r,c,v,b)
# a=y//x
# b=y/x
# c=y%x
# d=y*x
# e=y**x
# f=y+x
# g=y-x
# print(a)
# print(type(a))
# print(b)
# print(type(b))
# print(c)
# print(type(c))
# print(d)
# print(type(d))
# print(e)
# print(type(e))
# print(f)
# print(type(f))

# a=10
# b=20
# c=5

# a+=b
# # c+=(a+=b)
# print(a)
# print(c)

# x=int()
# print(x)
# print(type(x))
# y=float()
# print(y)
# print(type(y))

# c=[]
# d=list()
# e=str()
# f=tuple()
# g=dict()
# j=set()
# k=frozenset()
# print(c)
# print(type(c))
# print(d)
# print(e)
# print(f)
# print(g)
# print(j)
# print(k)

# x=eval(input("Enter any no."))
# print(x)
# print(type(x))
# y=eval(input("Enter list "))
# print(y)
# print(type(y))

# ASC II values
# space =32
# 0-9= 48-57
# A-Z=65-90
# a-z=97-122
# x=[9,8,7,'p']
#  print(sum(x))
# print(max(x))
#  print(min(x))
# print(len(x))
# print("hello")
# print("hi")
# in print by default in sep space is given and 2nd attribute is end='\n' by default we can edit is also
# sep= spearates by space or whatever u write in the sep
# end='\n'
# print("air",end=",")
# print("pro",end="-")


# telling the size of every dataset 
# import sys
# x=int()
# y=str()
# z=list()
# p=tuple()
# q=dict()
# r=set()
# f=frozenset()
# print(sys.getsizeof(x))
# print(sys.getsizeof(y))
# print(sys.getsizeof(z))
# print(sys.getsizeof(p))
# print(sys.getsizeof(q))
# print(sys.getsizeof(r))
# print(sys.getsizeof(f))

# x=10
# y=10
# print(id(x))
# print(id(y))
# a="Python"
# b="Python"
# print(id(a))
# print(id(b))
# z=["luke",9]
# w=["luke",9]
# print(id(z))
# print(id(w))
# e={1,2,"present"}
# q={1,2,"present"}
# print(id(e))
# print(id(q))
# t={6,5,"hello"}
# d=frozenset(t)
# print(id(d))

# x=9<<3
# print(x)
# s=("python")
# print(s.index("o"))
# print(s.index("y",2))
# print(s.index("p",2,4))
# print(s.index("p",-5,-1))
# tup=[10,20,30,"air","book","  ","study","pro","action"]
# print(tup.index("  ",3,6))
# l="python"
# print(l[0])
# print(l[-4])


