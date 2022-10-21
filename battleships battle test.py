#pacmax42 2018-
#v0.1.0
#planned features for the future:

#location system using 1 as north 2 as east 3 as south and 4 as west(currenty under development in battle system test.py)
# this abobe inculed a speed system so ships can only move in a certain time so for example yspeed = 2 so it will take two turns to run any move command
#dud shells
#torpedos
#creating your own ships(also under development
#muti-ship battles based on a point per ships system to balance things a little
#ability to knock out turrets and engines
#weather systems
#night fights
#different maps
#submaire and air strike events
#add a more realistic damage system
#other ship types
#ai to play against
#crew and crew actions
#ranges to effect accuresary

#pipe dreams which most likly wont happen:

#actual control of where you fire
#external html site
#combine with naval building game.py at some distant point
#gui(some point in the very distante future)
#improving code so its more readable and less suffering(so uses classes and making it look lot nicer)
#discord bot functionlity possibly if I dont go insane learning how to do that in js again or try do it in python..and if my pc finaly accpects discord.js as a thing
#withdrawal and long term campain mode which comes with a whole host of other things like up1grades and comander skills
import random,time,sqlite3,os, text_file_manger
#from debug import Debug
#import sqlite3
import os
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
kgVgunsc = 14
kgVarmour = 14.7
kgVgunsn = 10
ygunsc = 18.1
yarmour = 16.1
ygunsn = 9
yhp = 1000
kgVhp = 700
p1hp = 0
p2hp = 0
p2gunsc = 0
p1armour = 0
p1gunsn = 0
p2gunsc = 0
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

def restart():
    start = True
    return valid_ship1


def battle():
    global p2location,p2moving,p2speed,p2direction,p1location,p1direction,p1first_smoke_shot,p1shots,p2shots, p2first_smoke_shot,p2movespeed, p1smoke_charges,p1speed, p2smoke_charges, reset, p1movespeed, gameend, p1moving, p1hp, p2hp, firstime, p1smoke, p2smoke, p1smoke_time, p2smoke_time, p1armour, p2gunsc, p1gunsn, p2armour, p2gunsc, p2gunsn, shots1, shots2, gameend, your_turn, their_turn, p1
    your_turn = 1
    their_turn = 1
    y = 0
    x = 0
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
    targethit = [1, 5, 2, 4, 6, 8, 10, 20, 22, 24, 26, 28, 34, 11]
    smoke_target_hit = [5, 9, 40, 27, 32, 15]
    while your_turn == 1:
        p1turn = input('player 1 pick  what to do 1:fire guns 2:deploy smoke screen3:move to a new place')
        if (p1turn == '1'):
            while shots1 != p1gunsn:
                y = y +1
                shot = random.randint(1, 40)
                d.variable('shot',shot)
                time.sleep(1)
                shots1 = shots1 + 1
                if p2smoke_time >= 1:
                    if p2first_smoke_shot == True:
                        p2smoke_time = p2smoke_time - 1
                        p2first_smoke_shot = False
                    if p2smoke_time == 0:
                        print('the cloud of smoke will disapate soon')
                    if shot in smoke_target_hit:
                        print('target hit')
                        magkaboom = random.randint(1, 300)
                        if magkaboom in magdet:
                            print('you detonated the enemy ammo,target sunk')
                            damage = p2hp
                            gameend = 1
                            return gameend
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
                                  return gameend
                    else:
                        print('you missed')
                else:
                    if p2smoke == True and p2smoke_time == 0:
                        print('the enemy smoke has disapated')
                        p2smoke = False
                    else:
                        if shot in targethit:
                            print('target hit')
                            magkaboom = random.randint(1, 100)
                            if magkaboom in magdet:
                                print('you detonated the enemy ammo,target sunk')
                                damage = p2hp
                                gameend = 1
                                return gameend
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
                                        return gameend
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
                if p1moving == False:
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
                else:
                    print('your ship is already moving')
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
                    while shots2 != p2gunsn:
                        x = x + 1
                        shot = random.randint(1, 40)
                        print('{0}'.format(shot))
                        time.sleep(1)
                        shots2 = shots2 + 1
                        if p1smoke_time >= 1:
                            if p1first_smoke_shot == True:
                                p1smoke_time = p1smoke_time - 1
                                if p1smoke == 0:
                                    print('the cloud will disapate soon')
                                    p1first_smoke_shot = False
                                    if shot in smoke_target_hit:
                                        print('target hit')
                                        magkaboom = random.randint(1, 300)
                                        if magkaboom in magdet:
                                            print('you detonated the enemy ammo,target sunk')
                                            damage = p2hp
                                            gameend = 4
                                            return gameend
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
                                                    return gameend
                                    else:
                                        print('you missed')
                            else:
                                if p1smoke == True and p1smoke_time == 0:
                                    print('the enemy smoke has disapated completely ')
                                    p1smoke = False
                        else:
                            if shot in targethit:
                                magkaboom = random.randint(1, 100)
                                if magkaboom in magdet:
                                    print('you detaneted the enermy ammo,target sunk')
                                    damage = p1hp
                                    gameend = gameend + 4
                                    return gameend
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
                                        return gameend
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
                    else:
                        print('your ship is already moving')
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
            global p2gunsc
            global p1armour
            global p1gunsn
            global p1hp
            global kgVhp
            print('you have picked a king goerge V class ship')
            p2gunsc = kgVgunsc
            p1armour = kgVarmour
            p1gunsn = kgVgunsn
            p1hp = kgVhp
