#This part I caught of the base game, launched by Jacson Luiz Matte. I just can changed some parts.

import sys
from scenes import *

class Map(object):

    #Creates a dict to bind string to class name
    scenes = {
        'room': Room(),
        'corridor': Corridor(),
        'kitchen': Kitchen(),
        'bathroom': Bathroom(),
        'attic': Attic(),
        'bedroom': Bedroom(),
        'winehouse': WineHouse(),
    }

    #Defines the room class as the start scene
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return self.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)
