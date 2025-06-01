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
# n=int(input("enter a val of n "))
# sum=0
# for i in range(1,n+1):
#     if n%i==0:
#         sum=sum+i

# print(sum)
# if sum==2*n:
#     print(n," is perfect number")
# else:
#     print("not perfect ")
# l=[90,21,67,9,3,13,56]
# n=len(l)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if l[j]<l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)

# n=int(input("enter val of n "))
# i=n
# while i>=1:
    
#     print(' '*(n-i)+'*'*i)
#     i=i-1

# a = int(input("Enter value of a: "))
# b = int(input("Enter value of b: "))

# print(f"Before swapping: a = {a}, b = {b}")

# # Swapping using third variable
# temp = a
# a = b
# b = temp

# print(f"After swapping: a = {a}, b = {b}")


# string = input("Enter a string: ")

# vowels = "aeiouAEIOU"
# vowel_count = 0
# consonant_count = 0

# i = 0
# while i < len(string):
#     char = string[i]
#     if char.isalpha():  # Only letters
#         if char in vowels:
#             vowel_count += 1
#         else:
#             consonant_count += 1
#     i += 1

# print("Vowels:", vowel_count)
# print("Consonants:", consonant_count)


# l1=(10,20,30,40,50)
# i=0
# while i <len(l1):
#     l1.index(i)=l1.index(i)+5
#     i=i+1
# print(l1)

# l1 = (10, 20, 30, 40, 50)
# i = 0
# temp = []

# while i < len(l1):
#     temp.append(l1[i] + 5)
#     i += 1

# l1 = tuple(temp)
# print("Updated tuple:", l1)

# string = input("Enter a string: ")
# char_list = []
# i = 0

# while i < len(string):
#     char_list += [string[i]]
#     i += 1

# print("Characters in the string:", char_list)
# n=[20,40,59,32,44,65]
# i=0
# for i in range(len(n)):
#     n[i]=i
#     i=i+1
#     print(i)

# num = input("Enter a number: ")

# count = 0

# for digit in num:
#     if digit.isdigit():  # Skip minus sign or other characters
#         count += 1

# print("Total number of digits:", count)
# a=str(input("enter "))
# b=a[::-1]
# print(b)
# n = int(input("Enter value of n: "))
# original = n  # Backup the original number

# # 1. Count digits
# digit_count = 0
# x = n
# while x > 0:
#     digit_count += 1
#     x //= 10
# print(f"Total digits: {digit_count}")

# 2. Sum of digits
# x = n
# sum_digits = 0
# while x > 0:
#     sum_digits += x % 10
#     x //= 10
# print(f"Sum of digits: {sum_digits}")

# 3. Armstrong check

# x=n
# sum_armstrong = 0
# while x > 0:
#     last_digit = x % 10
#     sum_armstrong += last_digit ** digit_count
#     x //= 10

# if original == sum_armstrong:
#     print(f"{original} is an Armstrong number.")
# else:
#     print(f"{original} is not an Armstrong number.")


# start = int(input("Enter start of range: "))
# end = int(input("Enter end of range: "))

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# print(f"\nNon-prime numbers between {start} and {end} are:")
# for num in range(start, end + 1):
#     if not is_prime(num):
#         print(num, end=" ")


# num = int(input("enter val of num "))
# first_value, second_value = 0, 1
# # Print Fibonacci numbers less than or equal to 'num'
# for i in range(num):
#     if first_value > num:
#         break
#     print(first_value, end=" ")
#     next_value = first_value + second_value
#     first_value = second_value
#     second_value = next_value
# num = int(input("Enter value of num: "))

# factt = 1

# if num == 0:
#     print("Factorial is 1")
# else:
#     for i in range(1, num + 1):
#         factt = factt * i
#     print(f"Factorial of {num} is {factt}")

# given range
# given_range = 25
 
# # iterate using a for loop till the
# # given range
# for i in range(given_range+1):
#     print(i)
#     i+=1
 
    # if no. is multiple of 4 and 5
    # print fizzbuzz
    # if i % 4 == 0 and i % 5 == 0:
    #     print("fizzbuzz")
 
    #     # continue with the loop
    #     continue
 
    # # if no. is divisible by 4
    # # print fizz and no by 5
    # if i % 4 == 0 and i%5!=0:
    #     print("fizz")
 
    #     # continue with the loop
    #     continue
    # # if no. is divisible by 5
    # # print buzz and not by 4
    # if i % 5 == 0 and i % 4!= 0:
    #     print("buzz")
 
    # else:
 
    #     # else just print the no.
    #     print(i)



# Get the month name from user
month = input("Enter month name: ")

# Use title case to avoid case mismatches
month = month.capitalize()

# Check how many days it has
if month == "February":
    print("The month of February has 28 or 29 days.")
elif month in ("April", "June", "September", "November"):
    print("The month of", month, "has 30 days.")
elif month in ("January", "March", "May", "July", "August", "October", "December"):
    print("The month of", month, "has 31 days.")
