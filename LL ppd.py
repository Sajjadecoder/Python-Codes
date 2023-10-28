#unordered ll
class node:
    #PUBLIC data, nextnode : integer
    def __init__(self,datap, nextnodep):
        self.data = datap
        self.nextnode = nextnodep

#DECLARE linkedlist:ARRAY [0:9] OF node
linkedlist = [node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6),node(0,8),node(56,3),node(0,9),node(0,-1)]
startptr = 0
freelistptr = 5

def addnode(currentpointer):
    global freelistptr,linkedlist
    data= int(input("enter the data to add: "))
    if freelistptr<0 or freelistptr>9:
        return False
    else:
        linkedlist[freelistptr].data = data
        linkedlist[freelistptr].nextnode = -1
        prevpointer = 0
        while currentpointer != -1:
            prevpointer = currentpointer
            currentpointer = linkedlist[currentpointer].nextnode

        linkedlist[prevpointer].nextnode = freelistptr
        freelistptr = linkedlist[freelistptr].nextnode
        return True

def deletenode():
    global linkedlist, freelistptr,startptr
    datatoremove = int(input("enter the data to remove: "))
    currentpointer = startptr
    while currentpointer != -1 and linkedlist[currentpointer].data != datatoremove:
        prevpointer = currentpointer
        currentpointer = linkedlist[currentpointer].nextnode
    if currentpointer == -1:
        return False
    else:
        if currentpointer == startptr:
            startptr = linkedlist[startptr].nextnode
        else:
            linkedlist[prevpointer].nextnode = linkedlist[currentpointer].nextnode
            linkedlist[currentpointer].nextnode = freelistptr
            freelistptr = currentpointer
            return True

x = int(input("enter 1 to add, 2 to delete, -1 to end"))
while x != -1:
    if x == 1:
        flag = addnode(0)
        print (flag)
    else:
       flag = deletenode()
       print (flag)
    x = int(input("enter 1 to add, 2 to delete, -1 to end"))
print (linkedlist)