# # find the missing num in unorder array
# def missing_num(arr):
#     arr.sort()
#     for i in range(1, len(arr)):
#
#         if i == arr[i-1]:
#             continue
#         else:
#             arr.insert(i-1 , i)
#
#             print(arr)
#             break
#     if len(arr) == 1:
#         arr.append(arr[0] + 1)
#         print(arr)


def missing_num(arr):
    n = len(arr) + 1  # Total numbers should be n
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    missing = expected_sum - actual_sum
    return missing

print(missing_num( [8, 2, 4, 5, 3, 7, 1] ))


