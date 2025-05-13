# you have a num as string s and number of swap operations k
# you must get the largest num of given bits

def find_max_num(s, k):
    nums = list(s)
    n = len(nums)

    def find_max_digit_index(start):
        max_digit = max(nums[start:])
        for j in range(n-1, start, -1):
            if nums[j] == max_digit:
                return j
        return start

    i = 0
    while k > 0 and i < n - 1:
        max_index = find_max_digit_index(i)
        if nums[max_index] > nums[i]:
            nums[i], nums[max_index] = nums[max_index], nums[i]
            k -= 1
        i += 1

    return ''.join(nums)

print(find_max_num( s = "3435335", k = 3))



# def find_max_num(s , k):
#     nums = list(s)
#
#
#     if k > 0:
#         for i in range(len(nums) - 1):
#             index_largest = nums.index(max(nums[i+1 : ]))
#
#
#             temp  = nums[i]
#             nums[i] = nums[index_largest]
#             nums[index_largest] = temp
#             k -= 1
#
#
#     return nums

