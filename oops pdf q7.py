import random
class Character:
    def __init__(self,NameP):
        self.__Name = NameP
        self.__Skill = 0
        self.__Health = 50
        self.__Shield = random.randint(1,25)

    def GetSkill(self):
        return self.__Skill

    def SetSkill(self,newskill):
        if newskill < 10 or newskill > 25:
            return -1
        else:
            self.__Skill = self.__Skill + newskill
            if self.__Skill < 200:
                return 1
            if self.__Skill >= 200:
                self.__Skill = 200
                return 0
    def GetName(self):
        return self.__Name
#DECLARE CharacterArray: ARRAY [0:4] OF Character
CharacterArray = [""]*5
object = Character("Victory")
CharacterArray[0] = object


