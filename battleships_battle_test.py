#pacmax42 2018-
#v0.1.9
#planned features for the future:

#location system using 1 as north 2 as east 3 as south and 4 as west(done)
# this abobe inculed a speed system so ships can only move in a certain time so for example yspeed = 2 so it will take two turns to run any move command(needs to be done to fully finish location system)
#dud shells
#torpedos
#secondarys having a impact on the battle
#creating your own ships(also under development)
#muti-ship battles based on a point per ships system to balance things a little
#ability to knock out turrets and engines(turrets done engines not)
#weather systems
#night fights
#different maps
#submaire and air strike events
#add a more realistic damage system
#other ship types
#ai to play against(under development)
#crew and crew actions
#ranges to effect accuresary

#pipe dreams which most likly wont happen:

#actual control of where you fire(mostly finished)
#external html site
#combine with naval building game.py at some distant point
#gui(some point in the very distante future)
#improving code so its more readable and less suffering(so uses classes and making it look lot nicer)
#discord bot functionlity possibly if I dont go insane learning how to do that in js again or try do it in python..and if my pc finaly accpects discord.js as a thing
#withdrawal and long term campain mode which comes with a whole host of other things like up1grades and comander skills
import random,time,text_file_manger,battleships_battle_test_ai,os
#from debug import Debug
os.system("color")
print('\033[46m\033[97mPlayer\033[0m:')
#debuger made by shiromi
class Debug:
    def variable(self, name: str, value: any) -> None:
        print("[VARIABLE]: %s = %s" % (name, value))

    def function(self, name: str, args: dict) -> None:
        _args = ''

        for name, val in args.items():
            _args += "{0}: {1},".format(name, val)

        _args = _args[:len(_args) - 1]
        print("[FUNCTION]: Executed '%s' with '%s' as arguments." % (name, _args))
#d.function("p2turn", {'p2turn': p2turn})
#
#replay = 1
#this is the stats of the ship
ships = 1.1
kgVgunsc = 14
kgVarmour = 14.7
kgVgunsn = 10
valid_ship1 = False
valid_ship2 = False
ygunsc = 18.1
yarmour = 16.1
ygunsn = 9
yhp = 1000
kgVhp = 700
#dis = 4
game = True
p1hp = 0
p2hp = 0
p2gunsc = 0
p1armour = 0
p1gunsc = 0
p1gunsn = 0
p2armour = 0
p2gunsn = 0
p1movespeed = 0
p2movespeed = 0
karmour = 8
kgunsc = 14
fgunsc = 14
farmour = 12
fgunsn = 12
fhp = 700
khp = 600
qegunsc = 15
qearmour = 13
qegunsn = 8
qehp = 600
kgunsn = 8
ngunsc = 16.1
narmour = 12
ngunsn = 8
nhp = 700
nelgunsc = 16
nelarmour = 13
nelgunsn = 9
nelhp = 650
lgunsc = 16
larmour = 14.7
lgunsn = 9
lhp = 750
cgunsc = 13.5
carmour = 12
cgunsn = 10
chp = 570
hgunsc = 15
harmour = 12
hgunsn = 8
hhp = 550
vgunsc = 15
varmour = 14
vgunsn = 8
vhp = 800
igunsc = 14
iarmour = 11.8
igunsn = 12
ihp = 650
tgunsc = 16.1
tarmour = 11
tgunsn = 10
thp = 900
reset = True
p1smoke = False
p1smoke_time = 0
p2smoke = False
p2smoke_time = 0
gameend = 0
firstime = True
your_turn = 1
p1location = 1
p2location = 1
if p1location >= 5:
    p1location = 1
if p2location >= 5:
    p2location = 1
their_turn = 1
p1smoke_charges = 3
p2smoke_charges = 3
p1first_smoke_shot = False
p1location = 1
p2location = 1
p2first_smoke_shot = False
p1moving = False
p2moving = False
start = True
p1speed = 0
shots1 = 0
shots2 = 0
p2speed = 0
zero_in1 = 11
p1turrets=[]
p2turrets=[]
hit_scored1 = False
zero_in2 = 11
hit_scored2 = False
true_range1 = round(random.uniform(5, 60), 1)
true_range2 = round(random.uniform(5, 60), 1)
print(true_range1)
x = zero_in1 + 1
hit1=False
hit2=False
range_finder_damage1 = 0
range_finder_damage2 = 0
p1engine = True
p2engine = True
p1engine_status = 0
p2engine_status = 0

# this is the battle system
#if not os.path.isfile('ships.db'):
#    conn = sqlite3.connect('ships.db')
#    db = conn.cursor()

#    db.execute("""CREATE TABLE customships
#           (shipID INTEGER PRIMARY KEY AUTOINCREMENT,
#            name TEXT,
#            customgunsc TEXT,
#            customgunsn INTEGER,
#            customhp INTEGER,
#            customamour TEXT)""")
#conn.commit()
#conn.close()
#
#def create_custom():
#    name = input('input the ships name ')
#    customgunsc = input('input the ships nation ')
#    customgunsn = input('input the number of gun barrels this ship has ')
#    customhp = input('input the number of torpedo tubes this ship had ')
#    customamour = input('input the belt amour')
#    db.execute("INSERT INTO cruisers (name, nation, gun_number, torpedos, fate) VALUES ('{1}',\'{2}',\'{3}',\'{4}',\'{5}')".format(name,customgunsc, customgunsn, customhp, customamour));
#    conn.commit()