def yamato():
            global ships
            global p2gunsc
            global p1armour
            global p1gunsn
            global yhp
            global p1hp
            global ship1
            print('you have picked a yamato class ship')
            p2gunsc = ygunsc
            p1armour = yarmour
            p1gunsn = ygunsn
            p1hp = yhp
def hood():
            global ships
            global p2gunsc
            global p1armour
            global p1gunsn
            global hhp
            global p1hp
            print('you have picked a hood class ship')
            p2gunsc = hgunsc
            p1armour = harmour
            p1gunsn = hgunsn
            p1hp = hhp
def kongo():
            global ships
            global p2gunsc
            global p1armour
            global p1gunsn
            global khp
            global p1hp
            print('you have picked a kongo class ship')
            p2gunsc = kgunsc
            p1armour = karmour
            p1gunsn = kgunsn
            p1hp = khp
def fuso():
            global ships
            global p2gunsc
            global p1armour
            global p1gunsn
            global fhp
            global p1hp
            print('you have picked a fuso class ship')
            p2gunsc = fgunsc
            p1armour = farmour
            p1gunsn = fgunsn
            p1hp = fhp
def nagato():
            global ships
            global p2gunsc
            global p1armour
            global p1gunsn
            global fhp
            global p1hp
            print('you have picked a nagato class ship')
            p2gunsc = ngunsc
            p1armour = narmour
            p1gunsn = ngunsn
            p1hp = nhp
def nelson():
            global ships
            global p2gunsc
            global p1armour
            global p1gunsn
            global fhp
            global p1hp
            print('you have picked a nelson class ship')
            p2gunsc = nelgunsc
            p1armour = nelarmour
            p1gunsn = nelgunsn
            p1hp = nelhp
def lion():
            global ships
            global p2gunsc
            global p1armour
            global p1gunsn
            global lhp
            global p1hp
            print('you have picked a lion class ship')
            p2gunsc = lgunsc
            p1armour = larmour
            p1gunsn = lgunsn
            p1hp = lhp
def queen_elizabeth():
            global ships
            global p2gunsc
            global p1armour
            global p1gunsn
            global lhp
            global p1hp
            print('you have picked a lion class ship')
            p2gunsc = lgunsc
            p1armour = larmour
            p1gunsn = lgunsn
            p1hp = lhp
def centurion():
            global ships
            global p2gunsc
            global p1armour
            global p1gunsn
            global chp
            global p1hp
            print('you have picked a centurion class ship')
            p2gunsc = cgunsc
            p1armour = carmour
            p1gunsn = cgunsn
            p1hp = chp
