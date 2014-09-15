__author__ = 'Ciddhi'

import random
from gestures import *


# Class to define a player who chooses Rock / Paper / Scissor randomly
class Player:

    def play(self):
        nIndex = random.randint(1, 3)
        if nIndex == 1:
            return Rock()
        if nIndex == 2:
            return Scissor()
        if nIndex == 3:
            return Paper()


# Class to define a human player
class HumanPlayer(Player):

    # function asks for user input till a valid one is provided, and returns gesture accordingly
    def play(self):
        strHumanPlayerType = input('Enter your choice (Rock or Paper or Scissor) : ')
        strHumanPlayerType = strHumanPlayerType.lower()

        # to check validity of input
        while strHumanPlayerType != 'rock' and strHumanPlayerType != 'scissor' and strHumanPlayerType != 'paper':
            strHumanPlayerType = input('That choice is not valid. Enter your choice (Rock or Paper or Scissor) : ')
            strHumanPlayerType = strHumanPlayerType.lower()

        # return gesture depending upon user choice
        if strHumanPlayerType == 'rock':
            return Rock()
        if strHumanPlayerType == 'scissor':
            return Scissor()
        if strHumanPlayerType == 'paper':
            return Paper()


# Main flow of the game
if __name__ == "__main__":

    objComputerPlayer = Player()
    objHumanPlayer = HumanPlayer()
    nTie = 0
    nCompWon = 0
    nHumanWon = 0
    strContinue = 'y'

    # Continue till user specifically enters 'N' / 'n'
    while strContinue != 'n':

        # Get a gesture from computer player and human player
        objHumanPlayerChoice = objHumanPlayer.play()
        objComputerPlayerChoice = objComputerPlayer.play()
        print('You selected : ' + str(objHumanPlayerChoice))
        print('Computer selected : ' + str(objComputerPlayerChoice))

        # compare the gestures and update scores
        if objHumanPlayerChoice > objComputerPlayerChoice:
            print('You won.')
            nHumanWon += 1
        elif objHumanPlayerChoice == objComputerPlayerChoice:
            print('Game tied.')
            nTie += 1
        else:
            print('Computer won.')
            nCompWon += 1

        print('Scores till now are :\nNumber of Games : ' + str(nHumanWon+nCompWon+nTie) + '\nYou won : ' + str(nHumanWon) + '\nComputer won : ' + str(nCompWon) + '\nGames tied : ' + str(nTie))

        # ask for user input if he/she wants to continue the game
        strContinue = input('Enter N to quit the game or any other letter to continue : ')
        strContinue = strContinue.lower()

    print('Final Scores are :\nTotal Number of Games : ' + str(nHumanWon+nCompWon+nTie) + '\nYou won : ' + str(nHumanWon) + '\nComputer won : ' + str(nCompWon) + '\nGames tied : ' + str(nTie))