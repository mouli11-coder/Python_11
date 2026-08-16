'''#1(even or odd)

num=int(input("Enter Number:"))
if num%2==0:
  print("Number is even",num)
else:
  print("Number is odd",num)

#2(eligible to vote)
age=int(input("Enter Age:"))

if age>=18:
    print("Eligible")
else:
    print("Not Eligible")

#3(pass or fail)
mark=float(input("Enter mark:"))

if mark>=40:
    print("pass")
else:
    print("fail")

#4(pos or neg)
num=int(input("enter number:"))

if num>=0:
    print("Number is positive")
else:
    print("Number is negative")

#5(Grade)
mark=float(input("Enter Mark:"))

if mark>=90:
    print("grade A")
elif 75<=mark<=89:
    print("grade B")
elif 50<=mark<=74:
    print("grade C")
else:
    print("Fail")

#6(largest num)
a=int(input("Enter A:"))
b=int(input("Enter B:"))
c=int(input("Enter C:"))

if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("B is greater")
else:
    print("C is greater")

#7(day in week)
day=int(input("Enter Day:"))

if day==1:
    print("Mon")
elif day==2:
    print("Tue")
elif day==3:
    print("Wed")
elif day==4:
    print("Thu")
elif day==5:
    print("Fri")
elif day==6:
    print("Sat")
elif day==7:
    print("Sun")

#8(calculator)

a=int(input("Enter A:"))
b=int(input("Enter B:"))
oper=input("Enter operation(+,-,*,/):")

if oper=="+":
    print("Result:",a+b)
elif oper=="-":
    print("Result:",a-b)
elif oper=="*":
    print("Result:",a*b)
elif  oper=="/":
    print("Result:",a/b)
#9(user login)

username=str(input("Enter username:"))
password=int(input("Enter password:"))

if username=="admin":
    print("valid username")
    if password=="1234":
      print("valid password")
    else:
      print("Invalid password")
else:
    print("Invalid username")
#10(signal)

signal=str(input("Enter Signal:"))

if signal=="green":
    print("GO")
elif signal=="yellow":
    print("Get Ready")
else:
    print("Stop")'''

    

