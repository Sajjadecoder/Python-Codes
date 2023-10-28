array = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]


# inefficient bubble sort
def bubbleSort():
    for x in range(10):
        for y in range(9):
            if array[y] > array[y + 1]: #will use < sign for descending order
                temp = array[y]
                array[y] = array[y + 1]
                array[y + 1] = temp
    print(array)


bubbleSort()
array2 = [8765,654,234,87,345,876,2345]
def effbubblesort():
    boundary = 7
    noswaps = False
    while noswaps == False:
        noswaps = True
        for y in range(boundary-1):
            if array2[y] > array2[y + 1]: #will use < sign for descending order
                temp = array2[y]
                array2[y] = array2[y + 1]
                array2[y + 1] = temp
                noswaps = False
        boundary = boundary - 1
    print (array2)
effbubblesort()