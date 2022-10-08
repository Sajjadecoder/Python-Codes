# binarysearch
list = [4 , 5 , 6 , 8 , 9 , 15 , 17]

def binarysearch(value):
    lowerbound = 0
    upperbound = len(list)-1
    found = False
    notfound = False
    while found == False and notfound == False:
        midpoint = int((lowerbound+upperbound)/2)
        if lowerbound > upperbound:
            notfound=True
            return -1
        elif list[midpoint] == value:
            found = True
            return midpoint
        elif list[midpoint] < value:
            lowerbound = midpoint + 1
        elif list[midpoint] > value:
            upperbound = midpoint - 1

value=int(input("enter a number: "))
ans=binarysearch(value)
if ans!=-1:
    print("value is in the list")
else:
    print("not found")
