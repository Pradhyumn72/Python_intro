# Conditional -> if,if-else,if-elif,if-elif-else
# iterative-> while,for
# transfer-> continue,break,pass

# conditonal --> if 
# x=10
# if x>8:
#     print("this is if body")


# print("this is main body")

# x=input(str("enter your name :"))
# x=False
# if x :
#     print("hello" ,x)

# print("bye",x)

# to check if no is odd or not
# n=int(input("enter value of n :"))
# if(n%2==0):
#     print(f'{n} is even')
# else:
#     print(f'{n} is odd')

# x=int(input("enter val of x :"))
# y=int(input("enter val of y :"))
# z=int(input("enter val of z :"))

# if x>y and x>z:
#     print("x is greater")
# elif(y>x and y>z):
#     print("y is greater")
# else:
#     print("z is greater")

# dry principle:don't repeat the code:, to avoid sequential repetition of block of code we use iterative/looping statements

# iterative/looping: while n for loop

# while loop: for infinite iteration
# for loop; finite iteration

# ============ while===========:
# n=int(input("enter value of n "))
# i=1
# while i<=n:
#     print(i)

#     i=i+1
# n=int(input("enter value of n "))
# i=1
# summ=0
# while i<=n:
#     summ=summ+i
#     if i<n:
#         print(i,end="+")
#     else:
#         print(i,end="=")


#     i=i+1

# print(summ)
# n=int(input("enter value of n "))
# i=1
# mult=1
# summ=0
# while i<=n:
#     mult=mult*i
#     if i<n:
#         print(i,end="*")
#     else:
#         print(i,end="=")


#     i=i+1

# print(mult)

# n=int(input("enter val of n "))
# mult=1
# while n>0:
#     mult=mult*n
#     if n >1:
#         print(n,end="*")
#     else:
#         print(n,end="=")
#     n=n-1

# print(mult)


# n=int(input("enter val of n"))
# while n>0:
#     print(n)
#     n=n-1

# ================Questions for practice================
# Q1.even nos till n
# n=int(input("enter val of n :"))
# i=2
# while i<=n:
#     print(i,end=",")
#     i=i+2

# Q2. n even numbers 
# n=2
# i=1
# while i<=n:
#     print(i*n)
#     i=i+1

# Q3 sum of even nos till 10
# mult = 1
# i = 2
# while i <= 10:
#     mult *= i
#     i += 2
# print(mult)
# Q4 multiplication of even nos till n




# Q5 odd nos till n
# n=1
# while n<11:
#     print(n)
#     n=n+2
    
# Q6 n odd numbers
# n=int(input("enter val of n "))
# i=1
# while i<=n:
#     if(n%2!=0):
#         print(i,end=",")
    

# star pattern 

# s1="python"
# s2="java"
# s=s1+s2
# print(s)

# n=int(input("enter val of n "))
# i=1
# while i<=n:
#     print('*'*i)
#     i=i+1


# n=int(input("enter val of n "))
# i=1
# while i<=n:
#     print(""*(n-i)+'* '*i)
#     i=i+1
# n=int(input("enter val of n "))
# i=0
# while i<=n:
#     print("*"*(n-i) + " "*i)
#     i=i+1

# n=int(input("enter val of n "))
# i=0
# while i<=n:
#     print(" "*i+ "*"*(n-i))
#     i=i+1
# n=int(input("enter val of n "))
# i=0
# while i<=n:
#     print(" "*i+ "* "*(n-i))
#     i=i+1

# n=int(input("enter val of n "))
# i=0
# while i<n:
#     print(" "*i+"*"*(n-i))
#     i=i+1
# i=i-2
# while i>=0:
#     print(" "*i+"*"*(n-i))
#     i=i-1

# n=int(input("enter val of n "))
# i=0
# while i<n:
#     print(" "*i+"* "*(n-i))
#     i=i+1
# i=i-2
# while i>=0:
#     print(" "*i+"* "*(n-i))
#     i=i-1

# n=int(input("enter val of n "))
# i=0
# while i<n:
#     print("*  "*(n-i))
#     i=i+1
# i=i-2
# while i>=0:
#     print("*  "*(n-i))
#     i=i-1
# n=int(input("enter val of n "))
# i=1
# while i<=n:
#     print(" "*(n-i)+"*"*i)
#     i=i+1
# i=i-2
# while i>0:
#     print(" "*(n-i)+"*"*i)
#     i=i-1
# n=int(input("enter val of n "))
# i=1
# while i<=n:
#     print(" "*(n-i)+"* "*i)
#     i=i+1
# i=i-2
# while i>0:
#     print(" "*(n-i)+"* "*i)
#     i=i-1

# Armstrong number 
# 153=1^3+5^3+3^3 will be an armstrong
# WAP to find total no of digits in a number
n=int(input("enter val of n "))
# method 1 for cal of no of digits 
# x=str(n)
# print(len(x))

