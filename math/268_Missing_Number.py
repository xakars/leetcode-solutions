# Input: nums = [9,6,4,2,3,5,7,0,1]
#
# Output: 8
#
# Explanation:
#
# n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

# nums = [9,6,4,2,3,5,7,0,1]
# nums = [3,0,1]
nums = [0,1]



def missing_number(nums: list[int]) -> int:
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

print(missing_number(nums))


#O(n) - memory
#O(n) - time
# def missing_number(nums: list[int]) -> int:
#     nums_set = set(nums)
#     for i in range(len(nums)):
#         if i not in nums_set:
#             return i
#     return len(nums)
#
#
# print(missing_number(nums))