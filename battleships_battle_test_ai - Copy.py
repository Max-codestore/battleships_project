import random,time,text_file_manger
from decimal import Decimal
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
p1gunsc= 0
p1armour = 0
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
y = 0
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
ship2 =''
hit_scored1 = False
zero_in2 = 11
hit_scored2 = False
x = zero_in1 + 1
hit1=False
hit2=False
true_range1 = round(random.uniform(5, 60), 1)
true_range2 = round(random.uniform(5, 60), 1)
range_finder_damage1 = 0
range_finder_damage2 = 0
targethit1 = False
targethit2 = False
f = []
class Debug:
    def variable(self, name: str, value: any) -> None:
        print("[VARIABLE]: %s = %s" % (name, value))

    def function(self, name: str, args: dict) -> None:
        _args = ''

        for name, val in args.items():
            _args += "{0}: {1},".format(name, val)

        _args = _args[:len(_args) - 1]
        print("[FUNCTION]: Executed '%s' with '%s' as arguments." % (name, _args))
d=Debug()
def reset():
    global start,targethit1,p1speed,shots1,shots2,p2speed,p1turrets,p2turrets,ship2,hit_scored2,hit_scored1,zero_in2,zero_in1,x,hit1,hit2,range_finder_damage2,range_finder_damage1,targethit2,targethit2,reset,p1smoke,p1smoke_time,p2smoke_time,p2smoke,gameend,firstime,your_turn,their_turn,y,p1smoke_charges,p2smoke_charges,p1first_smoke_shot,p2first_smoke_shot,p1moving,p1location,p2location,p2moving
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
    y = 0
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
    p1turrets = []
    p2turrets = []
    ship2 = ''
    hit_scored1 = False
    zero_in2 = 11
    hit_scored2 = False
    x = zero_in1 + 1
    hit1 = False
    hit2 = False
    range_finder_damage1 = 0
    range_finder_damage2 = 0
    targethit1 = False
    targethit2 = False
def range_finder(true_range,hit_scored,damaged,zero_in,smoke):
    zero_in -= 1
    if damaged >= 4:
        message = ['....','EORROR 4234','...............','*indistinguable screaming*','*broken fax noices*','N/A','???????','*flames*']
        esimate = random.choice(message)
        return esimate
    if zero_in <= 0:
        zero_in = 0
    if hit_scored == True and smoke == False:
        estimate = true_range + round(random.uniform(1, 3)) - round(random.uniform(1, 3)) + damaged
        return estimate
    elif hit_scored == True and smoke == True:
        estimate = true_range + round(random.uniform(1, 3)) - round(random.uniform(1, 3)) + damaged
        return estimate
    if smoke == True:
        long_or_short = random.randint(0,1)
        if long_or_short == 1:
            estimate = true_range + round(random.uniform(0,zero_in+3),1) + damaged
        else:
            estimate = true_range - round(random.uniform(0,zero_in+3),1) - damaged
        return estimate
    else:
        long_or_short = random.randint(0,1)
        if long_or_short == 1:
            estimate = true_range + round(random.uniform(0,zero_in),1) + damaged
        else:
            estimate = true_range - round(random.uniform(0,zero_in),1) - damaged
        return estimate

def tosa2():
            global ships
            global p2gunsc
            global p2armour
            global p2gunsn
            global thp
            global p2hp
            global p2turrets
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
            p2gunsc = igunsc
            p2armour = iarmour
            p2gunsn = igunsn
            p2hp = ihp
            p2turrets = [2,2,2,2,2]
def fuso2():
            global ships
            global p2gunsc
            global p2armour
            global p2gunsn
            global fhp
            global p2hp
            global p2turrets
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
            p2gunsc = qegunsc
            p2armour = qearmour
            p2gunsn = qegunsn
            p2hp = qehp
            p2turrets = [2,2,2,2]
def set_ranges(range1,range2):
    global true_range1,true_range2
    true_range1 = range1
    true_range2 = range2
    gameend = 3
    return gameend
def ai_choose(choice: str, won: bool):
    global f
    if won == False:
        f.append(choice)
    else:
        text_file_manger.append_file_list('study.txt',f)
        h=text_file_manger.read_text_file('study.txt')
        return h