def Vangauard():
            global ships
            global p2gunsc
            global p1armour
            global p1gunsn
            global vhp
            global p1hp
            print('you have picked a Vangauard class ship')
            p2gunsc = vgunsc
            p1armour = varmour
            p1gunsn = vgunsn
            p1hp = vhp
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
    path = r"C:\Users\pacma\Documents\coding\python\battleships project\ships" #contiue work to save ships as indervidual files within ships folder
    os.mkdir(path)
    ship1=input('what name does this ship have? ')
    cushp=int(input('how much health does this ship have? '))
    cusarmour=float(input('how much armour does this ships belt have? '))
    cusgunsc=float(input('what caliber of guns does this ship have? '))
    cusgunsn=float(input('how many barrles does this ship have? '))
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
    list_ships = [ship1,cushp,cusarmour,cusgunsn,cgunsn]
    myfile.write(ship1.ship,list_ships)#this is broken and needs repairs
    p1gunsc = cusgunsc
    p1armour = cusarmour
    p1gunsn = cusgunsn
    p1hp = cushp

def ise():
            global ships
            global p2gunsc
            global p1armour
            global p1gunsn
            global ihp
            global p1hp
            print('you have picked a ise class ship')
            p2gunsc = igunsc
            p1armour = iarmour
            p1gunsn = igunsn
            p1hp = ihp
def tosa():
            global ships
            global p2gunsc
            global p1armour
            global p1gunsn
            global thp
            global p1hp
            print('you have picked a tosa class ship')
            p2gunsc = tgunsc
            p1armour = tarmour
            p1gunsn = tgunsn
            p1hp = thp
def custom_ship2():
    global ship2
    global p2gunsc
    global p2armour
    global p2gunsn
    global vhp
    global p2hp
    x = 1300
    a = 18
    b = 20
    f = 20
    list_ships = []
    y = text_file_manger.read_text_file('custom_ships.ship')
    print(y)
    ship2=input('what name does this ship have? ')
    cushp=int(input('how much health does this ship have? '))
    cusarmour=float(input('how much armour does this ships belt have? '))
    cusgunsc=float(input('what caliber of guns does this ship have? '))
    cusgunsn=float(input('how many barrles does this ship have? '))
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
    list_ships = [ship1,cushp,cusarmour,cusgunsn,cgunsn,pos]
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
            print('you have picked a tosa class ship')
            p2gunsc = tgunsc
            p2armour = tarmour
            p2gunsn = tgunsn
            p2hp = thp
def ise2():
            global ships
            global p2gunsc
            global p2armour
            global p2gunsn
            global ihp
            global p2hp
            print('you have picked a ise class ship')
            p2gunsc = igunsc
            p2armour = iarmour
            p2gunsn = igunsn
            p2hp = ihp
def fuso2():
            global ships
            global p2gunsc
            global p2armour
            global p2gunsn
            global fhp
            global p2hp
            print('you have picked a fuso class ship')
            p2gunsc = fgunsc
            p2armour = farmour
            p2gunsn = fgunsn
            p2hp = fhp
def lion2():
            global ships
            global p2gunsc
            global p2armour
            global p2gunsn
            global lhp
            global p2hp
            print('you have picked a lion class ship')
            p2gunsc = lgunsc
            p2armour = larmour
            p2gunsn = lgunsn
            p2hp = lhp
def Vangauard2():
            global ships
            global p2gunsc
            global p2armour
            global p2gunsn
            global vhp
            global p2hp
            print('you have picked a Vangauard class ship')
            p2gunsc = vgunsc
            p2armour = varmour
            p2gunsn = vgunsn
            p2hp = vhp
def hood2():
            global ships
            global p2gunsc
            global p2armour
            global p2gunsn
            global hhp
            global p2hp
            print('you have picked a hood class ship')
            p2gunsc = hgunsc
            p2armour = harmour
            p2gunsn = hgunsn
            p2hp = hhp
def nelson2():
            global ships
            global p2gunsc
            global p2armour
            global p2gunsn
            global nelhp
            global p2hp
            print('you have picked a nelson class ship')
            p2gunsc = nelgunsc
            p2armour = nelarmour
            p2gunsn = nelgunsn
            p2hp = nelhp