#the start of owrk on the location system
#if p1location >= 5:
#    p1location = 1
#if p2location >= 5:
#    p2location = 1
#print(p1location)
#move = input('where do you want to move')
#if move == 'west':
#    p1location = 4
#    if p1location != p2location:
#        print('help')
#    else:
#        print('it works')
d=Debug()

def range_finder(true_range,hit_scored,damaged,zero_in):
    zero_in -= 1
    if damaged >= 4:
        message = ['....','EORROR 4234','...............','*indistinguable screaming*','*broken fax noices*','N/A','???????','*flames*']
        esimate = random.choice(message)
        return esimate
    if zero_in <= 0:
        zero_in = 0
    if hit_scored == True:
        estimate = true_range + random.randint(0,1) - random.randint(0,1) + damaged
    else:
        long_or_short = random.randint(0,1)
        if long_or_short == 1:
            estimate = true_range + round(random.uniform(0,zero_in),1) + damaged
        else:
            estimate = true_range - round(random.uniform(0,zero_in),1) - damaged
    return estimate

def battle():
    global range_finder_damage1,range_finder_damage2,true_range2,hit1,hit2,p2location, p2moving,p1turrets,p2turrets,p2speed, p2direction, p1location, p1direction, p1first_smoke_shot, p1shots, p2shots, p2first_smoke_shot, p2movespeed, p1smoke_charges, p1speed, p2smoke_charges, reset, p1movespeed, gameend, p1moving, p1hp, p2hp, firstime, p1smoke, p2smoke, p1smoke_time, p2smoke_time, p1armour, p2gunsc, p1gunsn, p2armour, p1gunsc, p2gunsn, shots1, shots2, gameend, your_turn, their_turn, p1,p1engine,p2engine,p1engine_status,p2engine_status
    your_turn = 1
    their_turn = 1
    if p1gunsc == p2gunsc:
        true_range2 = true_range1
    p1movespeed = p1speed
    if p1moving == True:  # if the ship is already moving this contiues it and allows for p1speed vaules to be taken in
        p1movespeed = p1movespeed - 1
        print('your ship is moving...')
        if p1movespeed <= 0:
            p1movespeed = p1speed
            if p1direction == 1:
                p1location = 1
                print('player1 reached north')
                p1moving = False
            elif p1direction == 2:
                p1location = 2
                p1moving = False
                print('player1 reached east')
            elif p1direction == 3:
                p1location = 3
                print('player1 reached south')
                p1moving = False
            elif p1direction == 4:
                print('player1 reached west')
                p1location = 4
                p1moving = False
    if p1location >= 5:
        p1location = 1
    magdet = [23]
    targethit1 = true_range1
    targethit2 = true_range2
    smoke_target_hit = [5, 9, 40, 27, 32, 15]
    while your_turn == 1:
        p1turn = input('player 1 pick  what to do 1:fire guns 2:deploy smoke screen3:move to a new place')
        if (p1turn == '1'):
            solution = range_finder(true_range1, hit1, range_finder_damage1, zero_in1)
            print(solution)
            player1elevation = float(input("enter the elevation to fire at "))
            player1spreed=input("do you want to fire with a narrow spreed or wide spreed")
            player1spreed.lower()
            while shots1 != p1gunsn:
                if player1spreed == 'narrow':
                    long_or_short = random.randint(0, 1)
                    if long_or_short == 1:
                        disperstion = player1elevation + round(random.uniform(0, 2), 1)
                    else:
                        disperstion = player1elevation - round(random.uniform(0, 2), 1)
                else:
                    long_or_short = random.randint(0, 1)
                    if long_or_short == 1:
                        disperstion = player1elevation + round(random.uniform(0, 4), 1)
                    else:
                        disperstion = player1elevation - round(random.uniform(0, 4), 1)
                if disperstion <= 0:
                    disperstion = 0
                shot = disperstion
                d.variable('shot',shot)
                time.sleep(1)
                shots1 = shots1 + 1
                if p2smoke_time >= 1:
                    if p2first_smoke_shot == True:
                        p2smoke_time = p2smoke_time - 1
                        p2first_smoke_shot = False
                    if p2smoke_time == 0:
                        print('the cloud of smoke will disapate soon')
                    if shot == true_range1 :
                        print('target hit')
                        magkaboom = disperstion
                        a=random.randint(0,50)
                        if magkaboom == true_range1 and a == 23:
                            print('you detonated the enemy ammo,target sunk')
                            damage = p2hp
                            gameend = 1
                            S.game_management(gameend)
                        else:
                            damage = int(random.randint(1, 5) * p1gunsc - p2armour)
                            if damage <= 0:
                                damage = damage * 0
                                print('failed to penatrate target')

                            else:
                                print(' you did {0} damage'.format(damage))
                                p2hp = p2hp - damage
                                if p2hp <= 0:
                                  p2hp = 0
                                  gameend = 1
                                  S.game_management(gameend)
                    else:
                        print('you missed')
                else:
                    if p2smoke == True and p2smoke_time == 0:
                        print('the enemy smoke has disapated')
                        p2smoke = False
                    else:
                        if true_range1 - 1 <= shot <= true_range1 + 1:
                            print('target hit')
                            hit1=True
                            magkaboom = disperstion
                            a = random.randint(0, 10)
                            if magkaboom == true_range1 and a == 1:
                                print('critial hit')
                                print('you detonated the enemy ammo,target sunk')
                                damage = p2hp
                                gameend = 1
                                p2hp = p2hp - damage
                                S.game_management(gameend)
                            if magkaboom == true_range1 and a == 5:
                                print('critial hit')
                                r = random.choice(p2turrets)
                                p2turrets.remove(r)
                                p2gunsn = p2gunsn - r
                                damage = int(random.randint(3, 7) * p1gunsc - p2armour)
                                p2hp = p2hp - damage
                            if magkaboom == true_range1 and a == 7:
                                print('critical hit')
                                damage = int(random.randint(2, 5) * p1gunsc - p2armour)
                                p2hp = p2hp - damage
                                p2engine = False
                                p2engine_status =+ random.randint(1,3)
                                print(' you did {0} damage'.format(damage))
                            if magkaboom  == true_range1 and a == 10:
                                print('critical hit')
                                range_finder_damage2 += 1
                                damage = int(random.randint(1, 3) * p1gunsc - p2armour)
                                p2hp = p2hp - damage
                                print(' you did {0} damage'.format(damage))
                            else:
                                damage = int(random.randint(1, 5) * p1gunsc - p2armour)
                                if damage <= 0:
                                    damage = damage * 0
                                    print('failed to penatrate target')
                                else:
                                    print(' you did {0} damage'.format(damage))
                                    p2hp = p2hp - damage
                                    if p2hp <= 0:
                                        p2hp = 0
                                        gameend = 1
                                        S.game_management(gameend)
                        else:
                           print('you missed')
            else:
                your_turn = 0
        elif (p1turn == '2'):
                    print('depolying smoke...')
                    p1smoke = True
                    p1smoke_time = 2
                    p1first_smoke_shot = True
                    your_turn = 0
        elif (p1turn == '3'):
                if p1moving == False and p1engine == True:
                    p1move = input('which direction do you want to move?')
                    if p1move == 'north':
                        p1moving = True
                        p1direction = 1
                        print('you sail north')
                        your_turn = 0
                    elif p1move == 'south':
                        p1moving = True
                        p1direction = 3
                        print('you sail south')
                        your_turn = 0
                    elif p1move == 'east':
                        p1moving = True
                        p1direction = 2
                        print('you sail east')
                        your_turn = 0
                    elif p1move == 'west':
                        p1moving = True
                        p1direction = 4
                        print('you sail west')
                        your_turn = 0
                    else:
                        print('not a possible direction.skipping turn..')
                        your_turn = 0
                elif p1engine == True:
                    print('your ship is already moving')
                else:
                    if p1engine_status < 2:
                        print('reparing engine')
                        p1engine_status -= 1
                    print('engine critically damaged')
    else:
            if p2smoke_time >= 1:
                p2first_smoke_shot = True
            print('out of shots')
            print('enermy has {0} hp'.format(p2hp))
            shots1 = 0
            p2movespeed = p2speed
            if p2moving == True:  # if the ship is already moving this contiues it and allows for p1speed vaules to be taken in
                p2movespeed = p2movespeed - 1
                print('player2 ship is moving...')
                if p2movespeed <= 0:
                    p2movespeed = p2speed
                    if p2direction == 1:
                        p2location = 1
                        print('player2 reached north')
                        p2moving = False
                    elif p2direction == 2:
                        p2location = 2
                        p2moving = False
                        print('player2 reached east')
                    elif p2direction == 3:
                        p2location = 3
                        print('player2 reached south')
                        p2moving = False
                    elif p2direction == 4:
                        print('player2 reached west')
                        p2location = 4
                        p2moving = False
            if p2location >= 5:
                p2location = 1
            if p2location <= 0:
                p2location = 1
            while their_turn == 1:
                p2turn = input('player 2 pick  what to do 1:fire guns 2 deploy smoke screen:3:move to a new place')
                if (p2turn == '1'):
                    solution = range_finder(true_range2, hit2, range_finder_damage2, zero_in2)
                    print(solution)
                    player2elevation = float(input("enter the elevation to fire at "))
                    player2spreed=input('do you want to fire at narrow or wide spreed')
                    player2spreed.lower()
                    while shots2 != p2gunsn:
                        if player2spreed == 'narrow':
                            long_or_short = random.randint(0, 1)
                            if long_or_short == 1:
                                disperstion = player2elevation + round(random.uniform(0, 2), 1)
                            else:
                                disperstion = player2elevation - round(random.uniform(0, 2), 1)
                        else:
                            long_or_short = random.randint(0, 1)
                            if long_or_short == 1:
                                disperstion = player2elevation + round(random.uniform(0, 4), 1)
                            else:
                                disperstion = player2elevation - round(random.uniform(0, 4), 1)
                        if disperstion <= 0:
                            disperstion = 0
                        shot = disperstion
                        d.variable('shot', shot)
                        time.sleep(1)
                        shots2 = shots2 + 1
                        if p1smoke_time >= 1:
                            if p1first_smoke_shot == True:
                                p1smoke_time = p1smoke_time - 1
                                if p1smoke == 0:
                                    print('the cloud will disapate soon')
                                    p1first_smoke_shot = False
                                    if shot == true_range2:
                                        print('target hit')
                                        magkaboom = random.randint(1, 300)
                                        if magkaboom in magdet:
                                            print('you detonated the enemy ammo,target sunk')
                                            damage = p2hp
                                            gameend = 4
                                            S.game_management(gameend)
                                        else:
                                            damage = int(random.randint(1, 5) * p2gunsc - p1armour)
                                            if damage <= 0:
                                                damage = damage * 0
                                                print('failed to penatrate target')
                                            else:
                                                print(' you did {0} damage'.format(damage))
                                                p2hp = p2hp - damage
                                                if p2hp <= 0:
                                                    p2hp = 0
                                                    gameend = 4
                                                    S.game_management(gameend)
                                    else:
                                        print('you missed')
                        else:
                            if true_range2 - 1 <= shot <= true_range2 + 1:
                                print('target hit')
                                hit2 = True
                                magkaboom = disperstion
                                a = random.randint(0, 10)
                                if magkaboom == true_range2 and a == 1:
                                    print('critial hit')
                                    print('you detonated the enemy ammo,target sunk')
                                    damage = p1hp
                                    gameend = 1
                                    p1hp = p1hp - damage
                                    S.game_management(gameend)
                                if magkaboom == true_range2 and a == 5:
                                    print('critial hit')
                                    r = random.choice(p1turrets)
                                    p1gunsn = p1gunsn - r
                                    p1turrets.remove(r)
                                    damage = int(random.randint(3, 7) * p2gunsc - p1armour)
                                    p1hp = p1hp - damage
                                    print(' you did {0} damage'.format(damage))
                                if magkaboom == true_range2 and a == 7:
                                    print('critical hit')
                                    damage = int(random.randint(2, 5) * p2gunsc - p1armour)
                                    p1hp = p1hp - damage
                                    p1engine = False
                                    p1engine_status = + random.randint(1, 3)
                                    print(' you did {0} damage'.format(damage))
                                if magkaboom == true_range2 and a == 10:
                                    print('critical hit')
                                    range_finder_damage1 += 1
                                    damage = int(random.randint(1, 3) * p2gunsc - p1armour)
                                    p1hp = p1hp - damage
                                    print(' you did {0} damage'.format(damage))
                                else:
                                    damage = int(random.randint(1, 5) * p2gunsc - p1armour)
                                    if damage <= 0:
                                        damage = damage * 0
                                        print('failed to penatrate target')
                                    print(' you did {0} damage'.format(damage))
                                    p1hp = p1hp - damage
                                    if p1hp <= 0:
                                        p1hp = 0
                                        gameend = gameend + 4
                                        S.game_management(gameend)
                            else:
                                print('target missed')
                    else:
                        their_turn = 0
                elif (p2turn == '2'):
                    print('depolying smoke screen..')
                    p2smoke = True
                    p2smoke_time = 2
                    their_turn = 0
                    p2first_smoke_shot = True
                    if p2smoke_time >= 1:
                        p1first_smoke_shot = True
                elif (p2turn == '3'):
                    if p2moving == False:
                        p2move = input('which direction do you want to move?')
                        if p2move == 'north':
                            p2moving = True
                            p2direction = 1
                            print('you sail north')
                            their_turn = 0
                        elif p2move == 'south':
                            p2moving = True
                            p2direction = 3
                            print('you sail south')
                            their_turn = 0
                        elif p2move == 'east':
                            p2moving = True
                            p2direction = 2
                            print('you sail east')
                            their_turn = 0
                        elif p2move == 'west':
                            p2moving = True
                            p2direction = 4
                            print('you sail west')
                            their_turn = 0
                        else:
                            print('not a possible direction.skipping turn..')
                            their_turn = 0
                    elif p2engine == True:
                        print('your ship is already moving')
                    else:
                        if p2engine_status < 2:
                            print('reparing engine')
                            p2engine_status -= 1
                        else:
                            print('engine critically damaged')
            else:
                print('out of shots')
                print('enemy has {0} hp'.format(p1hp))
                shots1 = 0
                shots2 = 0
                reset = True
                firstime = False


