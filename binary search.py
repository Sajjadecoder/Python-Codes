# Binary search
print ("Enter value")
def binarysearch(value:int):
    list=[4,5,8,9,15,17]

    lowerbound=0
    upperbound=len(list)
    found=False
    notfound=False
    while found==False and notfound==False:
        midpoint=int((lowerbound+upperbound)/2)
        if list(midpoint)==value:
            found=True
        elif list(midpoint)>value:
            lowerbound =midpoint + 1
        elif list(midpoint)<value:
            upperbound =midpoint - 1

        if lowerbound>upperbound:
            notfound=True

    if found==True:
        return("value is in the list")
    else:
        return("not found")



