#DECLARE arrayData[0:10,0:1] OF STRING
arrayData = [[""]*2 for i in range(11)]

def ReadHighScores():
    try:
        file = open("HighScore.txt","r")
        for x in range(10):
            arrayData[x][0] = file.readline().strip()
            arrayData[x][1] = file.readline().strip()
        file.close()
    except:
        print("file not found")
def OutputHighScores():
    for x in range(10):
        combine = arrayData[x][0] + " " + arrayData[x][1]
        print (combine)
ReadHighScores()
OutputHighScores()
class Balloon():
    def __init__(self,d,c):
        self.__Health = 100
        self.__Color = c
        self.__DefenceItem = d
    def getdefenceitem(self):
        return self.__DefenceItem
    def changehealth(self,newhealth):
        self.__Health =self.__Health + newhealth
    def checkhealth(self):
        if self.__Health <= 0:
            return True
        else:
            return False
item = input("enter defence item ")
colour = input("enter color ")
Balloon1 = Balloon(item,colour)
def Defend(ballonobj):
    strength = int(input("enter strength "))
    ballonobj.changehealth(-strength)
    print(ballonobj.getdefenceitem())
    if ballonobj.checkhealth() == True:
        print("no health")
    else:
        print("health remaining")
    return ballonobj


Balloon1= Defend(Balloon1)







