class box:
    #PRIVATE size:string
    #PRIVATE contents
    #PRIVATE lock:string
    #PRIVATE strength:integer
    def __init__(self,lockp,sizep,firstitem):
        self.__lock = lockp
        self.__size=sizep
        self.__strength = 100
        self.__contents[0] = firstitem

    def unlock(self,usercode):
        if usercode ==  self.__lock:
           return True
        else:
            self.__strength= self.__strength-1
        if  self.__strength < 1:
            return True
        else:
            return False
def LoadGame():
    filename = "Progress.txt"
    try:
        file = open(filename,"rt")
        GameData = file.read()
        file.close()
    except:
        print("file not found")