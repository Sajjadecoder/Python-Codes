list = [2,4,5,7,3,76,98,11]
def linsearch(val):
    for x in range (len(list)):
        if list[x] == val:
            return True
    return False
val = int(input("enter number to search "))
if linsearch(val) == True:
    print("number in the list")
else:
    print("not found")