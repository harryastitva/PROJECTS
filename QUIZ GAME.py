print("WELCOME TO MY COMPUTER QUIZ!!!")

playing= input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay! lets play:)")
score=0

answer = input("CPU stands for? ")
if answer.lower() == "central processing unit":
    print ("CORRECT!")
    score +=1
else:
    print("INCORRECT! ")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("CORRECT!")
    score +=1
else:
    print("INCORRECT!")

answer = input("RAM stands for? ")
if answer.lower() == "random access memory":
    print ("CORRECT!")
    score +=1
else:
    print("INCORRECT! ")

answer = input("ROM stands for? ")
if answer.lower() == "read only memory":
    print ("CORRECT!")
    score +=1
else:
    print("INCORRECT! ")


print("YOU GOT " + str(score) + " question correct!! ")

print("YOU GOT " + str((score/4) * 100) + "%.")
