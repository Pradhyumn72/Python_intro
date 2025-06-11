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
# f3=open("n6.txt",'xb+') # makes it readable and writable 
# print(f3.name)
# print(f3.mode)
# # print(f3.encoding)
# print(f3.readable())
# print(f3.writable())
# f3.close()

# print(f3.closed)



#read()
#yeh kiisi bhi file ke  all data ko  read krta he eek ek character ke format me 

#read(n)== read(5) mtlb sirf 5 hi character read krne he 
#readline()=read single lines of data
#readlines()=read lines multiples liens of data


# f=open('n1.txt','r+')
# data=f.read()
# print(data)




# f=open('n1.txt','r+')
# data=f.read(10)
# print(data)


# f=open('n1.txt','r+')
# data=f.readline()
# print(data)


# f=open('n1.txt','r+')
# data=f.readlines()
# print(data)




# f=open('n1.txt','r+')
# data1=f.read(5)
# data2=f.read(10)
# print(data1)
# print(data2)


# f=open('n1.txt','r+')
# f.write("hello")
# f.close


# f=open('n1.txt','r+')
# f.readline()
# f.write("hello")

#cursor movement 
#tell()=to check current position of cursor
#seek()= how many positions move from where (0,1,2,) 0 is the starting point , 1 is the currenmt position , 2 is the last postion 
# f=open('n1.txt','r+')
# print(f.tell())
# f.read(5)
# print(f.tell())



# f=open('n1.txt','r+')
# print(f.tell())
# f.read(5)
# f.seek(0)
# f.seek(1)
# print(f.tell())

# tell=> finds out cursor current position 
# seek=> to move cursor,two attributes will be passed (kaha ko move krwana hai ,kaha se) 0,1,2 is for kaha se only
# 0 is for 0th index,1 for current positon,2 for last position
 
f=open('n.txt','a+')
# data=f.read(10)
# data1=f.seek(0,0)

# data2=f.seek(4,2)

# print(data)\
# print(data1)
# print(data2)
print(f.tell())
f.seek(5,0)
data = f.read(5)
print(data)
print(f.tell())
f.write('okayy')
f.seek(0,0)
# dt=f.read()
# print(dt)


