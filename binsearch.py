list = [22,33,44,45,56,78,90,98]
def bs():
    val = int(input(" enter value "))
    upper = len(list)-1
    lower = 0
    found = False

    while found==False and lower<upper:
        mid = (lower+upper)//2
        if list[mid] == val:
            found = True
            return mid
        elif list[mid] < val:
            lower = mid + 1
        else:
            upper = mid - 1
    if found == False:
        return -1
if bs() == -1:
    print("not found")
else:
    print("found")
