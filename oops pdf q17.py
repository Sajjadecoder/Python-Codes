class Account():
    def __init__(self,an,b):
        self.__AccountNumber = an
        self.__Balance = b
    def getaccountnumber(self):
        return self.__AccountNumber
    def getbalance(self):
        return self.__Balance
    def setaccountnumber(self,acc):
        self.__AccountNumber = acc
    def setbalance(self,bal):
        self.__Balance = bal
class SavingsAccount(Account):
    def __init__(self,an,b,paymentinterval,amount):
        super().__init__(an,b)
        self.__PaymentInterval = paymentinterval
        self.__Amount = amount