# this is the stats of the ship and the how the code tells which ship has been picked by each player

#a class to use if i was to convert it into classes
# class Ship:
#     def __init__(self,name:str,cal:float,barrels:int,amour:float,hp:int):
#         self.name = name
#         self.cal = cal
#         self.barrels = barrels
#         self.amour = amour
#         self.hp = hp
#         print('you have picked {0}.'.format(self.name))
#         print(self.hp)
# c=Ship('hello',32.2,3,34,900)



def kinggeorgeV():
            global ships
            global p1gunsc
            global p1armour
            global p1gunsn
            global p1hp
            global kgVhp
            global p1turrets
            print('you have picked a king goerge V class ship')
            p1gunsc = kgVgunsc
            p1armour = kgVarmour
            p1gunsn = kgVgunsn
            p1hp = kgVhp
            p1turrets = [4,2,4]
def yamato():
            global ships
            global p1gunsc
            global p1armour
            global p1gunsn
            global yhp
            global p1hp
            global ship1
            global p1turrets
            print('you have picked a yamato class ship')
            p1gunsc = ygunsc
            p1armour = yarmour
            p1gunsn = ygunsn
            p1hp = yhp
            p1turrets =[3,3,3]
def hood():
            global ships
            global p1gunsc
            global p1armour
            global p1gunsn
            global hhp
            global p1hp
            global p1turrets
            print('you have picked a hood class ship')
            p1gunsc = hgunsc
            p1armour = harmour
            p1gunsn = hgunsn
            p1hp = hhp
            p1turrets = [2,2,2,2]
