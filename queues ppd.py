names=[""] * 10
headpointer = -1
tailpointer = 0
def enqueue(data):
    global headpointer, tailpointer, names
    if tailpointer < 10:
        names[tailpointer] = data
        tailpointer += 1

        if headpointer == -1:
            headpointer = 0
    else:
        print ("queue is full")
def dequeue():
    global headpointer, tailpointer, names
    if headpointer == -1:
        print ("queue is empty")
    else:
        item = names[headpointer]
        names[headpointer] = ""
        headpointer += 1
        print (item)

enqueue("taha")
enqueue("ali")
enqueue("sajjad")
enqueue("ahmed")
enqueue("rizvi")
dequeue()
dequeue()
print(names)