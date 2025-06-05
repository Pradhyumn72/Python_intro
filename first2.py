# import first
# p=first.x
# q=first.y
# z=first.add(p,q)
# print(z)
# collection of variables ,fucntions,etc is modules 
# collection of modules containing init.py file is package
# collection of package is library

from first import *
# from first import x
from first import Act as a  # making nickname for a specific function known as alliasing
# p=x
# q=y
# z=add(p,q)
# print(z)

obj=a() # we can import class by making it obj

z=obj.add(10,20)
print(z)
