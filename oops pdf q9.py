class PrintAccount:
    def __init__(self,fname,lname,id):
        self.__FirstName = fname
        self.__LastName = lname
        self.__PrintID = id
        self.__Credits = 50

    def SetFirstName(self,FirstnameP):
        self.__FirstName = FirstnameP
    def GetName(self):
        name = self.__FirstName + self.__LastName
        return name
    def AddCredits(self,MoneyInput):
        paymentcredits = MoneyInput*25
        if MoneyInput >= 20:
            self.__Credits = self.__Credits + paymentcredits + 50
        elif MoneyInput>= 10 and MoneyInput<= 19:
            self.__Credits = self.__Credits + paymentcredits + 25
        else:
            self.__Credits = self.__Credits + paymentcredits
#DECLARE StudentAccounts: ARRAY [0:999] OF PrintAccounts
def CreateID(first,last):
    first = first[0:3].lower()
    last = last[0:3].lower()
    PrintID = first + last + str(1)
    isadded = False
    x = 0
    while isadded == False:
        if StudentAccounts[x].GetPrintID ==
