# Integer
# x=9
# c=8+9j
# y=0.9
# print(x)
# print(type(x))
# print(max(x)) 
# print(len(x))
# print(y)
# print(type(y))
# print(c)
# print(type(c))
# if id is same of any variable or collection then it is immutable
# on int methods are not applicable

# String=> collection of chars,reperesented through "",',''' . ordered collection ,due to this indexing,slicing is supported .it is immutable
# a="Swimming is my hobby123"
# b="and football also" 

# c=[a,b]

# python inbuilt functions
# print(max(a))
# print(min(a))
# print(id(a))
# print(type(a))
# print(len(a))


# print(a.lower())
# print(a.upper())
# print(a.swapcase()) #uppercase ko lower n lower ko upper
# print(a.title())
# print(a.capitalize())
# print(a.center(100,"-"))
# print(",".join([a,b]))
# print(a.split("from where",no of times u want to separate))
# print(a.split("m")) # if we don't write the no of times we need to separate the elemets ,it auto takes no of times the given string is apperared
# print(a.isascii())
# print(a.isnumeric())
# print(a.isdigit())
# print(a.isspace())
# print(a.isnumeric())
# print(a.isdecimal())


# List: collection of homo and hetro elements, is represnented by[] and separated by ,ordered collection due to which indexing suported
# and hence slicing and mutuable , max n min doesn't work

# air=["hello",1,2,3,"how are you"]
# l1=["python","java","php"]
# l2=[19,90,20,21,30,40,20,20]
# print(max(l1))
# print(min(l1))
# print(len(air))
# # print(sum(l1))
# print(sum(l2))

#list method: copy,clear,append,extend,insert,push,pop,remove,index,count(frequency),reverse,sort
# l2.append(40)
# print(l2)
# l2.extend(["p"]) 
# print(l2)
#takes input as collection only
# print(l2)
# l2.insert(2,90)
# print(l2)
# l2.pop()
# print(l2)
# l2.remove(30)
# print(l2)
# l2.index(19)
# print(l2)
# l2.count(20)
# print(l2)
# l2.reverse()
# print(l2)
# l2.sort()
# print(l2)
# l2.pop()
# l2.pop()
# print(l2)
# l2.index(20,3)
# print(l2)
#  print(l2.count("d"))
# l2.sort(reverse=True)
# print(l2)
# l2.reverse()
# print(l2)
# l3=l2.copy()
# print(l3)
# print(id(l2),id(l3))

# l2.clear()
# x=l2
# print(x)
# print(id(x))
# del(x)
# print(x)

# tuple: collecction of homogenous as well as hetrogenous elements,represented through parenthesis with (, as separator),indexing,slicings supported,immutable in nature
# inbuilt functions: len,max,min,sum,type,id are supported
# tup1=(12,32,34,"python","slice")
# tup2=(12,32,45,55)
# print(len(tup1))

# ==========Errors=========
# print(max(tup1))
# print(min(tup1))
# print(sum(tup1))
# print(len(tup2))
# print(max(tup2))
# print(min(tup2))
# print(sum(tup2))
# print(tup2.index(32))
# print(tup1.index("slice"))
# print(tup2.index(45,0))
# print(tup2.count(45))

# dictionary => collection of key value pair,key must be unique,value may be duplicate,{,},indexing & slicing not supported,mutable
# details={'name':'Ashly','age':30,'city':'noida'}
# details2={'name':'Ashly','age':30}
# details2.update(details)
# print(details2)
# l=[1,2,3,'a','b','c']
# print(len(details))
# print(max(details))
# print(min(details))
# print(sum(details))
# print(type(details))
# print(id(details))
# print(details)
# print(details.keys())
# print(details.values())
# print(details.items())
# print(details.get('name')) # for getting single item only 
# details=dict.fromkeys(l)
# print(details)
# details.setdefault('name','Bunny')
# print(details)

# SETS: unordered collection of unique elements,{,},indexing and slicing not supported,mutable in nature
# set1={2,4,6,8,2,4,'python','java','php',}
# set2={0,4,1,6,9,3,5,4,3} # sum will be taken of unique elements only..same goes with len also 
# set3=set2.copy()
# print(set3)
# print(set1)
# print(id(set1))
# print(set2)
# print(id(set2))
# print(max(set2))
# print(min(set2))
# print(sum(set2))
# print(type(set2)
# set1.add('C++')
# print(set1)
# set1.update([1,2])
# print(set1)
# set1.update((66,77),'hash')
# print(set1)
# set2.update((('humble',11),90))
# print(set2)
# set1.pop()
# set1.pop()
# set1.pop()
# set1.pop()
# print(set1)
# set2.remove(2)
# print(set2)
# set2.discard(2) #diff b/w discard n add is that, discard doesn't interrupt the code execution and add interrupts
# s1={1,2,3,4,5}
# s2={5,6,7,8,9,10}
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s1.symmetric_difference(s2)) # opposite of intersection
# print(s1.intersection_update(s2)) # kya common hai wo bta rha 
# print(s1)
# s1.difference_update(s2)
# print(s1)
# s1.symmetric_difference_update(s2)
# print(s1)
# print(s1.isdisjoint(s2))

# frozenset- union,intersection,difference,symmetric difference are appplicable
fs1={10,20,10,30,20,40}
fs2={2,4,6,8}
fs1=frozenset(fs1)
fs2=frozenset(fs2)
# print(fs1.union(fs2))
# print(fs1.intersection(fs2))
# print(fs1.difference(fs2))
# print(fs1.symmetric_difference(fs2))
# print(fs1.isdisjoint(fs2))
# print(fs1.issubset(fs2))
print(fs1.issuperset(fs2))

### empty declaration of datatypes will be :
# int()
# str()
# float()
# complex()
# list()
# tuple()
# dict{}
# set{}
# frozenset{}###

