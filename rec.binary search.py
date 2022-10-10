# binary recursive search
array=[2,5,7,11,23,45,69]
def rbs(lb,ub,value):
    mid=int((lb+ub)/2)
    if lb>ub:
        return -1
    else:
        if array[mid]==value:
            return mid
        elif array[mid]<value:
            return rbs(mid+1,ub,value)
        elif array[mid]>value:
            return rbs(lb,mid-1,value)

lb=0
ub=6
value=int(input("enter the number to search: "))
ans=rbs(0,6,value)
if ans != -1:
    print ("number found at location", ans)
else:
    print ("number not found")



