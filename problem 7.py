"""
Given an array of integers arr[] that is first strictly increasing and then maybe strictly decreasing,
find the bitonic point, that is the maximum element in the array.
Bitonic Point is a point before which elements are strictly increasing and
 after which elements are strictly decreasing.

Note: It is guaranteed that the array contains exactly one bitonic point.

Examples:

Input: arr[] = [1, 2, 4, 5, 7, 8, 3]
Output: 8
Explanation: Elements before 8 are strictly increasing [1, 2, 4, 5, 7]
and elements after 8 are strictly decreasing [3].
"""

def find_max(arr):
    is_bitonic = False
    bitonic = arr[0]
    for i in range(len(arr)-1):
        if arr[i+1] < arr[i]:
            bitonic = arr[i]
            is_bitonic = True
            break

    if not is_bitonic:
        bitonic = arr[-1]

    return bitonic



print(find_max([120, 100, 80, 20, 0]))