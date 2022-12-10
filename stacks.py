def push():
    global topptr , basepointer , arraysize
    if arraysize<topptr:
        return -1
    else:
        value=int(input("enter the value: "))
        topptr += 1
        stack[topptr]=value

def pop ():
    global topptr , basepointer , arraysize
    if topptr<basepointer:
        print ("UnderFlow, stack is empty")
    else:
        value = stack[topptr]
        stack[topptr] = ""
        topptr = topptr - 1
        return value

#main program
stack=[]
for i in range(5):
      stack.append("")
global topptr , basepointer , arraysize
topptr = -1
basepointer = 0
arraysize=

x = int(input("press 1 to start "))
while x != -1:
    print ("  ")
    print ("enter 1 to push")
    print ("enter 2 to pop")
    print ("enter -1 to end")
    x = int(input("Enter choice: "))
    if x == 1:
        push()
    elif x == 2:
        value=pop()
        if value != -1:
            print ("value popped is: " , value)
    else:
        print ("enter a valid option")

print (stack)
