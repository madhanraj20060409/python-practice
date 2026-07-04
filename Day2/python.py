#prime numbers
num=int(input("Enter a number: "))
if num<2:
    print(num,"is not a prime number")
else:
    for i in range(2,num):
        if num%i==0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")

#armstrong numbers for three digits 
num=int(input("Enter a three-digit number: "))
original_num=num
total=0
while num>0:
    digit=num%10
    total+=digit**3
    num//=10
if original_num==total:
    print(original_num,"is an Armstrong number")
else:
    print(original_num,"is not an Armstrong number")

#armstrong number for n numbers digits
num=int(input("enter the number:"))
count=len(str(num))
originalvalue=num
total=0
while num>0:
    digit=num%10
    total=total+digit**count
    num//=10
if originalvalue==total:
    print("this armstrong number")
else:
    print("not armstrong number")
    
#string traversal
str=input("Enter a string: ")
for char in range(len(str)):
    print(char,str[char])

#Print every character of a string.
string=input("Enter a string: ")
for char in string:
    print(char)

#Count the number of characters using len().
string=input("Enter a string: ")
for char in range(len(string)):
    print(char, string[char])

#Reverse a string.
string=input("Enter a string: ")
reverse_string=string[::-1]
print("Reversed string:", reverse_string)

#Convert lowercase to uppercase.
string=input("Enter a string: ")
print("Uppercase string:", string.upper())

#Convert uppercase to lowercase.
string=input("Enter a string: ")
print("Lowercase string:", string.lower())

#Count vowels.
string=input("Enter a string: ")
count=0
for char in string:
    if char.lower() in ['a','e','i','o','u']:
        count+=1
print("Number of vowels:", count)

#Count consonants.
string=input("Enter a string: ")
count=0
for char in string:
    if char.isalpha() and char.lower() not in ['a','e','i','o','u']:
        count+=1
print("Number of consonants:", count)

#Check whether a string is a palindrome.
string=input("Enter a string: ")
string=string.lower()
if string==string[::-1]:
    print(string,"is a palindrome")
else:
    print(string,"is not a palindrome")

#Count words in a sentence.
string = input("Enter a sentence: ")
words = string.split()
word_count = len(words)
print("Number of words in the sentence:", word_count,words)

#Remove spaces from a string.(btw two words)
string=input("Enter a string: ")
string_without_spaces=string.replace(" ","")
print("String without spaces:", string_without_spaces)

#remove spaces from a string.behind and beyond the string
string=input("Enter a string: ")
string_output=string.strip()
print("String after removing spaces:", string_output)

#Count uppercase and lowercase letters
string=input("Enter a string: ")
upper_case=0
lower_case=0
for char in string:
    if char.isupper():
        upper_case+=1
    elif char.islower():
        lower_case+=1
    else:
        print("Invalid character found:", char)
print("Number of uppercase letters:", upper_case)
print("Number of lowercase letters:", lower_case)

#find occurance of the string 
string=input("Enter a string: ")
substring=input("Enter a substring to find its occurrence: ")
index=string.find(substring)
if index!=-1:
    print("The substring",substring,"is found at index",index)
else:
    print("The substring",substring,"is not found in the string")