def kongo():
            global ships
            global p1gunsc
            global p1armour
            global p1gunsn
            global khp
            global p1hp
            global p1turrets
            print('you have picked a kongo class ship')
            p1gunsc = kgunsc
            p1armour = karmour
            p1gunsn = kgunsn
            p1hp = khp
            p1turrets = [2,2,2,2]
def fuso():
            global ships
            global p1gunsc
            global p1armour
            global p1gunsn
            global fhp
            global p1hp
            global p1turrets
            print('you have picked a fuso class ship')
            p1gunsc = fgunsc
            p1armour = farmour
            p1gunsn = fgunsn
            p1hp = fhp
            p1turrets = [2,2,2,2,2,2]
def nagato():
            global ships
            global p1gunsc
            global p1armour
            global p1gunsn
            global fhp
            global p1hp
            global p1turrets
            print('you have picked a nagato class ship')
            p1gunsc = ngunsc
            p1armour = narmour
            p1gunsn = ngunsn
            p1hp = nhp
            p1turrets = [2,2,2,2]
def nelson():
            global ships
            global p1gunsc
            global p1armour
            global p1gunsn
            global fhp
            global p1hp
            global p1turrets
            print('you have picked a nelson class ship')
            p1gunsc = nelgunsc
            p1armour = nelarmour
            p1gunsn = nelgunsn
            p1hp = nelhp
            p1turrets = [3,3,3]
