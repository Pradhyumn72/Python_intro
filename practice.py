# import re
import numpy as np

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
# def dutch(nums):
#     low=0
#     mid=0
#     high=len(nums)-1
#     while (mid<=high):
#         if (nums[mid]==0):
#             nums[low],nums[mid]=nums[mid],nums[low]
#             low+=1
#             mid+=1

#         elif (nums[mid]==1):
#             mid+=1

#         else:
#             nums[high],nums[mid]=nums[mid],nums[high]
#             high-=1
#     return nums

# nums=[1,2,2,0,1,2,2,0]
# print(dutch(nums))


# move zeroes to end

# def move_zeroes(nums):
#     i=0
#     j=0
#     for i in range(0,len(nums)):
#         if(nums[i]!=0):
#             nums[i],nums[j]=nums[j],nums[i]
#             i+=1
#             j+=1
#     return nums

# nums=[4,0,6,0,2,1,9,0,5]
# print(move_zeroes(nums))

# def count_elements(nums):
#     count=1
#     i=0
#     for i in range(1,len(nums)-1):
#         if nums[i]<nums[i+1]:
#             count+=1
#             i+=1
#     return count

# nums=[1,2,3,4,5]
# print(count_elements(nums))

# n=int(input())
# prod=1
# if n==0:
#     print(1)
# elif n<0:
#     print(False)
# for i in range(1,n+1):
#     prod*=i
#     print(prod)

# def violate():
#     n=list(map(int,input().split()))
#     d=int(input())
#     fine=int(input())
#     count=0
#     for i in range(len(n)):
#         if (d%2==0):
#             if (n[i]%2!=0):
#                 count+=1
#                 # print(count)
#         else:
#             if(n[i]%2==0):
#                 count+=1
#     return fine*count

# print(violate())


# def threat(n,r):
#     total_sum=0
#     total=0
#     while n>0:
#         d=n%10
#         total_sum+=d
#         n=n//10
#     total_sum=total_sum*r

    
#     while total_sum >=10:
#         newsum=0
#         while total_sum>0:
#             d=total_sum%10
#             newsum+=d
#             total_sum=total_sum//10
#         total=newsum
#     return total
# print(threat(99,3))


# def second_largest():
#     arr=list(map(int,input().split()))
#     largest=arr[0]
#     slargest=-1
#     for i in range(0,len(arr)):
#         if (arr[i]>largest):
#             slargest=largest
#             largest=arr[i]
#         elif (arr[i]<largest and arr[i]>slargest):
#             slargest=arr[i]
#     return slargest

# print(second_largest())


# def second_smallest():
#     arr=list(map(int,input().split()))
#     smallest=arr[0]
#     ssmallest=float('inf')
#     for i in range(0,len(arr)):
#         if (arr[i]<smallest):
#             ssmallest=smallest
#             smallest=arr[i]
#         elif(arr[i]543)

# def rev():
#     n=list(map(int,input().split()))
#     s=0
#     e=len(n)-1
#     while s<e:
#         n[s],n[e]=n[e],n[s]
#         s+=1
#         e-=1
#     return n

# print(rev())

# n=list(map(int,input().split()))
# i=0
# sum=0
# for i in range(0,len(n)):
#     sum+=n[i]
#     avg=sum//len(n)

# print(avg)

# n=str(input())
# f={}

# for ch in n :
#     f[ch]=f.get(ch,0)+1
# print(f)

# def sortti():
#     n=list(map(int,input().split()))
#     i=0
#     j=i+1
#     while i<j:
#         if(n[i]>n[j]):
#             n[i],n[j]=n[j],n[i]
#             i+=1
#             j+=1
#     return n

# print(sortti())
        
# def remove_duplicates(arr):
#     seen = set()
#     result = []

#     for num in arr:
#         if num not in seen:
#             seen.add(num)
#             result.append(num)

#     return result
# print(remove_duplicates([8,4,1,0,4,8,1]))

# def symmetric_pairs(arr):
#     seen = set()

#     for a, b in arr:
#         if (b, a) in seen:
#             print((a, b))
#         else:
#             seen.add((a, b))


# arr = [(1, 2), (2, 1), (3, 4), (5, 6), (4, 3)]

# symmetric_pairs(arr)

#  maximum product subarray
# def product(arr):
#     curr_max=arr[0]
#     curr_min=arr[0]
#     ans=arr[0]
#     for i in range(0,len(arr)):
#         num=arr[i]
#         temp=curr_max
#         curr_max=max(num,num*curr_max,num*curr_min)
#         curr_min=min(num,num*temp,num*curr_min)
#         ans=max(ans,curr_max)
#     return ans
# print(product([1,2,3,4,5,0]))

# def rank(arr):
#     print(arr)
#     arr.sort()
#     i=0
#     for i in range(0,len(arr)):
#         arr[i]=i+1
#         i+=1
#     return arr

# print(rank([1,6,2,9,3]))
# Function to find the equilibrium index in the array
# def findEquilibriumIdx(nums, n):
    
