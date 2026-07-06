#Find the length of a tuple.
num=(1,2,3,4,5,4,5,6,4,5,4,4,4,4)
print("count:",len(num))

#Count Occurrences of an Element
num=(1,2,3,4,5,4,5,6,4,5,4,4,4,4)
n=int(input("enter the numbers:"))
print("occurrence:",num.count(n))

#Find the Index of an Element
num=(1,2,3,4,5,4,5,6,4,5,4,4,4,4)
n=int(input("enter the number:"))
if n in num:
        print("index value:", num.index(n))

#Reverse a Tuple
num=(1,2,3,4,5,4,5,6,4,5,4,4,4,4)
print(num[::-1])

#Remove Duplicates from a List
num=[1,2,3,4,5,4,5,6,4,5,4,4,4,4]
print("value:",list(set(num)))

#union 
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)

#intersection
A = {1, 2, 3}
B = {3, 4, 5}
print(A & B)

#difference
A = {1, 2, 3}
B = {3, 4, 5}
print(A - B)

#symmatic_difference
A = {1, 2, 3}
B = {3, 4, 5}
print(A ^ B)

#update value in dictionary
student = {
    "name": "Madhan",
    "age": 21
}
student["age"]=23
print(student)

#Find the Character with the Highest Frequency
string=input("enter the string:")
frequency={}
for char in string:
    if char in frequency:
        frequency[char]+=1
    else:
        frequency[char]=1

highest=max(frequency,key=frequency.get)
print("highest frequency:",highest)
print("frequency:",frequency[highest])