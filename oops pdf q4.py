class puzzleplayer:
    def __init__(self):
        self.__playerid = "PL12a3"
        self.__name = ""
        self.__score = 0
    def getplayerid(self):
        return self.__playerid

    def setplayerid(self,id):
        idlength = len(id)
        char = id[2:0]
        if idlength == 6 and char =="PL":
            self.__playerid = id
            return True
        else:
            return False
