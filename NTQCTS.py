# day 1 and day2
# second largest
# def s_largest():
#     arr=list(map(int,input().split()))
#     largest=arr[0]
#     s_lar=-1
#     for i in range(1,(len(arr))):
#         if(arr[i]>largest):
#             s_lar=largest
#             largest=arr[i]
#         else:
#             if(arr[i]<largest and arr[i]>s_lar):
#                 s_lar=arr[i]
#     return s_lar

# print(s_largest())

#  Reverse an array
# def reversal_array():
#     arr=list(map(int,input("Enter elements").split()))
#     n=len(arr)
#     l=0
#     h=n-1
#     temp=0
#     while(l<h):
#         temp=arr[l]
#         arr[l]=arr[h]
#         arr[h]=temp
#         h=h-1
#         l=l+1
#     return arr

# print(reversal_array())

# checking if array is sorted?
# def sortedd():
#     arr=list(map(int,input("Enter elements").split()))

#     for i in range(1,len(arr)):
#         if arr[i]<arr[i-1]:
#             print("Array is not sorted")

#         print("array is sorted")

# Remove Duplicates

# def duplicates():
#     arr=list(map(int,input("Enter elements").split()))
#     i=0
#     for j in range(1,len(arr)):
#         if arr[j]!=arr[i]:
#             arr[i+1]=arr[j]
#             i=i+1

#         return i +1


# print(duplicates())

# rotate array by k places
# def reversee(arr,l,h):
#     temp=0
#     while(l<h):
#         temp=arr[l]
#         arr[l]=arr[h]
#         arr[h]=temp
#         l+=1
#         h-=1


# def rotate_array():
#     k=int(input("Enter the places by whihc you want to rotate"))
#     arr=list(map(int,input("Enter elements").split()))
#     n=len(arr)
#     k=k%n
    
#     reversee(arr,0,k-1)
#     reversee(arr,k,n-1)
#     reversee(arr,0,n-1)
#     return arr

# print(rotate_array())

# dutch national flag
# l=0


 




# Fibonacci Series

n = int(input("Enter number of terms: "))

a = 0
b = 1

# for i in range(n):
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c

# print()    # Moves the cursor to the next line after printing the series

n = int(input())

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()