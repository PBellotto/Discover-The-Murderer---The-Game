#This classes implements the people that will be in the game and some of its actions

class Person:
    def __init__(self):
        self.situation = 'Alive'

    def changeSituation(self, situation):
        self.situation = situation

class Detective(Person):
    def __init__(self):
        super().__init__()
        self.name = 'John Wick'
        self.profile = 'Honest'
        self.hairColor = 'Black'
        self.weapon = 'Gun'
        self.inventory = {}
    
    def changeName(self, name):
        self.name = name

    def changeSituation(self, situation):
        super().changeSituation(situation)

    def addItemToInventory(self, item):
        self.inventory.update(item)

    def checkInventory(self):
        return self.inventory 

class Visitor(Person):
    def __init__(self):
        super().__init__()
        self.name = 'Roger Waters'
        self.profile = {0: 'Authoritary', 1: 'Aggressive'}
        self.hairColor = 'Gray'
        self.weapon = None
        self.situation = 'Alive'

    def changeSituation(self, situation):
        super().changeSituation(situation)

class Waiter(Person):
    def __init__(self):
        super().__init__()
        self.name = 'Dave Mustaine'
        self.profile = 'Pacific'
        self.hairColor = 'Blond'
        self.weapon = 'Switchblade'
        self.situation = 'Alive'

    def changeSituation(self, situation):
        super().changeSituation(situation)

class Cooker(Person):
    def __init__(self):
        super().__init__()
        self.name = 'Zakk Wylde'
        self.profile = 'Pacific'
        self.hairColor = 'Brown'
        self.weapon = "Kitchen Knife"
        self.situation = 'Alive'

    def changeSituation(self, situation):
        super().changeSituation(situation)

class Housekeeper(Person):
    def __init__(self):
        super().__init__()
        self.name = 'Martha Clarke'
        self.profile = {0: 'Aggressive', 1: 'Passive'}
        self.hairColor = 'Green'
        self.weapon = 'Banana'

    def changeSituation(self, situation):
        super().changeSituation(situation)

class Butler(Person):
    def __init__(self):
        super().__init__()
        self.name = 'Anthony Kiedis'
        self.profile = 'Very passive'
        self.hairColor = 'Black'
        self.weapon = 'Hoe'

    def changeSituation(self, situation):
        super().changeSituation(situation)
