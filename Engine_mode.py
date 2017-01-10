from sys import exit

class Scene(object):
    
    def enter(self):
        print("-----not getin the correct way-----")
        exit(1)

class Scene_1(Scene):
    
    def enter(self):
        print("Scene_1")
        return 'key2'

class Scene_2(Scene):
    
    def enter(self):
        print("Scene_2")
        exit(1)
        #return 'key2'

class Engine(object):
    
    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):
        print('--------')
        current_scene = self.scene_map.opening_scene()

        while True:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Map(object):
    scene = {'key1':Scene_1(),'key2':Scene_2()}

    def __init__(self,a):# a is the key of dict
        self.a = a
    
    def next_scene(self,b):# b is the key of dick
        return Map.scene.get(b)

    def opening_scene(self):
        return self.next_scene(self.a)


a_map = Map('key1')
a_game = Engine(a_map)
a_game.play()