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
