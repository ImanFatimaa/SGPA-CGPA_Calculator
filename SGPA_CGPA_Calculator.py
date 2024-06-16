#calculating sgpa
a=int(input("entre credit hours of course 1: "))
h=input("entre grade of course 1: ")
if(h=="A"):
    h=4*a
elif(h=="B+"):
    h=3.5*a
elif(h=="B"):
    h=3*a
elif(h=="C"):
    h=2*a
elif(h=="D"):
    h=1*a
elif(h=="F"):
    h=0*a
else:
    print("input is invalid: ")
b=int(input("entre credit hours of course 2: "))
i=input("entre grade of course 2: ")
if(i=="A"):
    i=4*b
elif(i=="B+"):
    i=3.5*b
elif(i=="B"):
    i=3*b
elif(i=="C"):
    i=2*b
elif(i=="D"):
    i=1*b
elif(h=="F"):
    i=0*b
else:
    print("input is invalid: ")
c=int(input("entre credit hours of course 3: "))    
j=input("entre grade of course 3: ")
if(j=="A"):
    j=4*c
elif(j=="B+"):
    j=3.5*c
elif(j=="B"):
    j=3*c
elif(j=="C"):
    j=2*c
elif(j=="D"):
    j=1*c
elif(j=="F"):
    j=0*c
else:
    print("input is invalid: ")
d=int(input("entre credit hours of course 4: "))
k=input("entre grade of course 4: ")
if(k=="A"):
    k=4*d
elif(k=="B+"):
    k=3.5*d
elif(k=="B"):
    k=3*d
elif(k=="C"):
    k=2*d
elif(k=="D"):
    k=1*d
elif(k=="F"):
    k=0*d
else:
    print("input is invalid: ")
e=int(input("entre credit hours of course 5: "))
l=input("entre grade of course 5: ")
if(l=="A"):
    l=4*e
elif(l=="B+"):
    l=3.5*e
elif(l=="B"):
    l=3*e
elif(l=="C"):
    l=2*e
elif(l=="D"):
    l=1*e
elif(l=="F"):
    l=0*e
else:
    print("input is invalid: ")
f=int(input("entre credit hours of course 6: "))
m=input("entre grade of course 6: ")
if(m=="A"):
    m=4*f
elif(m=="B+"):
    m=3.5*f
elif(m=="B"):
    m=3*f
elif(m=="C"):
    m=2*f
elif(m=="D"):
    m=1*f
elif(m=="F"):
    m=0*f
else:
    print("input is invalid: ")
g=int(input("entre credit hours of course 7: "))
n=input("entre grade of course 7: ")
if(n=="A"):
    n=4*g
elif(n=="B+"):
    n=3.5*g
elif(n=="B"):
    n=3*g
elif(n=="C"):
    n=2*g
elif(n=="D"):
    n=1*g
elif(n=="F"):
    n=0*g
else:
    print("input is invalid")
z=a+b+c+d+e+f+g
y=h+i+j+k+l+m+n
x=y/z
print(x)
    
