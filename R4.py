#Write a Python program to make a Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
import random as r
list=[]
for i in range(100):
    list.append(r.randint(1000000000,9999999999))
w=r.sample(list,2)
print("Lotter Tickets are",w)
