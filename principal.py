import sys
from map import Map
from engine import Engine
from people import *

#This func main wheel the game and put him in a loop, besides instantiates the required objects in the game

def main():
    print('\n----------------------------------------------\n')
    print('Discover the Murderer - The Game')
    print('\n----------------------------------------------\n')
    print('>>> Okay, a little clue before begin the game: Pay attention in numbers, it helps you to find the password to Safebox! <<<')
    print('>>> Try to maintain the order of the rooms so you can discover the secret of the safebox. (ex: 1, 2, 3...) <<<')
    print('\n----------------------------------------------\n')
    initial = Map('room')
    eng_game = Engine(initial)
    eng_game.play_game()

if __name__ == '__main__':
    main()
