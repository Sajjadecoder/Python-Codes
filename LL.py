class node:
    def __init__(self):
        self.data = ""
        self.pointer = -1

global freeptr
global newnodeptr
global thisnodeptr
global startptr
global prevnodeptr
freeptr = 0
newnodeptr = 0
thisnodeptr = 0
startptr = 0
prevnodeptr = -1
list = [node() for x in range(5)]

def initializeLL():
    for i in range(4):
        list[i].data = ""
        list[i].pointer = i + 1
    list[4].pointer = -1

def insertnode(item):
    global list, freeptr, newnodeptr, thisnodeptr, startptr, prevnodeptr
    if freeptr == -1:
        print("list is full")
    else:
        newnodeptr = freeptr
        list[newnodeptr].data = item
        freeptr = list[freeptr].pointer
        thisnodeptr=startptr
        try:
            while thisnodeptr != -1 and list[thisnodeptr].data<item:
                prevnodeptr = thisnodeptr
                thisnodeptr = list[thisnodeptr].pointer
        except:
            pass
        if prevnodeptr == -1:
            list[newnodeptr].pointer = startptr
            startptr = newnodeptr
        else:
            list[newnodeptr].pointer = list[prevnodeptr].pointer
            list[prevnodeptr].pointer = newnodeptr

def deletenode():
    global list, freeptr,startptr
    datatoremove = int(input("enter the data to remove: "))
    thisnodeptr = startptr
    prevnodeptr = -1
    while thisnodeptr != -1 and list[thisnodeptr].data != datatoremove:
        prevnodeptr = thisnodeptr
        thisnodeptr = list[thisnodeptr].pointer
    if thisnodeptr == -1:
        return False
    else:
        if thisnodeptr == startptr:
            startptr = list[startptr].pointer
        else:
            list[prevnodeptr].pointer = list[thisnodeptr].pointer
            list[thisnodeptr].pointer = freeptr
            freeptr = thisnodeptr
            return True
def searchnode(val):
    currentptr = startptr
    while currentptr != -1 and list[currentptr].data != val:
        prevnodeptr = currentptr
        currentptr = list[currentptr].pointer
    if currentptr == -1:
        print("not found")
    else:
        print (currentptr)