def lion():
            global ships
            global p1gunsc
            global p1armour
            global p1gunsn
            global lhp
            global p1hp
            global p1turrets
            print('you have picked a lion class ship')
            p1gunsc = lgunsc
            p1armour = larmour
            p1gunsn = lgunsn
            p1hp = lhp
            p1turrets = [3,3,3]
def queen_elizabeth():
            global ships
            global p1gunsc
            global p1armour
            global p1gunsn
            global lhp
            global p1hp
            global p1turrets
            print('you have picked a Queen Elizabeth class ship')
            p1gunsc = lgunsc
            p1armour = larmour
            p1gunsn = lgunsn
            p1hp = lhp
            p1turrets = [2,2,2,2]
def centurion():
            global ships
            global p1gunsc
            global p1armour
            global p1gunsn
            global chp
            global p1hp
            global p1turrets
            print('you have picked a centurion class ship')
            p1gunsc = cgunsc
            p1armour = carmour
            p1gunsn = cgunsn
            p1hp = chp
            p1turrets = [2,2,2,2,2]
def Vangauard():
            global ships
            global p1gunsc
            global p1armour
            global p1gunsn
            global vhp
            global p1hp
            global p1turrets
            print('you have picked a Vangauard class ship')
            p1gunsc = vgunsc
            p1armour = varmour
            p1gunsn = vgunsn
            p1hp = vhp
            p1turrets = [2,2,2,2]
def custom_ship():
    global ship1
    global p1gunsc
    global p1armour
    global p1gunsn
    global vhp
    global p1hp
    list_ships=[]
    x = 1300
    a = 18
    b = 20
    f = 20
    y = text_file_manger.read_text_file('custom_ships.ship')
    print(y)
    ship1=input('what name does this ship have? ')
    cushp=int(input('how much health does this ship have? '))
    cusarmour=float(input('how much armour does this ships belt have? '))
    cusgunsc=float(input('what caliber of guns does this ship have? '))
    cusgunsn=float(input('how many barrles does this ship have? '))
    pos = len(y)
    if ship1 in y:
        print('ship already created')
    if cushp>=x:
        print('invaid hp')
        cushp = 300
    if cusarmour>=a:
        print('invaid armour')
        cusarmour = 5
    if cusgunsc >= b:
        print('invalid gun caliber')
        cusgunsc = 12
    if cusgunsn >=f:
        print('invalid number of guns')
        cusgunsc = 4
    list_ships = [ship1,cushp,cusarmour,cusgunsn,cgunsn,pos]
    text_file_manger.write_text_file_2d(list_ships,'custom_ships.ship')#this is broken and needs repairs
    p1gunsc = cusgunsc
    p1armour = cusarmour
    p1gunsn = cusgunsn
    p1hp = cushp
def ise():
            global ships
            global p1gunsc
            global p1armour
            global p1gunsn
            global ihp
            global p1hp
            global p1turrets
            print('you have picked a ise class ship')
            p1gunsc = igunsc
            p1armour = iarmour
            p1gunsn = igunsn
            p1hp = ihp
            p1turrets = [2,2,2,2,2,2]
def tosa():
            global ships
            global p1gunsc
            global p1armour
            global p1gunsn
            global thp
            global p1hp
            global p1turrets
            print('you have picked a tosa class ship')
            p1gunsc = tgunsc
            p1armour = tarmour
            p1gunsn = tgunsn
            p1hp = thp
            p1turrets = [2,2,2,2,2]

