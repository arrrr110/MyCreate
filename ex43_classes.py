from sys import exit
from random import randint
import random
import time

class Scene(object):

    def enter(self):
        print("Walking with a long time,get in enter().")
        exit(1)

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
        #result_death = death_type[randint(0,len(death_type))]

        #print (result_death)
        print(death_type[randint(0,5)])
        exit(1)


class CentralCorridor(Scene):
    
    def enter(self):
        print("""
        You have get in The CentralCorridor,
        there is a bad guy stand frount the door,
        Would you please say a joke to him?""")
        print("-------------\n")

        next = input('You say:')

        if next == 'joke':
            #LaserWeaponArmory()
            return 'laser_weapon_armory'
        else:
            print ("The guy don't laugh,he catch you and ...")
            #Death()
            return 'death'


class LaserWeaponArmory(Scene):
    
    def enter(self):

        print("""
        You get in a room with lots of Weapons,
        there is a big boom in the center of the room,
        maybe you should take it.
        But,there is a password have to Enter:""")
        print("-------------\n")
        code = '%s%s%s'%(randint(1,9),randint(1,9),randint(1,9))
        print(code)
        guess = input("[keypad]>")
        guesss = 0

        while guess != code and guesss < 9:
            print("BZZZZEDDDD")
            guesss += 1
            guess = input("[keypad]>")

        if guess == code:
            print("OK")
            return 'the_bridge'
        else:
            print('feil')
            return 'death'
        #boom_count = 0
        #while True:
            #next = int(input('Enter the pass word between num 0-9:'))
            #boom_count += 1 #(n for n in range(7))
            #it doesn't work!

            #if boom_count > 3:
                #print("'BOOM!'the big boom have been distroyed,the bad guy come in.")
                #Death()
                #return 'death'
            #elif next == 7:
                #print("'BILI~' the door to TheBridge is opening, harry up!")
                #TheBridge()
                #return 'the_bridge'
            #else:
                #print("'WRONG!' a big vioce appear, you found you have been throw out the room.")
                #next(boom_count)
                #LaserWeaponArmory()

class TheBridge(Scene): 

    def enter(self):
        print("""
        Here it is!
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
                return 'escape_pod'

            if set_count == 3:
                print ("""
                Chance run out,the boom is broken.
                The warning has run to bad guy,he is coming!
                You waste a lot of times...
                """)
                return 'death'

            a = num[set_count_1]
            next = int(input("The number is %s,you should click the number:" % a))
                #nu = num[set_count].__int__()
                #type(num[set_count])
    

            if a + next == 7:
                print ("RIGHT NUM!")
                set_count_1 += 1
                #exit
            else:
                print("Number Wrong,you lost One chance.")
                set_count += 1
                #exit
                #EscapePod()
                #return 'escape_pod'

class EscapePod(Scene):

    def enter(self):
        print("""
        Finally,you made it!You are a human hero!
        Now run quickly,There are three EscapeShips,
        you have to choose one
        #A, #B or #C
        """)

        #time out,game out,choose quickly.
        ship = input("choose a ship >>>")
        if ship == 'A':
            i = 0
            print("You push the START BUTTON...")
            time.sleep(2)
            print("It's work!")
            while i <= 10:
                print (10 - i) # 输出i
                i += 1
                time.sleep(1) # 休眠1秒
            print("You Win!")
            exit(1)
        else:
            print("You push the START BUTTON...")
            time.sleep(2)
            print("It's out of power!")
            print("you can not control the machine! and you have no way out, Dame it!")
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
            return 'central_corridor'
        else:
            exit (0)
     

class Map(object):
    scene = {"central_corridor":CentralCorridor(),
    "laser_weapon_armory":LaserWeaponArmory(),
    "the_bridge":TheBridge(),
    "escape_pod":EscapePod(),
    "death":Death()}

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scene.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

