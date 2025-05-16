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

x=int(input("enter val of x :"))
y=int(input("enter val of y :"))
z=int(input("enter val of z :"))

if x>y and x>z:
    print("x is greater")
elif(y>x and y>z):
    print("y is greater")
else:
    print("z is greater")