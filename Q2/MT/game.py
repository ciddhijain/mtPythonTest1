__author__ = 'Ciddhi'

import random
from gestures import *

class Player:

    def play(self):
        nIndex = random.randint(1, 3)
        if nIndex == 1:
            return Rock()
        if nIndex == 2:
            return Scissor()
        if nIndex == 3:
            return Paper()


class HumanPlayer(Player):

    def play(self):
        strHumanPlayerType = input('Enter your choice (Rock or Paper or Scissor) : ')
        strHumanPlayerType = strHumanPlayerType.lower()
        while strHumanPlayerType != 'rock' and strHumanPlayerType != 'scissor' and strHumanPlayerType != 'paper':
            strHumanPlayerType = input('That choice is not valid. Enter your choice (Rock or Paper or Scissor) : ')
            strHumanPlayerType = strHumanPlayerType.lower()
        if strHumanPlayerType == 'rock':
            return Rock()
        if strHumanPlayerType == 'scissor':
            return Scissor()
        if strHumanPlayerType == 'paper':
            return Paper()



if __name__ == "__main__":
    objComputerPlayer = Player()
    objHumanPlayer = HumanPlayer()
    nTie = 0
    nCompWon = 0
    nHumanWon = 0
    strContinue = 'y'
    while strContinue != 'n':
        objComputerPlayerChoice = objComputerPlayer.play()
        objHumanPlayerChoice = objHumanPlayer.play()
        if objHumanPlayerChoice > objComputerPlayerChoice:
            print('You won.')
            nHumanWon += 1
        elif objHumanPlayerChoice == objComputerPlayerChoice:
            print('Game tied.')
            nTie += 1
        else:
            print('Computer won.')
            nCompWon += 1
        strContinue = input('Enter N to quit the game or any other letter to continue : ')
        strContinue = strContinue.lower()
    print('Final Scores are :\nTotal Number of Games : ' + str(nHumanWon+nCompWon+nTie) + '\nYou won : ' + str(nHumanWon) + '\nComputer won : ' + str(nCompWon) + '\nGames tied : ' + str(nTie))