def custom_ship2():
    global ship2
    global p2gunsc
    global p2armour
    global p2gunsn
    global vhp
    global p2hp
    x = 1301
    a = 19
    b = 21
    f = 21
    list_ships = []
    y = text_file_manger.read_text_file('custom_ships.ship')
    print(y)
    ship2=input('what name does this ship have? ')
    cushp=int(input('how much health does this ship have? '))
    cusarmour=float(input('how much armour does this ships belt have? '))
    cusgunsc=float(input('what caliber of guns does this ship have? '))
    cusgunsn=float(input('how many barrles does this ship have? '))
    custurrets=float(input("how many barrels does it have per turret?"))#you need to add the system to create a list with the number of guns per turret
    pos = len(list_ships)
    if cushp>=x:
        print('invaid hp')
        cushp = 300
    if cusarmour>=a:
        print('invaid armour')
        cusarmour = 5
    if cusgunsc >= b:
        print('invalid gun caliber')
        cusgunsc = 12
    if cusgunsn >=f:
        print('invalid number of guns')
        cusgunsc = 4
    list_ships = [ship2,cushp,cusarmour,cusgunsn,cgunsn,pos]
    text_file_manger.append_text(list_ships,'custom_ships.ship')
    p2gunsc = cusgunsc
    p2armour = cusarmour
    p2gunsn = cusgunsn
    p2hp = cushp
def tosa2():
            global ships
            global p2gunsc
            global p2armour
            global p2gunsn
            global thp
            global p2hp
            global p2turrets
            print('you have picked a tosa class ship')
            p2gunsc = tgunsc
            p2armour = tarmour
            p2gunsn = tgunsn
            p2hp = thp
            p2turrets = [2,2,2,2,2]
def ise2():
            global ships
            global p2gunsc
            global p2armour
            global p2gunsn
            global ihp
            global p2hp
            global p2turrets
            print('you have picked a ise class ship')
            p2gunsc = igunsc
            p2armour = iarmour
            p2gunsn = igunsn
            p2hp = ihp
            p2turrets = [2,2,2,2,2,2]
def fuso2():
            global ships
            global p2gunsc
            global p2armour
            global p2gunsn
            global fhp
            global p2hp
            global p2turrets
            print('you have picked a fuso class ship')
            p2gunsc = fgunsc
            p2armour = farmour
            p2gunsn = fgunsn
            p2hp = fhp
            p2turrets = [2,2,2,2,2,2]
def lion2():
            global ships
            global p2gunsc
            global p2armour
            global p2gunsn
            global lhp
            global p2hp
            global p2turrets
            print('you have picked a lion class ship')
            p2gunsc = lgunsc
            p2armour = larmour
            p2gunsn = lgunsn
            p2hp = lhp
            p2turrets = [3,3,3]
def Vangauard2():
            global ships
            global p2gunsc
            global p2armour
            global p2gunsn
            global vhp
            global p2hp
            global p2turrets
            print('you have picked a Vangauard class ship')
            p2gunsc = vgunsc
            p2armour = varmour
            p2gunsn = vgunsn
            p2hp = vhp
            p2turrets = [2,2,2,2]
def hood2():
            global ships
            global p2gunsc
            global p2armour
            global p2gunsn
            global hhp
            global p2hp
            global p2turrets
            print('you have picked a hood class ship')
            p2gunsc = hgunsc
            p2armour = harmour
            p2gunsc = hgunsn
            p2hp = hhp
            p2turrets = [2,2,2,2]
def nelson2():
            global ships
            global p2gunsc
            global p2armour
            global p2gunsn
            global nelhp
            global p2hp
            global p2turrets
            print('you have picked a nelson class ship')
            p2gunsc = nelgunsc
            p2armour = nelarmour
            p2gunsn = nelgunsn
            p2hp = nelhp
            p2turrets = [3,3,3]
def nagato2():
            global ships
            global p2gunsc
            global p2armour
            global p2gunsn
            global nhp
            global p2hp
            global p2turrets
            print('you have picked a nagato class ship')
            p2gunsc = ngunsc
            p2armour = narmour
            p2gunsn = ngunsn
            p2hp = nhp
            p2turrets = [2,2,2,2]
def centurion2():
            global ships
            global p2gunsc
            global p2armour
            global p2gunsn
            global chp
            global p2hp
            global p2turrets
            print('you have picked a centurion class ship')
            p2gunsc = cgunsc
            p2armour = carmour
            p2gunsn = cgunsn
            p2hp = chp
            p2turrets = [2,2,2,2,2]
def kinggeorgeV2():
            global ships
            global p2gunsc
            global p2armour
            global p2gunsn
            global start
            global p2hp
            global kgVhp
            global p2turrets
            print('you have picked a king goerge V class ship')
            p2gunsc = kgVgunsc
            p2armour = kgVarmour
            p2gunsn = kgVgunsn
            p2hp = kgVhp
            p2turrets = [4,2,4]
def yamato2():
            global ships
            global p2gunsc
            global p2armour
            global p2gunsn
            global start
            global p2hp
            global yhp
            global p2turrets
            print('you have picked a yamato class ship')
            p2gunsc = ygunsc
            p2armour = yarmour
            p2gunsn = ygunsn
            p2hp = yhp
            p2turrets = [3,3,3]
def kongo2():
            global ships
            global p2gunsc
            global p2armour
            global p2gunsn
            global khp
            global p2hp
            global p2turrets
            print('you have picked a kongo class ship')
            p2gunsc = kgunsc
            p2armour = karmour
            p2gunsn = kgunsn
            p2hp = khp
            p2turrets = [2,2,2,2]
