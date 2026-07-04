import sys 
print(sys.version)

a=10
print(type(a))

#Easy

#Print your name.
print("Madhan raj")

#Print your college name.
print("Dhirajlal gandhi College of technology")

#Store your age in a variable.
age=20
print("my age is", age)

#Print your favorite programming language.
print("my favorite programming language is python")

#Print two numbers.
a=5
b=10
print("printing two numbers",a,b)

#Medium

#Calculate the sum of two numbers entered by the user.
num1=int(input("Enter the number 1:",))
num2=int(input("Enter the number 2:",))
print(sum([num1,num2]))

#Swap two numbers using a temporary variable.
temp=num1
num1=num2
num2=temp 
print("After swapping the numbers are:",num1,num2)

#Convert Celsius to Fahrenheit.
celsius=float(input("Enter the temperature in Celsius:",))
fahrenheit=((celsius*9/5)+32)
print("temperature in Fahrenheit is:",fahrenheit)

#Find the area of a rectangle.
length=float(input("Enter the length of rectangle:",))
width=float(input("Enter the width of rectangle:",))
area=length*width
print("Area of the rectangle is:",area)

#Display complete student details using input.
name=input("Enter your name:",)
age=int(input("Enter your age:",))
college=input("Enter your college name:",)  
print("Student Details:")
print("Name:", name)
print("Age:", age)
print("College:",college)

#arthimetic operations
a =int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)

#odd or ever
n=int(input("Enter a number: "))
if n%2==0:
    print(n,"is an even number")
else:
    print(n,"is an odd number")

#nest if
age=int(input("Enter your age: "))
license =input("Do you have a driving license? (yes/no): ")

if age >= 18:
    if license.lower()== "yes":
        print("You are eligible to drive.")
    else:
        print("You need a driving license to drive.")
else:
    print("You are not eligible to drive.")

#Check whether a number is positive or negative.
num=int(input("Enter a number: "))
if num>0:
    print(num,"is a positive number")
else:
    print(num,"is a negative number")

#Find the largest of two numbers.
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
if a>b:
    print(a,"is the largest number")
else:
    print(b,"is the largest number")

#Find the largest of three numbers.
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
if a>b and a>c:
    print(a,"is the largest number")
elif b>a and b>c:
    print(b,"is the largest number")
else:
    print(c,"is the largest number")

#Check whether a year is a leap year.
year=int(input("Enter a year: "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")

#Check whether a character is a vowel or consonant
char=input("Enter a character: ")
if char.lower() in ['a','e','i','o','u']:
    print(char,"is a vowel")
else:
    print(char,"is a consonant")

#Build a simple calculator using if-elif.
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice=input("Enter choice(1/2/3/4): ")
if choice=='1':
    print(num1,"+",num2,"=",num1+num2)
elif choice=='2':
    print(num1,"-",num2,"=",num1-num2)
elif choice=='3':
    print(num1,"*",num2,"=",num1*num2)
elif choice=='4':
    if num2!=0:
        print(num1,"/",num2,"=",num1/num2)
    else:
            print("Error: Division by zero")
else:
    print("Invalid input")

#loop
name = input("Enter your name: ")

for i in range(10):
    print(name)

#sum of 10 numbers
total=0
for i in range(10):
    num=int(input("Enter a number: "))
    total+=num
print("The sum of the first 10 numbers is:", total)

for i in range(3):
    for j in range(3):
        print(i,j)

#pattern printing
for i in range(10):
    for j in range(4):
        print("#", end="")
    print()


for i in range(1,11):
    for j in range(1,i+1):  
        print(j,end="")
    print()

#tables
n=int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    print(n, "x", i, "=", n*i)

#factorial
n=int(input("Enter a number to find its factorial: "))
fact=1
for i in range(1,n+1):
    fact*=i
print("The factorial of", n, "is:", fact)

#count digits
num = int(input("Enter a number: "))
count = 0

while num > 0:
    count += 1
    num //= 10

print("Digits =", count)

#Reverse counting from 20 to 1.
for i in range(20, 0, -1):
    print(i)

#Reverse a number.
num=int(input("Enter a number: "))
reverse=0
while num>0:
    digit=num%10
    reverse=(reverse*10)+digit
    num//=10
print("The reverse of the number is:", reverse)

#palindrome number
num=int(input("Enter a number: "))
ogvalue=num
reverse=0
while num>0:
    digit=num%10
    reverse=(reverse*10)+digit
    num//=10
if ogvalue==reverse:
    print(ogvalue,"is a palindrome number")
else:
    print(ogvalue,"is not a palindrome number")

#fabonacci series
n=int(input("Enter the number of terms in the Fibonacci series: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
