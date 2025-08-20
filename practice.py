import re

n = input("Enter your name: ")
e = input("Enter your email: ")
cno = input("Enter your contact number: ")
i = input("Upload file (filename with extension): ")
d = input("Upload document (filename with extension): ")
p = input("Enter your password: ")

if n:
# name
    if n.replace(" ", "").isalpha():
        print("Name:", n)
    else:
        print("Invalid name (only alphabets allowed)")

    # email
    if e[0].isalpha() and re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', e):
        print("Email:", e)
    else:
        print("Check email again")

    #  contact number
    if re.match(r'^[0-9]{10}$', cno):
        print("Contact Number:", cno)
    else:
        print("Invalid contact number (must be 10 digits)")

    # file
    if re.match(r'^.+\.(jpg|png|jpeg)$', i):
        print("File uploaded:", i)
    else:
        print("Invalid file (only .jpg ,.jepg, .png allowed)")

    # document
    if re.match(r'^.+\.(pdf|docx)$', d):
        print("Document uploaded:", d)
    else:
        print("Invalid document (only .pdf or .docx allowed)")

    # password
    if len(p) >= 6 and re.search(r'[A-Za-z]', p) and re.search(r'[0-9]', p):
        print("Password accepted")
    else:
        print("Invalid password (must be at least 6 characters with letters and numbers),you have given only",len(p),"digit")

    print("############# Dashboard #############")
    print("Welcome",n)
    print("Your details are as follows:")
    print("Contact Number :",cno)
    print("Image :",i)
    print("Document :",d)
    print("Current Password :",p)