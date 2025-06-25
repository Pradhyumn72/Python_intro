'''achieves code reusability
 write once call multiple time
 types => user defined 
 pre defined=> input ,print, max,min
 syntax: def func-name(parameter):
 body

 calling the fucntions
 func-name(arguments)
 return

 function without a name is called lambda function3

 '''

# def evennos(n):
#     for i in range(1,n+1):
#         if i < n:
#             print(2*i-1,end=",")
#         else:
#             print(2*i-1)
# print("hello")
# print("hi")
# evennos(int(input("enter no ")))

# def fact(n):
#     factt =1
#     for i in range(1,n+1):
#         factt=factt*i
#     print(factt)
# fact(int(input("enter val of n ")))

# fact(int(input("enter any no ")))
# def fact(n):
#     fact1=1
#     for i in range(n,0,-1):
#         fact1=fact1*i
#         if i >1:
#             print(i,end="*")
#         else:
#             print(i,end="=")
#     print(fact1)

# fact(int(input("enter any no ")))

# ''' user defined functions
# rel b/w parameter n argument
# i) positional argument: ex(x,y) passing value in this format only
# ii) keyword argument: ex (x=10,y=20) passing this while calling the function
# iii) default argument: ex(x=0,y=0) passing this while declaration of function
# iv) variable length positional argument(*args):
# v) keyword variable 
# '''

# # def sum(x=0,y=0):# default argument
# # def sum(x,y):
# #     print("val of x",x)
# #     print("val of y",y)
# #     print(x+y)
# # # sum(y=10,x=20) # keyword argument
# # sum(10) # default argument

# # def sum(*args):
# #     a=0
# #     for i in args:
# #         a=a+i
# #     print(a)
# # sum(10,20)

# # x=eval(input("enter any tuple : "))
# # print(x)
# # print(type(x))

# # def sum(*n):
# #     print(n)
# #     print(type(n))
# # x=eval(input("enter any tuple "))
# # sum(x)
# #  single * for taking tuple
# # def sum(*n):
# #     summ=0
# #     for i in n:
# #         for j in i:
# #             for k in j:
# #                 summ=summ+k
# #     print(summ)
# # x=eval(input("enter any list "))
# # sum(x)

# #  for taking dictionary as input use **
# def sum(**n):
#     for k,v in n.items():
#         print(k,"=",v)

# # sum(x=10,y=20,z=30)
# sum(name="Pradhyumn",age="19",college="VIT")

# l=[64,35,25,12,22,11,90,5]
# l.sort(reverse=True)
# print(l)

#higher order functions
#ek function ke argument me  agr ham ek or func pss  krde to usko hOF boltey he


                                                     #hof
                                                    # || 
              #map() same no of output,filter()less than or equal output ,reduce() only 1 output,lambda(),decortator(),generator()
              
              
#map()..................
#syntax

# map(fun_name,iterator 1, iterator2,....)

# map(fun_name,collection 1, collection2,....)

# l=[1,2,3,4,5]
# def sqr(n):
#     return n**2
# x=map(sqr,l)
# print(x)
# print(list(x))





# l1=[1,2,3,4,5]
# l2=[2,3,4,5,6]
# l3=[7,4,5,6,9]
# def add(x,y,z):
#     return(x+y+z)
# p=map(add,l1,l2,l3)
# print(list(p))

# l1=[5,6,7]
# l2=[3,2,1]
# def sub(x,y):
#     return(x-y)
# s=map(sub,l1,l2)
# print(list(s))

#...................................................


#map me input or output element  equal hote he isliye yeh wrong case he isme ek 2 kam output me ayenge  (yeh input/output wala concept mobile me hai)
# l1=[1,2,3,4,5]
# l2=[2,3,4]
# l3=[7,4,5,6,9]
# def add(x,y,z):
#     return(x+y+z)
# p=map(add,l1,l2,l3)
# print(list(p))
# l1=[4,9,16,25,36,49]
# def sqrt(n):
#     return n**(0.5)
# ma=map(sqrt,l1)
# print(list(ma))

# l1=[1,2,3,4,5,6]
# l2=[2,4,6,8,10]
# def even(n):
#     if n%2==0:
#         return (n)
# x=filter(even,l2)
# print(list(x))
# y=filter(even,l1)
# print(list(y))

# Reduce(func-name.iterator,initial val) - for single output 
from functools import reduce
l1=[1,2,3,4,5]
l2=[1,2,3,4,5,6,7,8]
l3=[1,2,3,4,5,6,7,2]
# def maxx(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# x=reduce(maxx,l1)
# print(x)
# def summ(x,y):
#     return x+y
# x=reduce(summ,l1)
# print(x)
# sum=0
# def sq(sum,x):
#     return sum + x

# q=reduce(sq,l1)
# print(q)

# lambda (); can take n no of parameters
# syntax : lambda (parameter ): expression
# x=lambda x,y: (x+y)
# p=int(input("enter val of p "))
# q=int(input("enter val of q "))
# z=x(p,q)
# print(z)


# when we will write print at both end...none will come,,because value of z stored is z


# x=map(lambda x:x**2,l1)
# print(list(x))


# l1=[1,2,3,4,5,6,7,8,9,10,12]
# # n=8
# # p= lambda x:['even'if x%2==0 else 'odd'] # writing if else in single line
# # print(p(n))
# p=map(lambda x:'even' if x%2==0 else 'odd',l1)
# print(list(p))

# l=[1,2,3,5,7,9,0,4]
# x=reduce(lambda p,q: p if p > q else q,l) # finding largest
# x=reduce(lambda p,q: p+q,l) 

# print(x)


# Decorators : it takes argument as a function and return also a function, denoted by @

# def decor(x):
#     def inner_func():
#         p=x
#         return p
#     return inner_func
# x=decor(10)
# print(x)
# z=x()
# print(z)
@decor

def decor(x):
    def inner_func(r,s):
        r=r+5
        s=s+5
        p=x(r,s)
        return p
    return inner_func
@decor
def add(x,y):
    return x+y
z=add(5,10)
print(z)
