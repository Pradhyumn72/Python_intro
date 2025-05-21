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

#  while:
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
# while i<=10:
#     print(i*n)
#     i=i+1

# Q3 sum of even nos till 10
# n=2
# i=1
# b=0
# while i<=n:
#     b=b+i
#     if i<n:
#         print(i,end="+")
#     else:
#         print(i,end="=")

# i=i+1

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
#     print(" "*(n-i)+'* '*i)
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
# n=int(input("enter val of n "))
# method 1 for cal of no of digits 
# x=str(n)
# print(len(x))

# digit=0
# while n >0:
#     n=n//10
#     digit=digit+1
# print(f'total digit is {digit}')

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

# palindrome
n=int(input("enter val of n "))
# method 1
# if n==n[::-1]:
#     print(n,"is palindrom2")
# else:
#     print("not")

x=n
rev=0
while n > 0:
    last_digit=n%10
    rev=rev*10+last_digit
    n=n//10
if x==rev:
    print(x,"is palindrome")
else:
    print("hence not a palindrome")