def nagato2():
            global ships
            global p2gunsc
            global p2armour
            global p2gunsn
            global nhp
            global p2hp
            print('you have picked a nagato class ship')
            p2gunsc = ngunsc
            p2armour = narmour
            p2gunsn = ngunsn
            p2hp = nhp
def centurion2():
            global ships
            global p2gunsc
            global p2armour
            global p2gunsn
            global chp
            global p2hp
            print('you have picked a centurion class ship')
            p2gunsc = cgunsc
            p2armour = carmour
            p2gunsn = cgunsn
            p2hp = chp
def kinggeorgeV2():
            global ships
            global p2gunsc
            global p2armour
            global p2gunsn
            global start
            global p2hp
            global kgVhp
            print('you have picked a king goerge V class ship')
            p2gunsc = kgVgunsc
            p2armour = kgVarmour
            p2gunsn = kgVgunsn
            p2hp = kgVhp
def yamato2():
            global ships
            global p2gunsc
            global p2armour
            global p2gunsn
            global start
            global p2hp
            global yhp
            print('you have picked a yamato class ship')
            p2gunsc = ygunsc
            p2armour = yarmour
            p2gunsn = ygunsn
            p2hp = yhp
def kongo2():
            global ships
            global p2gunsc
            global p2armour
            global p2gunsn
            global khp
            global p2hp
            print('you have picked a kongo class ship')
            p2gunsc = kgunsc
            p2armour = karmour
            p2gunsn = kgunsn
            p2hp = khp
def queen_elizabeth2():
            global ships
            global p2gunsc
            global p2armour
            global p2gunsn
            global qehp
            global p2hp
            print('you have picked a lion class ship')
            p2gunsc = qegunsc
            p2armour = qearmour
            p2gunsn = qegunsn
            p2hp = qehp
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




while valid_ship1 == False:
    if start == True:
        print(ukships[:])
        print(jships[:])
        start = False
    ship1 = input('player 1 pick a ship to play ')
    if (ship1 == 'yamato'):
        valid_ship1 = True
        yamato()
    elif (ship1 == 'musashi'):
        valid_ship1 = True
        yamato()
    elif (ship1 == 'duke of york'):
        valid_ship1 = True
        kinggeorgeV()
    elif (ship1 == 'howe'):
        valid_ship1 = True
        kinggeorgeV()
    elif (ship1 == 'king george V'):
        valid_ship1 = True
        kinggeorgeV()
    elif (ship1 == 'Prince of wales'):
        valid_ship1 = True
        kinggeorgeV()
    elif (ship1 == 'custom'):
        valid_ship1 = True
        custom_ship()
    elif (ship1 == 'hiei'):
        valid_ship1 = True
        kongo()
    elif (ship1 == 'kongo'):
        valid_ship1 = True
        kongo()
    elif (ship1 == 'kirashima'):
        valid_ship1 = True
        kongo()
    elif (ship1 == 'haruna'):
        valid_ship1 = True
        kongo()
    elif (ship1 == 'fuso'):
        valid_ship1 = True
        fuso()
    elif (ship1 == 'yamashiro'):
        valid_ship1 = True
        fuso()
    elif (ship1 == 'nagato'):
        valid_ship1 = True
        nagato()
    elif (ship1 == 'mutsu'):
        valid_ship1 = True
        nagato()
    elif (ship1 == 'nelson'):
        valid_ship1 = True
        nelson()
    elif (ship1 == 'rodney'):
        valid_ship1 = True
        nelson()
    elif (ship1 == 'lion'):
        valid_ship1 = True
        lion()
    elif (ship1 == 'queen elizabeth'):
        valid_ship1 = True
        queen_elizabeth()
    elif (ship1 == 'valiant'):
        valid_ship1 = True
        queen_elizabeth()
    elif (ship1 == 'malaya'):
        valid_ship1 = True
        queen_elizabeth()
    elif (ship1 == 'centurion'):
        valid_ship1 = True
        centurion()
    elif (ship1 == 'hood'):
        valid_ship1 = True
        hood()
    elif (ship1 == 'vangauard'):
        valid_ship1 = True
        Vangauard()
    elif (ship1 == 'ise'):
        valid_ship1 = True
        ise()
    elif (ship1 == 'tosa'):
        valid_ship1 = True
        tosa()
    else:
        print('not a vaild input')
