class TreasureChest():
    def __init__(self,q,a,p):
        self.__question = q
        self.__answer = a
        self.__points = p
def readData():
    try:
        file = open("TreasureChestData.txt","r")
        question = file.readline().strip()
        while question != ""
            answer = file.readline().strip()
            points = file.readline().strip()
            newobj = TreasureChest(question,answer,points)
            arrayTreasure.append(newobj)
        file.close()
    except:
        print("file not found")