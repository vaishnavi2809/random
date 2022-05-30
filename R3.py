#Write a Python Program to pick a random character from a given String.
import random as r
a=input("Enter a String\n")
list=[]
for i in a:
    list.append(i)
print(r.choice(list))
