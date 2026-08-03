# import re

# n = input("Enter your name: ")
# e = input("Enter your email: ")
# cno = input("Enter your contact number: ")
# i = input("Upload file (filename with extension): ")
# d = input("Upload document (filename with extension): ")
# p = input("Enter your password: ")

# if n:
# # name
#     if n.replace(" ", "").isalpha():
#         print("Name:", n)
#     else:
#         print("Invalid name (only alphabets allowed)")

#     # email
#     if e[0].isalpha() and re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', e):
#         print("Email:", e)
#     else:
#         print("Check email again")

#     #  contact number
#     if re.match(r'^[0-9]{10}$', cno):
#         print("Contact Number:", cno)
#     else:
#         print("Invalid contact number (must be 10 digits)")

#     # file
#     if re.match(r'^.+\.(jpg|png|jpeg)$', i):
#         print("File uploaded:", i)
#     else:
#         print("Invalid file (only .jpg ,.jepg, .png allowed)")

#     # document
#     if re.match(r'^.+\.(pdf|docx)$', d):
#         print("Document uploaded:", d)
#     else:
#         print("Invalid document (only .pdf or .docx allowed)")

#     # password
#     if len(p) >= 6 and re.search(r'[A-Za-z]', p) and re.search(r'[0-9]', p):
#         print("Password accepted")
#     else:
#         print("Invalid password (must be at least 6 characters with letters and numbers),you have given only",len(p),"digit")

#     print("############# Dashboard #############")
#     print("Welcome",n)
#     print("Your details are as follows:")
#     print("Contact Number :",cno)
#     print("Image :",i)
#     print("Document :",d)
#     print("Current Password :",p)

# S1='Neeraj'
# S2='Neraj'
# print(S1>S2)

# length function without inbuilt function
# def lengthh(s):
#     count=0
#     for i in s:
#         count+=1
        
#     return count
    
# s='Pradhyumn'
# lengthh(s)


# count function without inbuilt function
# def count_char(s,target):
#     count=0
#     for ch in s:
#         if ch==target:
#             count+=1
#     return count

# s='Pradhyumn'
# target='a'
# result=count_char(s,target)
# print(f"The character '{target}' appears {result} times in the string.")

# reversing string without inbuilt function
# def reverse_string(s):
#     reversed_s=''
#     for i in range(lengthh(s)-1,-1,-1):
#         reversed_s+=s[i]
#     return reversed_s
# s='Aman'
# reversed_s=reverse_string(s)
# if (reversed_s==s):
#     print("The string is a palindrome.")
# print("Reversed string:",reversed_s)

# # palindrome without inbuilt function\

# def is_palindrome(s):
#     n=lengthh(s)
#     for i in range(n//2):
#         if s[i]!=s[n-i-1]:
#             return False
#     return True
# s='madam'
# if is_palindrome(s):
#     print("The string is a palindrome.")

# to lower case without inbuilt function

# def to_lowercase(s):
#     rslt=''
#     for ch in s :
#         if 'A'<=ch<='Z':
#             rslt+=chr(ord(ch)+32)
#         else:
#             rslt+=ch
#     return rslt

# to upper case without inbuilt function
#  in the code of lower case just replace +32 with -32 

#  to remove spaces without inbuilt function
# def remove_spaces(s):
#     rsl=''
#     for ch in s:
#         if ch!=' ':
#             rsl+=ch
#     return rsl


#  check this once
# def remove_space_asc(s):
#     res=''
#     for ch in s:
#         if ord(s)!=32:
#             res+=ch
#     return res
# s='P r a d h y u m n'
# ans=remove_space_asc(s)
# print(ans)


# to calculate words in a sentence on the basis of spaces without inbuilt function

# l=[1,0,0,10]
# print(any(l)) # True
# print(all(l)) # False 

# a=[]
# aa=list()
# aaa=[1,2]
# b=()
# bb=tuple()
# bbb=(1,2)
# c={}
# cc=set()
# ccc={'hellor':1,'ge':1}
# d=frozenset()
# dd={'ee':1,'ss':2}
# ddd=frozenset(dd)

# print(bool(a))
# print(bool(aa))
# print(bool(aaa))
# print(bool(b))
# print(bool(bb))
# print(bool(bbb))
# print(bool(c))
# print(bool(cc))
# print(bool(ccc))
# print(bool(d))
# print(bool(dd))
# print(bool(ddd))
# print(bool(a))
# print(any(a))
# print(any(b))
# print(any(c))
# print(any(d))
# i=int()
# print(i)
# s=str()
# print(bool(s))

# s=' '
# print(bool(s)) # true

# x=0
# y='a'
# print(any([x,y]))

# namespace ---> identifier + object value



# import builtins
# x=10
# y=20
# z=30
# def first():
#     a=1
#     b=2
#     c=3
#     print(locals())

# first()

# print(globals())
# print(dir(builtins))

# x=10
# def outer_fun():
#     x=20
#     def inner_func():
#         # print(x)
#         nonlocal x
#         x=30
#     inner_func()
#     print(x)
# outer_fun()


# class Test():
#     x=10

# x=Test()
# print(id(x))
# print(dir(Test))
# examples of local variable , instance variable , class variable , global variable






# x=10
# class Test():
#     z=10
#     def test():
#         y=10


# access specifiers

# class A():
#     __x=10
#     def __xyz(self):
#         print("pvt method")
# class B(A):
#     pass

# obj=B()
# print(obj.__x)
# print(obj.__xyz())
# print(A.__x)
# print(A.__xyz)
# print(dir(A))
# print(A._A__xyz)
# print(A._A__x)
# print(obj._A__x)
# print(obj._A__xyz())

# x=input("enter any list ")
# print(x)
# print(type(x))  
# print(list(x))
# print(type(list(x)))
# y=eval(input("enter any list "))
# print(y)
# print(type(y))

# def reverse_string(s):
#     rvs_str=''
#     for i in (s):
#         rvs_str=i+rvs_str
#     return rvs_str
    
# def is_palindrome(s):
#     ab=reverse_string(s)
#     if s==reverse_string(s):
#         print("palindrome")
#     else:
#         print("not palindrome")

# s='Pradhyumn'
# is_palindrome(s)

# print(ord('h'))



#  dutch national flag 
def dutch(nums):
    low=0
    mid=0
    high=len(nums)-1
    while (mid<=high):
        if (nums[mid]==0):
            nums[low],nums[mid]=nums[mid],nums[low]
            low+=1
            mid+=1

        elif (nums[mid]==1):
            mid+=1

        else:
            nums[high],nums[mid]=nums[mid],nums[high]
    return nums

nums=[1,2,2,0,1,2,2,0]
dutch(nums)
