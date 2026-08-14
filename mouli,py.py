

'''
#1

a=int(input("Enter the value of A:"))
b=int(input("Enter the value of B:"))

print("sum=",a+b)
print("sub=",a-b)
print("multi=",a*b)
print("divid=",a/b)
print("Modu=",a%b)
print("Flor=",a//b)
print("Exp=",a**a)

#2Rectangle
l=float(input("Enter length="))
w=float(input("Enter width="))

area=l*w
perimeter=2*(l+w)

print("rect area=",area)
print("rect perimeter=",perimeter)

#Square
s= float(input("Enter sqaure side:"))

area= s*s
perimeter= 4*s

print("Square area=",area)
print("Square perimeter=",perimeter)


import math

#Circle
r=float(input("Enter radius:"))

area=math.pi*r*r
perimeter=2*math.pi*r

print("Cicle area=",area)
print("Circle perimeter=",perimeter)

#3Average
a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))

average= (a+b+c)/3

print("Average=",average)

#4comparision
a=int(input("Enter A:"))
b=int(input("Enter B:"))

print("Equal:", a==b)
print("A is greater than B:",a>b)
print("A is less than or equal than B:",a<=b)

#5Square root

import math

no=float(input("Enter the Number:"))

sqrt=math.sqrt(no)

print("Sq root:",sqrt)

#6(simple interest and compund interest)

p=float(input("Enter principal amount:"))
r=float(input("Enter rate of interest:"))
t=float(input("Enter time:"))
print("Simple interest:",p*r*t/100)
print("compund interest:",p*(1+r/100)**t-p)        


#7Assignment operator 

x=5

x+=3
x*=2

print(x)

#8swapping

a=10
b=20

a=a+b
b=a-b
a=a-b

print("a=",a)
print("b=",b)

#9logical operator
username=input("Enter username:")
password=input("Enter password:")

if username=="admin" and password=="1234":
      print("Login successful")
else:
    print("Invalid username or password")

#10CUBE ROOT

num= float(input("Enter a number:"))

cube_root=num**(1/3)

print("Cube Root:",cube_root)'''

      















