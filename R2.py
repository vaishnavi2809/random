# Write a Python program to generate a random number for console random number game.

import random as r
a=r.randint(1,10)
t=1
while True:
    b=int(input("Enter the no"))
    if a==b:
        break
    elif b<a:
        print("Enter no . greater than previous no")
        t=t+1
    elif b>a:
        print("Enter no . less than perivious no.")
        t=t+1
    else:
        pass
print(f'You won by commiting {t} time') 
