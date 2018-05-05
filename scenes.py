#This classes creates the scenes box of the game.
#These are parts of a sequence.

import sys
from people import *

detective = Detective()
cooker = Cooker()
housekeeper = Housekeeper()
visitor = Visitor()
waiter = Waiter()
butler = Butler()

class Scenes(object):
    pass

#Implemented
class Room(Scenes):
    def enterScene(self):
        print('>>> You want to customize the name of detective with your name? <<<')
        print('>>> If you choose no, the name of the detective will be {}'.format(detective.name))
        answer = input('Yes or no: ')
        if answer == 'yes':
            newName = input('Game says: - Please, before we start, tell me your name, detective: ')
            detective.changeName(newName)
        else: 
            pass
        response = 'no'
        print('\n----------------------------------------------\n')
        print('>>> In this 04/20/2018, there was a tragedy in the Gilmour\'s mansion. Your butler has been dead, misteriously. <<<')
        print('\n----------------------------------------------\n')
        print('Butler says: - Be welcome ladies and gentlemans, my name is ' + butler.name + ', I\'m the butler and this is the Gilmour\'s house, nº 67!')
        print('Butler says: - Can I get some wine for you?')
        while response == 'no':
            response = input('Yes or no: ')
            if response == 'yes':
                print('Butler says: - Of course, please gimme a little bit of time!')
                print('>>> The butler go to the kitchen. <<<')
                print('>>> 10 minutes passed bye and he\'s not came back. <<<')
                butler.changeSituation('Death')
            else:
                print('>>> The butler insists and asks again. <<<')
                print('Butler says: - I want that you take something, I\'ll insists!')
                print('Butler says: - Can I get something for you?')
        print('\n----------------------------------------------\n')
        print('Where\'s the butler? --> Asks ' + visitor.name + ', the visitor')
        print('\n----------------------------------------------\n')
        print('>>> And at this moment the crime occurs. <<<')
        print('>>> The housekeeper comes. <<<')
        print('Housekeeper says: - Ohhhhh, My name is {}, I\'m the housekeeper and I\'ve been encountered the butler in the Bathroom'.format(housekeeper.name))
        print('Housekeeper says: - HE IS DEAD!')
        print('Visitor says: - I think we should go into the corridor and call a detective to solute this.')
        return 'corridor'

#Implemented
class Corridor(Scenes):
    
    enter = {
        1: 'kitchen',
        2: 'bathroom',
        3: 'attic',
        4: 'winehouse',
        5: 'bedroom'
    }

    def enterScene(self):
        print('\n----------------------------------------------\n')
        print('>>> This is the corridor <<<')
        print('\n----------------------------------------------\n')
        print('>>> Please, insert a key to access a room! <<<')
        print('1 - Kitchen')
        print('2 - Bathroom')
        print('3 - Attic')
        print('4 - Winehouse')
        print('5 - Bedroom')
        print('6 - Access inventory')
        resp = input('> ')
        if int(resp) > 6 or int(resp) < 1:
            print('>>> This option isn\'t exists! <<<')
            return 'corridor'
        else:
            if int(resp) == 6:
                for key, value in detective.checkInventory().items():
                    print('{}: {}'.format(key, value))
                return 'corridor'
            else:
                return str(self.enter.get(int(resp)))
            

#Implemented
class Kitchen(Scenes):

    clue = {
        'clue': str('In my own name, I have 9 properties. But one of my sons wants all of they.')
    }

    def enterScene(self):
        print('\n----------------------------------------------\n')
        print('>>> This is the kitchen <<<')
        print('\n----------------------------------------------\n')
        print('Cooker says: - Hey, my name is {} and I\'m the cooker.'.format(cooker.name))
        print('You says: - Ok, my name is {} and I\'m the detective.'.format(detective.name))
        print('Cooker says: - Yeah, so, I was preparing a diner for you...')
        print('>>> The cooker shows your {} <<<'.format(cooker.weapon))
        print('>>> The cooker\'s weapon is covered in blood <<<')
        print('Detective says: - Whose blood is this?')
        print('Cooker says: - This blood is of the chiken that I killed to make diner, sir!')
        print('Cooker says: - But detective, I have a clue for you to discover the murderer.')
        detective.addItemToInventory(self.clue)
        print('>>> The clue has added to your inventory <<<')
        print('>>> To check him, press 1. Or, press 0 to exit <<<')
        response = input('> ')
        if int(response) == 1:
            for key, value in detective.checkInventory().items():
                print('\n----------------------------------------------\n')
                print('>>> The object is: {} and your description is: {} <<<'.format(key, value))
                print('\n----------------------------------------------\n')
            return 'corridor'
        elif int(response) == 0:
            return 'corridor'

#Implemented
class Bathroom(Scenes):
    def enterScene(self):
        print('\n----------------------------------------------\n')
        print('>>> This is the bathroom <<<')
        print('\n----------------------------------------------\n')
        print('>>> To enter inventory, press 1. To exit to the corridor, press 0. <<<')
        response = input('> ')
        if (int(response) > 1) or (int(response) < 0):
            print('>>> This is an invalid number! <<<')
            self.enterScene()
        else:
            if int(response) == 1:
                print('>>> This inventory is empty! <<<')
                return self.enterScene()
            elif int(response) == 0:
                return 'corridor'       

#Implemented
class Attic(Scenes):
    def enterScene(self):
        print('\n----------------------------------------------\n')
        print('>>> This is the attic <<<')
        print('\n----------------------------------------------\n')
        print('>>> To enter inventory, press 1. To exit to the corridor, press 0. <<<')
        response = input('> ')
        if (int(response) > 1) or (int(response) < 0):
            print('>>> This is an invalid number! <<<')
            self.enterScene()
        else:
            if int(response) == 1:
                print('>>> This inventory is empty! <<<')
                return self.enterScene()
            elif int(response) == 0:
                return 'corridor'    

