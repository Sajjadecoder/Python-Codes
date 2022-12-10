# queue


def push():
    global topptr
    global baseptr
    global arraysize
    if arraysize <= baseptr:
        print("overflow")
    else:
        value = int(input("enter an item: "))
        baseptr += 1
        queue[baseptr] = value


def pop():
    global topptr
    global baseptr
    global arraysize
    if baseptr < topptr:
        return -1
    else:
        value = queue[topptr]
        queue[topptr] = ""
        topptr += 1
        return value


queue = []
for i in range(5):
    queue.append("")
global topptr
global baseptr
global arraysize
topptr = 0
baseptr = -1
arraysize = 5

x = int(input("enter 1 to start "))
while x != -1:
    print("  ")
    print("enter 1 to push")
    print("enter 2 to pop")
    print("enter -1 to end")
    x = int(input("Enter choice: "))
    if x == 1:
        push()
    elif x == 2:
        value = pop()
        if value == -1:
            print("underflow")
        else:
            print("value popped is: ", value)
    else:
        print("re enter your choice")
print(queue)
