import random


arrayData = [['']*10 for x in range(10)]

for x in range(10):
    for y in range(10):
        arrayData[x][y] = random.randint(1,100)
def outputall():
    print(arrayData)

outputall()
ArrayLength = 10
for x in range(9):
    for y in range(8):
        for z in range(ArrayLength-y-1):
            if arrayData[x][z]>arrayData[x][z+1]:
                tempval = arrayData[x][z]
                arrayData[x][z] = arrayData[x][z+1]
                arrayData[x][z+1] = tempval
outputall()

