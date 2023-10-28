class Picture():
    def __init__(self,desP,WidP,HeiP,fc):
        self.__Description = desP
        self.__Width = WidP
        self.__Height = HeiP
        self.__FrameColor = fc
    def GetDescription(self):
        return self.__Description
    def GetWidth(self):
        return self.__Width
    def GetHeight(self):
        return self.__Height
    def GetColor(self):
        return self.__FrameColor
    def SetDescription(self,newdescription):
        self.__Description = newdescription
    #DECLARE PictureArray:ARRAY[1:100] OF Picture
def ReadData():
    x = 0
    try:
        file = open("Pictures.txt","r")
        description = file.readline().strip()
        while description != "":
            width = file.readline().strip()
            height = file.readline().strip()
            framecolor = file.readline().strip()
            PictureArray[x]= Picture(description,width,height,framecolor)
            x = x + 1
            description = file.readline().strip()
        file.close()
        return x
    except:
        print ("file not found")
colour = input("enter color ")
colour = colour.lower()
maxwidth = int(input("max width "))
maxheight = int(input("max height "))
for i in range(100):
    if PictureArray[i].GetColor == colour:
        print(PictureArray[i].GetDescription)
        print(PictureArray[i].GetColor)
        print(PictureArray[i].GetHeight)
        print(PictureArray[i].GetWidth)