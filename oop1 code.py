# oop1 MJ18 p41
class GameElement:
    def __init__(self , x , y , w , h , ifn):
        self.__PositionX  = x
        self.__PositionY = y
        self.__Width = w
        self.__Height = h
        self.__ImageFileName = ifn

    def GetDetails(self):
        details = "Position X is: " + str(self.__PositionX) + " " + "Position Y is: " + \
            str(self.__PositionY) + " " + "width is: " + str(self.__Width) + " " + "height is: " + \
            str(self.__Height) + " " + "Filename: " + self.__ImageFileName
        return details

class Scenery(GameElement):
    def __init__(self , x , y , w , h , ifn , cd , dp):
        super().__init__(x , y , w , h , ifn)
        self.__CauseDamage = cd
        self.__DamagePoints = dp

    def GiveDamagePoints(self,cd,dp):
        if self.__CauseDamage is True:
            return self.__DamagePoints
        else:
            self.__DamagePoints=0
            return self.__DamagePoints

    def GetScenery(self):
        details = super().GetDetails() + " " + "cause damage: " + \
            str(self.__CauseDamage) + " "+ "Damage points: " + str(self.__DamagePoints)
        return details


giftBox = Scenery(150, 150 , 50 , 75 , "box.png" , False , 50)
print(giftBox.GetScenery())






