# Program to play Quiz
print("Welcome to my Computer Quiz")
playing=input("Do you want to Play? ")

# We make use of .lower() fuction to lower the string 
# otherwise program would have differ yes/Yes/YEs/YES 
if playing.lower()!= "yes":
    quit()

print("Okay! Let's play :) ")
score=0
ans=input("What does CPU stand for? ")
if ans.lower()=="central processing unit":
    print('Correct!')
    score+=1
else: print("OOPS! your answer is wrong.")

ans=input("What does GPU stand for? ")
if ans.lower()=="grahics processing unit":
    print('Correct!')
    score+=1
else: print("OOPS! your answer is wrong.")

# both .lower() fuction same 
ans=input("What does RAM stand for? ").lower()
if ans=="random access memory":
    print('Correct!')
    score+=1
else: print("OOPS! your answer is wrong.")

ans=input("What does ROM stand for? ").lower()
if ans=="read only memory":
    print('Correct!')
    score+=1
else: print("OOPS! your answer is wrong.")

print("You got"+ str(score) +"correct answers!")