#     totalSum = sum(nums)

    
#     leftSum = 0
#     rightSum = totalSum

    
#     for i in range(n):
#         rightSum -= nums[i]  

#         if leftSum == rightSum:
#             return i  

#         leftSum += nums[i]  

#     return -1  


# def sortt_arr(arr1,arr2):
#     freq={}
#     for i in arr1:
#         freq[i]=freq.get(i,0)+1

#     result=[]
#     for i in arr2:
#         if i in freq:
#             result.extend([i]*freq[i])
#             del freq[i]

#     remaining=list(freq.keys())
#     remaining.sort()
#     for i in remaining:
#         result.extend([i]*freq[i])
#     return result

# print(sortt_arr([1,2,3,3,2,4,5],[2,2,3,4,5,3,6]))

# rows, cols = map(int, input().split())

# matrix = []

# for i in range(rows):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# print(matrix)

# def counting(n):
#     vowel="aeiou"
#     cnt=0
#     vow=0
#     spc=0
#     for ch in n:
#         if ch==" ":
#             spc+=1
#         elif ch in vowel:
#             vow+=1
#         else:
#             cnt+=1
#     return cnt,vow,spc
# print(counting("hello"))


# def remove(n):
#     vowel="aeiou"
#     result=""
#     for ch in n:
#         if ch not in vowel:
#             result+=ch
#     return result

# print(remove("hello"))

# def removedup(n):
#     seen=set()
#     result=""
#     for ch in n:
#         if ch not in seen:
#             result+=ch
#             seen.add(ch)
#     return result

# print(removedup("programming"))

# rows, cols = map(int, input().split())

# matrix = []

# for i in range(rows):
#     matrix.append(list(map(int, input().split())))

# print(matrix)

# row sum
# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# rows=len(matrix)
# cols=len(matrix[0])
# for i in range(cols):
#     total=0
#     for j in range(cols):
#         total+=matrix[i][j]
#     print(total)

# cols sum
# rows=len(matrix)
# cols=len(matrix[0])
# for j in range(cols):
#     total=0
#     for i in range(rows):
#         total+=matrix[i][j]
#     print(total)

# max and min of elements
# rows=len(matrix)
# cols=len(matrix[0])
# max=matrix[0][0]
# for i in range(rows):
#     for j in range(cols):
#          if matrix[i][j]>max:
#               max=matrix[i][j]
# print(max)



# matrix = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])

# transpose = matrix.T

# print(transpose)

# def ingri(arr,target):
#     i=0
#     j=0
#     found=False
#     for i in range(0,len(arr)):
#         if arr[i]==target:
#             print(arr[i])
#             found=True
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]+arr[j]==target:
#                 print(arr[i],arr[j])
#                 found=True
#     if not found:
#         print("No Target sum Found")

# (ingri([1,1,2,3],3))

# month = int(input())
# year = int(input())

# if month in [1, 3, 5, 7, 8, 10, 12]:
#     days = 31

# elif month in [4, 6, 9, 11]:
#     days = 30

# else:  # February
#     if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#         days = 29
#     else:
#         days = 28

# print("Number of days is", days)

# def identify(A,B):
#     for i in range(len(A)):
#             if A[i]<B[i]:
#                 return -1 

#     for ch in B:
#         if ch not in A:
#             return -1
#     ans=set()
#     for i in range(len(A)):
#         if A[i]!=B[i]:
#             ans.add(B[i])
#     return len(ans)
# (identify("abc","aab"))


# def energy(B,zombie):
#     zombie.sort(reverse=True)
#     for z in zombie:
#         if B<z:
#             return "NO"
#         loss=(z%2)+(z/2)
#         B-=loss
#     return "YES"
# print(energy(35,[6,7,10]))


# def jersey_no():
#     rows,cols=map(int,input().split())
#     matrix=[]
#     summ=0
#     summc=0
#     for i in range(rows):
#         matrix.append(rows)
#     for j in range(cols):
#         matrix.append(cols)
#     for x in range(rows):
#         maxsum1=0
#         for y in range(cols):
#             summ+=rows[x][y]
#             maxsum1=max(maxsum1,summ)
#     for y in range(cols):
#         maxsum2=0
#         for x in range(rows):
#             summc+=cols[x][y]
#             maxsum2=max(maxsum2,summc)
#     return maxsum1+maxsum2
# jersey_no()

# def jersey_no(matrixx):
#     rows=len(matrixx)
#     cols=len(matrixx[0])
#     maxsum1=0
#     maxsum2=0
#     for i in range(rows):
#         summr=0
#         for j in range(cols):
#             summr+=matrixx[i][j]
#         maxsum1=max(maxsum1,summr)
#     for j in range(cols):
#         summc=0
#         for i in range(rows):
#             summc+=matrixx[i][j]
#         maxsum2=max(maxsum2,summc)
#     return maxsum1+maxsum2

def check(n,m,k):

    if (2 * n * m) % k == 0:
        print("YES")
    else:
        print("NO")
check([1,0,0],[0,1,0],[0,0,3])
