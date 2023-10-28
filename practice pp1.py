#DECLARE nameData:ARRAY [0:6] OF STRING
nameData = ["Farjad","Khadija","Ali","Mazin","Taha","Fakhir","Zainab"]
def linearSearch (findname):
    for i in range(7):
        if nameData[i] == findname:
            return True
    return False
findname = input("enter the name to search: ")
found = linearSearch(findname)
if found == True:
    print(findname," was found")
else:
    print("not found")

def insertionSort():
    for x in range(1,7):
        thischar = nameData[x]
        holeposition = x
        while holeposition > 0 and thischar < nameData[holeposition-1]:
            nameData[holeposition] = nameData[holeposition-1]
            holeposition = holeposition - 1
        nameData[holeposition] = thischar
insertionSort()
print(nameData)

#q2
class Box:
    def __init__(self,size,item,code):
        self.__Size = size
        self.__Lock = code
        self.__Strength = 100
        self.__Contents = [""]*10
        self.__Contents[0] = item
    def Unlock(self,thiscode):
        if thiscode == self.__Lock:
            return True
        else:
            self.__Strength = self.__Strength - 1
            if self.__Strength < 1:
                return True
            else:
                return False

    def GetContents(self):
        return self.__Contents
