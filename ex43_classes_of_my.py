from sys import exit
from random import randint
import random
import time

class Scene(object):

    def enter(self):
        print("Walking with a long time,get in enter().")
        exit(1)
        
a = Scene()
a.enter()

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print("\n-------------")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        

class Death(Scene):

    def enter(self):#different death type and call it with random
        death_type = [
            "You fired getting suntan,death!",
            "You fell in a cement mixer full of quicksand,death!",
            "You met a space shark and be eaten,gone!",
            "You are caught in a mudslide,death!",
            "You got run over by a crappy purple Scion,death!"
            ]
        result_death = death_type[randint(0,len(death_type))]

        print (result_death)


class CentralCorridor(Scene):
    
    def enter(self):
        print("""You have get in The CentralCorridor,
        there is a bad guy stand frount the door,
        maybe you should say a joke to him?""")

        next = input('>')

        if next == 'joke':
            LaserWeaponArmory()
        else:
            print ("The guy don't laugh,he catch you and ...")
            Death()


class LaserWeaponArmory(Scene):

    def enter(self):
        print("""You get in a room with lots of Weapons,
        there is a big boom in the center of the room,
        maybe you should take it.
        But,there is a password have to Enter:""")

        next = input('Enter the pass word from 0-9:')
        boom_count = 0

        if boom_count == 7:
            print("'BOOM!'the big boom have been distroyed,the bad guy come in.")
            Death()
        elif next == '7':
            print("'BILL~' the door to TheBridge is opening, harry up!")
            TheBridge()
        else:
            print("'WRONG!' a big vioce appear, you found you have been throw out the room.")
            boom_count += 1
            LaserWeaponArmory()

class TheBridge(Scene): 

    def enter(self):
        print("""Here it is!
        it is a good place to set the big boom,
        click the butten 'SEVEN' to set up,
        do something to set the boom to READY.
        """)

        nums = []
        num =[]
        for n in range(7):
            nums.append(n)

 #nums = random.sample(nums, 3)
    #print(nums)

        set_count = 0
        set_count_1 = 0
 #random appear 3 num , we must input some num for == 7
 #we have 3 chances to do it 
        num = (random.sample(nums, 3))
        while True:
            if set_count_1 == 3:
                print("You are SUCCESS!")
                break

            if set_count == 3:
                print ("""Chance run out,the boom is broken.
                The warning has run to bad guy,he is coming!
                you waste a lot of times...
                """)
                Death()
                a = num[set_count_1]
                next = int(input("The number is %s,you should click the number:" % a))
                #nu = num[set_count].__int__()
                #type(num[set_count])
    

            if a + next == 7:
                print ("RIGHT NUM!")
                set_count_1 += 1
                exit
            else:
                print("Number Wrong,you lost One chance.")
                set_count += 1
                exit
                EscapePod()

class EscapePod(Scene):

    def enter(self):
        print("""Finally,you made it!You are a human hero!
        Now run quickly,There are three EscapeShips,you have to choose one
        #A, #B or #C""")

        #time out,game out,choose quickly.
        ship = input("choose a ship >>>")
        if ship == 'A':
            i = 0
            while i <= 10:
                print (10 - i) # 输出i
                i += 1
                time.sleep(1) # 休眠1秒
            print("You Win!")
            exit
        else:
            print("you can not control the machine!  Dame it!")
            i = 0
            while i <= 10:
                print (10 - i) # 输出i
                i += 1
                time.sleep(1) # 休眠1秒
            print("BOOOOOOOOM!!")
            print("You dead!")
            time.sleep(4)
            exit
        next = input("You nearly win, play again?yes or no >>>")
    
        if next == 'yes':
            CentralCorridor()
        else:
            exit (0)
     

class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