range_set = False
def battle_ai(gameend):
    global range_finder_damage1,range_finder_damage2,hit1,hit2,p2location, p2moving,p1turrets,p2turrets,p2speed, p2direction, p1location, p1direction, p1first_smoke_shot, p1shots, p2shots, p2first_smoke_shot, p2movespeed, p1smoke_charges, p1speed, p2smoke_charges, reset, p1movespeed, p1moving, p1hp, p2hp, firstime, p1smoke, p2smoke, p1smoke_time, p2smoke_time, p1armour, p2gunsc, p1gunsn, p2armour, p1gunsc, p2gunsn, shots1, shots2,your_turn, their_turn, p1,range_set,true_range1,true_range2
    if p1gunsc == p2gunsc:
        true_range2 = true_range1
    if p2hp <= 0:
        p2hp = 0
        gameend = 5
        range_set = False
        shots1 = 0
        return gameend
    if p1hp <= 0:
        p1hp = 0
        gameend = gameend + 4
        range_set = False
        shots2 = 0
        return gameend
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
    while your_turn == 1:
        p1turn = input('player 1 pick  what to do 1:fire guns 2:deploy smoke screen3:move to a new place')
        if (p1turn == '1'):
            solution = range_finder(true_range1, hit1, range_finder_damage1, zero_in1,p2smoke)
            print(solution)
            player1elevation = float(input("enter the elevation to fire at "))
            player1spreed=input("do you want to fire with a narrow spreed or wide spreed")
            player1spreed.lower()
            if p2smoke_time >= 1:
                if p2first_smoke_shot == True:
                    p2smoke_time = p2smoke_time - 1
                    if p2smoke == 0:
                        print('the cloud will disapate soon')
                        p2first_smoke_shot = False
            else:
                if p2smoke == True and p2smoke_time == 0:
                    print('the enemy smoke has disapated')
                    p2smoke = False
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
                if true_range1 - 1 <= shot <= true_range1 + 1:
                            print('target hit')
                            hit1=True
                            magkaboom = disperstion
                            a = random.randint(0, 10)
                            if magkaboom == true_range1 and a == 1:
                                print('critial hit')
                                print('you detonated the enemy ammo,target sunk')
                                damage = p2hp
                                gameend = 5
                                p2hp = p2hp - damage
                                range_set = False
                                shots1 = 0
                                return gameend
                            if magkaboom == true_range1 and a == 5:
                                print('critial hit..Ai turret has broken')
                                r = random.choice(p2turrets)
                                p2turrets.remove(r)
                                p2gunsn = p2gunsn - r
                                damage = int(random.randint(3, 7) * p1gunsc - p2armour)
                                p2hp = p2hp - damage
                            if magkaboom == true_range1 and a == 10:
                                print('critical hit..the AI rangefinders damaged ')
                                range_finder_damage2 += 1
                                damage = int(random.randint(1, 3) * p1gunsc - p2armour)
                                p2hp = p2hp - damage
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
                                        gameend = 5
                                        range_set = False
                                        shots1 = 0
                                        return gameend
                else:
                    print('you missed')
                    if p2hp <= 0:
                        p2hp = 0
                        gameend = 5
                        range_set = False
                        return gameend
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
            print('ai has {0} hp'.format(p2hp))
            shots1 = 0
            p2movespeed = p2speed
            if p2moving == True:  # if the ship is already moving this contiues it and allows for p1speed vaules to be taken in
                p2movespeed = p2movespeed - 1
                print('ai ship is moving...')
                if p2movespeed <= 0:
                    p2movespeed = p2speed
                    if p2direction == 1:
                        p2location = 1
                        print('ai reached north')
                        p2moving = False
                    elif p2direction == 2:
                        p2location = 2
                        p2moving = False
                        print('ai reached east')
                    elif p2direction == 3:
                        p2location = 3
                        print('ai reached south')
                        p2moving = False
                    elif p2direction == 4:
                        print('ai reached west')
                        p2location = 4
                        p2moving = False
            if p2location >= 5:
                p2location = 1
            if p2location <= 0:
                p2location = 1
            while their_turn == 1:
                action = ['1','1','1','1''1','2','3']
                p2turn = random.choice(action)
                ai_choose(p2turn,False)
                if (p2turn == '1'):
                    solution = range_finder(true_range2, hit2, range_finder_damage2, zero_in2,p1smoke)
                    player2elevation = solution
                    if hit2 == True:
                        player2spreed= 'narrow'
                    else:
                        player2spreed = 'wide'
                    player2spreed.lower()
                    if p1smoke_time >= 1:
                        if p1first_smoke_shot == True:
                            p1smoke_time = p1smoke_time - 1
                            if p1smoke == 0:
                                print('the cloud will disapate soon')
                                p1first_smoke_shot = False
                    else:
                        if p1smoke == True and p1smoke_time == 0:
                            print('the enemy smoke has disapated')
                            p1smoke = False
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
                        if true_range2 - 1 <= shot <= true_range2 + 1:
                            print('target hit')
                            hit2 = True
                            magkaboom = disperstion
                            a = random.randint(0, 10)
                            if magkaboom == true_range2 and a == 1:
                                print('critial hit')
                                print('the ammo exploded,we sunk')
                                damage = p1hp
                                gameend = 4
                                p1hp = p1hp - damage
                                range_set = False
                                shots2 = 0
                                return gameend
                            if magkaboom == true_range2 and a == 5:
                                print('critial hit..our  turret crippled')
                                r = random.choice(p1turrets)
                                p1gunsn = p1gunsn - r
                                p1turrets.remove(r)
                                damage = int(random.randint(3, 7) * p1gunsc - p2armour)
                                p1hp = p1hp - damage
                                print(' ai did {0} damage'.format(damage))
                            if magkaboom == true_range2 and a == 10:
                                print('critical hit..our range finder hit')
                                range_finder_damage1 += 1
                                damage = int(random.randint(1, 3) * p1gunsc - p2armour)
                                p1hp = p1hp - damage
                                print(' ai did {0} damage'.format(damage))
                                p1hp = p1hp - damage
                            else:
                                damage = int(random.randint(1, 5) * p2gunsc - p1armour)
                            if damage <= 0:
                                damage = damage * 0
                                print('failed to penatrate target')
                            print(' ai did {0} damage'.format(damage))
                            p1hp = p1hp - damage
                            if p1hp <= 0:
                                p1hp = 0
                                gameend = 4
                                range_set = False
                                shots2 = 0
                                return gameend
                        else:
                            print('target missed')
                else:
                        their_turn = 0
                if (p2turn == '2'):
                    print('depolying smoke screen..')
                    p2smoke = True
                    p2smoke_time = 2
                    their_turn = 0
                    p2first_smoke_shot = True
                    if p2smoke_time >= 1:
                        p1first_smoke_shot = True
                elif (p2turn == '3'):
                    if p2moving == False:
                        direction = ['north','south','east','west']
                        p2move = random.choice(direction)
                        if p2move == 'north':
                            p2moving = True
                            p2direction = 1
                            print('ai sails north')
                            their_turn = 0
                        elif p2move == 'south':
                            p2moving = True
                            p2direction = 3
                            print('ai sails south')
                            their_turn = 0
                        elif p2move == 'east':
                            p2moving = True
                            p2direction = 2
                            print('ai sails east')
                            their_turn = 0
                        elif p2move == 'west':
                            p2moving = True
                            p2direction = 4
                            print('ai sails west')
                            their_turn = 0
                        else:
                            print('not a possible direction.skipping turn..')
                            their_turn = 0
                    else:
                        print('ai ship is already moving')
            else:
                print('out of shots')
                print('you have {0} hp'.format(p1hp))
                shots1 = 0
                shots2 = 0
                reset = True
                firstime = False
                shots2 = 0
                return gameend