digit=0
while n >0:
    n=n//10
    digit=digit+1
print(f'total digit is {digit}')

# WAP to find total sum of digits in given no
# sum=0
# while n>0:
#     last_digit=n%10
#     sum=sum+last_digit
#     n=n//10
# print(f'total sum is {sum}')

# Armstrong
# x=y=n
# while n>0:
#     digit=digit+1
#     n=n//10
# while x>0:
#     last_digit=x%10
#     sum=sum+last_digit**digit
#     x=x//10
# if y==sum:
#     print(f'given number {y} is armstrong number ') 

# else:
#     print("not ")

# # palindrome
# n=int(input("enter val of n "))
# # method 1
# # if n==n[::-1]:
# #     print(n,"is palindrom2")
# # else:
# #     print("not")

# conventional method 
# s=str(input("enter a word"))
# palindrom=True
# l=int(len(s)/2)
# i,j=0,-1
# while l>0:
#     if s[i]==s[j]:
#         pass
#     else:
#         palindrom=False
#         break
#     i=i+1
#     j=j-1
#     l=l-1
# if palindrom:
#     print(s, "is palindrome")
# else:
#     print("not palindrome")


# =============For Loop=============
# l=[1,2,3,4,5]
# l1=[]
# for i in l:
#     l1.append(i**2)
# print(l1)

#  it will eject out every letter of the word 
# s="hello"
# for i in s:
#     print(i)


# char---> ascii ,use ord()
#  ascii----> char,use chr()
# x="abcde"
# y=str()

# for i in x:
#     print(chr(ord(i)+4))

# for getting in a string
# x="abcde"
# y=str()

# for i in x:
#     print(chr(ord(i)+4))
#     y=''.join([y,chr(ord(i)+4)])
# print(y)

# even number sum
# n=int(input("enter val of n "))
# sum=0
# for i in range(2,n+1,2):
#     sum=sum+i
    
#     if i<=n-2:
#         print(i,end="+")
#     else:
#         print(i,end="=")
# print(sum)

# for n even numbers

# for i in range(1,n+1):
#     sum=sum + (2*i)
#     if i<n:
#         print(2*i,end="+")
#     else:
#         print(2*i,end="=")
# print(sum)

# odd number sum
# for i in range(1,n+1,2):
#     sum=sum+i
#     if i<=n-2:
#         print(i,end="+")
#     else:
#         print(i,end="=")
# print(sum)


# ========Transfer statement========
# continue,break,pass

#  continue (skip current iteration)
# n=10
# i=1
# while i <=n:
#     if i==5:
#         i=i+1

#         continue
#     else:
#         print(i)
#         i=i+1

# break
# n=10
# i=1
# while i<=n:
#     if i==5:
#         break
#     else:
#         print(i)
#         i=i+1
# print("hello")

# n=10
# i=1
# while i<=n:
#     if i==5:
#         pass
#     else:
#         print(i)
#     i=i+1
# print("hello")

# for avoiding syntax error 
# n=10
# i=1
# if n>=1:
#     pass
# else:
#     print(i)
# while True:
#     print("1.Additon \n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.OFF"  )
#     n=int(input("enter operation u want to perform"))
#     x=(1,2,3,4,5)
#     if n in x:
#         if n==1:
#             p=int(input("enter val of p "))
#             q=int(input("enter val of q"))
#             print(p+q)
#         elif n==2:
#             p=int(input("enter val of p "))
#             q=int(input("enter val of q"))
#             print(p-q)
#         elif n==3:
#             p=int(input("enter val of p "))
#             q=int(input("enter val of q"))
#             print(p*q)
#         elif n==4:
#             p=int(input("enter val of p "))
#             q=int(input("enter val of q"))
#             print(p/q)
#     else:
#         print("please enter correct input")

#Q1
# l=[10,20,30,40,50]
# l[0],l[-1]=l[-1],l[0]
# print(l)



# Q2
# t=(10,20,30,40,50)
# l=list(t)
# l[0],l[-1]=l[-1],l[0]
# t=tuple(l)
# print(t)

#q3
# s='python'
# l=list(s)
# l[0],l[-1]=l[-1],l[0]
# print(l)
# s=''.join(l)
# print(s)


# Q4
# n=int(input("enter the numof th elements in the list"))
# s=str(n)
# l=list(s)
# l[0],l[-1]=l[-1],l[0]
# s=''.join(l)
# print(s)


# n=int(input("enter the number="))
# for i in range(n):
#     x='A'
#     for j in range(0,n):
#         print(chr(ord(x)+j),end=' ')
#     print()

# n=int(input("enter val of n "))
# i=0
# while i<=n:
#     print((n-i)*" "+ i*'*' )
#     i=i+1
