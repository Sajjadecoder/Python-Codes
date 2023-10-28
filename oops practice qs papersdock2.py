class Balloon:
    # PRIVATE Health:integer
    # PRIVATE Colour:string
    # PRIVATE DefenceItem:string
    def __init__(self, DefenceItemP, ColourP):
        self.Health = 100
        self.Colour = ColourP
        self.DefenceItem = DefenceItemP

    def GetDefenceItem(self):
        return self.DefenceItem

    def ChangeHealth(self, HealthP):
        self.Health = self.Health + HealthP

    def CheckHealth(self):
        if self.Health <= 0:
            return True
        else:
            return False


temp = input("Enter defence item: ")
temp2 = input("Enter colour: ")
Balloon1 = Balloon(temp, temp2)


def Defend(balloonobj):
    x = int(input("enter opponent's strength: "))
    balloonobj.ChangeHealth(-x)
    print (balloonobj.GetDefenceItem())
    flag = balloonobj.CheckHealth()
    if flag == True:
        print ("No health remaining")
    else:
        print ("Health remaining")
    return balloonobj


Balloon1 = Defend(Balloon1)









