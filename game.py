import numpy as np
c=["rock","paper","scissor"]
computer=np.random.choice(c)
print("Enter rock/paper/scissor : ")
user=input()
if(user=="paper" and computer=="scissor"):
    print("Computer won")
elif(user=="paper" and computer=="rock"):
    print("User won")
elif(user=="scissor" and computer=="paper"):
    print("User won")        
elif(user=="scissor" and computer=="rock"):
    print("Computer won")
elif(user=="rock" and computer=="paper"):
    print("Computer won")
elif(user=="rock" and computer=="scissor"):
    print("User won")
elif(user==computer):
    print("TIE! Retry")
print("Computer : ",computer)
print("User : ",user)
