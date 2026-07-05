# Example 1:
#
nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]
# Example 2:
#
# Input: nums = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
# - ans = [1,3,2,1,1,3,2,1]


def get_concatenation(nums: list[int]) -> list[int]:
    return nums * 2

print(get_concatenation(nums))


# def get_concatenation(nums: list[int]) -> list[int]:
#     nums.extend(nums)
#     return nums
#
# print(get_concatenation(nums))
