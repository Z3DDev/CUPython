#Zach Jagoda
#Student ID: 2274813
#Student Email: jagod101@mail.chapman.edu
#CPSC230
#Assignment 4 - Pig

#The game of Pig is a simple two-player dice game in which the first player to reach 100 or more points wins.  Players take turns.  On each turn a player rolls a six-sided die.  After each roll:
#a) If the player rolls a 1 then the player gets no new points and it becomes the other player’s turn.
#b) If the player rolls 2-6 then they can either roll again or hold.  If the player holds the sum of all rolls is added to his/her score and the turn passes to the other player.
#Write a program that plays the game of Pig where one player is human and the other is the computer.  When it is the human’s turn the program should show the score of both players and the previous roll.
#Allow the human to input “r” for roll again and “h” for hold.  (Hint: use the input function).
#When it is the computer’s turn you need not do any prompting.  Simply keep rolling until the computer has earned 20 or more points and then hold.
#If the computer rolls a 1 at any time, then the turn is lost and no points are added to the score.  If at any point the computer has enough points to win the game, then the computer holds and the game ends.
#Allow the human player to roll first.  A random roll can be simulated with a call to random.randint(1,6) which generates a uniform random number in [1,6].  Make sure to import the random module (ie. import random).

import random

playerSum = 0
playerTotalSum = 0
computerSum = 0
compTotalSum = 0

playerTurn = True
rollDice = True

dice = 0
previousRoll = 0

winCondition = 100

playerChoice = ""

while playerSum < winCondition || computerSum < winCondition:
    if playerTurn == True:
        while rollDice:
            playerChoice = input("Will you Roll (r) or Hold (h)? ")
            if playerChoice = "r":
                dice = random.randit(1, 6)

                if dice = 1:
                    rollDice = False
                    break
                else:
                    playerSum = playerSum + dice
                    continue
            elif:
                rollDice = False
                playerTotalSum = playerSum
                break
            else:
                print("Please Enter a Valid Option")
                continue
    else:
        while rollDice:
            if computerSum < 20:
                dice = random.randit(1, 6)
                if dice = 1:
                    rollDice = False
                    break
                else:
                    computerSum = computerSum + dice
                    continue
            else:
                compTotalSum = computerSum
                
if playerTotalSum = 100:
    print("Congratulations, you won!")
elif compTotalSum = 100:
    print("AI is the future, prepare to be terminated")
