# TASK 4 (LOOP)
'''
#1( 1 to 10)

for i in range(1,11):
    print(i,end="")                

#2(10 to 1)

for i in range(10,0,-1):
    print(i,end="")

#3(Even numbers)

for i in range(1,51):
    if i%2==0:
        print(i)

#4(odd numbers)

for i in range(1,50):
    if i%2!=0:
        print(i)

#5(mutli of 5)
t=int(input("Enter Number:"))
for i in range(1,11):
      print(i,'*',t,'=', t*i)

#6(sum of 100)
sum = 0
for i in range(1, 101):
    sum += i
print(sum)

#7(square number 1 to 10)
for i in range(1,11):
print(i*i)

#8(string)
string="PYTHON"
for i in string:
    print(i,end="  ")

# INTERMEDIATE TASKS

#9(count string)
text = input("Enter a string: ")

count = 0

for ch in text:
    if ch in "aeiouAEIOU":
        count += 1

    print("Number of vowels:", count)

#10(sum of even upto 100)
count=0
for i in range(1,101):
    if i%2==0:
        count+=1
print("sum of even:",count)

#11(factorial)
n=int(input("Enter Number:"))

f=1
for i in range(1,n+1):
    f=f*i
print("Factorial:",f)

#12(number is prime or )

n = int(input("Enter a number: "))

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")

#13(prime number upto 100) is nested loop

for n in range(2, 101):
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    if count == 2:
        print(n,"is Prime number")

#14(larg num in list)

nums = [10, 45, 23,89,12, 67]

largest = nums[0]

for num in nums:
    if num > largest:
        largest = num

print("Largest number:", largest)

#15(count pos and neg in list)

nums = [10, -5, 20, -8, 15, -2, 30]

positive = 0
negative = 0

for num in nums:
    if num > 0:
        positive += 1
    else:
        negative += 1

print("Positive numbers:", positive)
print("Negative numbers:", negative)

#16(Reverse string)

text = "PYTHON"

reverse = ""

for le in text:
    reverse = le + reverse

print("Reversed string:", reverse)

#17(character appears)
text = input("Enter a string: ")
char = input("Enter a character: ")

count = 0

for ch in text:
    if ch == char:
        count += 1

print("Character appears", count, "times")'''





