# -*- coding: utf-8 -*-
# this is a game for my study
import random
import time
from random import randint
from sys import exit


class Scene(object):
    def __init__(self):
        self.lv = 1

    def put_level(self, level_1):
        self.lv = level_1
        # return level_1

    def enter(self):
        print("-----class Scene appear----")
        exit(1)


class ShowCase(Scene):
    # welcome and show how to play
    def enter(self):
        print(">>>>>>>>Jarry-Hit<<<<<<<<")
        print("""
        Welcome to Jarry-Hit!
        This a 'Tiny Game' which is a challenge to your response speed.
        Are You Ready?
        """)
        go = input("yes or no? >>>")

        if go != 'yes':
            print('Bye!')
            exit(1)
        else:
            pass
        print(">>>>>>>>How To Play<<<<<<<<")
        time_1 = 0
        while time_1 < 3:
            print('.')
            time.sleep(1)
            time_1 += 1
        hole = 'O'
        jarry = '@'
        top = "---"
        frount = "|"
        item = ' %s |'
        print('\n')
        print(top * 4)
        print(frount + item * 3 % (hole, hole, hole))
        print(top * 4)
        print(frount + item * 3 % (hole, hole, hole))
        print(top * 4)
        print(frount + item * 3 % (hole, hole, hole))
        print(top * 4)
        print('\n')
        print("Here is a Gridiron Valve,\njarry has possibility came out from the gridirons.")
        input(">")
        print("\nLike this...")
        print(top * 4)
        print(frount + item * 3 % (jarry, 2, 3))
        print(top * 4)
        print(frount + item * 3 % (4, 5, 6))
        print(top * 4)
        print(frount + item * 3 % (7, 8, 9))
        print(top * 4)
        input(">")
        print("You should hit the corresponding number to beat his head.")
        print("If you are quickly enough, you can get 1 point.")
        print("""
        3 point,Win.
        3 failures Lose.
        Are we clear, dude?
        """)
        input(">")
        print("Good,let's start!")
        return "choose_mode"


class ChooseMode(Scene):
    def enter(self):
        print("""
        PLZ choose the grade of difficulty...
        [Level 2] with 4 gridirons...
        [Level 3] with 9 gridirons...
        [Level 4] with 16 gridirons...
        """)
        level = input("Level = : ")
        Scene().put_level(level)
        print("Loading...Level %s" % level)
        time.sleep(3)
        print("Ready...\n")
        input(">>>Enter Start<<<")
        return 'game_start'


class GameStart(Scene):
    def enter(self):
        # le = Super(GameStart, self).put_level()
        # print(le)

        # level = 3
        print("scene GameStart %s" % self.lv)
        return 'game_over'


class GameOver(Scene):
    def enter(self):
        print("game_over")


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_door()

        while True:
            print("---------------")
            next_scene_name = current_scene.enter()
            # if next_scene_name == 'GameStart':
            #     # le = Scene(level)
            current_scene = self.scene_map.next_door(next_scene_name)
            if current_scene is None:
                break


class Map(object):
    all_maps = {
        'show_case': ShowCase(),
        'choose_mode': ChooseMode(),
        'game_start': GameStart(),
        'game_over': GameOver()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_door(self, scene_name):
        s = Map.all_maps.get(scene_name)
        # print s
        return s

    def opening_door(self):
        return self.next_door(self.start_scene)


a_map = Map('show_case')
a_game = Engine(a_map)
a_game.play()
# text_map = ChooseMode()
# text_map.enter()
