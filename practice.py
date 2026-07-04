#find element in list
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

#concatanation two list
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

#funtion to sort by abs value
def myfunc(n):
  return abs(n - 50)
list = [100, 50, 65, 82, 23]
list.sort(key = myfunc)
print(list)

#descending order sorting
list = [100, 50, 65, 82, 23]
list.sort(reverse = True)
print(list)

#largest number in list 
numbers=[10,45,8,99,21] 
largest=numbers[0] 
for num in numbers: 
    if num>largest: 
        largest=num
print(largest)

#reverse the list without reverse()
numbers = [1, 2, 3, 4]
reverse = []
for i in range(len(numbers) - 1, -1, -1):
    reverse.append(numbers[i])
print(reverse)

#find smallest value in list
numbers=[10,45,8,99]
smallest=numbers[0]
for num in numbers:
    if num<smallest:
        smallest=num
print(smallest)

#sumof list
numbers=[10,20,30]
total=0
for num in numbers:
    total+=num
print(total)

#count even in list
numbers=[10,11,12,15,18]
count=0
for num in numbers:
    if num%2==0:
        count+=1
print(count)

#remove duplicate
numbers = [1, 2, 2, 3, 4, 4, 5]
result = []
for num in numbers:
    if num not in result:
        result.append(num)
print(result)

#find second largest value in list
numbers = [12, 45, 6, 89, 34]
largest = second = float("-inf")
for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif largest > num > second:
        second = num
print(second)

#find second smallest value in list
numbers = [12, 45, 6, 89, 34]
largest = second = float("inf")
for num in numbers:
    if num < largest:
        second = largest
        largest = num
    elif largest < num <second:
        second = num
print(second)

#check wheather value in list or not
numbers = [10, 20, 30, 40]
element = int(input())
found = False
for num in numbers:
    if num == element:
        found = True
        break
if found:
    print("Found")
else:
    print("Not Found")

#find number frequency in list
numbers = [1, 2, 2, 3, 3, 3]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
print(frequency)

#find common value in list
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
num1=[]
for num in list1:
    if num in list2:
        num1.append(num)
print(num1)

#count even and odd value in list
numbers = [1, 2, 3, 4, 5, 6]
even = []
odd = []
even_count=0
odd_count=0
for num in numbers:
    if num % 2 == 0:
        even.append(num)
        even_count+=1
    else:
        odd.append(num)
        odd_count+=1
print("Even =", even)
print("count=",even_count)
print("Odd =", odd)
print("count=",odd_count)

#Traversing Nested Lists
students = [
    ["Madhan", 90],
    ["Rahul", 85],
    ["Priya", 95]
]
for student in students:
    print(student)

#nested list
students = [
    ["Madhan", 90],
    ["Rahul", 85],
    ["Priya", 95]
]
for row in students:
    for item in row:
        print(item, end=" ")
    print()

#List of User Inputs
numbers = []
n = int(input("How many numbers? "))
for i in range(n):
    value = int(input("enter number:"))
    numbers.append(value)
print(numbers)
