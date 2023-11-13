print("Welcome TO Quiz Game")
play=input("Do You Want To Play? ")

if play.lower() !="yes":
    quit()
print("Let'ssss play !!")

score=0

#Quiz start
#1.
answer=input("Group of program written and arranged in an order to achive  multiple task is called?")
if answer.lower() =="software":
    print("correct!")
    score+=1

    
else:
    print("Wrong!!")

#2.
answer=input("Which of the following are not a python Data type? ")
if answer.lower() =="variable":
    print("correct!")
    score+=1
else:
    print("Wrong!!")

#3.
answer=input("What is called core of the operating system? ")
if answer.lower() =="kernal":
    print("correct!")
    score+=1
else:
    print("Wrong!!")

#4.
answer=input("Python file extension is? ")
if answer.lower() ==".py":
    print("correct!")
    score+=1
else:
    print("Wrong!!")

#5.
answer=input("Predefined words which are its  meaning is called? ")
if answer.lower() =="keywords":
    print("correct!")
    score+=1
else:
    print("Wrong!!")

#6.
answer=input("How many types of keywords contains in Python? ")
if answer.lower() =="35":
    print("correct!")
    score+=1
else:
    print("Wrong!!")


print("you got "+ str(score)+ " Questions correct")
print("you got "+ str((score/6)*100) +" %.")




