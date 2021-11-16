'''
name: Naser Al Madi
file: .py
data: 9/22/2020
course: CS151 fall
description: 
'''
from connect4game import Connect4Game

def main():
    ''' the main function where the game events take place '''

    game = Connect4Game()
    game.gameLoop()

    
if __name__ == "__main__":
	main()

