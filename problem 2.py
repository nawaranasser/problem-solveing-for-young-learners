
# the second problem is to find the index of target in the list

def find(arr , target):
    for i in range(len(arr)):
        if arr[i] == target:
            return arr.index(target)

    return -1


print(find([6,9,4,2,3,86] , 22))
