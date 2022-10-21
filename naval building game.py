import random
money = 30000
turn = 0
newship = False
idcv = 0
go = True
class Fleet():
        def __init__(self):
                fleet = []
                self.CV = random.randint(0, 3)
                self.BB = random.randint(2, 5)
                self.BC = random.randint(3, 5)
                self.CA = random.randint(3, 8)
                self.CL = random.randint(5, 11)
                self.DD = random.randint(11, 45)
                self.SS = -1
                self.dockspace_L=4
                self.dockspace_S=12
                self.money = 30000
                self.designation_1 = '  '
                self.designation_2 = '  '
                self.designation_3 = '  '
                self.designation_4 = '  '

        def start(self):
                if self.CV == 1:
                        print('you have {0} carrier'.format(self.CV))
                else:
                        print('you have {0} carriers'.format(self.CV))
                print('you have {0} battleships'.format(self.BB))
                print('you have {0} battlecrusiers'.format(self.BC))
                print('you have {0} heavy crusiers'.format(self.CA))
                print('you have {0} light crusiers'.format(self.CL))
                print('you have {0} destoryers'.format(self.DD))

        def i_d(self):
                i_d=''
                R=5
                lowercase = "abcdefghijklmnopqrstuvwxyz"
                while R >=0:
                        i_d += random.choice(lowercase)
                        R -=1
                return i_d
        

        def dockyard(self,name,designation,buildtime,size,cost,i_d):
                if designation == "CV" or "BB" or "BC" or "CA":
                        if self.dockspace_L == 0:
                                print("no large dockyard is avabile for construction of the requested ship so her designs will be placed on the plans folder")
                                f.plans()
                        else:
                                print("the {0} {1} has been layed down in dock {2} and will be finished in {3} turns".format(designation,name,self.dockspace_L,buildtime))
                                self.dockspace_L -= 1
                                buy=input('this will cost {0} do you want to buy it?'.format(cost))
                                if buy == 'yes':
                                        if cost > self.money:
                                                print('you cant afforc this')
                                                f.whole_shipyard()
                                                
                                        self.money = self.money - cost
                                        dock=self.dockspace_L + 1 
                                        f.constructing(name,designation,buildtime,size,cost,dock,'L',i_d)
                                else:
                                        f.plans()               
                else:
                        if self.dockspace_S == 0:
                                print('there is no small dockyard avabile for construction of the requested ship so her designs will be placed on the plans folder')
                                f.plans()
                        else:
                                 print("the {0} {1} has been layed down in dock {2} and will be finished in {3} turns".format(designation,name,self.dockspace_S,buildtime))
                                 self.dockspace_S -= 1
        def constructing(self,name,designation,buildtime,size,cost,dock,dock_type,i_d):
                if dock_type == 'L':
                        if dock == 1:
                                print('in dock one')
                                name_1=name
                                self.designation_1=designation
                                buildtime_1=buildtime
                                size_1=size
                                cost_1=cost
                                i_d_1=i_d
                                full_1 = True
                                f.whole_shipyard()
                        elif dock == 2:
                                print('in dock two')
                                name_2=name
                                self.designation_2=designation
                                buildtime_2=buildtime
                                size_2=size
                                cost_2=cost
                                i_d_2=i_d
                                full_2 = True
                                f.whole_shipyard() 
                        elif dock == 3:
                                print('in dock three')
                                name_3=name
                                self.designation_3=designation
                                buildtime_3=buildtime
                                size_3=size
                                cost_3=cost
                                i_d_3=i_d
                                full_3 = True
                                f.whole_shipyard()
                                
                        else:
                                print('in dock four')
                                name_4=name
                                self.designation_4=designation
                                buildtime_4=buildtime
                                size_4=size
                                cost_4=cost
                                i_d_4=i_d
                                full_4  = True
                                f.whole_shipyard()
        def whole_shipyard(self):
                print("""|----|  |----|  |----|  |----|
                         |    |  |    |  |    |  |    |
                         |    |  |    |  |    |  |    |
                         |{0} |  |{1} |  |{2} |  |{3} |                           
                         |    |  |    |  |    |  |    |
                         |----|  |----|  |----|  |----|""".format(self.designation_4,self.designation_3,self.designation_2,self.designation_1))
                pass 
                                         
