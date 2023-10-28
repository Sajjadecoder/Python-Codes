Queue = []
for i in range(5):
    Queue.append("")
global startptr
global queueptr
startptr = -1
queueptr = 0

def Enqueue(val):
    global startptr
    global queueptr
    if queueptr > 4:
        print("queue is full")
    else:
        if startptr == -1:
            startptr = 0
        Queue[queueptr] = val
        queueptr += 1
def Dequeue():
    global startptr
    global queueptr
    if startptr == -1:
        print("queue is empty")
    else:
        val = Queue[startptr]
        Queue[startptr] = ""
        print(val)
        startptr += 1
    if startptr == queueptr:
        startptr = -1
        queueptr = 0
Enqueue("syed")
Enqueue("sajjad")
Enqueue("ahmed")
Enqueue("rizvi")
Enqueue("a2c")
Dequeue()
Dequeue()
Dequeue()
Dequeue()
Dequeue()




print (Queue)