while valid_ship2 == False:
    ship2 = input('player 2 pick a ship to play ')
    if (ship2 == 'yamato'):
        valid_ship2 = True
        yamato2()
    elif (ship2 == 'custom'):
        valid_ship2 = True
        custom_ship2()
    elif (ship2 == 'musashi'):
        valid_ship2 = True
        yamato2()
    elif (ship2 == 'duke of york'):
        valid_ship2 = True
        kinggeorgeV2()
    elif (ship2 == 'howe'):
        valid_ship2 = True
        kinggeorgeV2()
    elif (ship2 == 'king george V'):
        valid_ship2 = True
        kinggeorgeV2()
    elif (ship2 == 'Prince of wales'):
        valid_ship2 = True
        kinggeorgeV2()
    elif (ship2 == 'hiei'):
            valid_ship2 = True
            kongo2()
    elif (ship2 == 'kongo'):
        valid_ship2 = True
        kongo2()
    elif (ship2 == 'kirashima'):
        valid_ship2 = True
        kongo2()
    elif (ship2 == 'haruna'):
        valid_ship2 = True
        kongo2()
    elif (ship2 == 'fuso'):
        valid_ship2 = True
        fuso2()
    elif (ship2 == 'yamashiro'):
        valid_ship2 = True
        fuso2()
    elif (ship2 == 'nagato'):
        valid_ship2 = True
        nagato2()
    elif (ship2 == 'mutsu'):
        valid_ship2 = True
        nagato2()
    elif (ship2 == 'nelson'):
         valid_ship2 = True
         nelson2()
    elif (ship2 == 'rodney'):
        valid_ship2 = True
        nelson2()
    elif (ship2 == 'lion'):
        valid_ship2 = True
        lion2()
    elif (ship2 == 'queen elizabeth'):
        valid_ship2 = True
        queen_elizabeth2()
    elif (ship2 == 'Valiant'):
        valid_ship2 = True
        queen_elizabeth2()
    elif (ship2 == 'Malaya'):
        valid_ship2 = True
        queen_elizabeth2()
    elif (ship2 == 'centurion'):
        valid_ship2 = True
        centurion2()
    elif (ship2 == 'hood'):
        valid_ship2 = True
        hood2()
    elif (ship2 == 'vangauard'):
        valid_ship2 = True
        Vangauard2()
    elif (ship2 == 'ise'):
        valid_ship2 = True
        ise2()
    elif (ship2 == 'tosa'):
        valid_ship2 = True
        tosa2()
    else:
        print('not a vaild input')

# this is the stats of the ship and the how the code tells which ship has been picked by each player
while gameend == 0:
    battle()
if gameend == 1:
    print('player one won using {0} against {1}'.format(ship1, ship2))
    myfile = open('battle_results', 'a')
    myfile.write('player one won using ')
    myfile.write(ship1)
    myfile.write(' with ')
    myfile.write(str(p1hp))
    myfile.write(' health left against ')
    myfile.write(ship2)
    myfile.write('\n')
    myfile.close()
    again = input('do you want to play again Y/N? ')
    if (again == 'Y'):
        valid_ship1 = False
        valid_ship2 = False

        restart()
    else:
        quit()


else:
    print('player two won using {0} against {1}'.format(ship2, ship1))
    myfile = open('battle_results', 'a')
    myfile.write('player two won using ')
    myfile.write(ship2)
    myfile.write(' with ')
    myfile.write(str(p2hp))
    myfile.write(' health left against ')
    myfile.write(ship1)
    myfile.write('\n')
    myfile.close()
    again = input('do you want to play again Y/N? ')
    if (again == 'Y'):
        valid_ship1 = False
        valid_ship2 = False
        restart()
    else:
        quit()


