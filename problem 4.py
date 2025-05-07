
# find the missing num of the sorted array of specific pattern
def find_missing(arr):
    p = arr[1] - arr[0]
    is_missing = False
    for i in range(len(arr)-1):
        p1 = arr[i+1] - arr[i]
        if p != p1 :
            missing = arr[i+1] - p
            print('the missing is ',missing)
            arr.insert(i+1, missing)
            print('the correct array is ',arr)
            is_missing = True
            break


    if not is_missing:
        next_item  = arr[-1] + p
        arr.append(next_item)
        print('the correct array is ', arr)

find_missing([1, 6, 11, 16, 21, 31])





