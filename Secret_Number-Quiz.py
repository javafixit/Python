#secret number
import random
print("Enter your name")
name = input()
print ("Welcome ",name);
secretNumber = random.randint(1,20)
print("Well Mr.",name," Lets play the game")
x = False
for i in range(1,5):
    print("Enter the number")
    numberEntered = input()
    if(int(secretNumber) == int(numberEntered)):
        print("Exceptional Mr.",name,"!!!!!!! you guessed it right!")
        x = True
        break;
    elif (int(secretNumber) < int(numberEntered)):
        print ("Secret number is less than your guess")
    elif (int(secretNumber) > int(numberEntered)):
        print ("Secret number is greater than your guess")

if(not x):
    print ("Sorry all chances expired, the number was ",secretNumber)