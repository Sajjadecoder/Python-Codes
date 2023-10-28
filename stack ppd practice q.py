#DECLARE StackData:ARRAY[0:9] OF integer
#DECLARE StackPointer: integer
global StackData
global StackPointer
StackData = [""]*10
StackPointer = 0
def outputstack():
    global StackData
    global StackPointer
    for x in range(10):
        print(StackData[x])
    print(StackPointer)
def Push(val):
    global StackData
    global StackPointer
    if StackPointer>9:
        return False
    else:
        StackData[StackPointer] = val
        StackPointer += 1
        return True
for i in range(11):
    val = int(input("enter value "))
    if Push(val) == True:
        print("value added")
    else:
        print ("overflow")
print(StackData)