class carrier(Fleet):
        def __init__(self):
                self.designation = "CV"

        def size(self):
                self.name =input("give your CV a name")
                self.i_d=f.i_d()
                self.size = int(input("enter the lenght of your CV"))
                self.airwing = int(input("enter the side of airgroup"))
                self.buildtime = round(self.size /12 + 11)
                self.cost = self.airwing+self.size*100
                self.built=False
                f.dockyard(self.name,self.designation,self.buildtime,self.size,self.cost,self.i_d)


                
f=Fleet()
f.start()
C=carrier()
while go == True:
        build = input('which ship class do you want to build?')
        if (build=='CV'):
                C.size()
        elif (build=='BB'):
                BBbuild()
        elif (build=='BC'):
                BCbuild()
        elif (build=='CA'):
                CAbuild()
        elif (build=='CL'):
                CLbuild()
        elif (build=='DD'):
                DDbuild()
        elif (build=='SS'):
                subbuild()
        else:
                print('not valid input')
                go = True
else:
        go = True

#while newship == True:
#global idcv
#if idcv == 20:
#   if


#class fleet:
 #def__init__self(CV,BC,BB,CA,Cl,DD,SS)
 #self.Cv = CV

#p2 = fleet('2,3,4,5,6,7,8,')
#print(p2.CV)

#class ship:
# def __init__(self, name, type,id,size,):
#  self.name = input('enter a name ')
# self.type = type
#self.id = id
#self.size = size

#p1 = ship("dragon", "CV",43,"medium", )

#print(p1.name)
#print(p1.type)
#print(p1.id)
#print(p1.CVnum)

#def CVbuild():
 # global CV
  #global idcv
#  global turn 
#  airgroup = input('what airgroup size do you want?..large,medium or small    ')
 # if   (airgroup=='large'):
##        airwing = 74
##        cost = 7000
##        buildtime = 10
##        newship = True
##        idcv = 20 
##        print('this cv will have a airwing of {0} the build time of {1} months and cost {2}'.format(airwing,buildtime,cost))
##        turn + 1
##  if   (airgroup=='medium'):
##        airwing = 54
##        cost = 5000
##        newship = True
##        idcv = 30 
##        print('this cv will have a airwing of {0} the build time of {1} months and cost {2}'.format(airwing,buildtime,cost))
##        buildtime = 7
##        turn + 1
##  if   (airgroup=='small'):
##        airwing = 34
##        cost = 3000
##        buildtime = 5
##        newship = True
##        idcv = 40  
##        class ship:
##           def_init_(self,id=1)
##           self.id
##           id 
##           shipname =(input('what is this CV called')) 
##        print('this cv will have a airwing of {0} the build time of {1} months and cost {2}'.format(airwing,buildtime,cost))
##
##        turn + 1
##CVbuild()
##def CVbuild():
##	global CV
##	global idcv
##	global turn
##	airgroup = input('what airgroup size do you want?..large,medium or small    ')
##	if (airgroup == 'large'):
##
##
##		print(
##		    'this cv will have a airwing of {0} the build time of {1} months and cost {2}'
##		    .format(airwing, buildtime, cost))
##		turn + 1
##	if (airgroup == 'medium'):
##
##		class ship:
##			def __init__(
##			    self,
##			    name,
##			    type,
##			    id,
##			    size,
##			):
##				self.name = input('enter a name ')
##				self.type = type
##				self.id = id
##				self.size = size
##				p1 = ship(
##				    "dragon",
##				    "CV",
##				    43,
##				    "medium",
##				)
##				print(p1.name)
##				print(p1.type)
##				print(p1.id)
##
##				#print('this cv will have a airwing of {0} the build time of {1} months and cost {2}'.format(airwing,buildtime,cost))
##
##	if (airgroup == 'small'):
##
##		def __init__(self, name, type, id, size, airwing, buildtime, cost):
##			self.name = name
##			self.type = type
##			self.id = id
##			self.id = size
##			self.id = airwing
##			self.id = buildtime
##			self.id = cost
##
##		shipname = (input('what is this CV called'))
##		self.airwing == 40
##		print('this cv will have a airwing of {0} the build time of {1} months and cost {2}'.format(self.airwing, id.buildtime, id.cost))
##
##		turn + 1
