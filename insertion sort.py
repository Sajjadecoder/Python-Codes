# insertion sort

array=[6, 7 , 2 , 8 , 15 , 1 , 4]
for index in range(1,7):
    temp=array[index]
    cn= index -1
    while temp<array[cn] and cn>-1:
        array[cn+1]=array[cn]
        cn=cn-1
    array[cn+1]=temp
    print (array)