#Implemented
class WineHouse(Scenes):

    clue = {
        'letter': 'One of pieces that opens my securebox is the number of my house, 67'
    }

    def enterScene(self):
        print('\n----------------------------------------------\n')
        print('>>> This is the Gilmour\'s winehouse <<<')
        print('\n----------------------------------------------\n')
        print('>>> In the Winehouse you encounter the waiter <<<')
        print('Waiter says: - Hi, I\'m {} and I\'m the waiter. How can I help you?'.format(waiter.name))
        print('You says: - I\'m detective {} and I have to discover the butler\'s murderer.'.format(detective.name))
        print('Waiter says: Uh, ok, I have something that can help! My boss give me this clue one day earlier!')
        detective.addItemToInventory(self.clue)
        for key, value in self.clue.items():
            print('>>> The item: {}'.format(key) + ' has added to your inventory! <<<')
        return 'corridor'

#Implemented
class Bedroom(Scenes):

    item = {
        'key': 'H3lps to o9en the safeb0x'
    }

    def enterScene(self):
        print('\n----------------------------------------------\n')
        print('>>> This is the Gilmour\'s bedroom <<<')
        print('\n----------------------------------------------\n')
        while True:
            search = int(input('>>> To access room\'s inventory, press 1. To access the safebox, press 2. To check your inventory, press 3. Otherwise, to exit bedroom, press 0: '))
            if int(search) > 3 or int(search) < 0:
                print('>>> This number is invalid! <<<')
            else:    
                if int(search) == 0:
                    return 'corridor'
                elif int(search) == 1:
                    self.inventory()
                elif int(search) == 2:
                    Safebox().enterScene()
                elif int(search) == 3:
                    print('\n----------------------------------------------\n')
                    for key, value in detective.checkInventory().items():
                        print('{}: {}'.format(key, value))
                    print('\n----------------------------------------------\n')

    def inventory(self):
        print('\n----------------------------------------------\n')
        print('>>> This is the bedroom\'s inventory <<<')
        print('\n----------------------------------------------\n')
        print('>>> This inventory contains a key that helps you to find the murder. <<<')
        response = input('>>> Say yes to get key or no to get away of inventary: ')
        if response == 'yes':
            detective.addItemToInventory(self.item)
            for key, value in self.item.items():
                print('>>> The item: {}'.format(key) + ' has added to your inventory! <<<')
            return self.enterScene()
        elif response == 'no': 
            self.enterScene()

#Implemented
class Safebox(Scenes):

    __password = 967390
    item = {
        'gun': 'This gun is covered in blood, and have a strand of hair that your color indicates the murderer! The strand of hair have the color {}'.format(housekeeper.hairColor)
    }

    def enterScene(self):
        print('\n----------------------------------------------\n')
        print('>>> This is the bedroom\'s safebox <<<')
        print('\n----------------------------------------------\n')

        key = input('>>> Please insert the correct key to discover murder or press 0 to return to bedroom: ')
        if int(key) == 0:
            return 'bedroom'
        elif int(key) == self.__password:
            print('>>> Yeah, you discovered the key! <<<')
            detective.addItemToInventory(self.item)
            for key, values in self.item.items():
                print('>>> The item: {}'.format(key) + ' has added to your inventory! <<<')
            return MurderSolve().enterScene()
        else:
            print('>>> This isn\'t a valid password! Please try again! <<<')
            return Safebox().enterScene()

#Implemented
class MurderSolve(Scenes):
    def enterScene(self):
        print('\n----------------------------------------------\n')
        print('>>> Ok, this is the conclusion! But isn\'t the finish, no yet! <<<')
        print('\n----------------------------------------------\n')
        print('>>> With last item of your inventory, you will discover the murderer <<<')
        print('\n----------------------------------------------\n')
        print('>>> This is your items: <<<')
        for key, value in detective.checkInventory().items():
            print('>>> In inventory you have -> {} with description: \"{}\" <<<'.format(key, value))
        print('\n----------------------------------------------\n')
        print('\n----------------------------------------------\n')
        print('>>> And the hair color of the visitors is: <<<')
        print('>>> Name: {} - Hair color: {} <<<'.format(str(cooker.name), str(cooker.hairColor)))
        print('>>> Name: {} - Hair color: {} <<<'.format(str(housekeeper.name), str(housekeeper.hairColor)))
        print('>>> Name: {} - Hair color: {} <<<'.format(str(visitor.name), str(visitor.hairColor)))
        print('>>> Name: {} - Hair color: {} <<<'.format(str(waiter.name), str(waiter.hairColor)))
        print('>>> Name: {} - Hair color: {} <<<'.format(str(butler.name), str(butler.hairColor)))
        print('\n----------------------------------------------\n')
        response = input('>>> So, the murderer is: ')
        while response != str(housekeeper.name):
            print('>>> No, this person isn\'t the murderer! Try again. <<<')
            response = input('So, the murderer is: ')
            if str(response) == str(housekeeper.name):
                break
        print('>>> Yes, you\'ve encountered the murderer. <<<')
        print('\n----------------------------------------------\n')
        print('     ***     ***     ****    **   ********  *****     ***   ********   ****')
        print('   ***     **   **   ** **   **   **        **  **  **   **    **     **')
        print('   **      **   **   **  **  **   **   ***  *****   ** * **    **      **')
        print('   ***     **   **   **   ** **   **    **  ** **   **   **    **       **')
        print('     ***     ***     **    ****   ********  **  **  **   **    **    ****')
        print('\n')
        print('\n')
        print('Game developer : Pedro Augusto de Lima Belotto')
        print('\n')
        print('\n')
        sys.exit(1)
