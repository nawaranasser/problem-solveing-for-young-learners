# the first problem is find the most second number in the list
def get_second_largest(arr):
    arr.sort(reverse=True)


    for i in range(0,len(arr)-1):

        if arr[i+1] < arr[i]:
            sec = arr[i+1]
            return sec

    return -1



print(get_second_largest([12, 35 ,1 ,10 ,34 ,1]))
