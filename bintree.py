#DECLARE arraynodes:ARRAY [0:20,0:3] OF INTEGER
arraynodes = [[0]*3 for x in range(20)]
rootpointer = -1
freenode = 0
def addnode():
    global rootpointer
    global freenode
    global arraynodes
    datatoinsert = int(input("enter data to insert: "))
    if freenode <= 19:
        arraynodes[freenode][0] = -1
        arraynodes[freenode][1] = datatoinsert
        arraynodes[freenode][2] = -1
        if rootpointer == -1:
            rootpointer = 0
        else:
            placed = False
            currentptr = rootpointer
            while placed == False:
                if datatoinsert < arraynodes[currentptr][1]:
                    #move left
                    if arraynodes[currentptr][0] == -1:
                        arraynodes[currentptr][0] = freenode
                        placed = True
                    else:
                        currentptr = arraynodes[currentptr][0]
                else:
                    # move right
                    if arraynodes[currentptr][2] == -1:
                        arraynodes[currentptr][2] = freenode
                        placed = True
                    else:
                        currentptr = arraynodes[currentptr][2]
        freenode = freenode + 1
    else:
        print("tree is full")

def searchnode():
    global rootpointer
    datatosearch = int(input("enter the data to search: "))
    currentptr = rootpointer
    while currentptr != -1 and arraynodes[currentptr][1] != datatosearch:
        if arraynodes[currentptr][1] > datatosearch:
            currentptr = arraynodes[currentptr][0]
        elif arraynodes[currentptr][1] < datatosearch:
            currentptr = arraynodes[currentptr][2]
    print (datatosearch, "Exists at location ",currentptr)

def inorder(array,root):
    if array[root][0] != -1: #left
        inorder(array,array[root][0])
    print(str(array[root][1]))#root
    if array[root][2] != -1:#right
        inorder(array,array[root][2])

def preorder(array,root):
    print(str(array[root][1]))#root
    if array[root][0] != -1:#left
        preorder(array,array[root][0])
    if array[root][2] != -1:#right
        preorder(array,array[root][2])

def postorder(array,root):
    if array[root][0] != -1:#left
        postorder(array,array[root][0])
    if array[root][2] != -1:#right
        postorder(array,array[root][2])
    print(str(array[root][1]))#root

for x in range(8):
    addnode()
inorder(arraynodes,rootpointer)