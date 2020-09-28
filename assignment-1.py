#!/usr/bin/env python
# coding: utf-8

# 1.
def newString(s1, s2):
  s2 = s2[::-1]
  l1 = len(s1) 
  l2 = len(s2)
  length  = l1 if l1 > l2 else l2
  newString=" "
  for i in range(length):
    if(i < l1):
      newString = newString + s1[i]
    if(i < l2):
      newString = newString +''.join(reversed(s2[i]))
    
  print(newString)
  
s1 = "Abc"
s2 = "Xyz"
newString(s1, s2)


# 2.
string1 = input("enter the string :")
string2 = "USA"
temp = string1.lower()
result = temp.count(string2.lower())
print("Substring USA count is:", result)


# 3
def midThreeChar():
    
    string = input("enter the string :")
    midIndex = int(len(string) /2)
    midThree = string[midIndex-1:midIndex+2]# On applying slising to extract middle 3 letters.
    print(midThree)
  
midThreeChar()
midThreeChar()


# 4
i=5
for m in range(0,i,2):
    print()
    for n in range(0,m+1):
        print("* ",end=" " )
    print()
for m in range(i-1,0,-2):
    print()
    for n in range(0,m-1):
        print("* ",end=" " )
    print()


# 5
number = int(input("enter the number"))
for n in range(1,11) :
    print(number*n)
    


# 6:
list1=[10,20,30,40,50]
for i in list1[::-1]:  #list[start:stop:step]
    print(i)


# 7
print("enter the numpber ")
num=int(input())
result=num

if (num==0):
    print("1")
else :
    temp=1
    while(num>0):
        temp=temp*num
        num=num-1
    
print("The ",result,"! is",temp)
        


#8
def convertArrToList(item):
    return float(item)

n=int(input("enter the number of values"))
arry=[]
i=0
while(i<n):
    item=input()
    arry.insert(i,item)
    i=i+1
result =list(map(convertArrToList,arry))
print(result)




#9
import random
import string

# get random string password with letters, digits, and symbols
def get_random_password_string(length):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters)for i in range(length))
    print('The randm password generated is ;',password)
    
size = int(input("enter the length of the password "))
get_random_password_string(size)









