#this is a game for my study
import random
#import math
import re
import time
from random import randint
from sys import exit
import os
import shelve


class Scene(object):

    #def __init__(self,aa):
        #self.aa = aa
    
    #def put_level(self,level_1):
        #return level_1

    def enter(self):
        print("-----class Scene appear----")
        exit(1)

class ShowCase(Scene):
    #welcome and show how to play
    def enter(self):
        print(">>>>>>>>Jarry-Hit<<<<<<<<")
        print("""
        Welcome to Jarry-Hit!
        This a 'Tiny Game' which is a challenge to your response speed. 
        Are You Ready?
        """  )
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
        print(frount+item *3 % (hole,hole,hole))
        print(top * 4)
        print(frount+item *3 % (hole,hole,hole))
        print(top * 4)
        print(frount+item *3 % (hole,hole,hole))
        print(top * 4)
        print('\n')
        print("Here is a Gridiron Valve,\njarry has possibility came out from the gridirons.")
        input(">")
        print("\nLike this...")
        print(top * 4)
        print(frount+item *3 % (jarry,2,3))
        print(top * 4)
        print(frount+item *3 % (4,5,6))
        print(top * 4)
        print(frount+item *3 % (7,8,9))
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
        shelfFile = shelve.open('hitjerry')
        #del shelfFile['the_level']
        #del shelfFile['save_point']  
        shelfFile['the_level'] = level
        shelfFile.close()

        print("Loading...Level %s"% level)
        time.sleep(3)
        print("Ready...\n")
        input(">>>Enter Start<<<")
        return 'game_start'

class GameStart(Scene):

    def rang(self):
        keys = input("Enter Your Name, dude:")
        a = keys
        rank = shelve.open('hitjerry_rank')
        rank[a] = None
        rank.close()
        pass

    def enter(self):
        #self.rang()
        #open a shelve to get the str
        shelfFile = shelve.open('hitjerry')
        #rank = shelve.open('hitjerry_rank')
        the_level_s = shelfFile['the_level']
        save_point = []
        shelfFile['save_point'] = save_point
        #print(list(rank.keys()))
        print('[Level %s]'% the_level_s)
        the_level = int(the_level_s) #turn

        top = "----"
        frount = "| "
        the_rounds = 1
        points = 0
        failure = 0
        

       #here is a gridiron with nums in it,and the jerry is everywhere by random
        while the_rounds < 4:
            gridiron_list = []

            for n in range(1,the_level**2+1):
                gridiron_list.append(n)
            the_answer = randint(1,the_level**2)

            shelfFile['%r'% the_rounds] = the_answer
            print('ROUND:',the_rounds)
            
            #put jerry in gridiron_list
            gridiron_list[the_answer - 1] = '@'
            gridiron_list.reverse()
            

            #here is a gridiron with nums in it
            print(top * the_level)
            for n in range(the_level):
                print('',end='| ' )
                for n in range(the_level):
                    print (gridiron_list.pop(),end=' | ')
                print(' ',end='\n')
                print(top * the_level)
            
            hit_num = input("Hit !!! in %ds>>>"% the_level)
            a = shelfFile['%r'% the_rounds]
            #print('hit answer is:',a)

            if int(hit_num) == int(a):
                save_point = shelfFile['save_point']
                save_point.append(hit_num)
                shelfFile['save_point'] = save_point
                point_num = len(shelfFile['save_point'])
                #print('the point is:',point_num)
            else:
                failure += 1
            points = len(shelfFile['save_point'])
            
            #print('the points is :',points)
            the_rounds += 1
        print("You get %d points,and %d failure"% (point_num,3-int(point_num)))
        #rank[a] = unichr(point_num)
        if len(shelfFile['save_point']) == 3:#shelfFile['%r'% the_rounds]:
            print(">>>Mission Complete<<<")
        else:
            print(">>>You Lose<<<")

        del shelfFile['save_point']
        del shelfFile['the_level']
        
        shelfFile.close()
        #rank.close()
        return "game_over"
        

class GameOver(Scene):
    
    def enter(self):
        print(">>>Game Over!<<<")
        print('The Rank:To Be Continue...\n')
        #rank = shelve.open('hitjerry_rank')
        #for item in rank.items():
            #print('键[{%d}] = 值[{%d}]'% format(rank[0], rank[item[0]]))
        #for n in len(rank.keys()):
            #print('Name: %d----Point:%d'%rank.keys(),rank.values())
        #rank.close()
        print("PLAY AGAIN?")
        over = input("yes or no >")
        if over == 'yes':
            return 'choose_mode'
        else:
            exit(1)

class Engine(object):

    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_door()      

        while True:
            print("---------------")
            next_scene_name = current_scene.enter()
            #if next_scene_name == 'GameStart':
                #le = Scene(level)
            current_scene = self.scene_map.next_door(next_scene_name)

class Map(object):

    all_maps = {
        'show_case':ShowCase(),
        'choose_mode':ChooseMode(),
        'game_start':GameStart(),
        'game_over':GameOver()
    }

    def __init__(self,start_scene):
        self.start_scene = start_scene
    
    def next_door(self,scene_name):
        return Map.all_maps.get(scene_name)

    def opening_door(self):
        return self.next_door(self.start_scene)

a_map = Map('show_case')
a_game = Engine(a_map)
a_game.play()
#text_map = GameStart()
#text_map = ChooseMode()
#text_map.work_gridiron_item()
#text_map.enter()

#data_clear()