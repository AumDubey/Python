# A simple quiz games that involves answering questions then receiving your score at the end
# Feature: Loops, I/O

print("Welcome to the quiz game")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's get started :)")
score = 0

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print('Correct! ')
    score += 1
else:
    print('Incorrect! ')
    
answer = input("What does GPU stand for? ")

if answer.lower() == "graphics processing unit":
    print('Correct! ')
    score += 1
else:
    print('Incorrect! ')
    
answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
    print('Correct! ')
    score += 1
else:
    print('Incorrect! ')
    
answer = input("What does PSU stand for? ")

if answer.lower() == "power supply unit":
    print('Correct! ')
    score += 1
else:
    print('Incorrect! ')
    
print("You got " + str(score) + " questions correct! ")

if score <= 3:
    print("Only " + str(score) + " correct? Ya Moron! - Aum")
else:
    print("You're still dumb but good job! - Aum")
