list = [9,7,565,4,23,12,5,6,2,8]
def insort():
    for pointer in range(1,len(list)):
        temp = list[pointer]
        holeposition = pointer-1
        while holeposition > -1 and list[holeposition] > temp:
            list[holeposition+1] = list[holeposition]
            holeposition = holeposition - 1
        list[holeposition+1] = temp
insort()
print(list)