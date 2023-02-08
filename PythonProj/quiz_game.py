print("Welcome to my first python quiz!")

playing = input("Do you want to play game? ")

if playing.lower() != "yes":
    quit()
    
print("Welcome to the game! Let's Play :") 
score = 0
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer!")
    score = score - 1
    
answer = input("What does GPU stand for? ")
if answer.lower() == "graphic processing unit":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer!")
    score = score - 1
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer!")
    score = score - 1
    
print("Your score is: " + str((score)/3 * 100) + "%.")
    
    
