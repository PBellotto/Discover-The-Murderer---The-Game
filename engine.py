#This part I caught of the base game, launched by Jacson Luiz Matte. I just can changed some parts.

import sys

class Engine(object):
    def __init__(self, select):
        self.scene_map = select

    def play_game(self):
        self.current_scene = self.scene_map.opening_scene()

        while True:
            next_scene = self.current_scene.enterScene()
            self.current_scene = self.scene_map.next_scene(next_scene) 