def queen_elizabeth2():
            global ships
            global p2gunsc
            global p2armour
            global p2gunsn
            global qehp
            global p2hp
            global p2turrets
            print('you have picked a Queen Elizabeth class ship')
            p2gunsc = qegunsc
            p2armour = qearmour
            p2gunsn = qegunsn
            p2hp = qehp
            p2turrets = [2,2,2,2]

# this is the list of ships to select from
ukships = ["centurion", "Duke of york", "howe", "King George V", "Malaya", "nelson", "Prince of wales",
                   "Vangauard", "Valiant", "Rodney", "Queen Elizabeth", "lion", "hood", ]
jships = ["Yamato", "Musashi", "Kongo", "Hiei", "haruna", "nagato", "mutsu", "fuso", "yamashiro", "kirashima",
                  "tosa", "ise"]

#while game == True:
#    gamemode = input('what gamemode do you want to play? ')

#    if (gamemode == 'battle'):
#        valid_ship2 = False
#        valid_ship1 = False
 #       game = False
 #   elif (gamemode == 'create ship'):
 #       create_custom()



def first_selection():
    global valid_ship1,start
    while valid_ship1 == False:
        if start == True:
            print(ukships[:])
            print(jships[:])
        start = False
        ship1 = input('player 1 pick a ship to play ')
        ship1.lower()
        if (ship1 == 'yamato'):
            valid_ship1 = True
            yamato()
            return ship1
        elif (ship1 == 'musashi'):
            valid_ship1 = True
            yamato()
            return ship1
        elif (ship1 == 'duke of york'):
            valid_ship1 = True
            kinggeorgeV()
            return ship1
        elif (ship1 == 'howe'):
            valid_ship1 = True
            kinggeorgeV()
            return ship1
        elif (ship1 == 'king george V'):
            valid_ship1 = True
            kinggeorgeV()
            return ship1
        elif (ship1 == 'Prince of wales'):
            valid_ship1 = True
            kinggeorgeV()
            return ship1
        elif (ship1 == 'custom'):
            valid_ship1 = True
            custom_ship()
            return ship1
        elif (ship1 == 'hiei'):
            valid_ship1 = True
            kongo()
            return ship1
        elif (ship1 == 'kongo'):
            valid_ship1 = True
            kongo()
            return ship1
        elif (ship1 == 'kirashima'):
            valid_ship1 = True
            kongo()
            return ship1
        elif (ship1 == 'haruna'):
            valid_ship1 = True
            kongo()
            return ship1
        elif (ship1 == 'fuso'):
            valid_ship1 = True
            fuso()
            return ship1
        elif (ship1 == 'yamashiro'):
            valid_ship1 = True
            fuso()
            return ship1
        elif (ship1 == 'nagato'):
            valid_ship1 = True
            nagato()
            return ship1
        elif (ship1 == 'mutsu'):
            valid_ship1 = True
            nagato()
            return ship1
        elif (ship1 == 'nelson'):
            valid_ship1 = True
            nelson()
            return ship1
        elif (ship1 == 'rodney'):
            valid_ship1 = True
            nelson()
            return ship1
        elif (ship1 == 'lion'):
            valid_ship1 = True
            lion()
            return ship1
        elif (ship1 == 'queen elizabeth'):
            valid_ship1 = True
            queen_elizabeth()
            return ship1
        elif (ship1 == 'valiant'):
            valid_ship1 = True
            queen_elizabeth()
            return ship1
        elif (ship1 == 'malaya'):
            valid_ship1 = True
            queen_elizabeth()
            return ship1
        elif (ship1 == 'centurion'):
            valid_ship1 = True
            centurion()
            return ship1
        elif (ship1 == 'hood'):
            valid_ship1 = True
            hood()
            return ship1
        elif (ship1 == 'vanguard'):
            valid_ship1 = True
            Vangauard()
            return ship1
        elif (ship1 == 'ise'):
            valid_ship1 = True
            ise()
            return ship1
        elif (ship1 == 'tosa'):
            valid_ship1 = True
            tosa()
            return ship1
        else:
            print('not a vaild input')

