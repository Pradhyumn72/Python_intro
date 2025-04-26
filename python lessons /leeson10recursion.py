# Recursion is calling itself 

# def add_one(num):

#     if (num >= 10):
#         return num + 1
    
#     total = num + 1
#     print(total)

#     return add_one(total)
# add_one(0)

value = "y"
count = 0

while value:
     count += 1 
     print(count)  
     if (count == 5):
          break
     else:
        value = 0
     continue