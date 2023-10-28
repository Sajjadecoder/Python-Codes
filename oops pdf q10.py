class Player:
    def __init__(self,InputPlayerID):
        self.__Score = 0
        self.__Category = "Not Qualified"
        self.__PlayerID = InputPlayerID
    def GetScore(self):
        return self.__Score
    def GetCategory(self):
        return self.__Category
    def GetPlayerID(self):
        return self.__PlayerID
    def SetPlayerID(self):
        newID = input("enter new player id: ")
        IDlength = len(newID)
        valid = False
        while valid == False:

            if IDlength <= 15 and IDlength >= 4:
                self.__PlayerID = newID
                valid = True
            else:
                newID = input("enter a valid id: ")
    def SetScore(self,ScoreInput):
            if ScoreInput >= 0 and ScoreInput <= 150:
                self.__Score = ScoreInput
                return True
            else:
                print ("invalid score input ")
                return False

    def SetCategory(self):
        if self.__Score>120:
            self.__Category = "Advanced"
        elif self.__Score>80 and self.__Score<=120:
            self.__Category = "Intermediate"
        elif self.__Score>=50 and self.__Score<= 80:
            self.__Category = "Beginner"
        else:
            self.__Category = "Not Qualified"
def CreatePlayer():
    playerid = input("enter a player id: ")
    score = int(input("enter a score: "))
    JoannePlayer = Player(playerid)
    if JoannePlayer.SetScore(score) == False:
        print("invalid score input")
    else:
        JoannePlayer.SetCategory()
        print (JoannePlayer.GetCategory())
CreatePlayer()