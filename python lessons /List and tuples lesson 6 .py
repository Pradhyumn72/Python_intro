users = ['dave','Bitti','Shanu']
data = ['Chinki',21,'Bhuru']
emptylist = []
# print("Dave" in data)
print(data[0:2])

# to know the positions we use index functions
print(data.index('Bhuru'))

# To add a element we can use append functions
print(users.append('Utkarsh'))
print(users)

# other method to ad element without using append
data += ['10']
print(data)

# extend method can be used to add element to the list
users.extend(['Ridhima','Samarth'])
print(users)

# for printing any particular elememt
# print((users[1:]))
# print(data[1:3])
# print(users[-3:-1])
# print(len(data))

# to insert a elememt bewteen any element we use insert function
users.insert(3, 'Aadhya')
print(users)

users[4:5] = ['Ravi','Bhuri']
data[4:4] = ['Mayur','Dhannu']
print(users)
print(data)

# to remove any element we use element function 
# list.remove() takes exactly one argument (2 given)
# users.remove('Dave')
# print(users)

data.remove('10')
print(data)

# pop function is used to remove last element 
print(users.pop())
print(users)

#  for deleting a element use del funtion with position but when we
# want to delete a list del listname
# when we want to clear elements of a list and make it empty 
del users[5]
print(users)
data.clear()
print(data)

# for alphabetical orders use sort 
users.sort()
print(users)


# for sorting a element with lower case into alphabetical order
users.sort(key=str.lower)
print(users)

# for reversing the order of a list
nums = [4,8,9,2,5]
nums.reverse()
print(nums)

# # numbers in desending order
# nums.sort(reverse=True) 
# print(nums)

# # for ascending order
# nums.sort(reverse=False)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)
print(type(nums))

#  Tuples

mytuple = tuple(('Krish', 20,True))
anothertuple  = (2,6,4,7,9)
print(mytuple)
print(tuple())