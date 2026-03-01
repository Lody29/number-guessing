#a simple guessing game: Computer logic:
# think : The computer gets to picka  number 
# the user has to guess th number.
#computer generate a number from 1-100
#user select diffficulty
#If guess is correct congratulations
#if guess is wrong ooof!! try again later
#tell user number is greater or lesser than guess
# if guess is lesse r bye bye if corect number  is guessed bye bye
#finished .. 

import random

Computer_choice = random.randint(1,100)
print("""welcome to the ultimate guessing game .._____..                               
      Do you have what it takes to be our champion ?                           
      Then guess a number And challenge the almighty pc! If you dare!!""")    #Fun game challenge
difficulty = input("What difficulty would you want.:" \
" hard = 6" \
"medium = 4" \
"easy=3.""")
guesses = 6

if difficulty.lower() == "hard":
    print("""Your guessses have been reduced to 3.""")

    guesses = 3
elif difficulty.lower() == "medium":
    print("Your guesses have been reduced to 4. Medium level selected:")
    guesses = 4
elif difficulty.lower() == "easy" :
    print("Your guesses are 6. Goodluck.")
else:
    print("Invalid difficulty")


while guesses > 0:
    User_choice = int(input("What is your number bruhver"))
    if User_choice == Computer_choice:
       print(""" You have guessed the computers number
             Congratulation Warrior !! 50xp granted""")
       break
    else:
        print("""You have failed to correctly guess the computer's number : -1 guess""")
        guesses = guesses- 1
        if Computer_choice > User_choice:
            print("The number you seek is greater than the one you have")
        else:
            print("The number you seek is smaller than the one you have.")
    if guesses == 0:
        print(f"game over: You loose . The number you seek was{Computer_choice}")