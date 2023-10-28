class foodItem:
    def __init__(self, nameP, codeP, costP):
        self.__name = nameP
        self.__code = codeP
        self.__cost = costP

    def getCode(self):
        return self.__code

    def getCost(self):
        return self.__cost


class vendingMachine:
    # PRIVATE items : Array [0:3]OF foodItem
    # PRIVATE moneyIn: real
    def __init__(self, item1, item2, item3, item4):
        self.__moneyIn = 0
        self.__items = []
        self.__items.append(item1)
        self.__items.append(item2)
        self.__items.append(item3)
        self.__items.append(item4)

    def checkValid(self, code):
        for x in range(4):
            if self.__items[x].getCode == code:
                if self.__moneyIn >= self.__items[x].getCost:
                    return x
                else:
                    return -2
        return -1
chocolate = foodItem("dairy",232,1)
sweets= foodItem("dair",2312,12)
sandwich = foodItem("dary",22,177)
apple = foodItem("dy",2,13)

Machine1 = vendingMachine(chocolate,sweets,sandwich,apple)
