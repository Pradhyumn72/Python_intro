def even_no(n):
    i=2
    while i<=2:
        yield i # return value ko leke function terminate krke bahar aata hai ,yield holds the address of value and 
        i=i+2
        
n=int(input("enter val of n "))
x=even_no(n)
for i in x:
    print(i)

