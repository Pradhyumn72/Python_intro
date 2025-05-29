'''achieves code reusability
 write once call multiple time
 types => user defined 
 pre defined=> input ,print, max,min
 syntax: def func-name(parameter):
 body

 calling the fucntions
 func-name(arguments)
 return

 function without a name is called lambda function
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
#     fact =1
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)

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

l=[64,35,25,12,22,11,90,5]
l.sort(reverse=True)
print(l)