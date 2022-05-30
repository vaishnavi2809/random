#Write a python Program to make rock-paper-scissor game.
import random as r
a=["rock","paper","scissor"]
b=["rock","paper","scissor"]
x=input("Enter rock/scissor/paper:\n")
y=r.choice(b)
if (x=="rock" and y=="paper") or (x=="paper" and y=="rock"):
	print("paper wins!!!")
elif (x=="scissor" and y=="rock") or (x=="rock" and y=="scissor"):
	print("rock wins!!!")
elif (x=="paper" and y=="scissor") or (x=="scissor" and y=="paper"):
	print("scissor wins!!!")
elif (x=="paper" and y=="paper") or (x=="paper" and y=="paper"):
	print("match draw!!!")
elif (x=="rock" and y=="rock") or (x=="rock" and y=="rock"):
	print("match draw!!!")
elif (x=="scissor" and y=="scissor") or (x=="scissor" and y=="scissor"):
	print("match draw!!!")
else:
	pass
