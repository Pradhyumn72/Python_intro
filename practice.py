import re

n=str(input("enter your name "))
e=str(input("enter your email "))
cno=str(input("enter your contact number"))
i=str(input(" upload file...."))
d=str(input("upload document"))
p=str(input("enter your pass"))

if n!=n.isalpha():
    print(n.replace(" ",""))
else:
    print(n)
if e[0].isalpha() and re.match():
    print(e)
else:
    print("check email again")