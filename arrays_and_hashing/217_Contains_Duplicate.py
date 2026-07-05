# Example 1:
#
# Input: nums = [1,2,3,1]
#
# Output: true
#
# Explanation:
#
# The element 1 occurs at the indices 0 and 3.
#
# Example 2:
#
# Input: nums = [1,2,3,4]
#
# Output: false
#
# Explanation:
#
# All elements are distinct.
#
# Example 3:
#
nums = [1,1,1,3,3,4,3,2,4,2]
#
# Output: true


def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for i in nums:
        if i in seen:
            return True
        else:
            seen.add(i)

    return False

print(contains_duplicate(nums))