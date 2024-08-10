#Purpose: Depicts if statements determining cost based off age.
#Edited version: Practice with if-else
#3-Alternative Decision
#Date: 1/25/17       #Reviewed on 1/30/17
#Programmer: Naylene Rondon
#FileName: amusment_park_NayleneRondon.py

#Start
print("Let's determine your admission cost based off your age.")

#Establishing Variable through Input
age = int(input("What is your age: "))

#Decision
if age < 4:
    print("Your admission cost is $0.") #Output if child is under 4.
else:
    if age < 18:
        print("Your admission cost is $5.") #Output if it's a child older than 4.
    else:
        print("Your admission cost is $10.") #Output if they're an adult.

#End
