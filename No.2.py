# Program of number Guessing
import random
print("Welcome! Try Number Guessing game")
n=(input("Enter Highest Number: "))

if n.isdigit():
    n=int(n)
    if n<=0:
        print("Please type a number larger than 0")
        quit()
else:
     print("Please enter number next time")
     quit()

r=random.randint(0,n)
#here we could have  also used random.randrange()
c=0
while True:#to make operation in loop without complications
    c+=1
    a=input("Enter your guess number: ")
    if a.isdigit():
        a=int(a)
    else:
     print("Please enter number next time")
     continue
    
    if a==r:
        print("You Got it!")
        break 
    elif a>r:
        print("too high")
    else:
        print("too low")
print("Amount of guesses is "+ str(c))