def ai_ship():
    global ship2
    return ship2

def ai_selection(p1h,p1armou,p1guns,p1guncs,p1turret):
    global valid_ship2,p1hp,p1armour,p1gunsn,p1gunsc,p1turrets,ship2
    p1hp = p1h
    p1armour = p1armou
    p1gunsn = p1guns
    p1gunsc = p1guncs
    p1turrets = p1turret
    valid_ship2 = False
    while valid_ship2 == False:
        ship2 = random.randint(0,25)
        if ship2 == 1:
            ship2 ='ai yamato'
            print('ai choose {0}'.format(ship2))
            valid_ship2 = True
            yamato2()
            return ship2
        elif ship2 == 2:
            ship2 = 'ai musashi'
            print('ai choose {0}'.format(ship2))
            valid_ship2 = True
            yamato2()
            return ship2
        elif ship2 == 3:
            ship2 = 'ai duke of york'
            print('ai choose {0}'.format(ship2))
            valid_ship2 = True
            kinggeorgeV2()
            return ship2
        elif ship2 == 4:
            ship2 = 'ai howe'
            print('ai choose {0}'.format(ship2))
            valid_ship2 = True
            kinggeorgeV2()
            return ship2
        elif ship2 == 5:
            ship2 = 'ai king george V'
            print('ai choose {0}'.format(ship2))
            valid_ship2 = True
            kinggeorgeV2()
            return ship2
        elif ship2 == 6:
            ship2 = 'ai prince of wales'
            print('ai choose {0}'.format(ship2))
            valid_ship2 = True
            kinggeorgeV2()
            return ship2
        elif ship2 == 7:
            ship2 = 'ai hiei'
            print('ai choose {0}'.format(ship2))
            valid_ship2 = True
            kongo2()
            return ship2
        elif ship2 == 8:
            ship2 = 'ai kongo'
            print('ai choose {0}'.format(ship2))
            valid_ship2 = True
            kongo2()
            return ship2
        elif ship2 == 9:
            ship2 = 'ai kirashima'
            print('ai choose {0}'.format(ship2))
            valid_ship2 = True
            kongo2()
            return ship2
        elif ship2 == 10:
            ship2 = 'ai haruna'
            print('ai choose {0}'.format(ship2))
            valid_ship2 = True
            kongo2()
            return ship2
        elif ship2 == 11:
            ship2 = 'ai fuso'
            print('ai choose {0}'.format(ship2))
            valid_ship2 = True
            fuso2()
            return ship2
        elif ship2 == 12:
            ship2 = 'ai yamashiro'
            print('ai choose {0}'.format(ship2))
            valid_ship2 = True
            fuso2()
            return ship2
        elif ship2 == 13:
            ship2 = 'ai nagato'
            print('ai choose {0}'.format(ship2))
            valid_ship2 = True
            nagato2()
            return ship2
        elif ship2 == 14:
            ship2 = 'ai mutsu'
            print('ai choose {0}'.format(ship2))
            valid_ship2 = True
            nagato2()
            return ship2
        elif ship2 == 15:
            ship2 = 'ai nelson'
            print('ai choose {0}'.format(ship2))
            valid_ship2 = True
            nelson2()
            return ship2
        elif ship2 == 16:
            ship2 = 'ai rodney'
            print('ai choose {0}'.format(ship2))
            valid_ship2 = True
            nelson2()
            return ship2
        elif ship2 == 17:
            ship2 = 'ai lion'
            print('ai choose {0}'.format(ship2))
            valid_ship2 = True
            lion2()
            return ship2
        elif ship2 == 18:
            ship2 = 'ai queen elizabeth'
            print('ai choose {0}'.format(ship2))
            valid_ship2 = True
            queen_elizabeth2()
            return ship2
        elif ship2 == 19:
            ship2 = 'ai valiant'
            print('ai choose {0}'.format(ship2))
            valid_ship2 = True
            queen_elizabeth2()
            return ship2
        elif ship2 == 20:
            ship2 = 'ai malaya'
            print('ai choose {0}'.format(ship2))
            valid_ship2 = True
            queen_elizabeth2()
            return ship2
        elif ship2 == 21:
            ship2 = 'ai centurion'
            print('ai choose {0}'.format(ship2))
            valid_ship2 = True
            centurion2()
            return ship2
        elif ship2 == 22:
            ship2 = 'ai hood'
            print('ai choose {0}'.format(ship2))
            valid_ship2 = True
            hood2()
            return ship2
        elif ship2 == 23:
            ship2 = 'ai vanguard'
            print('ai choose {0}'.format(ship2))
            valid_ship2 = True
            Vangauard2()
            return ship2
        elif ship2 == '24':
            ship2 = 'ai ise'
            print('ai choose {0}'.format(ship2))
            valid_ship2 = True
            ise2()
            return ship2
        elif ship2 == 25:
            ship2 = 'ai tosa'
            print('ai choose {0}'.format(ship2))
            valid_ship2 = True
            tosa2()
            return ship2
        else:
            pass
