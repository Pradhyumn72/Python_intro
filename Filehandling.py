'''
open : syntax: open('file name'=> wioth extension,'mode')
x- create
w-write
r-read,if file doesn't exists...gives an error
a-append,here if file doesn't exist...it will create the file
'''

# f2=open("n.txt",'x')
# print(f2.name)
# print(f2.mode)
# print(f2.encoding)
# print(f2.readable())
# print(f2.writable())
# f2.close()
# print(f2.closed)
# f2=open("n5.txt",'w+') # makes it readable and writable 
# print(f2.name)
# print(f2.mode)
# print(f2.encoding)
# print(f2.readable())
# print(f2.writable())
# f2.close()
# print(f2.closed)
f3=open("n6.txt",'xb+') # makes it readable and writable 
print(f3.name)
print(f3.mode)
# print(f3.encoding)
print(f3.readable())
print(f3.writable())
f3.close()

print(f3.closed)