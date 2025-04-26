# def hello():
#     print("Hello World")
# hello()


# def sum(num1,num2): 
#   if (type(num1) is not int or type(num2) is not int):
#     return
#   return num1 +num2

# total = sum("a",3)
# total1 = sum (4 , 5)
# print(total)
# print(total1)

#  putting default values 
# def sum(num1 = 6, num2 = 3 ): 
#   if (type(num1) is not int or type(num2) is not int):
#     return
#   return num1 +num2

# total = sum(1 ,2)
# print(total)

def multiple_items(*args):
    print(args)
    print(type(args))
multiple_items("Jones","Shanty","Chunks")

# kwargs is keyword agrument used when we want to define a keyword   

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))
mult_named_items(first = "Shanty",last = "Shanti")