def second_selection():
    global valid_ship2
    while valid_ship2 == False:
        ship2 = input('player 2 pick a ship to play ')
        ship2.lower()
        if (ship2 == 'yamato'):
            valid_ship2 = True
            yamato2()
            return ship2
        elif (ship2 == 'custom'):
            valid_ship2 = True
            custom_ship2()
            return ship2
        elif (ship2 == 'musashi'):
            valid_ship2 = True
            yamato2()
            return ship2
        elif (ship2 == 'duke of york'):
            valid_ship2 = True
            kinggeorgeV2()
            return ship2
        elif (ship2 == 'howe'):
            valid_ship2 = True
            kinggeorgeV2()
            return ship2
        elif (ship2 == 'king george V'):
            valid_ship2 = True
            kinggeorgeV2()
            return ship2
        elif (ship2 == 'Prince of wales'):
            valid_ship2 = True
            kinggeorgeV2()
            return ship2
        elif (ship2 == 'hiei'):
                valid_ship2 = True
                kongo2()
                return ship2
        elif (ship2 == 'kongo'):
            valid_ship2 = True
            kongo2()
            return ship2
        elif (ship2 == 'kirashima'):
            valid_ship2 = True
            kongo2()
            return ship2
        elif (ship2 == 'haruna'):
            valid_ship2 = True
            kongo2()
            return ship2
        elif (ship2 == 'fuso'):
            valid_ship2 = True
            fuso2()
            return ship2
        elif (ship2 == 'yamashiro'):
            valid_ship2 = True
            fuso2()
            return ship2
        elif (ship2 == 'nagato'):
            valid_ship2 = True
            nagato2()
            return ship2
        elif (ship2 == 'mutsu'):
            valid_ship2 = True
            nagato2()
            return ship2
        elif (ship2 == 'nelson'):
             valid_ship2 = True
             nelson2()
             return ship2
        elif (ship2 == 'rodney'):
            valid_ship2 = True
            nelson2()
            return ship2
        elif (ship2 == 'lion'):
            valid_ship2 = True
            lion2()
            return ship2
        elif (ship2 == 'queen elizabeth'):
            valid_ship2 = True
            queen_elizabeth2()
            return ship2
        elif (ship2 == 'Valiant'):
            valid_ship2 = True
            queen_elizabeth2()
            return ship2
        elif (ship2 == 'Malaya'):
            valid_ship2 = True
            queen_elizabeth2()
            return ship2
        elif (ship2 == 'centurion'):
            valid_ship2 = True
            centurion2()
            return ship2
        elif (ship2 == 'hood'):
            valid_ship2 = True
            hood2()
            return ship2
        elif (ship2 == 'vangauard'):
            valid_ship2 = True
            Vangauard2()
            return ship2
        elif (ship2 == 'ise'):
            valid_ship2 = True
            ise2()
            return ship2
        elif (ship2 == 'tosa'):
            valid_ship2 = True
            tosa2()
            return ship2
        else:
            print('not a vaild input')


class Starting_up:
    def __init__(self):
        gamemode = input      ('what game mode do you want to play? two player or ai ')
        gamemode.lower()
        if gamemode== 'ai':
            self.p1 = first_selection()
            battleships_battle_test_ai.ai_selection(p1hp,p1armour,p1gunsn,p1gunsc,p1turrets)
            gameend = 3
        else:
            self.p1 = first_selection()
            self.p2 = second_selection()
    def restart(self):
        global valid_ship2,valid_ship1
        valid_ship2 = False
        valid_ship1 = False
        gamemode = input('what game mode do you want to play? two player or ai ')
        gamemode.lower()
        if gamemode== 'ai':
            self.p1 = first_selection()
            battleships_battle_test_ai.ai_selection(p1hp,p1armour,p1gunsn,p1gunsc,p1turrets)
            gameend = 3
        else:
            self.p1 = first_selection()
            self.p2 = second_selection()
    def game_management(self,gameend):
        while gameend == 0:
            battle()
        if gameend == 1:
            print('player one won using {0} against {1}'.format(self.p1, self.p2))
            myfile = open('battle_results', 'a')
            myfile.write('player one won using ')
            myfile.write(self.p1)
            myfile.write(' with ')
            myfile.write(str(p1hp))
            myfile.write(' health left against ')
            myfile.write(self.p2)
            myfile.write('\n')
            myfile.close()
            again = input('do you want to play again Y/N? ')
            again.upper()
            print(again)
            if again == 'Y':
                S.restart()
            else:
                quit()
        while gameend == 3:
            r=battleships_battle_test_ai.battle_ai()
            gameend += r
        if gameend == 7:
            blank=''
            battleships_battle_test_ai.ai_choose(blank,True)
            self.p2 = battleships_battle_test_ai.ai_ship()
            myfile = open('battle_results','a')
            myfile.write(('ai won using {0} against {1}'.format(self.p2, self.p1)))
            print('ai won using {0} against {1}'.format(self.p2, self.p1))
            again = input('do you want to play again Y/N? ')
            again.upper()
            if again == 'Y':
                S.restart()
            else:
                quit()
        if gameend == 5:
            self.p2=battleships_battle_test_ai.ai_ship()
            print('player one won using {0} against {1}'.format(self.p1, self.p2))
            myfile = open('battle_results','a')
            myfile.write(('player one won using {0} against {1}'.format(self.p1, self.p2)))
            again = input('do you want to play again Y/N? ')
            again.upper()
            if again == 'Y':
                S.restart()
            else:
                quit()
        if gameend == 8:
            p2=battleships_battle_test_ai.ai_ship()
            print('player one won using {0} against  ai {1}'.format(self.p1, self.p2))
            myfile = open('battle_results','a')
            myfile.write(('player one won using {0} against ai {1}'.format(self.p1, self.p2)))
            again = input('do you want to play again Y/N? ')
            again.upper()
            if again == 'Y':
                S.restart()
            else:
                quit()
        else:
            print('player two won using {0} against {1}'.format(self.p2, self.p1))
            myfile = open('battle_results', 'a')
            myfile.write('player two won using ')
            myfile.write(self.p2)
            myfile.write(' with ')
            myfile.write(str(p2hp))
            myfile.write(' health left against ')
            myfile.write(self.p1)
            myfile.write('\n')
            myfile.close()
            again = input('do you want to play again Y/N? ')
            again.upper()
            if again == 'Y':
                S.restart()
            else:
                quit()

text_file_manger.read_text_file('C:\Users\MKnight.c82\OneDrive - The Cam Academy Trust\python\battleships project\study.txt')
S=Starting_up()
while True:
    S.game_management(gameend)