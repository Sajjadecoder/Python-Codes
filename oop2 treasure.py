# oop2 MJ17 P42 Q3
import random

class IslandClass:
    def __init__(self):
        sand='.'
        self.__grid =[[sand for col in range (30)] for row in range (10)]

    def HideTreasure(self):
        treasure = 'T'
        row=random.randint(0,9)
        col=random.randint(0,29)
        while self.__grid[row][col]==treasure:
            row = random.randint(0,9)
            col = random.randint(0,29)

        self.__grid[row][col]==treasure

    def DigHole(self,row,col):
        sand='.'
        treasure = 'T'
        found = 'X'
        notfound = 'O'
        if self.__grid[row][col]==treasure:
            self.__grid[row][col]=found
        else:
            self.__grid[row][col]=notfound

    def GetSquare(self,row,col):
        return self.__grid[row][col]

Island = IslandClass()

def DisplayGrid():
    for row in range(10):
        for col in range (30):
            z=Island.GetSquare(row,col)
            print (z, end=" ")
        print ("")

def StartDig():
    x=int(input("enter row: "))
    while x<0 or x>9:
        x=int(input("enter valid row: "))
    y=int(input("enter column: "))
    while y<0 or y>29:
        y=int(input("enter valid column: "))

    Island.DigHole(x, y)

DisplayGrid()
for i in range (3):
        Island.HideTreasure()
StartDig()
DisplayGrid()
