# Write your code here :-)
array = [[0,0,0,0], [1,1,1,1], [2,2,2,2], [3,3,3,3], [4,4,4,4]]
for x in range(5):
    print(array[x], "row ", x)
darray = [["ahmed","ali","bano"],["qasim","faisal","khalid"]]
for row in range(2):
    for col in range(3):
        if darray[row][col] == "faisal":
            print ("found")
