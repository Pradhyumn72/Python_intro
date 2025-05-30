# # s=("python")
# # print(s.index("o"))
# # print(s.index("y",2))
# # print(s.index("p",2,4))
# # print(s.index("p",-5,-1))
# # tup=[10,20,30,"air","book","  "]
# # print(tup.index("  ",3,6))
# l="python"
# print(l[0])
# # print(l[-4])

# s="I Love Python"
# print(s[0:0])
# print(s[7:-6]) # same indexing gives empty output
# print(s[::-1][1:7][::-1][2:3])
# print(s[::0])
# s = 'pythonista'
# output:inoh
# print(s[::-1])
# s = 'program'
# print(s[-6:-1:2])
# s1=["bunny","mac","book","pro","air","fruit","samsung","actually"]
s2= [1,2,3,4,4,4,5,5,1,2,43]
s3= [1,2,3,1,2,43]
# s3="Actually macbook is a samsung fruit"
# print(s3.split())
# b=str(input("enter a string "))
# for i in s1:
#     if i==b:
#         break
#     else:
#         print("not found ")``
# print("_",s1.join(s2))
# s1="Rhythrrrrm"
# # s2="World"
# print(s1.count("r"))
# s2.append(0)
# print(s2)
# s2.insert(2,4,12)
# s2.extend(s3)
# print(s2)
# print(s2.index(2))
# s3=[4,5,6,7]
# print(s3.index(6,1,2))
# var = "I love python" 
# print(var[::2])
d={1:"hello",2:"my",3:"name",4:"is bunny"}
# print(d.keys())
# print(d.values())
# print(d.items())
# d[4]="is ashwinn"
# print(d)
# del d[4]
# print(d)
# x = {'age': 25} 
# x.setdefault('name', 'Neeraj') 
# print(x)
# y=(1,8,0,6,0,5)
# print(y.index(6))
# n=int(input("enter anything "))
# m=int(input("enter anything "))
# x=n[::-1]
# # if n%4==0:
# #     print("a leap year")
# # else:
# #     print("not")
# if n==x:
#     print("a palindrome")
# else:
#     print("not")
# a=int()
# if n>m:
#     a=n
# else:
#     a=m

# while(1):
#     if a%n==0 and a%m==0:
#         print("lcm is ",a)
#         break
#     a=a+1
# x = int(input("Enter value of x: "))
# y = int(input("Enter value of y: "))
# a = min(x, y)
# while a > 0:
#     if x % a == 0 and y % a == 0:
#         print("HCF is", a)
#         break  
#     a -= 1

# couting digits
# t=0
# x=int(input("enter val of x "))
# while x>0:
#     x=x//10
#     t=t+1
# print("no of digits in x is ",t)
# x = int(input("Enter value of x: "))
# if x < 2:
#     print("Not prime")
# else:
#     for i in range(2, x):
#         if x % i == 0:
#             print("Not prime")
#             break
#     else:
#         print("Prime")
# x=102//10
# print(x)
# x=str(input("enter anything"))
# n=x[::-1]
# print("reverse of x is ",n)
# x=int(input("enter val of x "))
# if x%2!=0:
#         x=x-1
    
# for i in range(2,x+1,2):
#     if x%2==0:
#         print(i)
    
# num = int(input("Enter any number: ")) 
# factor = 0 

# if num == 0 or num == 1:     
#     print(num, "is not a prime number") 
# elif num > 1:     
#     for i in range(2, num):         
#         if num % i == 0:             
#             factor += 1             
#             break 

#     if factor == 0:     
#         print(num, "is a prime number") 
#     else:     
#         print(num, "is not a prime number") 

# n=int(input("enter val of n "))
# for i in range(1,n+1,2):
#     if n%2!=0:
#         print(i)
#     else:
#         n=n-1
#         print(i)


# n=int(input("Enter any no:")) 
# x=0
# for i in range(1,n+1):     
#     if n%i==0:         
#         # print(i)
#         x=x+1
# print("count of factor ",x)

# l = [64, 34, 25, 12, 22, 11, 90, 5] 
# n = len(l) 
# print(n)
# for i in range(n-1):     
#     for j in range(n-i-1):         
#         if l[j] > l[j+1]:             
#             l[j], l[j+1] = l[j+1], l[j] 
#             print(l)
# x=int(input("enter val of x "))
n=int(input("enter a val of n "))
sum=0
for i in range(1,n+1):
    if n%i==0:
        sum=sum+i

print(sum)
if sum==2*n:
    print("n is perfect number")
else:
    print("not perfect ")



    

