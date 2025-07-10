print("Welcome to the General Knowledge quiz! ")

playing = input("Would you like to play? \n1. Yes 2. No: ") #askes the user for input in this case if they want to play the game or not

if playing != "1": #quits the program is answer is not yes(1)
    quit()
    
print("Let's Play :-)\nPoints are based on how difficult the question is")
score = 0 #Implements a scoring function so the user gets points for each correct answer

# QUESTION 1
answer = input("What is the planet called we live on: ")
if answer.lower() == "earth":  # answer.lower makes it so that the console ignores case sensitivity
    print("Correct! ")
    score += 1 # += is equivalent to score = score + 1
else:
    print("Incorrect, the correct answer is Earth")

# QUESTION 2
answer = input("What is the longest river in the world: ")
if answer.lower() == "nile":
    print("Correct! ")
    score += 1
else:
    print("Incorrect, the correct answer is the Nile river")

# QUESTION 3
answer = input("In what year did world war 1 start: ")
if answer == "1914":  # years are numbers, no need for .lower()
    print("Correct! ")
    score += 1
else:
    print("Incorrect, the correct answer is 1914")

# QUESTION 4
answer = input("In what year did world war 2 start: ")
if answer == "1939":  # years are numbers, no need for .lower()
    print("Correct! ")
    score += 1
else:
    print("Incorrect, the correct answer is 1939")

# QUESTION 5
answer = input("What is the capital of Japan: ")
if answer.lower() == "tokyo":
    print("Correct! ")
    score += 1
else:
    print("Incorrect, the correct answer is Tokyo")
    
# QUESTION 6
answer = input("What color do you get when you mix red and white? ")
if answer.lower() == "pink":
    print("Correct!")
    score += 1
else:
    print("Incorrect, the correct answer is pink.")
    
# QUESTION 7
answer = input("What is the chemical symbol for water? ")
if answer.lower() == "h2o":
    print("Correct!")
    score += 2
else:
    print("Incorrect, the correct answer is H2O.")

#QUESTION 8
answer = input("What is the name of the largest moon of Saturn? ")
if answer.lower() == "titan":
    print("Correct!")
    score += 5
else:
    print("Incorrect, the correct answer is Titan.")


    
print("You got a score of: " + str(score) + " :)" ) # score is converted to a string since python can't add numbers and strings(words/letters) directly
print("You got " + str((score/13) * 100) + "% )" ) # shows how much % you got