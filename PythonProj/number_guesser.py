import random

Max_Number = input("Please enter a number: ")

if Max_Number.isdigit():
    Max_Number = int(Max_Number)
    if Max_Number <= 0:
        print("please enter the corrrect number")
        quit()
else:
    print("please enter a number next time") 
    quit()

ran_num = random.randrange(0, Max_Number)

print("Random number is: " + str(ran_num))
