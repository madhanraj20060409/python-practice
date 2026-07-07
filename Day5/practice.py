#Create a Function to Print Your Name
def my_func():
    print("madhan raj")
my_func()

#Create a Function to Add Two Numbers
def add(a,b):
    return a+b
B=int(input("enter number A:"))
A=int(input("enter number B:"))
print(add(A,B))

#Create a Function to Find the Square of a Number
def square(num):
    return num*num
num=int(input("enter the number:"))
print(square(num))

#Create a Function to Check Whether a Number is Even or Odd
def even_odd(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
num=int(input("enter the number:"))
print(even_odd(num))

#Create a Function to Find the Maximum of Two Numbers
def max(a,b):
    if a>b :
        return "A is max"
    else:
        return "B is max"
A=int(input())
B=int(input())
print(max(A,B))

#Find the Factorial Using a Function
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact
n=int(input("enter the number:"))
print(factorial(n))

#Check Whether a Number is Prime Using a Function
def is_prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num % i==0:
            return False
    return True
numbers=int(input("enter the number:"))
if is_prime(numbers):
    print("it prime")
else:
    print("it not prime")

#Find the Sum of Digits Using a Function
def sum_of_digits(num):
    total=0
    while num>0:
        digit=num%10
        total+=digit
        num=num//10
    return total
numbers=int(input("enter the numbers:"))
print(sum_of_digits(numbers))
